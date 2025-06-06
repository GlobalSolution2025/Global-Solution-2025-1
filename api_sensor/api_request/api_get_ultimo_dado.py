import requests

def get_sensor_data_renamed(url="https://api-sensor-e3edd8233f2e.herokuapp.com/api/sensor/"):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        # Se receber uma lista, pega o primeiro registro (por exemplo)
        if isinstance(data, list):
            data = data[0] if data else {}

        # Remove o timestamp se existir
        data.pop('timestamp', None)

        # Mapeamento das chaves antigas para novas
        rename_map = {
            "temperatura": "temperatura_superficie",
            "umidade": "umidade_relativa",
            "mq2": "concentracao_CO2"
        }

        # Cria um novo dicionário com as chaves renomeadas
        renamed_data = {}
        for old_key, new_key in rename_map.items():
            if old_key in data:
                renamed_data[new_key] = data[old_key]

        return renamed_data
    else:
        print(f"Erro ao acessar a API: {response.status_code}")
        return None

# Exemplo de uso
dados_renomeados = get_sensor_data_renamed()
print(dados_renomeados)
