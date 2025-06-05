#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT.h>
#include <ArduinoJson.h>
#include <time.h>  // Biblioteca para manipular hora

#define DHTPIN 4
#define DHTTYPE DHT22
#define MQ_PIN 32

const char* ssid = "Wokwi-GUEST";
const char* password = "";

const char* serverUrl = "https://api-sensor-e3edd8233f2e.herokuapp.com/api/sensor/";

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  randomSeed(analogRead(0));
  dht.begin();

  WiFi.begin(ssid, password);
  Serial.print("Conectando ao WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi conectado!");

  // Configura o fuso horário para UTC (0)
  configTime(0, 0, "pool.ntp.org", "time.nist.gov");  

  Serial.println("Sincronizando hora com NTP...");
  time_t now = time(nullptr);
  while (now < 8 * 3600 * 2) {  // espera até pegar a hora certa (pelo menos > 1970)
    delay(500);
    Serial.print(".");
    now = time(nullptr);
  }
  Serial.println("\nHora sincronizada!");
}

String getISO8601Time() {
  time_t now = time(nullptr);
  struct tm timeinfo;
  gmtime_r(&now, &timeinfo);

  char buf[25];
  // Formato ISO 8601 UTC: YYYY-MM-DDTHH:MM:SSZ
  strftime(buf, sizeof(buf), "%Y-%m-%dT%H:%M:%SZ", &timeinfo);
  return String(buf);
}

void loop() {
  float temperatura = random(200, 350) / 10.0;
  float umidade = random(300, 800) / 10.0;
  int mq2 = random(100, 1000);

  Serial.print("Temperatura simulada: ");
  Serial.print(temperatura);
  Serial.print(" °C | Umidade simulada: ");
  Serial.print(umidade);
  Serial.println(" %");

  Serial.print("Concentração simulada de Gases/Fumaça (MQ-2): ");
  Serial.println(mq2);

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverUrl);
    http.addHeader("Content-Type", "application/json");

    StaticJsonDocument<200> doc;
    doc["temperatura"] = temperatura;
    doc["umidade"] = umidade;
    doc["mq2"] = mq2;
    doc["timestamp"] = getISO8601Time();

    String jsonPayload;
    serializeJson(doc, jsonPayload);

    Serial.print("Enviando POST: ");
    Serial.println(jsonPayload);

    int httpResponseCode = http.POST(jsonPayload);

    if (httpResponseCode > 0) {
      Serial.print("Resposta HTTP: ");
      Serial.println(httpResponseCode);
      String resposta = http.getString();
      Serial.println("Resposta do servidor:");
      Serial.println(resposta);
    } else {
      Serial.print("Erro na requisição POST: ");
      Serial.println(httpResponseCode);
    }

    http.end();
  } else {
    Serial.println("WiFi desconectado");
  }

  Serial.println("-----------------------------");
  delay(5000);
}
