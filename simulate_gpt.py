import requests

# Funzione per chiamare l'endpoint del server Flask
def get_device_info_from_gpt(device_id):
    response = requests.get(f'http://localhost:5000/gpt-endpoint?device_id={device_id}')
    return response.json()

# Esempio di utilizzo
device_id = 'f20387d7-79e1-4348-aa1a-efea4e268d6c'
result = get_device_info_from_gpt(device_id)
print(result)
