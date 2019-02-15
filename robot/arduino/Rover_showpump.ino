

#include <Servo.h> //the library which helps us to control the servo motor

char incomingByte = 0;
//Headlight LED
int PUMPWATERPIN = 2;
//drive motor/shield parameters

//Motor A
const int RightMotorForward = 6;    // IN1
const int RightMotorBackward = 7;   // IN2

//Motor B
const int LeftMotorForward = 8;     // IN3
const int LeftMotorBackward = 9;    // IN4



//define the servo name
Servo myServo;
void setup() 
{
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pins:
  for (int thisPin = 2; thisPin < 7;  thisPin++) 
  {
  
  //motor output
    pinMode(PUMPWATERPIN,OUTPUT);
    pinMode(RightMotorForward , OUTPUT);
    pinMode(LeftMotorForward , OUTPUT);
    pinMode(LeftMotorBackward , OUTPUT);
    pinMode(RightMotorBackward , OUTPUT);

    Serial.begin(9600); 
     //define the servo input pins
    myServo.attach(14); //A0 
    
  }
}

void loop()
{
  // read the sensor:
  if (Serial.available() > 0) 
  
 {
    int inByte = Serial.read();   

    switch (inByte)
    {
      case 'M':
        // This is forwardR
       digitalWrite(PUMPWATERPIN, LOW); 
       
       
       digitalWrite(RightMotorForward, HIGH);    //M 
       digitalWrite(RightMotorBackward, LOW);
  
       digitalWrite(LeftMotorForward, HIGH);
       digitalWrite(LeftMotorBackward, LOW);

      break;
      
      case 'B':
       
       digitalWrite(PUMPWATERPIN, LOW); 
       
       // This is forward 
        
       
       digitalWrite(RightMotorForward, LOW);    //M 
       digitalWrite(RightMotorBackward, HIGH);
  
       digitalWrite(LeftMotorForward, LOW);
       digitalWrite(LeftMotorBackward, HIGH);

      break;
      
      case 'L':
        digitalWrite(PUMPWATERPIN, LOW); 
        
        // This is forwardR
        
       
       digitalWrite(RightMotorForward, LOW);    //M 
       digitalWrite(RightMotorBackward, HIGH);
  
       digitalWrite(LeftMotorForward, HIGH);
       digitalWrite(LeftMotorBackward, LOW);

      break;
      
      case 'R':
       digitalWrite(PUMPWATERPIN, LOW); 
       
        // This is RightR
        
       
       digitalWrite(RightMotorForward, HIGH);    //M 
       digitalWrite(RightMotorBackward, LOW);
  
       digitalWrite(LeftMotorForward, LOW);
       digitalWrite(LeftMotorBackward, HIGH);

      break;
      
      case 'S':
       digitalWrite(PUMPWATERPIN, HIGH); 
       
        // This is RightR
        
       
       digitalWrite(RightMotorForward, LOW);    //M 
       digitalWrite(RightMotorBackward, LOW);
  
       digitalWrite(LeftMotorForward, LOW);
       digitalWrite(LeftMotorBackward, LOW);
       delay(4000);
		
      break;
      
      }

    }
}


