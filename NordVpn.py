import subprocess
import time

import pyautogui
import pygetwindow as gw

from OCR_tela import IP_vpn, Vpn_sevidor

# Defina o caminho completo para o executável da NordVPN

nordvpn_path = r"C:\Program Files\NordVPN\NordVPN.exe"


def verificar_janela_nordvpn():
    # Procura janelas com "NordVPN" no título
    janelas = gw.getWindowsWithTitle("NordVPN ")  # Procura janelas com o título contendo "NordVPN"
    # Coordenadas e tamanho desejados
    nova_posicao_left = 461
    nova_posicao_top = 386
    nova_largura = 906
    nova_altura = 652

    for janela in janelas:
        if "NordVPN " == janela.title:
            print('titulo encontrado', janela.title)
            janela.activate()  # Traz a janela para o primeiro plano (ativa a janela)
            # Se a janela estiver minimizada, restaura-a
            if janela.isMinimized:
                janela.restore()  # Restaura a janela se estiver minimizada
            if (janela.left == nova_posicao_left and janela.top == nova_posicao_top and
                    janela.width == nova_largura and janela.height == nova_altura):
                print(f"A janela '{janela}' já está ajustada para a posição e tamanho desejados.")
            else:
                # Ajusta o tamanho e a posição da janela
                janela.moveTo(nova_posicao_left, nova_posicao_top)  # Move a janela
                janela.resizeTo(nova_largura, nova_altura)  # Redimensiona a janela
                print(f"Janela '{janela}' ajustada para posição ({nova_posicao_left}, {nova_posicao_top}) "
                      f"e tamanho ({nova_largura}x{nova_altura}).")
            pyautogui.click(489, 450)  # clica no anel
            return True, nova_posicao_left, nova_posicao_top  # Janela foi encontrada e ajustada ou já estava ajustada

    print('NordVPN não está aberta')
    return False  # Nenhuma janela ativa do NordVPN foi encontrada


def abrir_nordvpn():
    # Abre o NordVPN apenas se ele não estiver aberto
    while True:
        teste, nova_posicao_left, nova_posicao_top = verificar_janela_nordvpn()
        if not teste:
            print("Abrindo NordVPN...")
            subprocess.Popen(['start', 'nordvpn://'], shell=True)
            time.sleep(10)  # Dá tempo para a janela abrir
        else:
            print("NordVPN já estava aberto.")
            return nova_posicao_left, nova_posicao_top


def ajustar_tamanho_janela(nova_largura, nova_altura):
    # Obter a janela da NordVPN pelo título
    janela = None
    while janela is None:
        # Procura a janela da NordVPN
        janelas = gw.getAllTitles()
        for titulo in janelas:
            if "NordVPN" in titulo:
                janela = gw.getWindowsWithTitle(titulo)[0]
                break
        time.sleep(1)  # Espera 1 segundo para tentar novamente

    # Ajusta o tamanho da janela
    if janela is not None:
        janela.resizeTo(nova_largura, nova_altura)
        janela.activate()


# Função para conectar ao NordVPN com comando básico (quick connect)
def connect_nordvpn():
    try:
        print("Tentando conectar ao NordVPN...")
        subprocess.run([nordvpn_path, '-c'], check=True)
        print("Conexão realizada com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao tentar conectar: {e}")


# Função para conectar
def connect_by_group(group_name):
    try:
        print(f"Tentando conectar ao grupo: {group_name}...")
        result = subprocess.run([nordvpn_path, "-c", "-n", group_name], capture_output=True, text=True)

        # Se não houver erros no stderr, consideramos a conexão como bem-sucedida
        if result.returncode == 0 or not result.stderr:
            print(f"Conectado com sucesso ao grupo {group_name}!")
        else:
            print(f"Erro ao tentar conectar ao grupo {group_name}. Código de saída: {result.returncode}")
            print(f"Saída de erro: {result.stderr}")

    except Exception as e:
        print(f"Ocorreu um erro ao tentar conectar: {e}")


# Função para desconectar do NordVPN
def disconnect_nordvpn():
    try:
        print("Tentando desconectar do NordVPN...")
        subprocess.run([nordvpn_path, '-d'], check=True)
        print("Desconectado com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao tentar desconectar: {e}")


def teste_conectado():
    for _ in range(60):
        if pyautogui.pixelMatchesColor(591, 509, (39, 190, 86), tolerance=5):
            print('Conectado!')
            return True

        elif pyautogui.pixelMatchesColor(591, 509, (255, 112, 89), tolerance=5):
            print('Desconectado!')

        elif pyautogui.pixelMatchesColor(591, 509, (228, 72, 92), tolerance=5):
            print('Conectando...')
        time.sleep(1)
    return False


def gerar_lista_servidores(pais, inicio, fim):
    """
    Gera uma lista de servidores com base no nome do país e o intervalo de números.
    """
    return [f"{pais} #{i}" for i in range(inicio, fim + 1)]


def salvar_lista_em_txt(lista, nome_arquivo):
    """
    Salva a lista em um arquivo TXT.
    """
    with open(nome_arquivo, 'w') as arquivo:
        for item in lista:
            arquivo.write(f"{item}\n")
    print(f"Lista salva no arquivo {nome_arquivo}.")


def conectar_e_testar_servidores():
    """
    Percorre todos os servidores e verifica a conexão. Se o servidor estiver conectado,
    armazena o nome do servidor em uma lista e salva a lista no final.
    """
    # Gera a lista de servidores de 'United States #1' até 'United States #10700'
    servidores = gerar_lista_servidores("United States", 5055, 10700)
    print(servidores)
    servidores_conectados = []

    for connect_sevidor in servidores:

        nova_posicao_left, nova_posicao_top = abrir_nordvpn()  # Abre o NordVPN
        connect_by_group(connect_sevidor)  # Conecta ao servidor atual
        if teste_conectado():
            teste_con, status, sevidor = Vpn_sevidor(nova_posicao_left, nova_posicao_top)  # Verifica o status da conexão
            if teste_con and sevidor == connect_sevidor:
                print(f"Servidor conectado: {connect_sevidor}")
                servidores_conectados.append(connect_sevidor)  # Armazena o servidor conectado
                print(servidores_conectados)

    # Salva a lista de servidores conectados em um arquivo TXT
    salvar_lista_em_txt(servidores_conectados, "servidores_conectados.txt")


# Exemplo de execução:
# conectar_e_testar_servidores()


# # Exemplo de uso:
# if __name__ == "__main__":
#     connect_sevidor = "United States #6300"
#     while True:
#         while True:
#             nova_posicao_left, nova_posicao_top = abrir_nordvpn()  # Abre o NordVPN
#             connect_by_group(connect_sevidor)
#             if teste_conectado():
#                 break
#         teste_con, status, sevidor = Vpn_sevidor(nova_posicao_left, nova_posicao_top)
#         if teste_con== True and status == 'CONECTADO':
#             teste_ip, numero_ip = IP_vpn(nova_posicao_left, nova_posicao_top)
#             if teste_ip:
#                 break
