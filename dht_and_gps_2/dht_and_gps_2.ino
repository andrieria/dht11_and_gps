//#include <NMEAGPS.h>

//#include <Gpsneo.h>


//#include <neo6mGPS.h>
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
  dht.begin();
  NEO6M.begin(9600);
}

void loop() {

  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();
  //String nmea_gps = receberDadosGPS();

  //Enviar os dados via XBee
  //xbeeSerial.print("T:");

  //while (NEO6M.available() > 0) {
    Serial.print(temperature);
    Serial.print(humidity);
    if (gps.encode(NEO6M.read())){
      receberDadosGPS();
    };
      

  /*if (millis() > 5000 && gps.charsProcessed() < 10) {
    Serial.println("GPS NOT DETECTED!");
    while(true);
  }*/
  }
  
  //xbeeSerial.print("Testando %f %f %s", temperature, humidity, nmea_gps);
  //printf("Testando %f %f %s", temperature, humidity, nmea_gps);
  //Serial.print(nmea_gps);




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

void receberDadosGPS(){
  while (NEO6M.available() > 0) {
    if (gps.location.isValid()) {
      Serial.print(gps.location.lat(), 6);
      Serial.print(";");
      Serial.print(gps.location.lng(), 6);
    } else {
      Serial.println("Location is not available");
    }
  }
}

/*void showData()
{
  if (gps.location.isValid()) {
    Serial.print("Latitude: ");
    Serial.println(gps.location.lat(), 6);
    Serial.print("Longitude: ");
    Serial.println(gps.location.lng(), 6);
  }else {
    Serial.println("Location is not available");
  }
}*/


/*String receberDadosGPS() {
    String dados;
    while (NEO6M.available() > 0) {
        //int c = NEO6M.read();
        //String c = NEO6M.readString();
        //dados += c;
        Serial.write(NEO6M.read());
    }
    //return dados;
}
*/
