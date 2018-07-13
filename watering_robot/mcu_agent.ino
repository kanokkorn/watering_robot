
String state;
int Pin_F_R = 9;
int Pin_B_R = 10;// LED connected to digital pin 9
int Pin_F_L = 11;
int Pin_B_L = 12;
int Pin_WR  = 13;
void setup() {
  Serial.begin(115200);
}
void loop() {
    int fadeValue1 = 150;
    int fadeValue2 = 150;
    Serial.read();
    delay(300);
    if (Serial.available() != 0){
      state = Serial.readString();
      if (state == "Forward"){
        Serial.println(state);
        analogWrite(Pin_F_R, fadeValue1);
        analogWrite(Pin_F_L, fadeValue1);
        delay(3000);
        }
      if (state == "Backward"){
        Serial.println(state);
        analogWrite(Pin_F_R, fadeValue1);
        analogWrite(Pin_F_L, fadeValue1);
        delay(3000);
        }
       if (state == "Right"){
        Serial.println(state);
        analogWrite(Pin_F_R, fadeValue1);
        analogWrite(Pin_B_L, fadeValue1);
        delay(3000);
        }
       if (state == "Left"){
        Serial.println(state);
        analogWrite(Pin_F_L, fadeValue1);
        analogWrite(Pin_B_R, fadeValue1);
        delay(3000);
        }
      if (state == "Stop"){
        Serial.println(state);
        analogWrite(Pin_F_L, 0);
        analogWrite(Pin_B_R, 0);
        delay(3000);
        digitalWrite(Pin_WR, 1);
        delay(10000);
      }
      }
 }
