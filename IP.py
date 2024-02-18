import datetime
import os
import random
import socket
import time

import psutil
import pyautogui
import pygetwindow as gw
import pywinauto
import requests

import Google
import ListaIpFirebase
import Seleniun

# Desabilitar o fail-safe
pyautogui.FAILSAFE = False

LIMITE_IP = 6

conexao_x = 850
conexao_y = 710

# Título e nome da classe da janela que você deseja verificar
window_title = 'Configurações'
window_class = 'ApplicationFrameWindow'

precisao = 0.9

# Vero
telefone = r"Imagens\Conexao\telefone.png"
regiao_telefone = (conexao_x + 22, conexao_y + 109, 59, 56)
desconectar = r"Imagens\Conexao\desconectar.png"
regiao_desconectar = (conexao_x + 361, conexao_y + 185, 109, 36)
conectar = r"Imagens\Conexao\conectar.png"
regiao_conectar = (conexao_x + 124, conexao_y + 185, 92, 34)
conectado = r"Imagens\Conexao\conectado.png"
regiao_conectado = (conexao_x + 70, conexao_y + 133, 92, 34)
fechar = r"Imagens\Conexao\fechar.png"
regiao_fechar = (conexao_x + 380, conexao_y + 236, 91, 80)
cancelar = r"Imagens\Conexao\cancelar.png"
regiao_cancelar = (conexao_x + 358, conexao_y + 204, 111, 36)

# Modem
celular = r"Imagens\Conexao\celular.png"
regiao_celular = (conexao_x + 19, conexao_y + 261, 55, 22)
ativado = r"Imagens\Conexao\ativado.png"
desativado = r"Imagens\Conexao\desativado.png"
regiao_ativado_desativado = (conexao_x + 75, conexao_y + 292, 73, 22)

# chave nome do computador : tupla( valor 1 celula , valor 2 tipo de conexão)
# "F3" de 3 em 3       #"modem" ou "vero"
# cria um dicionario de tuplas par agurdar os valores das celulas e o tipo de conexao com a internete que cada computador usa
dicionari_PC_IP = {'PC-I5-8600K': ("F3", "modem"),
                   'PC-I5-9400A': ("F6", "modem"),
                   'PC-I5-9400B': ("F9", "modem"),
                   'PC-I5-9400C': ("F12", "modem"),
                   'PC-R5-7600A': ("F15", "modem"),
                   'PC-I5-13400A': ("F18", "modem"),
                   'PC-I5-13400B': ("F21", "modem"),
                   'PC-I5-13400C': ("F24", "modem"),
                   'PC-I5-13400D': ("F27", "modem"),
                   'PC-R5-5600G': ("F30", "modem"),
                   'PC-I5-13400E': ("F33", "modem"),
                   'PC-I7-9700KF': ("F36", "vero"),
                   'PC-i3-8145U': ("F39", "modem")}

# Obter o nome de usuário
nome_usuario = os.getlogin()
# print("Nome de usuário:", nome_usuario)

# Obter o nome do computador
nome_computador = socket.gethostname()
# print("Nome do computador:", nome_computador)

# usa o nome do computador para buscar os valores do dicionario
valor_dicionario = dicionari_PC_IP[nome_computador]
celula = valor_dicionario[0]  # pega o primeiro item da tupla
tipo_conexao = valor_dicionario[1]  # pega o segundo item da tuplas

sites = [
    'http://www.google.com',
    'http://www.facebook.com',
    'http://www.twitter.com',
    'http://www.youtube.com',
    'http://www.instagram.com',
    'http://www.linkedin.com',
    'http://www.github.com',
    'http://www.reddit.com',
    'http://www.amazon.com',
    'http://www.netflix.com'
]

lista_negra_ip = []
cont_lista_negra = 0


# def usuario_IP_nao():
#     # nome_usuario = os.getlogin()
#     if nome_usuario != "PokerIP":
#         ip(LIMITE_IP)
#         return


# def usuario_IP_sim():
#     # nome_usuario = os.getlogin()
#     if nome_usuario == "PokerIP":
#         ip(LIMITE_IP)
#         return


def testa_trocar_IP():
    if (nome_usuario == "PokerIP") and (
            nome_computador != "PC-I7-9700KF"):  # teste se o usuario do computador é o que troca IP se nao for fica esperando esta livre
        ip(LIMITE_IP)
        return
    elif (nome_usuario == "lgagu") and (nome_computador == "PC-I7-9700KF"):
        ip(LIMITE_IP)
        return
    else:
        return


def f5_quando_internete_ocila():
    # print('f5_quando_internete_ocila')
    conectado = True
    while True:
        try:
            response = requests.get('http://www.google.com', timeout=5)
            # if response.status_code == 200:
            if response.status_code == 200 or response.status_code == 429:
                print("Conexão com a internet ativa. ")
                if not conectado:
                    try:
                        print("------------------F5-----------------")
                        # pyautogui.press('f5')
                        # navegador.get(url)
                        pyautogui.click(86, 59)  # clica no atualizar
                        time.sleep(15)
                    except Exception as e:
                        print('erro autogui: ', e)

                    entrou_corretamente, stataus = Seleniun.teste_logado()
                return True
        except Exception as e:
            print("Sem conexão com a internet...")
            print(e)
            time.sleep(7)
            conectado = False


def tem_internet():
    cont_erro2 = 0
    cont_erro = 0
    # print('tem_internet')

    com_internete = True
    while com_internete:
        print('testa a internete')
        cont_erro2 += 1
        # site_aleatorio = random.choice(sites)
        # print(site_aleatorio)
        try:
            # response = requests.get(site_aleatorio, timeout=10)
            response = requests.get('http://www.google.com', timeout=5)
            if response.status_code == 200 or response.status_code == 429:
                print("Conexão com a internet ativa...")
                cont_erro = 0
                cont_erro2 = 0
                com_internete = False
                return True

        except Exception as e:
            print("Sem conexão com a internet. Encerrando os testes...")
            print(e)
            time.sleep(3)
            cont_erro += 1
            print('contagem de erro 1: ', cont_erro)
            if cont_erro >= 5:
                cont_erro = 0
                cont_erro2 = 0
                if nome_usuario == "PokerIP":  # teste se o usuario do computador é o que troca IP se nao for fica esperando esta livre
                    print("Vai par a função de trocar ip")
                    conexao()  # chama a função que troca ip
                elif (nome_usuario == "lgagu") and (nome_computador == "PC-I7-9700KF"):
                    print("Vai par a função de trocar ip")
                    conexao()  # chama a função que troca ip
            continue

        if cont_erro2 >= 20:
            cont_erro = 0
            cont_erro2 = 0
            if nome_usuario == "PokerIP":  # teste se o usuario do computador é o que troca IP se nao for fica esperando esta livre
                print("Vai par a função de trocar ip")
                conexao()  # chama a função que troca ip
            elif (nome_usuario == "lgagu") and (nome_computador == "PC-I7-9700KF"):
                print("Vai par a função de trocar ip")
                conexao()  # chama a função que troca ip
            continue
        print('contagem de erro 1: ', cont_erro)
        print('contagem de erro 2: ', cont_erro2)
    return True


def meu_ip():
    urls = [
        'https://api.ipify.org',
        'http://checkip.amazonaws.com',
        'http://ipinfo.io/ip',
        'http://whatismyip.akamai.com',
        'http://ip.42.pl/raw',
        'http://eth0.me',
        'http://myip.dnsomatic.com',
        'https://ipv4.icanhazip.com/',
        'http://ipv4.ident.me/',
        'https://ipv4.icanhazip.com/',
        'http://whatismyipv4.net']

    random.shuffle(urls)  # Embaralha a lista de URLs
    while True:
        for url in urls:
            # print(url)
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    texto = response.text
                    texto = texto.strip()  # remove os espaços em branco (espaços, tabulações e quebras de linha) no início e no final da string
                    print(texto)
                    return texto, True
                else:
                    print("Não houve resposta da API de IP:", url)
            except Exception as e:
                print("Tempo limite excedido ao procurar o elemento.")
                hora_atual = datetime.datetime.now().strftime('%H:%M:%S')
                print("Sem conexão com a internet, hora:", hora_atual, "nova tentativa e outro servidor")
                print(e)
                time.sleep(5)


def nao_tem_internet():
    falhou = False
    for i in range(60):
        try:
            response = requests.get('http://www.google.com', timeout=2)
            if response.status_code == 200:
                print("Conexão com a internet ativa...")
                time.sleep(0.5)  # Espera por 5 segundos antes de fazer o próximo teste
                if falhou:
                    time.sleep(15)
                    return
        except Exception as e:
            print("Sem conexão com a internet. Encerrando os testes...")
            print(e)
            print()
            time.sleep(5)
            falhou = True



def ip_troca_agora():
    while True:
        # com_internete = tem_internet()
        # if com_internete:
        if nome_usuario == "PokerIP":  # teste se o usuario do computador é o que troca IP se nao for fica esperando esta livre
            print("Vai par a função de trocar ip")
            conexao()  # chama a função que troca ip
            print('espera a internete estar estavel')
            tem_internet()  # testa ate que internete esteja estavel
            meu_ip_agora, teste = meu_ip()
            if testa_lista_negra_ip(meu_ip_agora):
                if ListaIpFirebase.verifica_e_adiciona_ip(meu_ip_agora):
                    print("Vai para a função que zera a contagem")
                    Google.zera_cont_IP(celula)  # Zera a contegem de ip na planilha
                    return
        elif (nome_usuario == "lgagu") and (nome_computador == "PC-I7-9700KF"):
            print("Vai par a função de trocar ip")
            conexao()  # chama a função que troca ip
            print('espera a internete estar estavel')
            tem_internet()  # testa ate que internete esteja estavel
            meu_ip_agora, teste = meu_ip()
            if testa_lista_negra_ip(meu_ip_agora):
                if ListaIpFirebase.verifica_e_adiciona_ip(meu_ip_agora):
                    print("Vai para a função que zera a contagem")
                    Google.zera_cont_IP(celula)  # Zera a contegem de ip na planilha
                    return
        else:
            return


# def contagem_IP():
#     while True:
#         try:
#             cont_IP = int(Google.pega_valor('IP', celula))  # pega o valor de contas que ja rodaram no IP atual
#             print("A contagem atual de IP é:", cont_IP)
#             return cont_IP
#         except Exception as e:
#             print(e)
#             continue


def ip(LIMITE_IP):
    # LIMITE_IP = 5

    while True:

        com_internete = tem_internet()
        # tem_internet() # testa se tem internete ativa
        cont_IP = int(Google.pega_valor('IP', celula))  # pega o valor de contas que ja rodaram no IP atual

        if com_internete:

            if cont_IP >= LIMITE_IP or cont_IP < 0:  # testa se esta maior que o lilite ou se esta negativo

                if nome_usuario == "PokerIP":  # teste se o usuario do computador é o que troca IP se nao for fica esperando esta livre
                    print("Vai par a função de trocar ip")
                    conexao()  # chama a função que troca ip
                    print('espera a internete estar estavel')
                    tem_internet()  # testa ate que internete esteja estavel
                    meu_ip_agora, teste = meu_ip()
                    if testa_lista_negra_ip(meu_ip_agora):
                        if ListaIpFirebase.verifica_e_adiciona_ip(meu_ip_agora):
                            print("Vai para a função que zera a contagem")
                            Google.zera_cont_IP(celula)  # Zera a contegem de ip na planilha
                            return

                elif (nome_usuario == "lgagu") and (nome_computador == "PC-I7-9700KF"):
                    print("Vai par a função de trocar ip")
                    conexao()  # chama a função que troca ip
                    print('espera a internete estar estavel')
                    tem_internet()  # testa ate que internete esteja estavel
                    meu_ip_agora, teste = meu_ip()
                    if testa_lista_negra_ip(meu_ip_agora):
                        if ListaIpFirebase.verifica_e_adiciona_ip(meu_ip_agora):
                            print("Vai para a função que zera a contagem")
                            Google.zera_cont_IP(celula)  # Zera a contegem de ip na planilha
                            return

                else:
                    print("Espera liberar IP")
                    nao_tem_internet()
                    continue

            else:
                print("Continua não tem que trocar IP")
                return


def conexao():
    while True:
        while True:
            # Tempo máximo para esperar (em segundos)
            tempo_passado = 0

            # Loop até que a janela esteja ativa ou o tempo máximo seja atingido
            while tempo_passado < 3:
                # Encontre a janela pelo título
                target_window = gw.getWindowsWithTitle("Configurações")

                # Verifique se a janela foi encontrada e está ativa
                if target_window and target_window[0].isActive:
                    print("Janela encontrada e ativa.")
                    break
                else:
                    print("Manda a jenela de conexao abrir")
                    if tipo_conexao == "vero":
                        os.system("start ms-settings:network-dialup")  # abre a conexão discada
                    elif tipo_conexao == "modem":
                        os.system("start ms-settings:network-airplanemode")  # modo aviao

                # Aguarde um curto período antes de verificar novamente
                time.sleep(0.2)
                tempo_passado += 0.2

            try:
                app = pywinauto.Application().connect(title=window_title, class_name=window_class)
                # A janela já está aberta, ative-a
                app_top_window = app.top_window()
                app_top_window.restore()
                app_top_window.move_window(x=conexao_x, y=conexao_y, width=500, height=330)
                # conexao_x = app_top_window.rectangle().left
                # conexao_y = app_top_window.rectangle().top
                app_top_window.set_focus()
                # Verifique se a janela está respondendo
                if app_top_window.is_active():
                    print("A janela está ativa.")
                    break
                time.sleep(0.5)
            except:
                # A janela não está aberta, abra-a
                target_window = gw.getWindowsWithTitle("Configurações")

                # Verifique se a janela foi encontrada
                if target_window:
                    # Feche a janela
                    target_window[0].close()
                    print("Janela configuraçoes ativa.")
                    time.sleep(1)
                else:
                    print("Janela não encontrada.")
                time.sleep(0.5)
                continue
        # time.sleep(0.5)
        if tipo_conexao == "vero":
            app_top_window.set_focus()
            print("conexão vero")
            cont_erro = 0
            clicou_conecar = False

            for _ in range(200):
                app_top_window.set_focus()
                posicao_telefone = localizar_imagem(telefone, regiao_telefone, precisao)
                if posicao_telefone is not None:
                    centro_discada = pyautogui.center(posicao_telefone)  # Obtém o centro da posição da imagem encontrada
                    pyautogui.click(centro_discada)  # Clica no centro da posição encontrada
                    print("clica no telefoen")

                    posicao_desconectar = localizar_imagem(desconectar, regiao_desconectar, precisao)
                    if posicao_desconectar is not None:
                        centro_desconectar = pyautogui.center(posicao_desconectar)  # Obtém o centro da posição da imagem encontrada
                        pyautogui.click(centro_desconectar)  # Clica no centro da posição encontrada
                        print("clica no desconectar")
                        time.sleep(1)

                    posicao_fechar = localizar_imagem(fechar, regiao_fechar, precisao)
                    if posicao_fechar is not None:
                        centro_fechar = pyautogui.center(posicao_fechar)  # Obtém o centro da posição da imagem encontrada
                        pyautogui.click(centro_fechar)  # Clica no centro da posição encontrada
                        print("clica no fechar 1")
                        time.sleep(2)

                    posicao_conectar = localizar_imagem(conectar, regiao_conectar, precisao)
                    if posicao_conectar is not None:
                        centro_conectar = pyautogui.center(posicao_conectar)  # Obtém o centro da posição da imagem encontrada
                        pyautogui.click(centro_conectar)  # Clica no centro da posição encontrada
                        time.sleep(1)
                        print("clica no conectar")
                        clicou_conecar = True
                        break
                time.sleep(0.3)

            if clicou_conecar:
                app_top_window.set_focus()
                for _ in range(200):
                    cont_erro += 1
                    posicao_conectado = localizar_imagem(conectado, regiao_conectado, precisao)
                    if posicao_conectado is not None:
                        print("Esta conectado")
                        # app_top_window.minimize()  # minimiza a janela
                        app_top_window.close()  # fecha a janela
                        return None

                    posicao_conectar = localizar_imagem(conectar, regiao_conectar, precisao)
                    if posicao_conectar is not None:
                        centro_conectar = pyautogui.center(posicao_conectar)  # Obtém o centro da posição da imagem encontrada
                        pyautogui.click(centro_conectar)  # Clica no centro da posição encontrada
                        print("clica no conectar 2")
                        time.sleep(1)

                    # se deu algum erro e nao conectou aparece um mensagem de erro e opção de fechar
                    posicao_fechar = localizar_imagem(fechar, regiao_fechar, precisao)
                    if posicao_fechar is not None:
                        cont_erro = 0
                        centro_fechar = pyautogui.center(posicao_fechar)  # Obtém o centro da posição da imagem encontrada
                        pyautogui.click(centro_fechar)  # Clica no centro da posição encontrada
                        print("clica no fechar 2")
                        time.sleep(2)

                    # se esta demorando muito para conectar clia em cancelar e tenta novamente
                    if cont_erro >= 60:
                        posicao_cancelar = localizar_imagem(cancelar, regiao_cancelar, precisao)
                        if posicao_cancelar is not None:
                            cont_erro = 0
                            centro_cancelar = pyautogui.center(posicao_cancelar)  # Obtém o centro da posição da imagem encontrada
                            pyautogui.click(centro_cancelar)  # Clica no centro da posição encontrada
                            time.sleep(2)
                    time.sleep(0.5)

        elif tipo_conexao == "modem":
            print('modem')

            for _ in range(400):
                app_top_window.set_focus()
                posicao_celular = localizar_imagem(celular, regiao_celular, precisao)
                if posicao_celular is not None:
                    centro_celular = pyautogui.center(posicao_celular)  # Obtém o centro da posição da imagem encontrada
                    posicao_botao = pyautogui.Point(centro_celular.x, centro_celular.y + 30)
                    posicao_ativado = localizar_imagem(ativado, regiao_ativado_desativado, precisao)
                    if posicao_ativado is not None:
                        time.sleep(0.3)
                        pyautogui.click(posicao_botao)  # Clica para desativar a coneção
                        print("foi desativado")
                        time.sleep(0.3)
                        for _ in range(50):
                            status = obter_status_conexao("Celular")
                            print('esperando desconectar')
                            if status == "Desconectado":
                                print(status)
                                time.sleep(0.5)
                                break
                            time.sleep(0.5)
                        app_top_window.set_focus()

                    posicao_desativado = localizar_imagem(desativado, regiao_ativado_desativado, precisao)
                    if posicao_desativado is not None:
                        pyautogui.click(posicao_botao)  # Clica para ativar a coneção
                        print("foi ativado")
                        for _ in range(100):
                            status = obter_status_conexao("Celular")
                            print('esperando conectar')
                            if status == "Conectado":
                                print(status)
                                # app_top_window.minimize()  # minimiza a janela
                                app_top_window.close()  # fecha a janela
                                return None
                            time.sleep(0.5)
                        app_top_window.set_focus()
                time.sleep(0.3)

        app_top_window.set_focus()
        app_top_window.close()  # fecha a janela
        print('Não consegiu realizar a abertura da janela de conexão para a troca de ip')
        time.sleep(1)

        # elif tipo_conexao == "vpn":
        #     conexao_vpn_x = 930
        #     conexao_vpn_y = 440
        #     while True:
        #         print('refazendo conexao')
        #         # testa se esta verde e ligado
        #         if pyautogui.pixelMatchesColor((conexao_vpn_vpn_x + 189), (conexao_vpn_vpn_y + 186), (15, 134, 108), tolerance=10) \
        #                 or pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (77, 182, 172), tolerance=10):
        #             pyautogui.click(conexao_vpn_x + 189, conexao_vpn_y + 186)
        #             print('desligou')
        #             for i in range(100):
        #                 # testa se esta vermelho e desligado
        #                 if pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (126, 15, 83), tolerance=10) \
        #                         or pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (164, 17, 94), tolerance=10):
        #                     time.sleep(0.5)
        #                     print('VPN Desconectado')
        #                     break
        #                 time.sleep(0.5)
        #
        #         # testa se esta vermelho e desligado
        #         elif pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (126, 15, 83), tolerance=10) \
        #                 or pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (164, 17, 94), tolerance=10):
        #             pyautogui.click(conexao_vpn_x + 189, conexao_vpn_y + 186)
        #             print('ligou')
        #             for i in range(100):
        #                 # testa se esta vermelho e desligado
        #                 if pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (15, 134, 108), tolerance=10) \
        #                         or pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (77, 182, 172), tolerance=10):
        #                     print('VPN Conectado')
        #                     # Minimizar a janela
        #                     vpn_window.minimize()
        #                     return None
        #                 time.sleep(0.5)
        # elif tipo_conexao == "vpn":
        #     # Caminho para o executável da VPN
        #
        #     caminho_executavel_vpn = "C:/Program Files (x86)/ExpressVPN/expressvpn-ui/ExpressVPN.exe"
        #     conexao_vpn_x = 930
        #     conexao_vpn_y = 440
        #     while True:
        #
        #         print('abre a vpn')
        #         try:
        #             vpn_window = gw.getWindowsWithTitle('ExpressVPN')[0]
        #             print(vpn_window)
        #             # vpn_window.activate()
        #             # Verificar se a janela está visível antes de movê-la
        #             if vpn_window.left == 930 and vpn_window.top == 440:
        #                 conexao_vpn_vpn_x = vpn_window.left
        #                 conexao_vpn_vpn_y = vpn_window.top
        #                 print("A posição da janela é (930, 440).")
        #                 break
        #             if vpn_window.left < 0 and vpn_window.top < 0:
        #                 print('esta minizada')
        #                 subprocess.Popen(caminho_executavel_vpn)
        #             else:
        #                 vpn_window.activate()
        #                 # Mover a janela da VPN para a posição desejada (x, y) da tela
        #                 conexao_vpn_vpn_x = 930
        #                 conexao_vpn_vpn_y = 440
        #
        #                 vpn_window.moveTo(conexao_vpn_vpn_x, conexao_vpn_vpn_y)
        #         except Exception as e:
        #             print("Erro ao abrir a VPN:", e)
        #             subprocess.Popen(caminho_executavel_vpn)
        #             time.sleep(5)
        #             continue
        #         time.sleep(0.5)


def localizar_imagem(imagem, regiao, precisao):
    try:
        posicao = pyautogui.locateOnScreen(imagem, region=regiao, confidence=precisao, grayscale=True)
        return posicao
    except:
        print("Ocorreu um erro ao localizar a imagem")
        time.sleep(2)
        return None


def obter_status_conexao(nome_conexao):
    conexoes = psutil.net_if_stats()
    if nome_conexao in conexoes:
        status = conexoes[nome_conexao].isup
        if status:
            return "Conectado"
        else:
            return "Desconectado"
    else:
        time.sleep(0.5)
        return "Conexão não encontrada"


# def obter_nomes_conexoes():
#     conexoes = psutil.net_if_stats()
#     nomes = conexoes.keys()
#     print(nomes)
#     return nomes


def testa_lista_negra_ip(meu_ip_agora):
    global lista_negra_ip
    global cont_lista_negra

    cont_lista_negra += 1

    if not lista_negra_ip:
        # lista_negra_ip = Google.lista_ip_banidos()
        lista_negra_ip = ListaIpFirebase.lista_ip_banidos()

    if cont_lista_negra >= 40:
        cont_lista_negra = 0
        # lista_negra_ip = Google.lista_ip_banidos()
        lista_negra_ip = ListaIpFirebase.lista_ip_banidos()

    print('testa lista negra')
    # meu_ip_agora, teste = meu_ip()
    if meu_ip_agora in lista_negra_ip:
        print(f"IP {meu_ip_agora} está na lista de IPs banidos.")
        return False
    else:
        print(f"IP {meu_ip_agora} não está na lista de IPs banidos.")
        return True

# # Exemplo de uso
# nomes_conexoes = obter_nomes_conexoes()
# for nome in nomes_conexoes:
#     print(nome)

# def ativar_destivar_conexao(nome_conexao, status):
#     try:
#         comando = f'netsh interface set interface "{nome_conexao}" admin="{status}"'
#         #subprocess.run(comando, shell=True, check=True)
#         subprocess.run(comando, shell=True, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
#         print(f"A conexão {nome_conexao} foi ativada com sucesso.")
#     except subprocess.CalledProcessError as e:
#         if e.returncode == 1:
#             ctypes.windll.shell32.ShellExecuteW(None, "runas", "python", __file__, None, 1)
#         else:
#             print(f"Erro ao ativar a conexão {nome_conexao}: {e}")


# #ip()
# #tem_internet()
#
# tipo_conexao = "modem"
# # # print("chma conexao")
# conexao(tipo_conexao)

# conexao()
