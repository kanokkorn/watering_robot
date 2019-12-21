#include <SparkFun_MAG3110.h>

MAG3110 mag = MAG3110(); //Instantiate MAG3110

void setup() {
  Serial.begin(9600);

  mag.initialize(); //Initialize the MAG3110
}

void loop() {

  int x, y, z;

  if(!mag.isCalibrated()) //If we're not calibrated
  {
    if(!mag.isCalibrating()) //And we're not currently calibrating
    {
      Serial.println("Entering calibration mode");
      mag.enterCalMode(); //This sets the output data rate to the highest possible and puts the mag sensor in active mode
    }
    else
    {
      //Must call every loop while calibrating to collect calibration data
      //This will automatically exit calibration
      //You can terminate calibration early by calling mag.exitCalMode();
      mag.calibrate(); 
    }
  }
  else
  {
    Serial.println("Calibrated!");
  }
  mag.readMag(&x, &y, &z);

  Serial.print("X: ");
  Serial.print(x);
  Serial.print(", Y: ");
  Serial.print(y);
  Serial.print(", Z: ");
  Serial.println(z);

  Serial.print("Heading: ");
  Serial.println(mag.readHeading());

  Serial.println("--------");

  delay(500);
}
