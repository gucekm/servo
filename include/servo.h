#ifndef _SERVO_H
#define _SERVO_H

#include <Arduino.h>

#define SERVO_POSITION_PIN    PIN_A0

void ServoSetup();
void ServoLoop();
int ServoPosition();

#ifdef SIMULATION
void ServoSimulatePosition(int position);
#endif // SIMULATION
#endif