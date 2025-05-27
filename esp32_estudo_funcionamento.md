# Estudo do Funcionamento do ESP32

## 1 · Objetivo
Este estudo cumpre a primeira tarefa do desafio: entender o funcionamento do ESP32.

## 2 · Características Elétricas do ESP32 (ESP32‑WROOM‑32)

| Parâmetro | Valor típico / faixa | Observações |
|-----------|----------------------|-------------|
| Tensão de alimentação (VDD) | 3,0 – 3,6 V (típico: 3,3 V) | Conforme datasheet |
| Corrente máxima por GPIO | 40 mA (absoluto); **recomendado: até 20 mA** | Pode danificar o chip acima disso |
| Corrente de pico do módulo | ≥ 500 mA durante transmissão Wi‑Fi | Importante para fontes externas |
| Resolução do ADC | 12 bits (faixa 0–3,3 V) | Varia conforme canal |
| Resolução do DAC | 8 bits (GPIO 25 e 26) | Saída analógica |
| Wi‑Fi | 802.11 b/g/n até 150 Mbps | Embutido no chip |
| Bluetooth | Clássico + BLE v4.2 | |

## 3 · Mapeamento de Pinos (ESP32 DevKit v1)

| GPIO | Função principal | Observações |
|------|------------------|-------------|
| 1 / 3 | UART0 TX/RX | Usado para gravação serial |
| 21 / 22 | I²C SDA / SCL (padrão) | Pode ser remapeado |
| 18 / 19 / 23 / 5 | SPI (VSPI) | MOSI / MISO / CLK / CS |
| 25 / 26 / 27 / 32 / 33 | ADC disponíveis | 12 bits |
| 34 a 39 | Somente entrada (ADC) | Sem pull-up interno |
| 0, 2, 4, 12, 15 | Pinos de boot | Cuidado ao usar |
| 25 / 26 | DAC | Saída analógica |

Para referência visual, veja o [diagrama de pinos do ESP32 DevKit v1](https://www.circuitstate.com/pinouts/doit-esp32-devkit-v1-wifi-development-board-pinout-diagram-and-reference/).

## 4 · Código de Teste: “Hello, ESP32”

```cpp
#include <Arduino.h>

void setup() {
  Serial.begin(115200);
  delay(1000); // Aguarda inicialização USB
}

void loop() {
  Serial.println("ESP32 OK");
  delay(2000);
}
```

## 5 · Saída Esperada

```
10:01:47.000 -> ESP32 OK
10:01:49.004 -> ESP32 OK
10:01:51.005 -> ESP32 OK
```


## 6 · Referências Bibliográficas

- **Espressif Systems.** [ESP32-WROOM-32 Datasheet v3.9 (EN)](https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32_datasheet_en.pdf)  
  Documento técnico oficial com tensões, correntes, pinos e características físicas do módulo.

- **Espressif Systems.** [ESP32 Technical Reference Manual v4.2 (EN)](https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_en.pdf)  
  Guia completo de funcionamento interno do ESP32: periféricos, ADC, DAC, UART, SPI, modos de boot, etc.

- **CircuitState.** [ESP32 DevKit v1 Pinout Diagram (CC BY-SA)](https://www.circuitstate.com/pinouts/doit-esp32-devkit-v1-wifi-development-board-pinout-diagram-and-reference/)  
  Imagem colorida e explicativa dos pinos da placa de desenvolvimento ESP32 DevKit v1.
