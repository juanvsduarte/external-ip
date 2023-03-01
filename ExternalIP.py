import requests

def get_external_ip():
    # Faz uma solicitação HTTP para um serviço de detecção de IP externo
    response = requests.get('https://api.ipify.org')
    # Analisa a resposta para obter o endereço IP externo
    external_ip = response.text
    return external_ip

if __name__ == '__main__':
    external_ip = get_external_ip()
    print(f'O endereço IP externo é: {external_ip}')
