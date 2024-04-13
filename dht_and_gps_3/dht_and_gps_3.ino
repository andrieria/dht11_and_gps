
#include <DHT.h>
#include <SoftwareSerial.h>
#include <TinyGPS++.h>


#define DHTPIN 8
#define DHTTYPE DHT11
#define XBEE_RX 1   // Pino do Arduino conectado ao pino TX do módulo XBee
#define XBEE_TX 0   // Pino do Arduino conectado ao pino RX do módulo XBee
TinyGPSPlus gps;

DHT dht(DHTPIN, DHTTYPE);
SoftwareSerial xbeeSerial(XBEE_RX, XBEE_TX); // Inicialização da comunicação serial com o módulo XBee
SoftwareSerial NEO6M(2, 3);

void setup() {
 
  Serial.begin(9600);
  xbeeSerial.begin(9600); // Inicialização da comunicação serial com o módulo XBee
  dht.begin(9600);
  NEO6M.begin(9600);
}

void loop() {

  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();
  // nmea_gps = receberDadosGPS();


  //while (NEO6M.available() > 0) {
  Serial.print(temperature);
  Serial.print(" | ");
  Serial.print(humidity);
  Serial.print(" | ");
  while (NEO6M.available() > 0) {
    if (gps.encode(NEO6M.read())) {
      receberDadosGPS();
    }
  }

  if (millis() > 5000 && gps.charsProcessed() < 10) {
    Serial.println("GPS NOT DETECTED!");
    while(true);
  }
  //Serial.println(receberDadosGPS());
  //receberDadosGPS();
  Serial.println();
  //Serial.print(gps.encode(NEO6M.read()));
  /*if (gps.encode(NEO6M.read())){
    receberDadosGPS();
  };*/
  //Serial.print(";");
  //Serial.println("Acabou");
    

  delay(10000);
  
}

void receberDadosGPS(){
  if (gps.location.isValid()) {
    Serial.print(" | Latitude: ");
    Serial.print(gps.location.lat(), 6);
    Serial.print(" | Longitude: ");
    Serial.print(gps.location.lng(), 6);
    Serial.print(" | Altitude: ");
    Serial.print(gps.altitude.meters());
  } else {
    Serial.println("Location is not available");
  }
}



/*void receberDadosGPS(){
  while (NEO6M.available() > 0) {
    //gps_value = gps.encode(NEO6M.read());
    if (gps.encode(NEO6M.read()) && gps.location.isValid()) {
      Serial.print("Latitude: ");
      Serial.println(gps.location.lat(), 6);
      Serial.print(";");
      Serial.print("Longitude: ");
      Serial.println(gps.location.lng(), 6);
    } else {
      Serial.println("Location is not available");
    }
  }
}*/
