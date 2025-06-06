import os
import json
import pandas as pd
import joblib
from api_sensor.api_request.api_get_ultimo_dado import get_sensor_data_renamed

def main(json_input):
    # Diretório raiz do projeto (2 níveis acima da pasta atual)
    raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    
    # Caminhos dos arquivos
    caminho_modelo = os.path.join(raiz_projeto, "models", "modelo_decision_tree.pkl")
    caminho_scaler = os.path.join(raiz_projeto, "models", "scaler_modelo.pkl")

    # Carregar modelo e scaler
    modelo_carregado = joblib.load(caminho_modelo)
    scaler = joblib.load(caminho_scaler)

    # Carregar entrada JSON para DataFrame
    entrada_dict = json.loads(json_input)
    
    # Manter só as 3 variáveis que você quer usar (descartar as outras)
    variaveis_necessarias = ["temperatura_superficie", "umidade_relativa", "concentracao_CO2"]
    entrada_filtrada = {k: entrada_dict[k] for k in variaveis_necessarias if k in entrada_dict}

    entrada_df = pd.DataFrame([entrada_filtrada])

    # Normalizar os dados de entrada
    entrada_scaled = scaler.transform(entrada_df)

    # Fazer predição
    predicao = modelo_carregado.predict(entrada_scaled)

    # Imprime a predição (pode mudar para retornar, salvar, etc)
    print(predicao[0])

if __name__ == "__main__":
    dados_renomeados = get_sensor_data_renamed()
    json_input = f'{dados_renomeados}'

    type(json_input)
