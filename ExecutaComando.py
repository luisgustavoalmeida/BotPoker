import datetime
import os
import socket
import threading
import time

import Firebase
import Google
import IP
import Limpa
import Mesa
import OCR_tela
import Origem_pg
import Seleniun
import Tarefas
import Aneis
import Recolher
import Cofre

# from Variaveis_Globais import alterar_global_aviso_sistema
#
# global aviso_sistema_global

# Obter o nome de usuário
nome_usuario = os.getlogin()
# Obter o nome do computador
nome_computador = socket.gethostname()
LIMITE_IP = 6

print("limite de troca de IP: ", LIMITE_IP)

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

posi_lista = 0

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
            id_novo, senha_novo, fichas_novo, linha_novo, cont_IP_novo = Google.credenciais(guia, False)  # pega id e senha para o proximo login
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

url = str(Google.pega_valor('Dados', 'F1'))

navegador = Seleniun.cria_nevegador()
Seleniun.abrir_navegador(url)
print('manda sair do facebook')
Seleniun.sair_face(url)

while True:
    # alterar_global_aviso_sistema(False)

    guia = 'Up'

    print("guia:", guia)
    if id == id_novo or id == "":

        id, senha, fichas, linha, cont_IP = Google.credenciais(guia, False)

        if id == "":
            Seleniun.sair_face(url)
            id, senha, fichas, linha, cont_IP = Google.credenciais(guia, False)
    else:
        id, senha, fichas, linha, cont_IP = id_novo, senha_novo, fichas_novo, linha_novo, cont_IP_novo

    Firebase.confirmacao_comando_resposta('Cont IP: ' + str(cont_IP))

    Firebase.confirmacao_escravo('Entrando em uma nova conta')  # troca o ultimo comando enviado

    # login
    while True:
        # parte deo codigo que faz loguin
        # ip, com_internet = IP.meu_ip()  # obtem meu endereço de IP
        ip = ""
        hora_que_rodou = 0
        valor_fichas = ""
        valor_fichas_perfil = ""
        pontuacao_tarefas = ""
        hora_atual = ""
        level_conta = ""
        status_poker = None
        valores = [""]
        roda = True
        entrou_corretamente = True
        stataus_facebook = 'Carregada'
        hora_fim_tarefa = False

        while roda:
            print('\n\n')
            time_atual = time.perf_counter()
            # print('time_id: ', time_id)
            # print('time_atua: ', time_atual)
            time_decorrido_id = time_atual - time_id
            print('time_decorrido_id: ', time_decorrido_id)
            print('cont_IP: ', cont_IP)
            print('\n\n')
            if (1 + cont_IP) >= LIMITE_IP or cont_IP < 0 or time_decorrido_id > 120:  # se a contagem de ip ta fora da faixa vai para a função
                IP.ip(LIMITE_IP)  # testa se o numero de contas esta dentro do limite antes de trocar ip

            entrou_corretamente, stataus_facebook = Seleniun.fazer_login(id, senha, url)

            print('____________________ manda iniciar a tarefa independete_________________')
            # Comando para iniciar a tarefa independente
            continuar_tarefa = True
            iniciar_tarefa.release()

            if entrou_corretamente is False:  # se nao entrou no face
                print("conta nao entou no Facebook")
                # Google.marca_caida(stataus_facebook, guia, linha)
                Firebase.confirmacao_comando_resposta('Conta não entou no Facebook: ' + stataus_facebook)

                break

            while True:

                if entrou_corretamente is True:
                    x_origem, y_origem, status_poker = Origem_pg.carregado_origem()
                    print(status_poker)
                    if status_poker is not None:
                        break

                entrou_corretamente, stataus_facebook = Seleniun.teste_logado()
                if entrou_corretamente is False:  # se nao entrou no face
                    print("conta nao entou no Facebook")
                    Firebase.confirmacao_comando_resposta('Conta não entou no Facebook: ' + stataus_facebook)
                    # Google.marca_caida(stataus_facebook, guia, linha)
                    break

            if entrou_corretamente is False:  # se nao entrou no face
                # Google.marca_caida(stataus_facebook, guia, linha)
                break

            Firebase.confirmacao_comando_resposta('Facebook: ' + stataus_facebook)

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

            Firebase.confirmacao_comando_resposta('Facebook: ' + stataus_facebook)

            #######################Tarefas
            if guia == "Up":

                Firebase.confirmacao_comando_resposta('Iniciou o limpa')

                pontuacao_tarefas = ""
                meta_atingida = False
                conta_upad = True
                valor_fichas = 0
                parar_tarefas = False
                lista_tarefas_fazer = []
                blind = '2K/4K'
                lugares = 9
                sorte = True

                if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
                    parar_tarefas = True
                    break
                if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                    parar_tarefas = True
                    break

                for i in range(7):
                    Limpa.limpa_total(x_origem, y_origem)
                    time.sleep(2)

                Firebase.confirmacao_comando_resposta('Terminou de limpa')

                # codigo deve ser escrito aqui dentro ...
                # status_comando = xp2.pega_2xp(x_origem, y_origem)
                # Firebase.confirmacao_comando_resposta(status_comando)

                recebido1 = "padrao"
                recebido2 = "padrao"
                comando = None
                status_comando_anterior = None

                valor_fichas = OCR_tela.valor_fichas(x_origem, y_origem, fichas)
                status_comando = 'Valor ficha: ' + str(valor_fichas)
                Firebase.confirmacao_comando_resposta(status_comando)

                # if valor_fichas < 300000:
                #     habilitado = False
                # else:
                #     habilitado = True
                #     # status_comando = 'Aguardando comando'
                #     status_comando = Mesa.escolher_blind(x_origem, y_origem, blind, lugares, posi_lista)
                #     Firebase.confirmacao_comando_resposta(status_comando)

                habilitado = True
                # status_comando = 'Aguardando comando'
                status_comando = Mesa.escolher_blind(x_origem, y_origem, blind, lugares, posi_lista)
                Firebase.confirmacao_comando_resposta(status_comando)

                while habilitado:
                    time.sleep(1)
                    # Limpa.limpa_total(x_origem, y_origem)

                    recebido1 = str(Firebase.comando_escravo())
                    if (recebido1 != recebido2) and (recebido1 is not None):
                        recebido2 = recebido1
                        comando = recebido1.strip().title()  # remove espaços vasiao e coloca a primeira letra amiusculo
                    print('comando :', comando)

                    Tarefas.recolher_tarefa_upando(x_origem, y_origem)

                    if comando == "Sair":
                        status_comando = "Saindo"
                        comando = 'Executado'
                        Firebase.confirmacao_escravo('Saindo')  # troca o ultimo comando enviado
                        break

                    elif comando == "Limpa":
                        status_comando = "Limpando"
                        comando = 'Executado'
                        for i in range(5):
                            Limpa.limpa_total(x_origem, y_origem)

                    elif comando == 'Levanta':
                        # status_comando = "levantando"
                        comando = 'Executado'
                        Firebase.confirmacao_comando_resposta("Levantando")
                        Mesa.levantar_mesa(x_origem, y_origem)
                        Limpa.limpa_jogando(x_origem, y_origem)
                        valor_fichas = OCR_tela.valor_fichas(x_origem, y_origem, fichas)
                        status_comando = 'Valor ficha: ' + str(valor_fichas)

                    elif comando == 'Cofre':
                        comando = 'Executado'
                        Cofre.cofre_abrir(x_origem, y_origem)
                        Cofre.cofre_sacar(x_origem, y_origem)

                    elif 'Posi_' in comando:
                        if comando == 'Posi_0':
                            posi_lista = 0
                        elif comando == 'Posi_1':
                            posi_lista = 1
                        elif comando == 'Posi_2':
                            posi_lista = 2

                        comando = 'Executado'

                    elif '/' in comando:
                        blind = comando
                        lugares = 9
                        # if blind == '20K/40K':
                        #     lugares = 5
                        # else:
                        #     lugares = 9
                        comando = 'Executado'
                        Limpa.limpa_total(x_origem, y_origem)
                        status_comando = Mesa.escolher_blind(x_origem, y_origem, blind, lugares, posi_lista)

                    elif comando == "Senta":
                        comando = 'Executado'
                        if Mesa.cadeiras_livres(x_origem, y_origem, lugares=lugares):
                            sentou = Mesa.sentar_mesa(x_origem, y_origem, True, blind, True)
                            if sentou:
                                status_comando = "Sentou"
                                # Mesa.mesa_recolher(x_origem, y_origem, 2, blind)
                                Recolher.mesa_recolher(x_origem, y_origem, 2, blind, sorte)
                            else:
                                status_comando = "Não sentou"
                        else:
                            status_comando = "Mesa ocupada"
                        time.sleep(2)
                        valor_fichas = OCR_tela.valor_fichas(x_origem, y_origem, fichas)
                        status_comando = 'Valor ficha: ' + str(valor_fichas)

                    elif comando == "Senta2":
                        # Começa ja apostando na primeira jogada
                        comando = 'Executado'
                        if Mesa.cadeiras_livres(x_origem, y_origem, lugares=lugares):
                            sentou = Mesa.sentar_mesa(x_origem, y_origem, True, blind, True)
                            if sentou:
                                status_comando = "Sentou"
                                # Mesa.mesa_recolher(x_origem, y_origem, 1, blind)
                                Recolher.mesa_recolher(x_origem, y_origem, 1, blind, sorte)
                            else:
                                status_comando = "Não sentou"
                        else:
                            status_comando = "Mesa ocupada"
                        time.sleep(2)
                        valor_fichas = OCR_tela.valor_fichas(x_origem, y_origem, fichas)
                        status_comando = 'Valor ficha: ' + str(valor_fichas)

                    elif comando == "Senta3":
                        print('Vai perder')
                        sorte = False
                        comando = 'Executado'

                    if status_comando_anterior != status_comando:
                        Firebase.confirmacao_comando_resposta(status_comando)
                        status_comando_anterior = status_comando

                Aneis.recolhe_aneis(x_origem, y_origem)

                Firebase.confirmacao_comando_resposta('Saindo da conta')

                valor_fichas_perfil = OCR_tela.valor_fichas_perfil(x_origem, y_origem)
                valor_fichas = OCR_tela.valor_fichas(x_origem, y_origem, fichas, valor_fichas_perfil)
                hora_que_rodou = datetime.datetime.now().strftime('%H:%M:%S')

                print('\n\nvalor_fichas', valor_fichas, '\n\n')

                roda = False
                break

        ip, com_internet = IP.meu_ip()  # obtem meu endereço de IP
        valores = [valor_fichas, pontuacao_tarefas, hora_que_rodou, ip, level_conta]
        Seleniun.sair_face(url)
        Firebase.confirmacao_escravo('Entrando em uma nova conta')  # troca o ultimo comando enviado

        print('-----------------espera terminar tarefa independente----------------')
        # Aguardar a tarefa terminar
        tarefa_concluida.acquire()

        print('tarefa independente liberada')

        while True:
            if not continuar_tarefa:
                break
            time.sleep(0.3)

        print('tarefa independente terminada')

        # id = ""

        if entrou_corretamente is False:  # se nao entrou no face

            print("Conta não entou, o Statos é: ", stataus_facebook)
            Google.marca_caida(stataus_facebook, guia, linha)
            id, senha, fichas, linha, cont_IP = id_novo, senha_novo, fichas_novo, linha_novo, cont_IP_novo


        elif status_poker == 'Banida':

            print("Conta não entou, o Statos é: ", status_poker)
            Google.marca_caida(status_poker, guia, linha)
            id, senha, fichas, linha, cont_IP = id_novo, senha_novo, fichas_novo, linha_novo, cont_IP_novo


        elif status_poker == 'Atualizar':

            print("Conta não entou, o Statos é: ", status_poker)
            id, senha, fichas, linha, cont_IP = id_novo, senha_novo, fichas_novo, linha_novo, cont_IP_novo


        elif entrou_corretamente:  # se nao entrou no face

            Google.escrever_valores_lote(valores, guia, linha)  # escreve as informaçoes na planilha apartir da coluna E
            id, senha, fichas, linha, cont_IP = id_novo, senha_novo, fichas_novo, linha_novo, cont_IP_novo

