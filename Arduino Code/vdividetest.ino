
const int analogInPin = A0;  

int sensorValue = 0;        // value read from the pot
int outputValue = 0;        // value output to the PWM (analog out)

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);
}

void loop() {
  sensorValue = analogRead(analogInPin);
  
  outputValue = map(sensorValue, 0, 1023, 0, 255);
  
  if (outputValue==50)
  {
    Serial.println("1");
   }
   else if (outputValue==101)
  {
    Serial.println("2");
   }
   else if (outputValue==254)
  {
    Serial.println("3");
   }
   else
   Serial.println("0");
  delay(2);
}
