import requests
api_token = "5xsyt45sa0nsiwv2sr5vagjtptw8agk7ld18fx6z"

def verificar_ip_autorizado():
    """
    Verifica se o IP público já está na lista de IPs autorizados na Webshare.

    :param api_token: Token da API do Webshare
    :return: True se o IP já estiver autorizado, False caso contrário
    """
    ip_publico = obter_ip_publico_via_webshare()
    if not ip_publico:
        print("Não foi possível obter o IP público.")
        return False

    url = "https://proxy.webshare.io/api/v2/proxy/ipauthorization/"

    headers = {
        "Authorization": f"Token {api_token}"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        ip_list = response.json().get('results', [])
        # Verifica se o IP público está na lista de IPs autorizados
        for ip_entry in ip_list:
            if ip_entry['ip_address'] == ip_publico:
                print(f"O IP {ip_publico} está autorizado.")
                return True
        print(f"O IP {ip_publico} não está na lista de IPs autorizados.")
        return False
    else:
        print(f"Erro ao obter lista de IPs autorizados: {response.status_code}, {response.text}")
        return False

def obter_ip_publico_via_webshare():
    """
    Obtém o endereço IP público da máquina usando o endpoint 'whatsmyip' da Webshare.

    :param api_token: Token da API do Webshare
    :return: O endereço IP público como string, ou None se houver um erro
    """
    url = "https://proxy.webshare.io/api/v2/proxy/ipauthorization/whatsmyip/"
    headers = {
        "Authorization": f"Token {api_token}"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            ip_address = response.json().get("ip_address")
            print(f"Seu IP público é: {ip_address}")
            return ip_address
        else:
            print(f"Erro ao obter IP público: {response.status_code}, {response.text}")
            return None
    except requests.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")
        return None

def criar_autorizacao_ip():
    """
    Cria uma autorização de IP na Webshare para um IP público específico.

    :param api_token: Token da API do Webshare
    :param ip_publico: IP público que deseja adicionar à lista de permitidos
    """
    ip_publico = obter_ip_publico_via_webshare()

    # URL para adicionar IP autorizado
    url = "https://proxy.webshare.io/api/v2/proxy/ipauthorization/"

    headers = {
        "Authorization": f"Token {api_token}",
        "Content-Type": "application/json"
    }

    data = {
        "ip_address": ip_publico
    }

    try:
        # Fazer a requisição para adicionar o IP autorizado
        response = requests.post(url, headers=headers, json=data)

        # Verificar o código de resposta
        if response.status_code in [200, 201]:
            print(f"IP {ip_publico} autorizado com sucesso.")
            print("Detalhes da autorização:", response.json())
            return response.json()
        elif response.status_code == 400:
            # Verifica se o erro é porque o IP já existe
            response_data = response.json()
            if "ip_address" in response_data and response_data["ip_address"][0]["code"] == "invalid":
                print(f"O IP {ip_publico} já está autorizado.")
            else:
                print(f"Erro ao autorizar IP: {response.status_code}, {response_data}")
        else:
            print(f"Erro ao autorizar IP: {response.status_code}, {response.text}")
    except requests.RequestException as e:
        print(f"Erro na requisição: {e}")



# obter_ip_publico_via_webshare()
# criar_autorizacao_ip()
# verificar_ip_autorizado()