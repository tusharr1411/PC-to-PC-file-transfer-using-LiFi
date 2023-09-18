// Define the LED pin
int ledPin = 13;

void setup() {
  // Initialize the LED pin as an output
  pinMode(ledPin, OUTPUT);
  
  // Initialize the serial connection
  Serial.begin(9600);
}

void loop() {
  // Wait for data to be available on the serial port
  if (Serial.available() > 0) {
    // Read the next character from the serial port
    char c = Serial.read();
    
    // If the character is '1', turn the LED on
    if (c == '1') {
      digitalWrite(ledPin, HIGH);
    }
    
    // If the character is '0', turn the LED off
    else if (c == '0') {
      digitalWrite(ledPin, LOW);
    }
    
    // Wait for a short period of time ( this will define the speed of data transfer) ( same for the python script to send file over the serial  communication port)
    delay(300);
  }
}
