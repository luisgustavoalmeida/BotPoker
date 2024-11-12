import requests
from collections import defaultdict
from typing import List, Dict
from datetime import datetime, timedelta, timezone

# Configuração da sessão e cabeçalhos de API
API_TOKEN = "5xsyt45sa0nsiwv2sr5vagjtptw8agk7ld18fx6z"
BASE_URL = "https://proxy.webshare.io/api/v2/proxy/ipauthorization/"
HEADERS = {
    "Authorization": f"Token {API_TOKEN}",
    "Content-Type": "application/json"
}

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
        print(f"[ERRO] Erro ao fazer a requisição {method} para {url}: {e}")
        return None


def obter_ip_publico_via_webshare() -> str:
    """Obtém o endereço IP público da máquina usando o endpoint 'whatsmyip' da Webshare."""
    response = requisicao_http("GET", f"{BASE_URL}whatsmyip/")
    if response:
        ip_address = response.json().get("ip_address", "")
        print(f"[INFO] Seu IP público é: {ip_address}")
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
            print(f"[INFO] O IP {ip_publico} já está autorizado.")
            return True

        next_url = data.get('next')

    print(f"[INFO] O IP {ip_publico} não está na lista de IPs autorizados.")
    return False


def criar_autorizacao_ip(ip_publico: str) -> bool:
    """Cria uma autorização de IP na Webshare para um IP público específico."""
    data = {"ip_address": ip_publico}
    response = requisicao_http("POST", BASE_URL, json=data)
    if response and response.status_code in [200, 201]:
        print(f"[INFO] IP {ip_publico} autorizado com sucesso.")
        return True
    elif response and response.status_code == 400:
        response_data = response.json()
        if "ip_address" in response_data and response_data["ip_address"][0].get("code") == "invalid":
            print(f"[INFO] O IP {ip_publico} já está autorizado.")
        else:
            print(f"[ERRO] Erro ao autorizar IP: {response_data}")
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
        print(f"[SIMULAÇÃO] IP com ID {ip_id} seria removido.")
        return
    delete_url = f"{BASE_URL}{ip_id}/"
    response = requisicao_http("DELETE", delete_url)
    if response and response.status_code == 204:
        print(f"[INFO] IP com ID {ip_id} removido com sucesso.")
    else:
        print(f"[ERRO] Erro ao excluir IP com ID {ip_id}.")


def remover_ips_duplicados(dry_run: bool = False):
    """Remove autorizações de IP duplicadas, mantendo apenas uma entrada para cada endereço IP."""
    autorizacoes = obter_ips_autorizados()
    if not autorizacoes:
        print("[INFO] Nenhuma autorização de IP encontrada.")
        return

    ip_map = defaultdict(list)
    for entry in autorizacoes:
        ip_address = entry.get('ip_address')
        ip_id = entry.get('id')
        if ip_address and ip_id:
            ip_map[ip_address].append(ip_id)

    for ip_address, ids in ip_map.items():
        if len(ids) > 1:
            print(f"[INFO] Removendo duplicatas para o IP {ip_address}. Mantendo o ID {ids[0]} e removendo {ids[1:]}")
            for ip_id in ids[1:]:
                excluir_ip_por_id(ip_id, dry_run=dry_run)

    print("[INFO] Processo de remoção de IPs duplicados concluído.")


def remover_ips_inativos(dias_inatividade: int = 10, dry_run: bool = False):
    """
    Remove autorizações de IP que não foram usadas por mais de `dias_inatividade` dias.

    :param dias_inatividade: Número de dias de inatividade para considerar um IP como inativo.
    :param dry_run: Se True, apenas simula a remoção sem realmente excluir os IPs.
    """
    autorizacoes = obter_ips_autorizados()
    if not autorizacoes:
        print("[INFO] Nenhuma autorização de IP encontrada.")
        return

    # Define a data limite com timezone UTC
    limite_inatividade = datetime.now(timezone.utc) - timedelta(days=dias_inatividade)

    for entry in autorizacoes:
        ip_id = entry.get('id')
        ip_address = entry.get('ip_address')
        last_used_str = entry.get('last_used_at')

        if last_used_str:
            last_used_date = datetime.fromisoformat(last_used_str.replace("Z", "+00:00"))
            if last_used_date < limite_inatividade:
                print(f"[INFO] O IP {ip_address} está inativo desde {last_used_date} e será removido.")
                excluir_ip_por_id(ip_id, dry_run=dry_run)
        else:
            print(f"[INFO] O IP {ip_address} nunca foi usado e será removido.")
            excluir_ip_por_id(ip_id, dry_run=dry_run)

    print("[INFO] Processo de remoção de IPs inativos concluído.")


def finalizar_sessao():
    session.close()
    print("[INFO] Sessão HTTP encerrada.")


# if __name__ == "__main__":
    # remover_ips_duplicados(dry_run=False)  # Modo "dry_run=True" para simular
    # remover_ips_inativos(dias_inatividade=5, dry_run=False)  # `dry_run=True` para simulação
    # adicionar_ip_ao_servidor_proxy()
