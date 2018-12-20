#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
// เรียกใช้ไลบรารี่ WiFi.h และ IOXhop_FirebaseESP32.h มาใช้งาน
#include <WiFi.h>
#include <IOXhop_FirebaseESP32.h>
#include <time.h>
#include <DHT.h>

// Config Firebase
#define FIREBASE_HOST "dht22-esp8266-filebase.firebaseio.com"
#define FIREBASE_AUTH "eteOlOuCcaB78jhaYNtBAqdIbnyA9H2neMJ3iS5B"

// Config connect WiFi
#define WIFI_SSID "KMITL-WiFi"
#define WIFI_PASSWORD ""

// Config time server
int timezone = 7;
String DateandTime;
char ntp_server1[20] = "ntp.ku.ac.th";
char ntp_server2[20] = "fw.eng.ku.ac.th";
char ntp_server3[20] = "time.uni.net.th";
#define sense_Pin 32
int dst = 0;
int  i= 10;
float soilmoisture;
float soilmoisture_b;
void setup() 
{
  // connect to wifi.
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("connecting");
  Serial.begin(9600);
  while (WiFi.status() != WL_CONNECTED) 
  {
       Serial.print(".");
      delay(5);
  }
  Serial.print("connected: ");
  Serial.println(WiFi.localIP());
  
 //connet to time
  configTime(timezone * 3600, dst, ntp_server1, ntp_server2, ntp_server3);
  Serial.println("Waiting for time");
  while (!time(nullptr)) 
  {
    Serial.print(".");
    delay(5);
  }
  Serial.println();
  Serial.println("Now: " + Timenow());
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);

}

void loop() {
  // Read  soilmoisture 
    soilmoisture = analogRead(sense_Pin);
     soilmoisture_b = (soilmoisture*256)/5000;

  if (isnan(soilmoisture)) 
  {  
        Serial.println("Failed to read from sensor!");
        delay(1);
        return;
  }
  Serial.print("soilmoisture: ");
  Serial.print(soilmoisture_b);
  Serial.print(" %\t");
  Serial.println();

  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& root = jsonBuffer.createObject();
  root["humidity"] = soilmoisture;
  root["time"] = Timenow();
  root["date"] = Datenow();
  DateandTime = Datenow();

  // append a new value to soilmoisture
  String name = Firebase.push("MARCH", root);
                delay(1);
                Firebase.set("s-ruzi12",soilmoisture);

 if(soilmoisture_b > 200.0)
      {
              Firebase.set("s-ruzi12-SS12","Air");
              Serial.println("Air");        
      }    
  else if(soilmoisture_b <= 200 && soilmoisture_b >= 170 )
      {
              Firebase.set("s-ruzi12-SS12","Dry");
              Serial.println("Dry");          
      }

   else if (soilmoisture_b < 170)
      {
              Firebase.set("s-ruzi12-SS12","Wet");
              Serial.println("Wet");          
      }
   else 
   
         
      Firebase.set("s-ruzi12-SS12","broken");
      Serial.println("broken");
   }
  
  // handle error
  if (Firebase.failed()) {
      Serial.print("pushing /logSensor failed:");
      Serial.print(Firebase.error());  
      Serial.print (Timenow());
      delay(1);
      return;
  }
}

String Timenow() {
  time_t now = time(nullptr);
  struct tm* newtime = localtime(&now);

  String tmpNow = "";
  tmpNow += String(newtime->tm_hour + 12);
  tmpNow += ":";
  tmpNow += String(newtime->tm_min + 49);
  tmpNow += ":";
  tmpNow += String(newtime->tm_sec);
  return tmpNow;
 
}
String Datenow() {
  time_t now = time(nullptr);
  struct tm* newtime = localtime(&now);

  String tmpNow = "";
  tmpNow += String(newtime->tm_year + 1948);
  tmpNow += "-";
  tmpNow += String(newtime->tm_mon + 11);
  tmpNow += "-";
  tmpNow += String(newtime->tm_mday + 17);
  return tmpNow;
}
