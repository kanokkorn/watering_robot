#include <Wire.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x3F,20,4);
int value = A0;
void setup() {
lcd.begin();
Serial.begin(9600);
lcd.setCursor(5,0);
lcd.print("KMITL PCC");
lcd.setCursor(5,1);
lcd.print("WELCOME TO");
lcd.setCursor(3,2);
lcd.print("SOIL NPK METER");
lcd.setCursor(2,3);
lcd.print("FOR COCONUT FARM");
delay(5000);
lcd.clear();
lcd.setCursor(8,1);
lcd.print("READY");

//use to turn off and turn Display 3 time
{ 
   lcd.noDisplay();
   delay(1000);
   lcd.display();
   delay(1000);
}
{ 
   lcd.noDisplay();
   delay(1000);

   lcd.display();
   delay(1000);
}
{
   lcd.noDisplay();
   delay(1000);
   lcd.display();
   delay(1000);
}
//use to clear Display
lcd.clear();
delay(1000);
}
   void loop()
{
   lcd.setCursor(1,0);
   lcd.print("SOIL NPK METER");
   if(value<5)
{
   lcd.setCursor(16,0);
   lcd.print("       ");
   lcd.setCursor(16,0);
   lcd.print(0);
}else
{
   lcd.setCursor(16,0);
   lcd.print("       ");
   lcd.setCursor(16,0);
   lcd.print(value);
}
//Read analog signal
value = analogRead(A0);
Serial.println(value); //Print value to Serial Port
delay(1000); //delay for 1 second


float hug = (0.2689*value)-14.277;
if(value<5)
{
   lcd.setCursor(2,1);
   lcd.print("N = ");
   lcd.setCursor(6,1);
   lcd.print("       ");
   lcd.setCursor(6,1);
   lcd.print(0);
   lcd.setCursor(15,1);
   lcd.print("ppm");
}else
{
   lcd.setCursor(2,1);
   lcd.print("N = ");
   lcd.setCursor(6,1);
   lcd.print("       ");
   lcd.setCursor(6,1);
   lcd.print(hug);
   lcd.setCursor(15,1);
   lcd.print("ppm");
}

float lucky = (0.0184*value)-0.6373;
if(value<5)
{
   lcd.setCursor(2,2);
   lcd.print("P = ");
   lcd.setCursor(6,2);
   lcd.print("       ");
   lcd.setCursor(6,2);
   lcd.print(0);
   lcd.setCursor(15,2);
   lcd.print("ppm");
}else
{
   lcd.setCursor(2,2);
   lcd.print("P = ");
   lcd.setCursor(6,2);
   lcd.print("       ");
   lcd.setCursor(6,2);
   lcd.print(lucky);
   lcd.setCursor(15,2);
   lcd.print("ppm");
}

float smile = (0.2689*value)-14.277;
if(value<5)
{
   lcd.setCursor(2,3);
   lcd.print("K = ");
   lcd.setCursor(6,3);
   lcd.print("       ");
   lcd.setCursor(6,3);
   lcd.print(0);
   lcd.setCursor(15,3);
   lcd.print("ppm");
}else
{
   lcd.setCursor(2,3);
   lcd.print("K = ");
   lcd.setCursor(6,3);
   lcd.print("       ");
   lcd.setCursor(6,3);
   lcd.print(smile);
   lcd.setCursor(15,3);
   lcd.print("ppm");
}
}

