#include <Arduino.h>
#include <servo.h>
#include "simulation/simulation.h"

void ServoSetup()
{
    pinMode(SERVO_POSITION_PIN, INPUT);
}

void ServoLoop()
{
    // Serial.print("Position: ");
    // Serial.println(ServoPosition());
}

void SetServoSetSpeed(int newSpeed)
{
#ifdef SIMULATION
    setSimulatedServoSpeed(newSpeed);
#else
    // Not implemented
#endif
}

int ServoPosition()
{
#ifdef SIMULATION
    return getSimulatedServoPosition();
#else
    return analogRead(SERVO_POSITION_PIN);
#endif
}
