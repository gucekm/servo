#include <board.h>

void LEDSetup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void LEDLoop() {
  static unsigned long ledTime = millis();

  if (millis() - ledTime > LED_PERIOD) {
    digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN));
    ledTime = millis();
  }
}

void SerialSetup() {
  Serial.begin(115200);
}
