int STROBE_PIN = 2;
int RESET_PIN = 3;
int ANALOG_PIN = A0;
 
int bandValues[7];
int bandNo;
 
char buf[4];
 
void setup()
{
  Serial.begin(9600);
 
  pinMode(RESET_PIN, OUTPUT);
  pinMode(STROBE_PIN, OUTPUT);
 
  // RESET
  digitalWrite(RESET_PIN, LOW);
  digitalWrite(STROBE_PIN, HIGH);
}
 
void readMSGEQ7()
{
  digitalWrite(RESET_PIN, HIGH);
  digitalWrite(RESET_PIN, LOW);
 
  for (bandNo = 0; bandNo < 7; bandNo++)
  {
    digitalWrite(STROBE_PIN, LOW);
    delayMicroseconds(30);
    bandValues[bandNo] = analogRead(ANALOG_PIN);
    digitalWrite(STROBE_PIN, HIGH);
  }
}
 
void loop()
{
  // pobieramy amplitudy
  readMSGEQ7();
 
  // wyswietlamy kolejne zakresy
  for (bandNo = 0; bandNo < 7; bandNo++)
  {
    sprintf(buf, "%4d", bandValues[bandNo]);
    
    Serial.print(buf);
    Serial.print(" ");
  }
 
  Serial.println();
}
