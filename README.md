# 🔥 **FireGuard - Sistema Inteligente de Prevenção de Incêndios Florestais**

**Global Solution 2025 - 1**

---

## 1. 🏷️ **Capa**

* **Projeto:** FireGuard - Sistema Inteligente de Prevenção de Incêndios Florestais
* **Integrantes:** \[Nomes dos participantes]
* **Instituição:** \[Nome da instituição]
* **Disciplina:** Global Solution 2025

---

## 2. 📖 **Introdução**

Os incêndios florestais têm se intensificado nos últimos anos, gerando impactos ambientais, econômicos e sociais significativos. As principais causas incluem mudanças climáticas, ação humana e períodos prolongados de seca.

O desafio do nosso projeto é desenvolver uma solução capaz de **prever e detectar incêndios florestais antes que eles se tornem incontroláveis**, utilizando uma combinação de sensores ambientais, microcontroladores (ESP32) e algoritmos de Machine Learning.

### 🎯 **Justificativa**

* Preservar o meio ambiente, a fauna, a flora e vidas humanas;
* Reduzir os custos e danos associados ao combate de incêndios;
* Utilizar tecnologia acessível e de baixo custo para monitoramento contínuo.

### 🔗 **Integração IoT + Machine Learning**

Nosso sistema une:

* 🔥 **Sensores** (temperatura, umidade, gases e fumaça);
* 🔌 **ESP32** como unidade de coleta e transmissão de dados;
* 🧠 **Machine Learning** para análise e predição de risco;
* 📲 Interface de alertas para moradores e autoridades.

---

## 3. 🏗️ **Desenvolvimento**

### 🔧 **Arquitetura da Solução**

#### 🗺️ **Diagrama da Arquitetura**

```
[Sensores no Ambiente]
   ↓
[ESP32] ---> [API/MQTT] ---> [Servidor com ML em Python]
                                     ↓
                         [Análise + Predição de Risco]
                                     ↓
              [Interface: Dashboard + Alertas (E-mail, LED, Buzzer)]
```

#### 🎨 **Descrição dos Componentes**

* **Sensores:**

  * 🔥 Temperatura e Umidade (DHT11/DHT22)
  * 🔥 Gás e Fumaça (MQ-2, MQ-135)

* **ESP32:**

  * Coleta dados dos sensores;
  * Envia dados via Wi-Fi (MQTT ou HTTP) para o servidor.

* **Servidor com Machine Learning (Python):**

  * Recebe dados dos sensores em tempo real;
  * Executa modelo preditivo para avaliar risco de incêndio;
  * Gera alertas com níveis: **Baixo, Moderado, Alto, Crítico**.

* **Interface:**

  * Dashboard Web (opcional - Streamlit);
  * Alertas locais (buzzer, LED no ESP32);
  * Alertas digitais (e-mail, SMS ou notificação no dashboard).

---

### 🧠 **Machine Learning**

* **Modelo:** Classificação (Random Forest ou Regressão Logística)
* **Objetivo:** Classificar o nível de risco de incêndio com base em:

  * Temperatura;
  * Umidade do ar;
  * Concentração de gases (fumaça, CO₂, CO).

#### ⚙️ **Ferramentas:**

* Python (Pandas, Scikit-Learn, NumPy, Streamlit);
* Dataset real ou simulado com base em:

  * Dados de estações meteorológicas;
  * Dados de incêndios passados.

#### 🔄 **Pipeline:**

1. **Coleta:** Dados do ESP32 ou datasets históricos;
2. **Pré-processamento:** Limpeza e padronização dos dados;
3. **Treinamento:** Com algoritmos de classificação;
4. **Validação:** Testes de precisão, recall e F1-score;
5. **Deploy:** API local ou na nuvem para receber dados e retornar risco.

---

### 📡 **ESP32 + Sensores**

* **Sensores utilizados:**

  * DHT11/DHT22 → Temperatura e Umidade;
  * MQ-2/MQ-135 → Fumaça e Gases inflamáveis.

* **Comunicação:**

  * Via Wi-Fi, utilizando protocolos MQTT ou HTTP.

* **Fluxo de Dados:**

  1. Leitura periódica dos sensores (ex.: a cada 5 minutos);
  2. Envio dos dados para a API do servidor com ML;
  3. Recebimento da resposta (nível de risco);
  4. Acionamento de alertas locais (LED, buzzer) se o risco for alto ou crítico.

---

### 🖥️ **Integração Geral**

* O ESP32 atua como cliente, coletando dados dos sensores e enviando para o servidor Python.
* O servidor executa o modelo treinado e retorna uma resposta com o nível de risco.
* A resposta pode ser exibida em:

  * Painéis (Streamlit);
  * Aplicativos;
  * Alertas físicos no próprio dispositivo.

---

## 4. 🚀 **Resultados Esperados**

### ✅ **Funcionamento Esperado:**

* Monitoramento ambiental em tempo real;
* Detecção de condições favoráveis ao início de incêndios;
* Geração de alertas imediatos para prevenção.

### 🌟 **Benefícios da Solução:**

* Eficiência no combate preventivo;
* Proteção ambiental e social;
* Redução dos custos operacionais;
* Sistema de baixo custo, escalável e replicável.

### 📸 **Evidências:**

* Prints dos dashboards;
* Fotos do ESP32 com sensores funcionando;
* Prints dos alertas acionados;
* Print do modelo de ML rodando e processando dados.

---

## 5. 🔍 **Conclusão**

O **FireGuard** demonstra como a integração de IoT e Machine Learning pode transformar a prevenção de desastres ambientais. Apesar dos desafios técnicos na comunicação e calibragem dos sensores, o MVP entrega resultados promissores.

### 🚧 **Limitações:**

* Acurácia dependente da qualidade dos sensores;
* Latência na transmissão dependendo da rede Wi-Fi;
* Dataset inicial pode ser limitado, precisando de mais dados reais para aumentar a precisão.

### 🔥 **Melhorias Futuras:**

* Integração com imagens de satélite (NDVI, MODIS);
* Uso de LoRa para comunicação de longa distância em áreas sem Wi-Fi;
* Dashboard mobile para alertas mais rápidos;
* Inclusão de IA embarcada no próprio ESP32 (TinyML).

---

## 6. 📎 **Anexos**

* ✔️ Códigos comentados (ESP32 e Python);
* ✔️ Diagramas elétricos do circuito (ESP32 + sensores);
* ✔️ Diagrama da arquitetura do sistema;
* ✔️ Link do vídeo de demonstração (**Não listado no YouTube**);
* ✔️ Referências de datasets e bibliografia técnica.
