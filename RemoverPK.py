import datetime
import os
import socket
import time

import pyautogui

import Google
import IP
import Limpa
import OCR_tela
import Origem_pg
import Roletas
import Seleniun
from Variaveis_Globais import alterar_global_aviso_sistema

global aviso_sistema_global

# Obter o nome de usuário
nome_usuario = os.getlogin()
# Obter o nome do computador
nome_computador = socket.gethostname()
LIMITE_IP = 6

print("limite de troca de IP: ", LIMITE_IP)

id = "x"
senha = ""
linha = ""
cont_IP = 10
guia = ""
guia_recebida = ""

ja_fez_tutorial = True

# Variáveis globais para as variáveis e controle da tarefa independente
id_novo = "x"
senha_novo = ""
fichas_novo = ""
linha_novo = ""
cont_IP_novo = ""
continuar_tarefa = False

# url = "https://pt-br.facebook.com/"
url = 'https://www.facebook.com/login.php?next=https%3A%2F%2Fwww.facebook.com%2Fsettings%3Ftab%3Dapplications%26ref%3Dsettings'

urlpkrl = "https://apps.facebook.com/rallyacespoker/?fb_source=appcenter&fb_appcenter=1"

navegador = Seleniun.cria_nevegador()
Seleniun.abrir_navegador(url)
while True:
    alterar_global_aviso_sistema(False)

    guia = 'Up'

    print("guia:", guia)
    if id == id_novo or id == "":

        id, senha, fichas, linha, cont_IP = Google.credenciais(guia)

        if id == "":
            Seleniun.sair_face(url)
            id, senha, fichas, linha, cont_IP  = Google.credenciais(guia)
    else:
        id, senha, fichas, linha, cont_IP = id_novo, senha_novo, fichas_novo, linha_novo, cont_IP_novo



    # login
    while True:

        # parte deo codigo que faz loguin
        # ip, com_internet = IP.meu_ip()  # obtem meu endereço de IP
        ip = ""
        hora_que_rodou = 0
        valor_fichas = ""
        pontuacao_tarefas = ""
        level_conta = ""
        roleta = 'roleta_1'
        conta_upada = True
        hora_atual = ""
        status_poker = None
        valores = [""]
        roda = True
        entrou_corretamente = True
        stataus_facebook = 'Carregada'
        hora_fim_tarefa = False

        while roda:

            # if cont_IP >= LIMITE_IP or cont_IP < 0:  # se a contagem de ip ta fora da faixa vai para a função
            IP.ip(LIMITE_IP)  # testa se o numero de contas esta dentro do limite antes de trocar ip

            entrou_corretamente, stataus_facebook = Seleniun.fazer_login(id, senha, url, False)

            if entrou_corretamente is False:  # se nao entrou no face
                print("Conta nao entou no Facebook")
                # Google.marca_caida(stataus_facebook, guia, linha)
                break

            print(" Tudo certo conta logada : ", stataus_facebook, 'poker brasil removido ')

            if stataus_facebook == 'Remover Poker não ok':
                while True:
                    print('Olhar manualmente')
                    time.sleep(10)

            # print('Loga no RL')
            # time.sleep(5)
            # navegador.get(urlpkrl)
            # print('espera 5 segundos')
            # time.sleep(15)

            while True:

                if entrou_corretamente is True:
                    x_origem, y_origem, status_poker = Origem_pg.carregado_origem()
                    print(status_poker)
                    if status_poker is not None:
                        break

                entrou_corretamente, stataus_facebook = Seleniun.teste_logado()
                if entrou_corretamente is False:  # se nao entrou no face
                    print("conta nao entou no Facebook")
                    # Google.marca_caida(stataus_facebook, guia, linha)
                    break

            if entrou_corretamente is False:  # se nao entrou no face
                # Google.marca_caida(stataus_facebook, guia, linha)
                break

            ja_fez_tutorial = True

            if status_poker != 'Carregada':  # testa status da conta
                if status_poker == 'Banida':  # se aconta esta banida
                    print("conta banida tem que marcar na plinilha")
                    # Google.marca_banida("Banida", guia, linha)
                    break

                elif status_poker == 'Tutorial':
                    ja_fez_tutorial = False
                    print('vai fazer tutorial')
                    entrou_corretamente, stataus_facebook = Seleniun.teste_logado()
                    if entrou_corretamente is False:  # se nao entrou no face
                        # Google.marca_caida(stataus_facebook, guia, linha)
                        break
                    time.sleep(2)
                    if Limpa.limpa_pequeno(x_origem, y_origem) == "sair da conta":
                        break
                    Limpa.faz_tutorial(x_origem, y_origem)
                    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                        break

                elif status_poker == 'Atualizar':
                    break

            entrou_corretamente, stataus_facebook = Seleniun.teste_logado()
            if entrou_corretamente is False:  # se nao entrou no face
                # Google.marca_caida(stataus_facebook, guia, linha)
                break

            if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
                break

            if guia != "T1":

                if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
                    break

                valor_fichas = OCR_tela.valor_fichas(x_origem, y_origem)
                # valor_fichas = OCR_tela.valor_fichas_perfil(x_origem, y_origem)
                # level_conta = OCR_tela.level_conta(x_origem, y_origem)

                roleta, hora_que_rodou, time_rodou = Roletas.roletas(x_origem, y_origem)
                print("roleta: ", roleta)

                if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
                    break

                if ja_fez_tutorial:  # so entra se a conta ja é velha
                    # para pegar os pontos das tarefas
                    if roleta == 'roleta_1':  # saber se roleta R1

                        conta_upada = Limpa.limpa_abre_tarefa(x_origem, y_origem)  # retorna se a conta ta upada ou nao
                        if conta_upada:
                            IP.f5_quando_internete_ocila()
                            entrou_corretamente, stataus_facebook = Seleniun.teste_logado()
                            if not entrou_corretamente:  # se nao entrou no face
                                # Google.marca_caida(stataus_facebook, guia, linha)
                                break
                            pontuacao_tarefas = OCR_tela.pontuacao_tarefas(x_origem, y_origem)
                            Limpa.fecha_tarefa(x_origem, y_origem)

                entrou_corretamente, stataus_facebook = Seleniun.teste_logado()
                if entrou_corretamente is False:  # se nao entrou no face
                    # Google.marca_caida(stataus_facebook, guia, linha)
                    break

                if hora_que_rodou is None:
                    hora_que_rodou = datetime.datetime.now().strftime('%H:%M:%S')

                if roleta == 'roleta_1':  # saber se roleta R1 ja terminou de rodar para sair da conta
                    for i in range(50):
                        time_sair = time.perf_counter()
                        tempo_total = time_sair - time_rodou
                        print('tempo que ja clicou no rodou: ', tempo_total)
                        if tempo_total >= 12:
                            print('ja pode sair do r1')
                            if pyautogui.pixelMatchesColor((x_origem + 495), (y_origem + 315), (211, 110, 12), tolerance=10):
                                # testa de roleta 1 ta aberta Pino dourado apontando para cima
                                pyautogui.click(882 + x_origem, 171 + y_origem)  # clica para fechar a roleta 1
                            break

                        time.sleep(0.3)
                        pyautogui.doubleClick(x_origem + 683, y_origem + 14)  # clica no icone da roleta para abir
                        if pyautogui.pixelMatchesColor((x_origem + 495), (y_origem + 315), (227, 120, 14), tolerance=20):
                            # testa de roleta 1 ta aberta
                            pyautogui.doubleClick(x_origem + 492, y_origem + 383)  # clica no meio da roleta para rodar

                    level_conta, valor_fichas_perfil = OCR_tela.level_conta(x_origem, y_origem)
                    # Mesa.dia_de_jogar_mesa(x_origem, y_origem, dia_da_semana, level_conta, time_rodou, roleta)

                elif roleta == 'roleta_2':
                    for i in range(20):
                        pyautogui.doubleClick(x_origem + 683, y_origem + 14)  # clica no icone roleta, ja roda sozinho
                        time_sair = time.perf_counter()
                        tempo_total = time_sair - time_rodou
                        print('tempo que ja clicou no rodou', tempo_total)
                        if tempo_total >= 0.5:
                            print('ja pode sair do r2')
                            break
                        time.sleep(0.3)

                # Tarefas.recolher_tarefa_upando(x_origem, y_origem)

                roda = False
                break

        ip, com_internet = IP.meu_ip()  # obtem meu endereço de IP
        valores = [valor_fichas, pontuacao_tarefas, hora_que_rodou, ip, level_conta]
        Seleniun.sair_face(url)

        id = ""

        if entrou_corretamente is False:  # se nao entrou no face

            print("Conta não entou, o Statos é: ", stataus_facebook)
            Google.marca_caida(stataus_facebook, guia, linha)
            # id, senha, linha, cont_IP = id_novo, senha_novo, linha_novo, cont_IP_novo
            break

        elif status_poker == 'Banida':

            print("Conta não entou, o Statos é: ", status_poker)
            Google.marca_caida(status_poker, guia, linha)
            # id, senha, linha, cont_IP = id_novo, senha_novo, linha_novo, cont_IP_novo
            break

        elif status_poker == 'Atualizar':

            print("Conta não entou, o Statos é: ", status_poker)
            # id, senha, linha, cont_IP = id_novo, senha_novo, linha_novo, cont_IP_novo
            break

        elif entrou_corretamente:  # se nao entrou no face

            Google.escrever_valores_lote(valores, guia, linha)  # escreve as informaçoes na planilha apartir da coluna E
            # id, senha, linha, cont_IP = id_novo, senha_novo, linha_novo, cont_IP_novo
            break
