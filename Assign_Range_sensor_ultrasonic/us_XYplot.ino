#define trigPin1 9
#define echoPin1 10
#define trigPin2 4
#define echoPin2 ;
int power_us = 7;

long duration, distance, X_Sensor,Y_Sensor;
 
void setup()
{
Serial.begin (9600);
pinMode(trigPin1, OUTPUT);
pinMode(echoPin1, INPUT);
pinMode(trigPin2, OUTPUT);
pinMode(echoPin2, INPUT);
pinMode(power_us, OUTPUT);
}
 
void loop() {
digitalWrite(power_us, HIGH);
SonarSensor(trigPin1, echoPin1);
if (distance>=100){
  distance=100;
}
X_Sensor = distance*5;
SonarSensor(trigPin2, echoPin2);
if (distance>=100){
  distance=100;
}
Y_Sensor = distance*5;
 
Serial.print(X_Sensor);
Serial.print(",");
Serial.println(Y_Sensor);
delay(20);
}
 
void SonarSensor(int trigPin,int echoPin)
{
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);
duration = pulseIn(echoPin, HIGH);
distance = (duration/2) / 29.1;
 
}
