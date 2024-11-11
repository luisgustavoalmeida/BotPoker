import requests
from collections import defaultdict
import logging
from typing import List, Dict

# Configuração da sessão e cabeçalhos de API
API_TOKEN = "5xsyt45sa0nsiwv2sr5vagjtptw8agk7ld18fx6z"
BASE_URL = "https://proxy.webshare.io/api/v2/proxy/ipauthorization/"
HEADERS = {
    "Authorization": f"Token {API_TOKEN}",
    "Content-Type": "application/json"
}

# Configuração de logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Sessão global para ser usada em todas as requisições HTTP
session = requests.Session()
session.headers.update(HEADERS)


def requisicao_http(method: str, url: str, **kwargs):
    """Função de utilidade para lidar com requisições HTTP e tratamento de erros."""
    try:
        response = session.request(method, url, **kwargs)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        logging.error(f"Erro ao fazer a requisição {method} para {url}: {e}")
        return None


def obter_ip_publico_via_webshare() -> str:
    """Obtém o endereço IP público da máquina usando o endpoint 'whatsmyip' da Webshare."""
    response = requisicao_http("GET", f"{BASE_URL}whatsmyip/")
    if response:
        ip_address = response.json().get("ip_address", "")
        logging.info(f"Seu IP público é: {ip_address}")
        return ip_address
    return ""


def verificar_ip_autorizado(ip_publico: str) -> bool:
    """Verifica se o IP público já está na lista de IPs autorizados na Webshare."""
    autorizado = False
    next_url = BASE_URL

    while next_url:
        response = requisicao_http("GET", next_url)
        if not response:
            break

        data = response.json()
        ip_list = data.get('results', [])
        autorizado = any(ip_entry.get('ip_address') == ip_publico for ip_entry in ip_list)
        if autorizado:
            logging.info(f"O IP {ip_publico} já está autorizado.")
            return True

        next_url = data.get('next')

    logging.info(f"O IP {ip_publico} não está na lista de IPs autorizados.")
    return False


def criar_autorizacao_ip(ip_publico: str) -> bool:
    """Cria uma autorização de IP na Webshare para um IP público específico."""
    data = {"ip_address": ip_publico}
    response = requisicao_http("POST", BASE_URL, json=data)
    if response and response.status_code in [200, 201]:
        logging.info(f"IP {ip_publico} autorizado com sucesso.")
        return True
    elif response and response.status_code == 400:
        response_data = response.json()
        if "ip_address" in response_data and response_data["ip_address"][0].get("code") == "invalid":
            logging.info(f"O IP {ip_publico} já está autorizado.")
        else:
            logging.error(f"Erro ao autorizar IP: {response_data}")
    return False


def adicionar_ip_ao_servidor_proxy():
    ip_publico = obter_ip_publico_via_webshare()
    if ip_publico and not verificar_ip_autorizado(ip_publico):
        criar_autorizacao_ip(ip_publico)


def obter_ips_autorizados() -> List[Dict[str, str]]:
    """Obtém todas as autorizações de IP e retorna uma lista de dicionários com os IPs e seus IDs."""
    autorizacoes = []
    next_url = BASE_URL

    while next_url:
        response = requisicao_http("GET", next_url)
        if not response:
            break
        data = response.json()
        autorizacoes.extend(data.get('results', []))
        next_url = data.get('next')

    return autorizacoes


def excluir_ip_por_id(ip_id: str, dry_run: bool = False):
    """Exclui uma autorização de IP usando o ID fornecido. Permite modo 'dry-run'."""
    if dry_run:
        logging.info(f"[SIMULAÇÃO] IP com ID {ip_id} seria removido.")
        return
    delete_url = f"{BASE_URL}{ip_id}/"
    response = requisicao_http("DELETE", delete_url)
    if response and response.status_code == 204:
        logging.info(f"IP com ID {ip_id} removido com sucesso.")
    else:
        logging.error(f"Erro ao excluir IP com ID {ip_id}.")


def remover_ips_duplicados(dry_run: bool = False):
    """Remove autorizações de IP duplicadas, mantendo apenas uma entrada para cada endereço IP."""
    autorizacoes = obter_ips_autorizados()
    if not autorizacoes:
        logging.info("Nenhuma autorização de IP encontrada.")
        return

    ip_map = defaultdict(list)
    for entry in autorizacoes:
        ip_address = entry.get('ip_address')
        ip_id = entry.get('id')
        if ip_address and ip_id:
            ip_map[ip_address].append(ip_id)

    for ip_address, ids in ip_map.items():
        if len(ids) > 1:
            logging.info(f"Removendo duplicatas para o IP {ip_address}. Mantendo o ID {ids[0]} e removendo {ids[1:]}")
            for ip_id in ids[1:]:
                excluir_ip_por_id(ip_id, dry_run=dry_run)

    logging.info("Processo de remoção de IPs duplicados concluído.")


if __name__ == "__main__":
    remover_ips_duplicados(dry_run=False)  # Modo "dry_run=True" para simular
    adicionar_ip_ao_servidor_proxy()
