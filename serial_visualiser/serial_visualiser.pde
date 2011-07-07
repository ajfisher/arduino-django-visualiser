/**

  Django Admin Visualiser (Serial)
  Serial version of the visualiser that waits for pulse commands to drive an RGB LED

  Author: Andrew Fisher
  source: https://github.com/ajfisher/arduino-django-visualiser
  version: 0.2
  Date: 4/07/2011
  
**/

#define RED_PIN 9
#define GREEN_PIN 10
#define BLUE_PIN 11

long value;

void setup() {
  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(BLUE_PIN, OUTPUT);
  digitalWrite(RED_PIN, HIGH);
  digitalWrite(GREEN_PIN, HIGH);
  digitalWrite(BLUE_PIN, HIGH);

  Serial.begin(2400);

}


void loop() {
  
  if(Serial.available()){
    
    char ch = Serial.read();
    
    if (ch >= '0' && ch<= '9') {
      value = (value * 10) + (ch - '0');
    }
    else if (ch == 10) {
      // newline so end of val.
      pulse(value);
      value=0;
    }
  }
}

void pulse(long pulsetime) {

 for (int i=255; i>=0; i-- ){
  analogWrite(RED_PIN, i); 
  analogWrite(BLUE_PIN, i);
  analogWrite(GREEN_PIN, i);
  delay(10);
 } 
 
 delay(pulsetime);

 for (int i=0; i<256; i++ ){
  analogWrite(RED_PIN, i); 
  analogWrite(BLUE_PIN, i);
  analogWrite(GREEN_PIN, i);
  delay(10);
 }

 Serial.println("0");
  
}
