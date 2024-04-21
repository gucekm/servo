#include <Arduino.h>
#include "board.h"
#include "servo.h"
#include "motor.h"
#include "measure.h"
#include "simulation/simulation.h"

unsigned long start;

void setup(void)
{
#ifdef SIMULATION
    SimulatedServoSetup();
#endif
    LEDSetup();
    SerialSetup();
    ServoSetup();
    MotorSetup();
    motor1.setEnabled(true);
    start = millis();
    MeasurementSetup();
}

void loop(void)
{
#ifdef SIMULATION
    SimulatedServoLoop();
#endif
    LEDLoop();
    ServoLoop();
    MotorLoop();
    MeasurementLoop();
}