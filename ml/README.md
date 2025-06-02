# Projeto de Machine Learning

Este projeto realiza [classificação/regressão] utilizando o dataset XYZ.

## Estrutura
- `data/`: dados brutos e processados.
- `notebooks/`: notebooks de exploração e prototipagem.
- `src/`: código-fonte modular.
- `models/`: modelos salvos.
- `reports/`: gráficos e relatórios.

## Como rodar
1. Clone o repositório.
2. Instale as dependências: `pip install -r requirements.txt`.
3. Execute o treinamento: `python src/models/train_model.py`.


```
project_name/
│
├── data/                          # Dados brutos e processados
│   ├── raw/                       # Dados originais (não mexer)
│   │   └── dataset.csv
│   └── processed/                 # Dados tratados para modelagem
│       └── dataset_clean.csv
│
├── notebooks/                     # Jupyter notebooks para EDA e protótipos
│   ├── 01_eda.ipynb
│   └── 02_model_prototype.ipynb
│
├── src/                           # Código-fonte organizado por função
│   ├── data/
│   │   └── load_data.py           # Função para carregar dados
│   ├── features/
│   │   ├── build_features.py      # Feature engineering
│   │   └── preprocess.py          # Pré-processamento
│   ├── models/
│   │   ├── train_model.py         # Script de treinamento
│   │   └── evaluate_model.py      # Avaliação de modelo
│   └── visualization/
│       └── plot.py                # Funções de visualização
│
├── models/                        # Modelos treinados serializados
│   └── model.pkl
│
├── reports/                       # Relatórios gerados
│   └── figures/                   # Gráficos e imagens
│       ├── correlation_matrix.png
│       └── feature_importance.png
│
├── tests/                         # Testes unitários
│   ├── test_load_data.py
│   └── test_train_model.py
│
├── requirements.txt               # Dependências do projeto
├── README.md                      # Documentação do projeto
└── .gitignore                     # Arquivos/formatos ignorados pelo Git

```
