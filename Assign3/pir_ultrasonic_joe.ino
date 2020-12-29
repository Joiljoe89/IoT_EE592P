/*
 * PIR + Ultrasonic sensor range tester *** joe johnson d17024
 */

int ledPin = 13;                // choose the pin for the LED
int inputPin = 2;               // choose the input pin (for PIR sensor)
int pirState = LOW;             // we start, assuming no motion detected
int val = 0;                    // variable for reading the pin status

const int trigPin1 = 9; 
const int echoPin1 = 10;

void setup() {
  pinMode(ledPin, OUTPUT);      // declare LED as output
  pinMode(inputPin, INPUT);     // declare sensor as input

  pinMode(trigPin1, OUTPUT); 
  pinMode(echoPin1, INPUT);
 
  Serial.begin(9600);
}
 
void loop(){
  val = digitalRead(inputPin);  // read input value
  if (val == HIGH) {            // check if the input is HIGH
    digitalWrite(ledPin, HIGH);  // turn LED ON
    if (pirState == LOW) {
      
      digitalWrite(trigPin1, LOW);
      delayMicroseconds(2); 
      digitalWrite(trigPin1, HIGH);
      delayMicroseconds(10); 
      digitalWrite(trigPin1, LOW);
      duration1 = pulseIn(echoPin1, HIGH); 
      distance1 = (duration1*.0343)/2;
      Serial.println(distance1);
      delay(100);
      
      Serial.println("Motion detected!");
      // We only want to print on the output change, not state
      pirState = HIGH;
    }
  } else {
    digitalWrite(ledPin, LOW); // turn LED OFF
    if (pirState == HIGH){
      // we have just turned of
      Serial.println("Motion ended!");
      // We only want to print on the output change, not state
      pirState = LOW;
    }
  }
}
