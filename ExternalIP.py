import requests

response = requests.get('https://api.ipify.org')
    # Analisa a resposta para obter o endereço IP externo
external_ip = response.text
resposta = (f'O endereço IP externo é: {external_ip}')
print(resposta)
