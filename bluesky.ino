#include "Wire.h"    // imports the wire library for talking over I2C
#include "Adafruit_BMP085.h" 
Adafruit_BMP085 sensor;  // create sensor object called mySensor
 
float tempC;  // Variable for holding temp in C
float pressure; //Variable for holding pressure reading
 
void setup(){
Serial.begin(9600); //turn on serial monitor
sensor.begin();   //initialize mySensor
}
 
void loop() {
tempC = sensor.readTemperature(); 
//  Read Temperature
pressure = sensor.readPressure(); 

//Read Pressure
Serial.print(tempC);
Serial.print(",");
Serial.println(pressure); 
delay(10);
}

