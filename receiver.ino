const int ldrPin = A0;

void setup() {
  Serial.begin(9600);
}


// read ldrValue continuously 
void loop() {
  int ldrValue = analogRead(ldrPin);
  Serial.println(ldrValue);
  delay(300); //same as for the  arduino program for LED
}
