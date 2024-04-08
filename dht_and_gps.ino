#include <DHT.h>
#include <SoftwareSerial.h>



#define DHTPIN 7
#define DHTTYPE DHT11
#define XBEE_RX 1   // Pino do Arduino conectado ao pino TX do módulo XBee
#define XBEE_TX 0   // Pino do Arduino conectado ao pino RX do módulo XBee

DHT dht(DHTPIN, DHTTYPE);
SoftwareSerial xbeeSerial(XBEE_RX, XBEE_TX); // Inicialização da comunicação serial com o módulo XBee
SoftwareSerial NEO6M(2, 3);

void setup() {
  Serial.begin(9600);
  xbeeSerial.begin(9600); // Inicialização da comunicação serial com o módulo XBee
  dht.begin();
  NEO6M.begin(9600);
}

void loop() {
  while (NEO6M.available() > 0) {
    Serial.write(NEO6M.read());
  }

  delay(2000);
  int temperature = dht.readTemperature();
  int humidity = dht.readHumidity();

  //Enviar os dados via XBee
  //xbeeSerial.print("T:");
  xbeeSerial.print(temperature);
  //xbeeSerial.print(",H:");
  xbeeSerial.println(humidity);

  //Serial.print("Dados enviados: ");
  //Serial.print("T:");
  Serial.print(temperature);
  Serial.print(";");
  Serial.print(humidity);
   //Serial.print(", H:");
  Serial.print("\n");

  delay(10000);
}
