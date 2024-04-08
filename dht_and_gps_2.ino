//#include <NMEAGPS.h>

//#include <Gpsneo.h>


//#include <neo6mGPS.h>
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

  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();
  String nmea_gps = receberDadosGPS();

  //Enviar os dados via XBee
  //xbeeSerial.print("T:");
  xbeeSerial.print("%f %f %s", temperature, humidity, nmea_gps);
  printf("%f %f %s", temperature, humidity, nmea_gps);
  //xbeeSerial.print(",H:");
  //xbeeSerial.println(humidity);

  //Serial.print("Dados enviados: ");
  //Serial.print("T:");
  /*Serial.print(temperature);
  Serial.print("|");
  Serial.print(humidity);
  Serial.print("|");
  Serial.println(nmea_gps);*/
   //Serial.print(", H:");
  //Serial.print("\n");
  //Serial.print(gps);
  //Serial.print("\n");

  delay(10000);
  
}

String receberDadosGPS() {
    String dados;
    while (NEO6M.available() > 0) {
        String c = NEO6M.read();
        dados += c;
    }
    return dados;
}
