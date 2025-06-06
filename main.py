from api_sensor.api_request.api_get_ultimo_dado import get_sensor_data_renamed
from ml.src.models.train_model import main
import os

if __name__ == "__main__":
    dados_renomeados = get_sensor_data_renamed()
    json_input = dados_renomeados

    main(json_input)