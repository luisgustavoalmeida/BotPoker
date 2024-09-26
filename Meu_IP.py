import random
import re

import requests

apis = [
    'https://api.ipify.org?format=json',
    # 'https://api64.ipify.org?format=json',
    'https://ipinfo.io/json',
    'https://checkip.amazonaws.com',
    'http://httpbin.org/ip',
    # 'https://ident.me/.json',
    # 'https://ipapi.co/json',
    'https://api.ipify.org',
    'http://checkip.amazonaws.com',
    'http://ipinfo.io/ip',
    'http://whatismyip.akamai.com',
    # 'http://myip.dnsomatic.com',
    'http://ipv4.ident.me/',
    'https://api.ipify.org/',
    'http://whatismyipv4.net',
    'https://l2.io/ip',
    'http://ip-api.com/line/?fields=query',
    'https://api4.ipify.org',
    'https://ipinfo.io/ip',
    # 'https://wtfismyip.com/text',
    # 'http://icanhazip.com',
    'https://ipwhois.app/json/',
    # 'https://ifconfig.co/json',
    'https://ipv4.icanhazip.com',
    # 'https://myexternalip.com/raw',
]


def get_ip_from_response(response, api_url):
    """
    Extrai o IP da resposta, tratando diferentes formatos de JSON ou texto.
    """
    try:
        if 'ip' in response:  # Formato comum em várias APIs
            return response['ip']
        elif 'origin' in response:  # httpbin.org
            return response['origin']
        elif 'ip_address' in response:  # Possível formato em algumas APIs
            return response['ip_address']
        elif 'ip_addr' in response:  # ifconfig.me retorna ip como 'ip_addr'
            return response['ip_addr']
        elif 'address' in response:  # Possível outro formato para IP
            return response['address']
        else:
            print(f"Formato desconhecido da resposta da API {api_url}: {response}")
            return None
    except Exception as e:
        print(f"Erro ao tentar extrair o IP da resposta da API {api_url}: {e}")
        return None


def validar_ip(ip):
    """
    Valida se a string fornecida é um IP no formato correto.
    """
    # Expressão regular para validar o formato de IP (IPv4)
    padrao_ip = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

    if padrao_ip.match(ip):
        return True
    return False


def obter_ip():
    random.shuffle(apis)  # Embaralha a lista de URLs
    while True:
        for api in apis:
            try:
                response = requests.get(api, timeout=5)

                if response.status_code in (200, 429):
                    # Algumas APIs retornam texto puro, outras JSON
                    if 'application/json' in response.headers.get('Content-Type', ''):
                        ip_info = response.json()  # Para APIs que retornam JSON
                    else:
                        ip_info = {'ip': response.text.strip()}  # Para APIs que retornam texto simples

                    ip_address = get_ip_from_response(ip_info, api)  # Extração do IP
                    if ip_address:
                        print(f"IP obtido com sucesso de {api}: {ip_address}")
                        if validar_ip(ip_address):
                            print('IP no formato IPV4')
                            return ip_address, True  # Retorna o IP se a extração foi bem-sucedida
                    else:
                        print(f"Falha ao extrair o IP da resposta da API {api}.")
                else:
                    print(f"Falha ao obter o IP de {api}. Código de status: {response.status_code}")
            except Exception as e:
                print(f"Erro ao tentar obter o IP de {api}: {e}")

    print("Não foi possível obter o IP de nenhuma API.")
    return None  # Se todas as tentativas falharem, retorna None


# obter_ip()
