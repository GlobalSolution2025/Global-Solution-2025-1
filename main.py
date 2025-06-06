from api_sensor.api_request.api_get_10_ultimo_data import get_ultimos_dados_sensor
from api_sensor.api_request.api_get_ultimo_dado import get_sensor_data_renamed
from ml.src.models.train_model import main
import os
import json
import time

INTERVALO_SEGUNDOS = 10  # tempo de espera entre as execuções

if __name__ == "__main__":
    while True:
        try:
            # Limpa o terminal
            os.system('cls' if os.name == 'nt' else 'clear')

            # Coleta e processa os dados
            dados_renomeados = get_sensor_data_renamed()
            json_input = json.dumps(dados_renomeados)
            main(json_input)
            get_ultimos_dados_sensor()

            # Aguarda o próximo ciclo
            time.sleep(INTERVALO_SEGUNDOS)

        except KeyboardInterrupt:
            print("Encerrando o loop por interrupção do usuário.")
            break
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            time.sleep(INTERVALO_SEGUNDOS)
