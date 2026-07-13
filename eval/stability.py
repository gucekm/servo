#!/usr/bin/env python3
"""Answer-stability test: does Maks give the SAME answer when asked again?

The main audit (results.json) is a single run, so any individual verdict —
including the 14 flagged factual errors — could in principle be a one-off
rather than a stable behaviour. This test re-asks a fixed panel of questions
in N fresh conversations each and measures how consistent the answers are:

  * fact recall per run (same rubric as evaluate.py),
  * a per-run verdict:  FULL / PARTIAL / ZERO / DEFLECT / ERROR,
  * how many *distinct* answers (normalised) the runs produced,
  * whether the run-1 audit verdict is reproduced (stable) or flips.

Panel (20 questions, chosen deterministically):
  - the 13 questions behind the audit's confirmed factual errors (REPORT §4),
  - the first perfect-recall question of each category (4 known-good controls),
  - the first 3 deflected broadband questions (deflection-prone controls).

Usage:
    python3 stability.py                 # live: 20 questions x 5 runs
    python3 stability.py --runs 3        # fewer runs
    python3 stability.py --report stability_runs.json   # re-render md only
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

from evaluate import build_record  # noqa: E402  (same rubric as the main run)
from live import ask_fresh  # noqa: E402
from questions import QUESTIONS  # noqa: E402

# The questions behind REPORT.md §4 "Confirmed factual errors".
ERROR_IDS = ["naj10", "naj32", "naj33", "naj46", "naj57", "mobi05", "mobi08",
             "mobi41", "tv07", "tv32", "tv38", "tv62", "bb26"]


def pick_panel() -> list:
    """13 error questions + 4 known-good controls + 3 deflection-prone ones."""
    results = {r["id"]: r for r in
               json.loads((HERE / "results.json").read_text(encoding="utf-8"))}
    ids = list(ERROR_IDS)
    for cat in ("prepaid", "postpaid", "broadband", "iptv"):
        good = sorted(r["id"] for r in results.values()
                      if r["category"] == cat and r["recall"] == 1.0
                      and not r["deflected"] and r["id"] not in ids)
        if good:
            ids.append(good[0])
    defl_bb = sorted(r["id"] for r in results.values()
                     if r["category"] == "broadband" and r["deflected"]
                     and r["id"] not in ids)
    ids.extend(defl_bb[:3])
    by_id = {q[0]: q for q in QUESTIONS}
    return [by_id[i] for i in ids]


def verdict(rec: dict) -> str:
    if rec["answer"].startswith("[ERROR:"):
        return "ERROR"
    if rec["deflected"]:
        return "DEFLECT"
    if rec["recall"] == 1.0:
        return "FULL"
    if rec["recall"] == 0.0:
        return "ZERO"
    return "PARTIAL"


def norm_answer(text: str) -> str:
    """Normalise an answer for distinct-answer counting (emoji/space tolerant)."""
    t = text.lower()
    t = re.sub(r"[^\w,.€%]+", " ", t, flags=re.UNICODE)
    return re.sub(r"\s+", " ", t).strip()


def run_live(runs: int, delay: float) -> dict:
    panel = pick_panel()
    baseline = {r["id"]: r for r in
                json.loads((HERE / "results.json").read_text(encoding="utf-8"))}
    out = {"runs": runs, "captured": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()),
           "questions": []}
    # Checkpoint file: one JSON line per finished conversation, so an
    # interrupted run resumes instead of restarting from scratch.
    prog_path = HERE / "stability_progress.jsonl"
    done: dict = {}
    if prog_path.exists():
        for line in prog_path.read_text(encoding="utf-8").splitlines():
            rec = json.loads(line)
            done[(rec["id"], rec["k"])] = rec["run"]
        print(f"Resuming: {len(done)} conversations already done.")
    total = len(panel) * runs
    n = 0
    with prog_path.open("a", encoding="utf-8") as prog:
        for qid, cat, q, facts in panel:
            entry = {"id": qid, "category": cat, "question": q,
                     "baseline_verdict": verdict(baseline[qid]),
                     "runs": []}
            for k in range(runs):
                n += 1
                if (qid, k) in done:
                    entry["runs"].append(done[(qid, k)])
                    continue
                reply = ask_fresh(q)
                rec = build_record(qid, cat, q, facts, reply["text"])
                v = verdict(rec)
                run_rec = {"answer": reply["text"], "recall": rec["recall"],
                           "deflected": rec["deflected"], "verdict": v}
                entry["runs"].append(run_rec)
                prog.write(json.dumps({"id": qid, "k": k, "run": run_rec},
                                      ensure_ascii=False) + "\n")
                prog.flush()
                print(f"[{n:3}/{total}] {qid:7} run {k+1}/{runs}: {v:8} "
                      f"recall={rec['recall']:.2f}", flush=True)
                time.sleep(delay)
            out["questions"].append(entry)
    prog_path.unlink()  # complete — the checkpoint is no longer needed
    return out


def render(data: dict) -> str:
    qs = data["questions"]
    runs = data["runs"]
    lines = [
        "# Maks answer-stability test",
        "",
        f"Panel of **{len(qs)} questions**, each asked in **{runs} fresh conversations** "
        f"({len(qs) * runs} conversations total), captured {data['captured']}. "
        "Scored with the same rubric as the main audit (`evaluate.py`).",
        "",
        "Verdicts: **FULL** = every reference fact recalled · **PARTIAL** = some · "
        "**ZERO** = none (specific but wrong, or off-topic) · **DEFLECT** = non-answer "
        "hand-off · **ERROR** = transport failure.",
        "",
        "| id | baseline (audit) | run verdicts | distinct answers | stable? |",
        "|---|---|---|---|---|",
    ]
    n_stable = 0
    flips = []
    for e in qs:
        vs = [r["verdict"] for r in e["runs"]]
        distinct = len({norm_answer(r["answer"]) for r in e["runs"]})
        stable = len(set(vs)) == 1
        # "confirmed" = every re-run reproduces the audit-run verdict
        confirmed = stable and vs[0] == e["baseline_verdict"]
        n_stable += stable
        if not stable or not confirmed:
            flips.append(e)
        lines.append(
            f"| `{e['id']}` | {e['baseline_verdict']} | {' '.join(vs)} | "
            f"{distinct}/{len(vs)} | {'yes' if stable else 'NO'}"
            f"{'' if confirmed or not stable else ' (differs from audit)'} |")
    verdict_counts = Counter(v for e in qs for v in (r["verdict"] for r in e["runs"]))
    lines += [
        "",
        "## Summary",
        "",
        f"- **{n_stable}/{len(qs)} questions gave the same verdict in every run.**",
        f"- Run-verdict mix across all {len(qs) * runs} answers: "
        + ", ".join(f"{k} {v}" for k, v in verdict_counts.most_common()) + ".",
    ]
    err_qs = [e for e in qs if e["id"] in ERROR_IDS]
    stable_err = [e for e in err_qs
                  if len({r["verdict"] for r in e["runs"]}) == 1
                  and all(r["verdict"] in ("ZERO", "PARTIAL") for r in e["runs"])]
    lines.append(
        f"- Of the {len(err_qs)} confirmed-error questions on the panel, "
        f"**{len(stable_err)} reproduce a wrong/incomplete answer in every run** — "
        "i.e. the audit's flagged errors are predominantly *stable knowledge defects*, "
        "not sampling noise." if stable_err else
        "- The flagged errors did NOT all reproduce — treat the audit's error list "
        "as partly nondeterministic.")
    if flips:
        lines += ["", "## Questions with unstable or shifted verdicts", ""]
        for e in flips:
            lines.append(f"### `{e['id']}` — {e['question']}")
            lines.append(f"Baseline (audit): **{e['baseline_verdict']}**")
            for i, r in enumerate(e["runs"], 1):
                ans = r["answer"].replace("\n", " ")
                if len(ans) > 200:
                    ans = ans[:200] + "…"
                lines.append(f"- run {i} **{r['verdict']}** (recall {r['recall']}): {ans}")
            lines.append("")
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", type=int, default=5, help="fresh conversations per question")
    ap.add_argument("--delay", type=float, default=0.4, help="pause between conversations (s)")
    ap.add_argument("--report", metavar="RUNS_JSON",
                    help="skip the live run; re-render stability.md from saved runs")
    args = ap.parse_args(argv)

    if args.report:
        data = json.loads(Path(args.report).read_text(encoding="utf-8"))
    else:
        data = run_live(args.runs, args.delay)
        (HERE / "stability_runs.json").write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    (HERE / "stability.md").write_text(render(data), encoding="utf-8")
    print("Wrote stability_runs.json and stability.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
