#ifndef _MOTOR_H
#define _MOTOR_H

#include <Arduino.h>

#define MOTOR1_ENABLE_PIN 5
#define MOTOR1_DIRECTION_PIN 4
#define MOTOR2_ENABLE_PIN 6
#define MOTOR2_DIRECTION_PIN 7

#define MOTOR_DIRECTION_FWD 0
#define MOTOR_DIRECTION_BCK 1

class motor
{
    unsigned char enablePin;
    unsigned char directionPin;
    unsigned char enabled : 1;
    unsigned char direction : 1;
    unsigned int speed;
    void Update();
public:
    motor();
    motor(unsigned char newEnablePin, unsigned char newDirectionPin);
    void setEnabled(unsigned char newEnable, bool update = true);
    void setDirection(unsigned char newDirection, bool update = true);
    void setSpeed(int newSpeed, bool update = true);
};

extern motor motor1;
extern motor motor2;

void MotorSetup();
void MotorLoop();

#endif