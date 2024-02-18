import datetime
import os
import socket
import threading
import time

import pyautogui

import Aneis
import Cartas
import Genius
import Google
import HoraT
import IP
import Limpa
import Mesa
import OCR_tela
import Origem_pg
import Roletas
import Seleniun
import Slot
import Tarefas
from Variaveis_Globais import alterar_global_aviso_sistema

global aviso_sistema_global

# Obter o nome de usuário
nome_usuario = os.getlogin()
# Obter o nome do computador
nome_computador = socket.gethostname()
LIMITE_IP = 6

# print("limite de troca de IP: ", LIMITE_IP)

id = "x"
senha = ""
fichas = ""
linha = ""
cont_IP = 10
guia = ""
guia_recebida = ""

ja_fez_tutorial = True

# Variáveis globais para as variáveis e controle da tarefa independente
time_id = 0
id_novo = "x"
senha_novo = ""
fichas_novo = ""
linha_novo = ""
cont_IP_novo = ""
continuar_tarefa = False

# Semaphore para iniciar a tarefa independente
iniciar_tarefa = threading.Semaphore(0)
# Semaphore para a tarefa independente indicar que terminou e aguardar novo comando
tarefa_concluida = threading.Semaphore(0)


# Função que será executada na tarefa independente
def tarefa_independente():
    global continuar_tarefa
    global guia
    global id_novo
    global senha_novo
    global fichas_novo
    global linha_novo
    global cont_IP_novo
    global time_id

    while True:
        # Aguardar o comando para iniciar a execução
        iniciar_tarefa.acquire()
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        # Verificar se a tarefa deve continuar executando ou parar
        if continuar_tarefa:
            print("Executando tarefa independente...")

            # Atualizar as variáveis
            id_novo, senha_novo, fichas_novo, linha_novo, cont_IP_novo = Google.credenciais(guia)  # pega id e senha para o proximo login
            time_id = time.perf_counter()
            continuar_tarefa = False

            # Indicar que a tarefa terminou e está pronta para aguardar novo comando
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            tarefa_concluida.release()
        else:
            print("&&&&&&&&     &&&&&&&&     Tarefa independente parada.     &&&&&&&&     &&&&&&&&")
            # Indicar que a tarefa terminou de executar
            tarefa_concluida.release()


# Iniciar a execução da tarefa independente
tarefa = threading.Thread(target=tarefa_independente)
tarefa.start()

navegador = Seleniun.cria_nevegador()

url = str(Google.pega_valor('Dados', 'F1'))
pega_url = False

# navegador = Seleniun.cria_nevegador()
Seleniun.abrir_navegador(url)

while True:
    alterar_global_aviso_sistema(False)

    guia = HoraT.mudar_guia(id, guia)

    if pega_url:
        url = str(Google.pega_valor('Dados', 'F1'))
    pega_url = True

    print("guia:", guia)

    if id == id_novo or id == "":
        id, senha, fichas, linha, cont_IP = Google.credenciais(guia)

        if id == "":
            Seleniun.sair_face(url)
            guia = HoraT.mudar_guia(id, guia)
            id, senha, fichas, linha, cont_IP = Google.credenciais(guia)

    else:
        id, senha, fichas, linha, cont_IP = id_novo, senha_novo, fichas_novo, linha_novo, cont_IP_novo

    # 0 segunda, 1 terça, 2 quarta, 3 quinta, 4 sexta, 5 sabado,6 domingo

    # login
    while True:
        dia_da_semana = int(datetime.datetime.now().weekday())
        # dia_da_semana = int(datetime.datetime.now().weekday())  # busca o dia da semana 0 segunda 1 terça ... 6 domeingo
        print('dia_da_semana: ', dia_da_semana)
        # parte deo codigo que faz loguin
        # ip, com_internet = IP.meu_ip()  # obtem meu endereço de IP
        ip = ""
        hora_que_rodou = 0
        valor_fichas = ""
        valor_fichas_perfil = ""
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
        ja_fez_tutorial = True

        while roda:
            print('\n\n')
            time_atual = time.perf_counter()
            # print('time_id: ', time_id)
            # print('time_atua: ', time_atual)
            time_decorrido_id = time_atual - time_id
            print('time_decorrido_id: ', time_decorrido_id)
            print('cont_IP: ', cont_IP)
            print('\n\n')
            if (3 + cont_IP) >= LIMITE_IP or cont_IP < 0 or time_decorrido_id > 120:  # se a contagem de ip ta fora da faixa vai para a função
                IP.ip(LIMITE_IP)  # testa se o numero de contas esta dentro do limite antes de trocar ip

            entrou_corretamente, stataus_facebook = Seleniun.fazer_login(id, senha, url)

            print('____________________ manda iniciar a tarefa independete_________________')
            # Comando para iniciar a tarefa independente
            continuar_tarefa = True
            iniciar_tarefa.release()

            if not entrou_corretamente:  # se nao entrou no face
                print("conta nao entou no Facebook")
                break

            while True:
                if entrou_corretamente:
                    x_origem, y_origem, status_poker = Origem_pg.carregado_origem()
                    print(status_poker)
                    if status_poker is not None:
                        break

                entrou_corretamente, stataus_facebook = Seleniun.teste_logado()
                if not entrou_corretamente:  # se nao entrou no face
                    print("conta nao entou no Facebook")
                    break

            if not entrou_corretamente:  # se nao entrou no face
                break

            if status_poker != 'Carregada':  # testa status da conta
                if status_poker == 'Banida':  # se aconta esta banida
                    print("conta banida tem que marcar na plinilha")
                    break
                elif status_poker == 'Bloqueado Temporariamente':  # se aconta esta Bloqueado Temporariamente
                    print("conta Temporariamente bloqueado tem que marcar na plinilha")
                    break
                elif status_poker == 'Tutorial':
                    ja_fez_tutorial = False
                    print('vai fazer tutorial')
                    entrou_corretamente, stataus_facebook = Seleniun.teste_logado()
                    if entrou_corretamente is False:  # se nao entrou no face
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
            if not entrou_corretamente:  # se nao entrou no face
                break

            if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
                break

            ###########Roletas
            if guia != "T1":

                roleta, hora_que_rodou, time_rodou = Roletas.roletas(x_origem, y_origem)
                print("roleta: ", roleta)

                if hora_que_rodou is None:
                    hora_que_rodou = datetime.datetime.now().strftime('%H:%M:%S')

                if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
                    break

                entrou_corretamente, stataus_facebook = Seleniun.teste_logado()
                if not entrou_corretamente:  # se nao entrou no face
                    break

                if roleta == 'roleta_1':  # saber se roleta R1 ja terminou de rodar para sair da conta

                    # if ja_fez_tutorial:  # so entra se a conta ja é velha
                    # para pegar os pontos das tarefas
                    conta_upada = Limpa.limpa_abre_tarefa(x_origem, y_origem)  # retorna se a conta ta upada ou nao
                    if conta_upada:
                        IP.f5_quando_internete_ocila()
                        entrou_corretamente, stataus_facebook = Seleniun.teste_logado()
                        if not entrou_corretamente:  # se nao entrou no face
                            break
                        pontuacao_tarefas = OCR_tela.pontuacao_tarefas(x_origem, y_origem)
                        Limpa.fecha_tarefa(x_origem, y_origem)

                    level_conta, valor_fichas_perfil = OCR_tela.level_conta(x_origem, y_origem)
                    print('level_conta', level_conta)
                    print('valor_fichas_perfil', valor_fichas_perfil)

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

                    level_conta, valor_fichas_perfil = Mesa.dia_de_jogar_mesa(x_origem, y_origem, roleta, level_conta, valor_fichas_perfil,
                                                                              conta_upada, dia_da_semana)
                    print('level_conta', level_conta)
                    print('valor_fichas_perfil', valor_fichas_perfil)

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

                Tarefas.recolher_tarefa_upando(x_origem, y_origem)

                Aneis.recolhe_aneis(x_origem, y_origem)

                valor_fichas = OCR_tela.valor_fichas(x_origem, y_origem, fichas, valor_fichas_perfil)

                roda = False
                break

            #######################Tarefas
            elif guia == "T1":

                pontos_disponiveis = 200
                pontuacao_tarefas = 0
                meta_atingida = False
                conta_upad = True
                valor_fichas = 0
                parar_tarefas = False
                lista_tarefas_fazer = []

                if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
                    parar_tarefas = True
                    break
                if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                    parar_tarefas = True
                    break

                for _ in range(2):
                    Aneis.recolhe_aneis(x_origem, y_origem)
                    print('procura tarefa, tentativa:')
                    for i in range(3):
                        print('\n TAREFAS \n')

                        (parar_tarefas, valor_fichas, conta_upada, meta_atingida, pontuacao_tarefas, lista_tarefas_fazer, pontos_disponiveis,
                         hora_fim_tarefa) = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, dia_da_semana)

                        time.sleep(2)

                        if parar_tarefas:
                            print('Fim das tarefas')
                            time.sleep(2)
                            break

                        print("--------------parte 1---------------")

                        if ('Jogar o caca-niquel da mesa' in lista_tarefas_fazer
                                or 'Jogar o caca-niquel da mesa 150 vezes' in lista_tarefas_fazer
                                or 'Jogar o caca-niquel da mesa 70 vezes' in lista_tarefas_fazer
                                or 'Jogar o caca-niquel da mesa 10 vezes' in lista_tarefas_fazer):
                            print("\n\n Jogar o caca-niquel da mesa vezes \n\n")

                            Mesa.joga(x_origem, y_origem, 200)

                            (parar_tarefas, valor_fichas, conta_upada, meta_atingida, pontuacao_tarefas, lista_tarefas_fazer, pontos_disponiveis,
                             hora_fim_tarefa) = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, dia_da_semana)

                        print("--------------parte 2---------------")
                        if parar_tarefas:
                            break

                        if ('vezes nas Cartas Premiadas' in lista_tarefas_fazer
                                or 'Jogar 100 vezes nas Cartas Premiadas' in lista_tarefas_fazer
                                or 'Jogar 50 vezes nas Cartas Premiadas' in lista_tarefas_fazer
                                or 'Jogar 10 vezes nas Cartas Premiadas' in lista_tarefas_fazer):
                            print("\n\n Jogar vezes nas Cartas Premiadas \n\n")
                            Cartas.cartas_premidas_joga_vezes(x_origem, y_origem)

                            (parar_tarefas, valor_fichas, conta_upada, meta_atingida, pontuacao_tarefas, lista_tarefas_fazer, pontos_disponiveis,
                             hora_fim_tarefa) = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, dia_da_semana)

                        print("--------------parte 3---------------")
                        if parar_tarefas:
                            break

                        if ('fichas nas Cartas Premiadas' in lista_tarefas_fazer
                                or 'Ganhar 100.000 fichas nas Cartas Premiadas' in lista_tarefas_fazer
                                or 'Ganhar 30.000 fichas nas Cartas Premiadas' in lista_tarefas_fazer
                                or 'Ganhar 4.000 fichas nas Cartas Premiadas' in lista_tarefas_fazer):
                            print("\n\n Ganhar fichas nas Cartas Premiadas \n\n")
                            Cartas.cartas_premidas_joga_valor(x_origem, y_origem, lista_tarefas_fazer, valor_fichas)

                            (parar_tarefas, valor_fichas, conta_upada, meta_atingida, pontuacao_tarefas, lista_tarefas_fazer, pontos_disponiveis,
                             hora_fim_tarefa) = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, dia_da_semana)

                        if parar_tarefas:
                            break

                        if ('Jogar no Casino Genius Pro' in lista_tarefas_fazer
                                or 'Jogar no Casino Genius Pro 100 vezes' in lista_tarefas_fazer
                                or 'Jogar no Casino Genius Pro 50 vezes' in lista_tarefas_fazer
                                or 'Jogar no Casino Genius Pro 10 vezes' in lista_tarefas_fazer):
                            print("\n\n Jogar no Casino Genius Pro vezes \n\n")
                            Genius.genius_joga_vezes(x_origem, y_origem)

                            (parar_tarefas, valor_fichas, conta_upada, meta_atingida, pontuacao_tarefas, lista_tarefas_fazer, pontos_disponiveis,
                             hora_fim_tarefa) = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, dia_da_semana)

                        print("--------------parte 4---------------")
                        if parar_tarefas:
                            break

                        if ('fichas no Casino Genius Pro' in lista_tarefas_fazer
                                or 'Ganhar 100.000 fichas no Casino Genius Pro' in lista_tarefas_fazer
                                or 'Ganhar 30.000 fichas no Casino Genius Pro' in lista_tarefas_fazer
                                or 'Ganhar 4.000 fichas no Casino Genius Pro' in lista_tarefas_fazer):
                            print("\n\n Ganhar fichas no Casino Genius Pro \n\n")
                            Genius.genius_joga_valor(x_origem, y_origem, lista_tarefas_fazer)

                            (parar_tarefas, valor_fichas, conta_upada, meta_atingida, pontuacao_tarefas, lista_tarefas_fazer, pontos_disponiveis,
                             hora_fim_tarefa) = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, dia_da_semana)

                        print("--------------parte 5---------------")
                        if parar_tarefas:
                            break

                        if ('Apostar 20 fichas ou mais em 9 linhas do caca' in lista_tarefas_fazer
                                or 'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 150 vezes' in lista_tarefas_fazer
                                or 'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 70 vezes' in lista_tarefas_fazer
                                or 'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 10 vezes' in lista_tarefas_fazer):
                            print("\n\n Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot vezes \n\n")

                            Slot.solot_joga_vezes(x_origem, y_origem, True)

                            (parar_tarefas, valor_fichas, conta_upada, meta_atingida, pontuacao_tarefas, lista_tarefas_fazer, pontos_disponiveis,
                             hora_fim_tarefa) = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, dia_da_semana)

                        print("--------------parte 6---------------")
                        if parar_tarefas:
                            break

                        if ('fichas no caca niquel slot poker' in lista_tarefas_fazer
                                or 'Ganhar 100.000 fichas no caca niquel Slot Poker' in lista_tarefas_fazer
                                or 'Ganhar 30.000 fichas no caca niquel Slot Poker' in lista_tarefas_fazer
                                or 'Ganhar 10.000 fichas no caca niquel Slot Poker' in lista_tarefas_fazer):
                            print("\n\n Ganhar fichas no caca niquel slot poker \n\n")

                            Slot.solot_joga_vezes(x_origem, y_origem, False)

                            (parar_tarefas, valor_fichas, conta_upada, meta_atingida, pontuacao_tarefas, lista_tarefas_fazer, pontos_disponiveis,
                             hora_fim_tarefa) = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, dia_da_semana)

                        print("--------------parte 7---------------")
                        if parar_tarefas:
                            break

                        if ('fichas no caca niquel da mesa' in lista_tarefas_fazer
                                or 'Ganhar 100.000 fichas no caca niquel da mesa' in lista_tarefas_fazer
                                or 'Ganhar 30.000 fichas no caca niquel da mesa' in lista_tarefas_fazer
                                or 'Ganhar 10.000 fichas no caca niquel da mesa' in lista_tarefas_fazer):
                            print("\n\n Ganhar fichas no caca niquel da mesa \n\n")

                            Mesa.joga(x_origem, y_origem, 2000)

                            (parar_tarefas, valor_fichas, conta_upada, meta_atingida, pontuacao_tarefas, lista_tarefas_fazer, pontos_disponiveis,
                             hora_fim_tarefa) = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, dia_da_semana)

                        print("--------------parte 8---------------")
                        if parar_tarefas:
                            break

                Aneis.recolhe_aneis(x_origem, y_origem)
                hora_que_rodou = datetime.datetime.now().strftime('%H:%M:%S')

                print('valor_fichas', valor_fichas)
                print('pontuacao_tarefas', pontuacao_tarefas)
                print('hora_que_rodou', hora_que_rodou)

                roda = False
                break

        ip, com_internet = IP.meu_ip()  # obtem meu endereço de IP
        valores = [valor_fichas, pontuacao_tarefas, hora_que_rodou, ip, level_conta]
        Seleniun.sair_face(url)

        print('-----------------espera terminar tarefa independente----------------')
        # Aguardar a tarefa terminar
        tarefa_concluida.acquire()

        print('tarefa independente liberada')

        while True:
            if not continuar_tarefa:
                break
            time.sleep(0.3)

        print('tarefa independente terminada')

        if entrou_corretamente is False:  # se nao entrou no face

            print("Conta não entou, o Statos é: ", stataus_facebook)
            Google.marca_caida(stataus_facebook, guia, linha)
            id, senha, fichas, linha, cont_IP = id_novo, senha_novo, fichas_novo, linha_novo, cont_IP_novo

        elif status_poker == 'Banida' or status_poker == 'Bloqueado Temporariamente':

            print("Conta não entou, o Statos é: ", status_poker)
            Google.marca_caida(status_poker, guia, linha)
            id, senha, fichas, linha, cont_IP = id_novo, senha_novo, fichas_novo, linha_novo, cont_IP_novo

        elif status_poker == 'Atualizar':

            print("Conta não entou, o Statos é: ", status_poker)
            id, senha, fichas, linha, cont_IP = id_novo, senha_novo, fichas_novo, linha_novo, cont_IP_novo

        elif entrou_corretamente:  # se nao entrou no face

            if hora_fim_tarefa:
                valores = [""]
                #  apaga os valore quando da a hoara de sair do tarefas
                Google.apagar_numerodo_pc(valores, guia, linha)  # apaga o nume do pc
                Google.apagar_numerodo_pc(valores, guia, linha_novo)  # apaga o nume do pc

            else:
                # escre os valores na planilha
                Google.escrever_valores_lote(valores, guia, linha)  # escreve as informaçoes na planilha apartir da coluna E
                id, senha, fichas, linha, cont_IP = id_novo, senha_novo, fichas_novo, linha_novo, cont_IP_novo

        guia_recebida = HoraT.mudar_guia(id, guia)
        if guia != guia_recebida:

            if (nome_computador == "PC-I5-9400A") and (nome_usuario == "PokerIP"):
                Seleniun.busca_link()
            elif nome_computador == "PC-I7-9700KF":
                Seleniun.busca_link()

            dia_da_semana = datetime.datetime.now().weekday()  # busca o dia da semana 0 segunda 1 terça ... 6 domeingo
            url = str(Google.pega_valor('Dados', 'F1'))
            guia = guia_recebida
            id, senha, fichas, linha, cont_IP = Google.credenciais(guia)  # pega id e senha par o proximo login
        guia = guia_recebida

        # cont_IP = IP.contagem_IP()
