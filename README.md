# FIAP - Faculdade de Informática e Administração Paulista 

<p align="center">
  <a href="https://www.fiap.com.br/">
    ![logo-fiap](https://github.com/user-attachments/assets/e188b677-da62-4d5a-9c55-19ded1723126)
  </a>
</p>


<br>

# 🔥 Fire Monitoring - Sistema de Alerta de Incêndios (Global Solution 2025/1)
## 👨‍🎓 **Integrantes:**

- Antônio Ancelmo Neto barros
```
 - RM: rm563683
 - E-mail: antonio.anbarros@gmail.com
 - GitHub: [@AntonioBarros19](https://github.com/AntonioBarros19)
```
- Beatriz Pilecarte de Melo
```
 - RM: rm564952
 - E-mail: beatrizpilecartedemelo@gmail.com
 - GitHub: [@BPilecarte](https://github.com/BPilecarte)
```
- Francismar Alves Martins Junior
```
 - RM: m562869
 - E-mail: yggdrasil.git@gmail.com
 - GitHub: [@yggdrasilGit](https://github.com/yggdrasilGit
```
- Matheus Soares Bento da Silva
```
 - RM: rm565540
 - E-mail: matheusbento044@gmail.com
 - GitHub: [matheusbento044](https://github.com/matheusbento04)
```
- Vitor Eiji Fernandes Teruia
```
- RM: rm563683
- E-mail: vitorfer2018@gmail.com
- GitHub: [@Vitor985-hub](https://github.com/Vitor985-hub)
```

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/leonardoorabona/">Leonardo Ruiz Orabona</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusc">André Godoi Chiovato</a>


## 📜 **Descrição**

Os incêndios florestais têm se intensificado nos últimos anos, gerando impactos ambientais, econômicos e sociais significativos. As principais causas incluem mudanças climáticas, ação humana e períodos prolongados de seca.

O desafio do nosso projeto é desenvolver uma solução capaz de **prever e detectar incêndios florestais antes que eles se tornem incontroláveis**, utilizando uma combinação de sensores ambientais, microcontroladores (ESP32) e algoritmos de Machine Learning.

## 🎯 **Justificativa**

* Preservar o meio ambiente, a fauna, a flora e vidas humanas;
* Prever incêndios antes que eles ocorram;
* Utilizar tecnologia acessível e de baixo custo para monitoramento contínuo e prevenção de desastres.


---
## 🔧 **Tecnologias Utilizadas**

- ESP32 com PlatformIO (VS Code)
- Simulador Wokwi.com
- C/C++ (para o firmware do ESP32)
- Python 3
- SQLite (banco de dados local)
- Machine Learning para análise e predição de risco;
- Interface de alertas para moradores e autoridades.

---

## 🧠 Lógica do Projeto - Arquitetura de Dados

### Sensores Simulados

| Origem                | Tipo de dado                           | Destino                      |
| --------------------- | -------------------------------------- | ---------------------------- |
| Sensor de umidade     | Numérico contínuo                      | ESP32 → LCD → Banco de Dados |
| Sensor de nutrientes  | Numérico contínuo                      | ESP32 → LCD → Banco de Dados |
| Sensor de temperatura | Numérico contínuo                      | ESP32 → Banco de Dados       |
| Predição de ML        | Binário (0 - alerta, 1 - normal)       | Streamlit → ESP32            |


### Software Utilizado

| Componente          | Tecnologia                    |
| ------------------- | ----------------------------- |
| Sistema embarcado   | C/C++ para ESP32              |
| Monitoramento       | Serial Plotter (Wokwi)        |
| Exibição local      | LCD I2C                       |
| Modelagem preditiva | Python com Scikit-learn       |
| Dashboard           | Python com Streamlit          |
| Banco de dados      | MySQL / PostgreSQL / Firebase |
| Versionamento       | GitHub                        |


## Descrição dos Componentes

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

## 🗺️ **Diagrama da Arquitetura**

```
[Sensores no Ambiente]
   ↓
[ESP32] ---> [API/MQTT] ---> [Servidor com ML em Python]
                                     ↓
                         [Análise + Predição de Risco]
                                     ↓
              [Interface: Dashboard + Alertas (E-mail, LED, Buzzer)]
```

---

## **Hardware Utilizado**

* **ESP32** — microcontrolador central.
* **Sensores** — umidade, temperatura.
* **Servidor ou PC** — para rodar modelo de ML e banco de dados.
* **PC com Streamlit** — dashboard interativo.
 
---


---

##  🧠 **Machine Learning**

### Tabelas — Modelos de Machine Learning para o FireGuard

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

## **Pipeline**

1. **Coleta:** Dados do ESP32 ou datasets históricos;
2. **Pré-processamento:** Limpeza e padronização dos dados;
3. **Treinamento:** Com algoritmos de classificação;
4. **Validação:** Testes de precisão, recall e F1-score;
5. **Deploy:** API local ou na nuvem para receber dados e retornar risco.

---

## 🔁 **Fluxo do Sistema**
1. **Repositório publicado no Heroku**
A API foi implantada na nuvem utilizando o Heroku, permitindo que fique online e acessível para receber dados dos sensores.

2. **Sensor envia dados para o servidor (POST request)**
O dispositivo sensor (ex: ESP32) coleta dados ambientais (temperatura, umidade, etc.) e faz uma requisição POST para a API hospedada no Heroku.

3. **Dados são armazenados no banco PostgreSQL**
Ao receber os dados, a API os registra em um banco de dados PostgreSQL, garantindo persistência e rastreabilidade.

4. **Requisição para obter o último registro**
O sistema realiza uma requisição GET para recuperar o último dado inserido no banco, servindo como entrada para o modelo de Machine Learning.

5. **Processamento com Machine Learning**
Os dados coletados são analisados por um modelo de Machine Learning, que avalia a probabilidade de ocorrência de foco de incêndio.

6. **Resultado encaminhado ao dashboard**
O resultado da análise é enviado para o dashboard, criado com a ferramenta Streamlit, que apresenta em tempo real a mensagem de risco ou tranquilidade, com base na última atualização.

## ✅ **Funcionamento Esperado:**

* Monitoramento ambiental em tempo real;
* Detecção de condições favoráveis ao início de incêndios;
* Geração de alertas imediatos para prevenção.

## 🌟 **Benefícios da Solução:**

* Eficiência no combate preventivo;
* Proteção ambiental e social;
* Redução dos custos operacionais;
* Sistema de baixo custo, escalável e replicável.

## 📸 **Evidências:**

* Prints dos dashboards;
* Fotos do ESP32 com sensores funcionando;
* Prints dos alertas acionados;
* Print do modelo de ML rodando e processando dados.****

## 🚧 **Limitações:**

* Acurácia dependente da qualidade dos sensores;
* Latência na transmissão dependendo da rede Wi-Fi;
* Dataset inicial pode ser limitado, precisando de mais dados reais para aumentar a precisão.

## 🔥 **Melhorias Futuras:**

* Integração com imagens de satélite (NDVI, MODIS);
* Uso de LoRa para comunicação de longa distância em áreas sem Wi-Fi;
* Dashboard mobile para alertas mais rápidos;
* Inclusão de IA embarcada no próprio ESP32 (TinyML).

## 6. 📎 **Anexos**

* ✔️ Códigos comentados (ESP32 e Python);
* ✔️ Diagramas elétricos do circuito (ESP32 + sensores);
* ✔️ Diagrama da arquitetura do sistema;
* ✔️ Link do vídeo de demonstração (**Não listado no YouTube**);
* ✔️ Referências de datasets e bibliografia técnica.

---

## 📁 Estrutura de pastas

```bash
GLOBAL-SOLUTION-2025-1/
├── .git/
├── .venv/
├── api_sensor/
│   ├── api_request/
│   ├── sensor/
│   ├── sensor_api/
│   ├── staticfiles/
├── .gitignore
├── manage.py
├── Procfile
├── README.md
├── requirements.txt
├── runtime.txt
├── dashboard/
│   ├── __init__.py
│   └── app.py
├── ml/
│   ├── __pycache__/
│   ├── data/
│   ├── models/
│   ├── notebooks/
│   ├── src/
│   │   ├── __init__.py
│   │   └── README.md
│   ├── requirements.txt
├── sensor_circuit/
│   ├── .pio/
│   ├── .vscode/
│   ├── src/
│   ├── .gitignore
│   ├── diagram.json
│   ├── platformio.ini
│   ├── wokwi.toml
│   ├── esp32_estudo_funcionamento.md
│   ├── LICENSE
├── .gitignore
├── main.py
├── pip
├── README.md
└── requirements.txt
```

## ▶️ Como utilizar:

💾 Instalação
---
1. clone o repositório:
```

```
2. Crie e ative um ambiente virtual (opcional, mas recomendado):
```
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```
3. Instale as bibliotecas necessárias:
```
pip install -r requirements.txt
```

🔧 1. Preparar o Dispositivo Sensor
---
1. Acesse o sensor pelo link https://wokwi.com/projects/432764471641420801;
2. Acione o sensor clicando no botão verde de "play";
3. Acesse o Dashboard (Streamlit)
4. Vá até a pasta dashboard/.
5. Execute o seguinte comando:
   ```
   streamlit run app.py
6. O dashboard será aberto no navegador, mostrando a última predição com base nos dados recebidos.
7. Acesse via navegador: http://localhost:8501
   
---

🚀 **Fluxo Resumido**
Sensor → envia dados via POST

API (Heroku) → armazena no PostgreSQL

ML → analisa o último dado

Dashboard (Streamlit) → mostra se há risco de incêndio

---

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
