

#define BLUE_PIN 9
#define RED_PIN 10
#define GREEN_PIN 11
#define R2 3
#define G2 5
#define B2 6

int value;
int blinkrate;

void setup() {
  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(BLUE_PIN, OUTPUT);
  pinMode(R2, OUTPUT);
  pinMode(G2, OUTPUT);
  pinMode(B2, OUTPUT);
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
 
 for (int i=0; i<256; i++ ){
  analogWrite(RED_PIN, i); 
  analogWrite(BLUE_PIN, i);
  analogWrite(GREEN_PIN, i);
  analogWrite(R2, i); 
  analogWrite(B2, i);
  analogWrite(G2, i);
  delay(5);
 }
 
 delay(pulsetime);
 
 for (int i=255; i>=0; i-- ){
  analogWrite(RED_PIN, i); 
  analogWrite(BLUE_PIN, i);
  analogWrite(GREEN_PIN, i);
  analogWrite(R2, i); 
  analogWrite(B2, i);
  analogWrite(G2, i);
  delay(5);
 }
  
}
