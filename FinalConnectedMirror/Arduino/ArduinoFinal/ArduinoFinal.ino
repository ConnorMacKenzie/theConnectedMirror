const int trigPin = 5;
const int echoPin = 6;
const int redPin = 11;
const int greenPin = 10;
const int bluePin = 9;

// defines variables
long duration;
int distance;
int screen = 0;


void setup(){
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  Serial.begin(9600); // Starts the serial communication
  Serial.println(90);
  Serial.setTimeout(100);
}

void controlLED(){

  int redVal = Serial.parseInt();
  int greenVal = Serial.parseInt();
  int blueVal = Serial.parseInt();

  if(redVal != 0 && greenVal !=0 && blueVal != 0){
    analogWrite(redPin, redVal);
    analogWrite(greenPin, greenVal);
    analogWrite(bluePin, blueVal);
  }

}

void getDistance(){

  delay(200);

  // Clears the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);

  // Calculating the distance
  distance= duration*0.034/2;

  // Prints the distance on the Serial Monitor
  Serial.println(distance);

}

void loop(){

  delayMicroseconds(200);

  getDistance();

  controlLED();

}
