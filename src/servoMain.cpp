#include <Arduino.h>
#include "board.h"
#include "servo.h"
#include "motor.h" 
#include "measure.h"

unsigned long start;

void setup(void) {
  LEDSetup();
  SerialSetup();
  ServoSetup();
  MotorSetup();
  motor1.setEnabled(true);
  start = millis();
  MeasurementSetup();

}

void loop(void) {
  LEDLoop();
  ServoLoop();
  MotorLoop();
  MeasurementLoop();
}