

#include <Servo.h> //the library which helps us to control the servo motor

unsigned char incomingByte = 0;
// set water pump 
uint8_t water_pump = 2;


// Motor A
const uint8_t RightMotorForward = 6;    // IN1
const uint8_t RightMotorBackward = 7;   // IN2

//Motor B
const uint8_t LeftMotorForward = 8;     // IN3
const uint8_t LeftMotorBackward = 9;    // IN4

Servo minion_servo;
void setup() 
{
  
  Serial.begin(9600);
  
  for (int thisPin = 2; thisPin < 7;  thisPin++) 
  {
  
  //motor output
    pinMode(water_pump,OUTPUT);
    pinMode(RightMotorForward , OUTPUT);
    pinMode(LeftMotorForward , OUTPUT);
    pinMode(LeftMotorBackward , OUTPUT);
    pinMode(RightMotorBackward , OUTPUT);

    Serial.begin(9600); 
    
    minion_servo.attach(14); //A0 
    
  }
}
// TODO: Seperate function for accessibility
void loop()
{
  // Check if serial available
  if (Serial.available() > 0) 
  
  {
    int inByte = Serial.read();   
    switch (inByte)
    {
      case 'M':

        digitalWrite(water_pump, LOW);
        for(uint8_t analog_val = 0; analog_val < 255 ; analog_val++)
        {
          analogWrite(RightMotorForward, analog_val);    
          analogWrite(RightMotorBackward, LOW);
          analogWrite(LeftMotorForward, analog_val);
          analogWrite(LeftMotorBackward, LOW);
          delay(50);
        }
        break;
      
      case 'B':
       
        digitalWrite(analog_val, LOW);
        for(uint8_t analog_val = 0; analog_val < 255 ; analog_val++)
        {
          analogWrite(RightMotorForward, LOW);    
          analogWrite(RightMotorBackward, analog_val);
          analogWrite(LeftMotorForward, LOW);
          analogWrite(LeftMotorBackward, analog_val);
          delay(50);
        }
        break;
      
      case 'L':
        
        digitalWrite(water_pump, LOW);
        digitalWrite(RightMotorForward, LOW);    
        digitalWrite(RightMotorBackward, HIGH);
        digitalWrite(LeftMotorForward, HIGH);
        digitalWrite(LeftMotorBackward, LOW);

        break;
      
      case 'R':

        digitalWrite(water_pump, LOW); 
        digitalWrite(RightMotorForward, HIGH);    
        digitalWrite(RightMotorBackward, LOW);
        digitalWrite(LeftMotorForward, LOW);
        digitalWrite(LeftMotorBackward, HIGH);

        break;
      
      case 'S':
       
        digitalWrite(water_pump, LOW);
        digitalWrite(RightMotorForward, LOW);    
        digitalWrite(RightMotorBackward, LOW);
        digitalWrite(LeftMotorForward, LOW);
        digitalWrite(LeftMotorBackward, LOW);
		
        break;
      
    }
  }
}
