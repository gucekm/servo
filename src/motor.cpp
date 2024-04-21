#include <motor.h>
#include "simulation/simulation.h"

motor motor1(MOTOR1_ENABLE_PIN, MOTOR1_DIRECTION_PIN);
motor motor2(MOTOR2_ENABLE_PIN, MOTOR2_DIRECTION_PIN);

motor::motor(unsigned char newEnablePin, unsigned char newDirectionPin)
{
    enablePin = newEnablePin;
    directionPin = newDirectionPin;
    enabled = false;
    direction = MOTOR_DIRECTION_FWD;
    speed = 0;
}

motor::motor()
{
    enabled = false;
    direction = MOTOR_DIRECTION_FWD;
    speed = 0;
}

void motor::Update()
{
    if (enabled)
    {
        if (direction == MOTOR_DIRECTION_FWD)
        {
            digitalWrite(directionPin, HIGH);
        }
        else
        {
            digitalWrite(directionPin, LOW);
        }
        analogWrite(enablePin, speed);
#ifdef SIMULATION
        if (direction == MOTOR_DIRECTION_FWD)
            setSimulatedServoSpeed(speed);
        else
            setSimulatedServoSpeed(-speed);
#endif
    }
    else
    {
        analogWrite(enablePin, 0);
#ifdef SIMULATION
        setSimulatedServoSpeed(0);
#endif
    }
}

void motor::setEnabled(unsigned char newEnable, bool update)
{
    enabled = newEnable;
    if (update)
        Update();
}

void motor::setDirection(unsigned char newDirection, bool update)
{
    direction = newDirection;
    if (update)
        Update();
}

void motor::setSpeed(int newSpeed, bool update)
{
    speed = newSpeed < 0 ? -newSpeed : newSpeed;
    direction = newSpeed < 0 ? MOTOR_DIRECTION_BCK : MOTOR_DIRECTION_FWD;
    if (update)
        Update();
}

void MotorSetup()
{
    pinMode(MOTOR1_DIRECTION_PIN, OUTPUT);
    pinMode(MOTOR1_ENABLE_PIN, OUTPUT);
    pinMode(MOTOR2_DIRECTION_PIN, OUTPUT);
    pinMode(MOTOR2_ENABLE_PIN, OUTPUT);
}

void MotorLoop()
{
}
