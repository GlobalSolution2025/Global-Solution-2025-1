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

###### **1. Fluxo de Dados** 

1. **Coleta de Dados:**

   * O **ESP32** realiza leituras periódicas de sensores de umidade do solo, temperatura e gases no ar.
   * Dados enviados via **Wi-Fi** ou **Bluetooth** para servidor ou dashboard.

2. **Exibição Local:**

   * Dados principais (umidade, temperatura, qualidade do ar) são exibidos em tempo real.

3. **Transmissão e Armazenamento:**

   * Dados transmitidos para um **servidor** ou **banco de dados** (MySQL, PostgreSQL ou Firebase).
   * Utilizado para **armazenamento histórico** e **treinamento de modelo**.

4. **Processamento e Predição:**

   * O modelo de **Machine Learning** treinado com **Scikit-learn** recebe dados históricos.

5. **Visualização:**

   * **Streamlit** apresenta:

     * Dashboard com gráficos históricos.
     * Predições do modelo.

6. **Ação:**

   * Caso a predição indique algum risco de incêncio, o **ESP32** ativa o sistema de alerta.

7. **Monitoramento em Tempo Real:**

   * **Serial Plotter** no **Wokwi** para monitorar variáveis críticas (umidade, temperatura, qualidade do ar).

---

###### **Arquitetura de Dados**

| Origem                | Tipo de dado                           | Destino                      |
| --------------------- | -------------------------------------- | ---------------------------- |
| Sensor de umidade     | Numérico contínuo                      | ESP32 → LCD → Banco de Dados |
| Sensor de nutrientes  | Numérico contínuo                      | ESP32 → LCD → Banco de Dados |
| Sensor de temperatura | Numérico contínuo                      | ESP32 → Banco de Dados       |
| Predição de ML        | Binário (0 - não irrigar, 1 - irrigar) | Streamlit → ESP32            |

---

### **Hardware Utilizado**

* **ESP32** — microcontrolador central.
* **Sensores** — umidade, temperatura.
* **Servidor ou PC** — para rodar modelo de ML e banco de dados.
* **PC com Streamlit** — dashboard interativo.

---

### **Software Utilizado**

| Componente          | Tecnologia                    |
| ------------------- | ----------------------------- |
| Sistema embarcado   | C/C++ para ESP32              |
| Monitoramento       | Serial Plotter (Wokwi)        |
| Exibição local      | LCD I2C                       |
| Modelagem preditiva | Python com Scikit-learn       |
| Dashboard           | Python com Streamlit          |
| Banco de dados      | MySQL / PostgreSQL / Firebase |
| Versionamento       | GitHub                        |

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

###  **Machine Learning**

#### Tabelas — Modelos de Machine Learning para o FireGuard

---

##### Modelos Recomendados

| Modelo                       | Vantagens                                                       | Desvantagens                                       | Aplicação                                  |
| ---------------------------- | --------------------------------------------------------------- | -------------------------------------------------- | ------------------------------------------ |
| Random Forest                | Robusto, boa generalização, interpreta variáveis importantes    | Pode ser mais lento com muitos dados               | Classificação multinível de risco          |
| Regressão Logística          | Simples, rápido, eficiente para classificações binárias         | Pode ter baixa precisão em relações não-lineares   | Classificação binária: risco ou não        |
| Gradient Boosting (XGBoost)  | Alta precisão, bom para dados complexos                         | Mais lento para treinar, mais difícil de ajustar   | Classificação multinível de risco          |
| K-Nearest Neighbors (KNN)    | Fácil implementação, funciona bem com poucos dados              | Não escala bem com grandes datasets                | Classificação baseada em vizinhos próximos |
| Support Vector Machine (SVM) | Eficiente em alta dimensão, suporta classificações não-lineares | Difícil de ajustar e interpretar, sensível a ruído | Classificação com dados complexos          |

---

#### Variáveis de Entrada (Features)

| Variável                    | Tipo       | Origem                |
| --------------------------- | ---------- | --------------------- |
| Temperatura do ar (°C)      | Numérico   | Sensor DHT11/DHT22    |
| Umidade relativa (%)        | Numérico   | Sensor DHT11/DHT22    |
| Concentração de gases (ppm) | Numérico   | Sensor MQ-2 ou MQ-135 |
| Fumaça (ppm)                | Numérico   | Sensor MQ-2 ou MQ-135 |
| Histórico meteorológico     | Numérico   | Dados externos        |
| Hora do dia, data           | Categórico | Sistema interno       |

---

####  Variável de Saída (Target)

| Saída             | Tipo                     | Valores                        |
| ----------------- | ------------------------ | ------------------------------ |
| Risco de incêndio | Classificação            | Baixo, Moderado, Alto, Crítico |
|                   | ou Classificação Binária | 0: Sem risco, 1: Com risco     |

---

#### Pipeline de Machine Learning

| Etapa             | Descrição                                          |
| ----------------- | -------------------------------------------------- |
| Coleta de dados   | Dados do ESP32 ou datasets públicos                |
| Pré-processamento | Limpeza, normalização, engenharia de atributos     |
| Treinamento       | Divisão em treino, validação e teste               |
| Avaliação         | Métricas: Accuracy, Precision, Recall, F1, AUC-ROC |
| Deploy            | API local ou na nuvem, integração com ESP32        |

---

#### Bibliotecas Recomendadas (Python)

| Categoria             | Biblioteca                      |
| --------------------- | ------------------------------- |
| Modelos ML            | Scikit-learn, XGBoost, LightGBM |
| Manipulação de Dados  | Pandas, NumPy                   |
| Visualização          | Matplotlib, Seaborn             |
| Dashboard             | Streamlit                       |
| Comunicação com ESP32 | Flask, FastAPI, MQTT libraries  |
| Versionamento         | GitHub                          |

---

#### Critérios para Escolha do Modelo Final

| Critério                          | Importância |
| --------------------------------- | ----------- |
| Acurácia                          | Alta        |
| Velocidade de inferência          | Média/Alta  |
| Capacidade de interpretação       | Alta        |
| Facilidade de integração (Python) | Alta        |
| Robustez com dados ruidosos       | Alta        |

---

#### Resultado Esperado

| Resultado                                             | Benefício                               |
| ----------------------------------------------------- | --------------------------------------- |
| Classificação automática do risco de incêndio         | Ações preventivas e resposta rápida     |
| Sistema de alertas preventivos                        | Proteção ambiental e social             |
| Base para futuras integrações com imagens de satélite | Expansão do sistema para maior precisão |

---

**Justificativa:**

* O **ESP32** possui limitações de memória e processamento, inadequadas para executar modelos mais complexos de ML.
* A execução em um **servidor** ou **PC local** permite:

  * Utilização de algoritmos como **Random Forest**, **Gradient Boosting**.
  * Treinamento e inferência mais rápidos.
  * Facilidade de integração com **Streamlit**.
* O **ESP32** receberá apenas o resultado da predição (por exemplo, via MQTT, HTTP ou WebSocket).

---

##### Resumo Gráfico do Fluxo

```plaintext
[Sensores] → ESP32 → [Display LCD + Serial Plotter] 
                          ↓
                [Banco de Dados] ←→ [ML - Scikit-learn]
                          ↓
                   [Streamlit Dashboard]
```

##### **Ferramentas:**

* Python (Pandas, Scikit-Learn, NumPy, Streamlit);
* Dataset real ou simulado com base em:

  * Dados de estações meteorológicas;
  * Dados de incêndios passados.

##### **Pipeline:**

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
