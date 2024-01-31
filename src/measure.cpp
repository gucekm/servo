#include <measure.h>

#include <Arduino.h>
#include <servo.h>
#include <motor.h>

#define MAX_MEASUREMENTS 20  
#define MEASUREMENT_RUNS 10
#define MEASUREMENT_INTERVAL 1000
#define MAX_SERVO_POSITION 1023  
#define MIN_SERVO_SWING_POSITION 100
#define MAX_SERVO_SWING_POSITION 1000


typedef struct {
    unsigned long time;
    union {
        float floatVal;
        int intVal;
        unsigned int uintVal;
    } value;
} measurement;

measurement measurements[MAX_MEASUREMENTS];
int measurementIndex;
unsigned long measurementTime; // Declare the variable measurementNextTime
bool isNewMeasurementAvailable;
bool isMeasurementComplete;
bool isMeasurementPrinted;

/*
Finite State Machine (FSM) comprises of the following:
- State variables
- State machine handler

State variables:
- State variables are used to keep track of the current state of the state machine.
- State variables are declared as static variables inside the state machine handler.
- State variables are initialized to the initial state of the state machine.
- State variables are updated by the state machine handler.
- State variables are used by the state machine handler to determine the next state of the state machine.

State machine handler:
- State machine handler is a function that implements the state machine.
- State machine handler is called periodically by the main loop.

State machine handler implementation:
- Machine starts with state declaration as static variable and initialization to initial state.

- State machine handler is implemented as a switch statement.
- Each case in the switch statement corresponds to a state in the state machine.
- Each case in the switch statement is responsible for performing the actions associated with the state.
- Each case in the switch statement is responsible for determining the next state of the state machine.
- Each case in the switch statement is responsible for handling the transition to the next state machine.
- Before returning from the state machine handler, the state variable is updated to the next state.
- In case of invalid state, the state machine handler stays in idle state

State machine can implement infinite as well as finite processes. Finite process can be used as single state in larger parent state machine.
Since states of parent state machine are unknown to child state machine, output of child state machine is used as internal event to parent state machine.
This way complex processes can be decomposed into smaller finite processes using nested state machines.

If you have multiple state machines you can group their variables into structs.
I believe this is not necessary in case of single state machine.
For each state machine you need to define memory space for the variables that will persits between calls to the state machine.
Variables can be packed into a struct to make it easier to pass them to the state machine functions as a reference to the struct.

For example:

typedef struct {
  int state;
  struct {
    int var1;
    int var2;
  } variable;
} myStateMachine;
*/

typedef struct {
    int state;
    struct {
        int var1;
        int var2;
    } variable;
} measureMachine;


/**
 * Measures the time it takes for the servo to swing from min to max position.
 * Servo first moves to min position, then to max position.
 * Time needed to reach min position is measured.
 * Result is stored in measurements array.
 *
 * @return 1 if the state machine is completed, 0 otherwise.
 */
int MeasureSwingTimeLoop() {
    static int state = 0;

    switch (state) {
    case 0: //measuremnt setup
        measurementIndex = 0;
        isNewMeasurementAvailable = false;
        isMeasurementComplete = false;
        isMeasurementPrinted = false;
        motor1.setSpeed(-255);
        state = 1;
    case 1: //wait for servo to reach min position
        if (ServoPosition() < MIN_SERVO_SWING_POSITION) {
            measurements[measurementIndex].time = micros();
            measurements[measurementIndex].value.intVal = ServoPosition();
            measurementIndex++;
            motor1.setSpeed(255);
            state = 2;
        } else {
            return 0; //state machine not completed yet
        }
    case 2: //wait for servo to reach max position
        ServoSimulatePosition(MAX_SERVO_POSITION);
        if (ServoPosition() >= MAX_SERVO_SWING_POSITION) {
            measurements[measurementIndex].time = micros();
            measurements[measurementIndex].value.intVal = ServoPosition();
            isMeasurementComplete = true;
            isNewMeasurementAvailable = true;
            measurementIndex++;
            state = 3;
        } else {
            return 0; //stay in this state
        }
    case 3:
        return 1;   //state machine completed
    }
    //In case of error stay in same state.
    //Optional: add error handling code here
    return 0;
}

/**
 * Measures response of the motor against step input signal.
 * Response is stored in measurements array.
 * Servo first moves to min position, then to max position.
 * Position of the servo is recorded every MEASUREMENT_INTERVAL microseconds.
 *
 * @return 1 if the state machine is completed, 0 otherwise.
 */
int  MeasureMotorSpeedLinearityLoop() {
    static int state = 0;
    static unsigned long currentTime;
    static unsigned long measurementTime;

    switch (state) {
    case 0: //measurement setup
        measurementIndex = 0;
        isNewMeasurementAvailable = false;
        isMeasurementComplete = false;
        isMeasurementPrinted = false;
        motor1.setSpeed(-255);
        state = 1;
    case 1: //wait for servo to reach min position
        ServoSimulatePosition(MIN_SERVO_SWING_POSITION);
        if (ServoPosition() > MIN_SERVO_SWING_POSITION) {
            return 0;
        }
        motor1.setSpeed(0);
        measurementTime = micros() + 500000; //wait motor to stop for half a second
        state = 2;
    case 2: //wait for motor to stop
        if (micros() < measurementTime) {
            return 0;
        }
        state = 3;
    case 3:
        currentTime = micros(); //wait for next measurement 
        if (currentTime < measurementTime)
            return 0;

        measurements[measurementIndex].time = currentTime;
        measurements[measurementIndex].value.intVal = ServoPosition();
        isNewMeasurementAvailable = true;
        measurementIndex++;
        measurementTime += MEASUREMENT_INTERVAL;
        if (measurementIndex < MAX_MEASUREMENTS)
            return 0;

        isMeasurementComplete = true;
        state = 4;
    case 4:
        return 1; //state machine completed
    }
    //In case of error stay in same state.
    //Optional: add error handling code here
    return 0;
}

/**
 * @brief Checks if a new measurement is available.
 *
 * @return true if a new measurement is available, false otherwise.
 */
bool IsNewMeasurementAvailable() {
    bool retValue = isNewMeasurementAvailable;
    isNewMeasurementAvailable = false;
    return retValue;
}

/**
 * @brief Checks if the measurement is complete.
 *
 * @return true if the measurement is complete, false otherwise.
 */
bool IsMeasurementComplete() {
    return isMeasurementComplete;
}

/**
 * @brief Retrieves the last measurement.
 *
 * This function returns a reference to the last measurement in the measurements array.
 *
 * @return A reference to the last measurement.
 */
measurement& GetLastMeasurement() {
    return measurements[measurementIndex - 1];
}

/**
 * @brief Prints all measurements.
 *
 * This function prints all measurements to the console.
 */
int  PrintAllMeasurementsLoop() {
    static int state = 0;
    static int i = 0;
    switch (state) {
    case 0:
        i = 0;
        state = 1;
    case 1:
        if (i == measurementIndex) {
            isMeasurementPrinted = true;
            return 1;
        }
        Serial.print(measurements[i].time);
        Serial.print(",");
        Serial.println(measurements[i].value.intVal);
        i++;
        return 0;
    }
    //In case of error stay in same state.
    //Optional: add error handling code here
    return 0;
}

/**
 * @brief Checks if the measurement has been printed.
 *
 * This function returns a boolean value indicating whether the measurement has been printed or not.
 *
 * @return True if the measurement has been printed, false otherwise.
 */
bool IsMeasurementPrinted() {
    return isMeasurementPrinted;
}

void MeasurementSetup() {

}

int MeasurementLoop() {
    static int state = 0;
    switch (state) {

    case 0:
        if (!MeasureSwingTimeLoop())
            return 0;
        state = 1;
    case 1:
        if (!MeasureMotorSpeedLinearityLoop())
            return 0;
        motor1.setEnabled(false); //measurements are complete, disable motor
        state = 2;
    case 2:
        if (!PrintAllMeasurementsLoop())
            return 0;
        state = 3;
    case 3:
        return 1;
    }
    return 0;
}