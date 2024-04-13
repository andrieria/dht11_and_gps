#include <DHT.h>          // Biblioteca para o sensor DHT11
#include <TinyGPS++.h>    // Biblioteca para o módulo GPS
#include <SoftwareSerial.h>

#define DHTPIN 8         // Pino ao qual o sensor DHT11 está conectado
#define DHTTYPE DHT11    // Tipo do sensor DHT

#define RXPin 2          // Pino RX do módulo GPS
#define TXPin 3          // Pino TX do módulo GPS

DHT dht(DHTPIN, DHTTYPE);   // Inicialização do objeto DHT
TinyGPSPlus gps;            // Inicialização do objeto TinyGPS++
SoftwareSerial gpsSerial(RXPin, TXPin);  // Inicialização da comunicação serial para o módulo GPS

void setup() {
  Serial.begin(9600);       // Inicialização da comunicação serial com o computador
  gpsSerial.begin(9600);     // Inicialização da comunicação serial com o módulo GPS
  dht.begin();               // Inicialização do sensor DHT11
}

void loop() {
  // Leitura dos dados do sensor DHT11
  float temperature = dht.readTemperature();   // Leitura da temperatura
  float humidity = dht.readHumidity();         // Leitura da umidade

  // Verifica se a leitura do DHT11 foi bem-sucedida
  if (!isnan(temperature) && !isnan(humidity)) {
    // Exibe os dados do sensor DHT11
    Serial.print("Temperature: ");
    Serial.print(temperature);
    Serial.print(" °C | Humidity: ");
    Serial.print(humidity);
    Serial.println(" %");

    // Leitura e exibição dos dados do módulo GPS
    while (gpsSerial.available() > 0) {
      if (gps.encode(gpsSerial.read())) {
        showGPSData();
      }
    }
  } else {
    Serial.println("Failed to read from DHT sensor!");
  }

  delay(5000);  // Aguarda 5 segundos antes da próxima leitura
}

void showGPSData() {
  if (gps.location.isValid()) {
    Serial.print("Latitude: ");
    Serial.print(gps.location.lat(), 6);
    Serial.print(" | Longitude: ");
    Serial.print(gps.location.lng(), 6);
    Serial.print(" | Altitude: ");
    Serial.print(gps.altitude.meters());
    Serial.println(" meters");
  } else {
    Serial.println("GPS data is not valid");
  }
}
