#define incomingByte 0
#include <Servo.h> 

//Motor A
const int RightMotorForward = 6;    // IN1
const int RightMotorBackward = 7;   // IN2

//Motor B
const int LeftMotorForward = 8;     // IN3
const int LeftMotorBackward = 9;    // IN4

//Relay Switch Motor Controller
#define CW 4  
#define CCW 5 

int8_t LmotorSpeed = (255*3)/4; 
int8_t RmotorSpeed = (255*3)/4; 


//define the servo name
Servo myServo;
void setup() 
{
  Serial.begin(9600);
  for (int thisPin = 2; thisPin < 7; thisPin++) {
  pinMode(RightMotorForward, OUTPUT);
  pinMode(LeftMotorForward, OUTPUT);
  pinMode(LeftMotorBackward, OUTPUT);
  pinMode(RightMotorBackward, OUTPUT); 
 
  pinMode(CW, OUTPUT);
  pinMode(CCW, OUTPUT);
   
  myServo.attach(14); //A0 
  }
}

void loop() {
  // read the sensor:
  if (Serial.available() > 0) {
    int inByte = Serial.read();
    switch (inByte) {
      // forward
      case 'M':
      analogWrite(RightMotorForward, LmotorSpeed);
      analogWrite(RightMotorBackward, 0);
      analogWrite(LeftMotorForward, RmotorSpeed);
      analogWrite(LeftMotorBackward, 0);
      delay(100);
        break;
      // backward
      case 'B':
      analogWrite(RightMotorForward, 0);
      analogWrite(RightMotorBackward, LmotorSpeed);
      analogWrite(LeftMotorForward, 0);
      analogWrite(LeftMotorBackward, RmotorSpeed);
      delay(100);
        break;
      // backward
      case 'L':
      analogWrite(RightMotorForward, LmotorSpeed);
      analogWrite(RightMotorBackward,0);
      analogWrite(LeftMotorForward, 0);
      analogWrite(LeftMotorBackward, RmotorSpeed);
      delay(100);
        break;
      
      case 'R':
      analogWrite(RightMotorForward, 0);     //R
      analogWrite(RightMotorBackward, LmotorSpeed);
      analogWrite(LeftMotorForward, RmotorSpeed);
      analogWrite(LeftMotorBackward, 0);
      delay(100);
        break;
      // Stop Motors
      case 'S':
      analogWrite(RightMotorForward, 0);
      analogWrite(RightMotorBackward, 0);
      analogWrite(LeftMotorForward, 0);
      analogWrite(LeftMotorBackward, 0);
        break;
      //  Linear moter 
      case 'F':
      digitalWrite(CW,HIGH); 
      delay(5000); 
      digitalWrite(CW, LOW);
      digitalWrite(CW, LOW);
      digitalWrite(CW, LOW);
      delay(5000);
      digitalWrite(CCW, HIGH);
      delay(5000); 
      digitalWrite(CCW, LOW);
        break;
        }
    }
}