const int sensorDOPin = 2;     // connect DO pin to pin 2 of Arduino
const int ledPin =  13;      // the number of the LED pin

// variables will change:
int SensorState = 0;         // variable for the state of the sensor

void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the sensor pin DO as input
  pinMode(sensorDOPin, INPUT);
}

void loop() {
  // read the state of the sensor value:
  SensorState = digitalRead(sensorDOPin);
// by default, the sensor sends a HIGH all the time
  //if the sensor sends a LOW
    if (SensorState == LOW) {
    // turn LED on:
    digitalWrite(ledPin, HIGH);
  }
  else {
    // turn LED off:
    digitalWrite(ledPin, LOW);
  }
}
