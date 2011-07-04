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

int value;
int blinkrate;

void setup() {
  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(BLUE_PIN, OUTPUT);
  digitalWrite(RED_PIN, HIGH);
  digitalWrite(GREEN_PIN, HIGH);
  digitalWrite(BLUE_PIN, HIGH);

  Serial.begin(9600);

}


void loop() {
  byte brightness;
  
  if(Serial.available()){
    
    char ch = Serial.read();
    
    if (ch >= '0' && ch<= '9') {
      value = (value * 10) + (ch - '0');
    }
    else if (ch == 10) {
      // newline so end of val.
      blinkrate = value;
      value=0;
  
      pulse(blinkrate);
    }
  }
}

void pulse(int pulsetime) {

 for (int i=255; i>=0; i-- ){
  analogWrite(RED_PIN, i); 
  analogWrite(BLUE_PIN, i);
  analogWrite(GREEN_PIN, i);
  delay(5);
 } 
 
 delay(pulsetime);

 for (int i=0; i<256; i++ ){
  analogWrite(RED_PIN, i); 
  analogWrite(BLUE_PIN, i);
  analogWrite(GREEN_PIN, i);
  delay(5);
 }

 Serial.println("0");
  
}
