int sensor_pin = A4;

const int analogInPin = A1; 

// connect 5v to vcc
//connect gnd to gnd 
// connect A4 to AO

int output_value ;
//declaring raw sensor values
int dry_value = 1023;
int wet_value = 275;
//converting to percent values
int friendlyDryValue = 0;
int friendlyWetValue = 100;
int sensorValue = 0; 

double maxValueRain = 425;
int minValueRain = 0;
double calc;




void setup() {

   Serial.begin(9600);

   Serial.println("Reading From the Sensor ...");

   delay(2000);

   }

void loop() {

   int rawValue= analogRead(sensor_pin);// loop reads sensor value
    //Serial.println(" Refreshing  soil sensor ");
   // Serial.print("Raw value of soil sensor : ");
   Serial.print(" soil raw:");
    Serial.print(rawValue);
    
    //Serial.print(" | ");  
    int friendlyValue = map(rawValue, dry_value, wet_value, friendlyDryValue, friendlyWetValue);// maps raw to percent value
  
    //Serial.print("Friendly: ");
    Serial.print(" | soil percent:");
    Serial.print( friendlyValue);//prints precent value
    //Serial.println("%");
    //set delay of 10 seconds
    delay(10000);


    //Serial.println("refreshing rain sensor");
    //Serial.print(" rain sensor = Sensor = " ); 
    
    sensorValue = analogRead(analogInPin);

    calc = ((sensorValue/maxValueRain)) * 100;
    Serial.println(" | rain raw:");
    Serial.println(calc); 
    //Serial.println("Raw value of rain sensor");
    Serial.println(" | rain percent:");
    Serial.println(sensorValue);
    //Serial.println("% of rain sensor");
    delay(10000);


    
   

   //output_value = map(output_value,550,0,0,100);

  
   

   }
   
