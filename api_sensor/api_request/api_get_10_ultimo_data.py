import requests

def get_ultimos_dados_sensor():
    url = "https://api-sensor-e3edd8233f2e.herokuapp.com/api/sensor/?last=10"

    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            dados = response.json()
            print("Últimos 10 dados do sensor:")
            for i, dado in enumerate(dados, 1):
                print(f"{i}. {dado}")
            return dados
        else:
            print(f"Erro ao obter dados: {response.status_code} - {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None

# Exemplo de chamada
if __name__ == "__main__":
    get_ultimos_dados_sensor()
