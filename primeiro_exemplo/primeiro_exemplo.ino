#include<SoftwareSerial.h>
SoftwareSerial NEO6M(2, 3);

void setup() {
  Serial.begin(9600);

  NEO6M.begin(9600);

}

void loop() {
  while (NEO6M.available() > 0) {
    Serial.write(NEO6M.read());
  }

}
