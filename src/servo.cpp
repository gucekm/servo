#include <Arduino.h>
#include <servo.h>


void ServoSetup() {
    pinMode(SERVO_POSITION_PIN, INPUT);
}

void ServoLoop() {
    // Serial.print("Position: ");
    // Serial.println(ServoPosition());
}

#ifdef SIMULATION
int servoSimulationPosition = 0;

void ServoSimulatePosition(int position) {
    servoSimulationPosition = position;
}
#endif

int ServoPosition() {
#ifdef SIMULATION
    return servoSimulationPosition;
#else
    return analogRead(SERVO_POSITION_PIN);
#endif
}
