

#include <Servo.h> //the library which helps us to control the servo motor

char incomingByte = 0;

//define our L298N control pins
//Motor A
const int RightMotorForward = 6;    // IN1
const int RightMotorBackward = 7;   // IN2
//Motor B
const int LeftMotorForward = 8;     // IN3
const int LeftMotorBackward = 9;    // IN4

//Relay Switch Motor Controller
#define CW 4  //CW is defined as pin #4//
#define CCW 5 //CCW is defined as pin #5//

int8_t LmotorSpeed = (255*3)/4; //set motor speed to max speed
int8_t RmotorSpeed = (255*3)/4; //set motor speed to max speed


//define the servo name
Servo myServo;
void setup() 
{
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pins:
  for (int thisPin = 2; thisPin < 7; thisPin++) {
   //H-Bridge Switch Motor Controller
  pinMode(RightMotorForward, OUTPUT);
  pinMode(LeftMotorForward, OUTPUT);
  pinMode(LeftMotorBackward, OUTPUT);
  pinMode(RightMotorBackward, OUTPUT); 
 
 //Relay Switch Motor Controller
  pinMode(CW, OUTPUT); //Set CW as an output//
  pinMode(CCW, OUTPUT); //Set CCW as an output//
   
     //define the servo input pins
  myServo.attach(14); //A0 
  }
}

void loop() {

  
  
  // read the sensor:
  if (Serial.available() > 0) {
    int inByte = Serial.read();
    

    switch (inByte) {
      case 'M':
        // This is forward
    // Set a Motor A forward
    
    analogWrite(RightMotorForward, LmotorSpeed);    //M 
    analogWrite(RightMotorBackward, 0);
    // Set a Motor B forward
   ;  
    analogWrite(LeftMotorForward, RmotorSpeed);
    analogWrite(LeftMotorBackward, 0);
    delay(100);
        break;
      
      case 'B':
        // This is backward
    // Set a Motor A backward
    analogWrite(RightMotorForward, 0);     //B
    analogWrite(RightMotorBackward, LmotorSpeed);
    // Set a Motor B backward
    analogWrite(LeftMotorForward, 0);
    analogWrite(LeftMotorBackward, RmotorSpeed);
    delay(100);
        break;
      
      case 'L':
    analogWrite(RightMotorForward, LmotorSpeed);     //L
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
      
      case 'S':
       // Stop Motors
    analogWrite(RightMotorForward, 0);     //S
    analogWrite(RightMotorBackward, 0);
    analogWrite(LeftMotorForward, 0);
    analogWrite(LeftMotorBackward, 0);
        break;
///////////////////////////////////////////////////////////////
      case 'F':
       //  Linear moter 
digitalWrite(CW,HIGH); //Motor runs clockwise//
delay(5000); //for 5 second//
digitalWrite(CW, LOW); //Motor stops//

digitalWrite(CW,LOW); //Motor stops//
digitalWrite(CW, LOW); //Motor stops//
delay(5000); //for 5 second//

digitalWrite(CCW, HIGH);//Motor runs counter-clockwise//
delay(5000); //For 5 second//
digitalWrite(CCW, LOW); //Motor stops//
    
        break;
        
     
        }

    }
  }

