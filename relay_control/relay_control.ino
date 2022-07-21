int data;

void setup() 
{ 
  Serial.begin(9600); 
  pinMode(LED_BUILTIN,OUTPUT);
  digitalWrite (LED_BUILTIN, LOW);  // Set to LOW so it starts as closed
}
 
void loop() 
{

while (Serial.available())
  {
    data = Serial.read();  // Listening serial port
  }

  if (data == '1')
  digitalWrite (LED_BUILTIN, HIGH);  // Trigger pin for turn on LEDS
  
  else if (data == '0')
  digitalWrite (LED_BUILTIN, LOW);  // Trigger pin for turn off LEDS
  
}
