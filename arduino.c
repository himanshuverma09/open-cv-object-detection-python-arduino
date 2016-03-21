//Flash in Arduino
#define MOTOR1 10		//Define the points of motor connection to arduino
#define MOTOR2 11
#define MOTOR3 3
#define MOTOR4 4


void setup() {
	pinMode(MOTOR1, OUTPUT);	//Set Pin Mode
	pinMode(MOTOR2, OUTPUT);
	pinMode(MOTOR3, OUTPUT);
	pinMode(MOTOR4, OUTPUT);
	Serial.begin(9600);
}


void loop() {
	if (Serial.available()) 
		{
		char c = Serial.read();
		if (c == 'R') {
			digitalWrite(MOTOR1, HIGH);
			digitalWrite(MOTOR2, LOW);
			delay(20);
			digitalWrite(MOTOR1, LOW);
			digitalWrite(MOTOR2, LOW);
			delay(30);
			}
		else if (c == 'L') {
			digitalWrite(MOTOR1, LOW);
			digitalWrite(MOTOR2, HIGH);
			delay(20);
			digitalWrite(MOTOR1, LOW);
			digitalWrite(MOTOR2, LOW);
			delay(30);
			}
		else if (c == 'X'){
			digitalWrite(MOTOR1, LOW);
			digitalWrite(MOTOR2, LOW);
			}
		
		if (c == 'U') {
			digitalWrite(MOTOR3, HIGH);
			digitalWrite(MOTOR4, LOW);
			delay(40);
			digitalWrite(MOTOR3, LOW);
			digitalWrite(MOTOR4, LOW);
			delay(30);
			}
		else if (c == 'D') {
			digitalWrite(MOTOR3, LOW);
			digitalWrite(MOTOR4, HIGH);
			delay(40);
			digitalWrite(MOTOR3, LOW);
			digitalWrite(MOTOR4, LOW);
			delay(30);
			}
		else if (c == 'Y'){
			digitalWrite(MOTOR3, LOW);
			digitalWrite(MOTOR4, LOW);
			}
		}
	}
