import datetime
import os
import socket
import threading
import time

import pyautogui

import Aneis
import Cartas
import Cofre
import Firebase
import Genius
import Google
import HoraT
import IP
import Limpa
import Mesa
import OCR_tela
import Origem_pg
import Recolher
import Roletas
import Seleniun
import Slot
import Tarefas
import Telegran
from Firebase import ler_configuracao

global aviso_sistema_global

# Obter o nome de usuário
nome_usuario = os.getlogin()
# Obter o nome do computador
nome_computador = socket.gethostname()

# hora_atual = datetime.datetime.now()
# hora_formatada = hora_atual.strftime("%H:%M:%S")


Telegran.monta_mensagem(f'inicializando o codigo.  ⚡🤑', True)

LIMITE_IP = 6

x_origem = 4
y_origem = 266

id = "x"
guia = ""
confg_funcao = 'roleta_auto'
confg_funcao_anterior = ''
blind_recolher_auto = ''

senha = ""
fichas = ""
linha = ""
cont_IP = 10
blind = ""
lugares = ""
guia_anterior = ""
posi_lista = 0

# Variáveis globais para as variáveis e controle da tarefa independente
time_id = 0
id_novo = "x"
senha_novo = ""
fichas_novo = ""
linha_novo = ""
cont_IP_novo = ""
continuar_tarefa = False

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
entrou_corretamente = True
stataus_facebook = 'Carregada'
hora_fim_tarefa = False

url = str(Google.pega_valor('Dados', 'F1'))

navegador = Seleniun.cria_nevegador()

Seleniun.abrir_navegador(url)

Seleniun.sair_face(url)

# Semaphore para iniciar a tarefa independente
iniciar_tarefa = threading.Semaphore(0)
# Semaphore para a tarefa independente indicar que terminou e aguardar novo comando
tarefa_concluida = threading.Semaphore(0)


# Função que será executada na tarefa independente
def tarefa_independente():
    global continuar_tarefa, guia, id_novo, senha_novo, fichas_novo, linha_novo, cont_IP_novo, time_id

    while True:
        # Aguardar o comando para iniciar a execução
        iniciar_tarefa.acquire()
        print("\n Executando tarefa independente...\n")
        # Verificar se a tarefa deve continuar executando ou parar
        if continuar_tarefa:
            # Atualizar as variáveis
            id_novo, senha_novo, fichas_novo, linha_novo, cont_IP_novo = Google.credenciais(guia)  # pega id e senha para o proximo login
            time_id = time.perf_counter()
            continuar_tarefa = False
            # Indicar que a tarefa terminou e está pronta para aguardar novo comando
            print("\n Tarefa independente finalizada\n")
            tarefa_concluida.release()
        else:
            print("\n Tarefa independente parada.\n")
            # Indicar que a tarefa terminou de executar
            tarefa_concluida.release()


# Iniciar a execução da tarefa independente
tarefa = threading.Thread(target=tarefa_independente)
tarefa.start()


def logar_carregar():
    global entrou_corretamente, stataus_facebook, continuar_tarefa, x_origem, y_origem, status_poker, url, confg_funcao

    time_atual = time.perf_counter()
    time_decorrido_id = time_atual - time_id

    print('Entando em uma nova conta id / senha / cont_IP / time_decorrido_id: ', id, senha, cont_IP, time_decorrido_id)

    if (2 + cont_IP) >= LIMITE_IP or cont_IP < 0 or time_decorrido_id > 120:  # se a contagem de ip ta fora da faixa vai para a função
        IP.ip(LIMITE_IP)  # testa se o numero de contas esta dentro do limite antes de trocar ip

    if confg_funcao in ('Recolher_automatico', 'Recolher', 'roleta_auto', 'T1', 'R1', 'R2', 'R3', 'R4', 'R5'):
        # loga nomamente no jogo
        entrou_corretamente, stataus_facebook = Seleniun.fazer_login(id, senha, url, True, False)
    elif confg_funcao in ('Remover', 'Face'):
        url_remove_app = 'https://www.facebook.com/login.php?next=https%3A%2F%2Fwww.facebook.com%2Fsettings%3Ftab%3Dapplications%26ref%3Dsettings'
        if confg_funcao == 'Face':
            print('\n Loga apenas o Fecebook \n')
            entrou_corretamente, stataus_facebook = Seleniun.fazer_login(id, senha, url_remove_app, False, True)
        elif confg_funcao == 'Remover':
            print('\n Inicia o remover poker Brasil \n')
            entrou_corretamente, stataus_facebook = Seleniun.fazer_login(id, senha, url_remove_app, False, False)
            if stataus_facebook == 'Remover Poker não ok':
                while True:
                    print('Olhar manualmente')
                    Telegran.monta_mensagem(f'Olhar manualmente falhar remover poker. ', False)
                    # colocar um alarme no telegram
                    time.sleep(30)
    else:
        print('Padrao de configuração não esperado na função logar_carregar')
        Telegran.monta_mensagem(f'Padrao de configuração não esperado na função logar_carregar. ', True)
        stataus_facebook = 'confg_funcao fora do padrão'
        entrou_corretamente = False

    print('\n Manda iniciar a tarefa independete\n ')
    # Comando para iniciar a tarefa independente
    continuar_tarefa = True
    iniciar_tarefa.release()

    if stataus_facebook == "Logou so face":
        return False

    if not entrou_corretamente:  # se nao entrou no face
        print("Conta não entrou no Facebook")
        return False

    while True:
        if entrou_corretamente:
            x_origem, y_origem, status_poker = Origem_pg.carregado_origem()
            print(status_poker)
            if status_poker is not None:
                break

        entrou_corretamente, stataus_facebook = Seleniun.teste_logado()
        if not entrou_corretamente:  # se nao entrou no face
            print("Conta não entrou no Facebook")
            return False

    if status_poker != 'Carregada':  # testa status da conta
        if status_poker == 'Banida':  # se aconta esta banida
            print("Conta banida tem que marcar na plinilha")
            return False
        elif status_poker == 'Bloqueado Temporariamente':  # se aconta esta Bloqueado Temporariamente
            print("Conta Temporariamente bloqueado tem que marcar na plinilha")
            return False
        elif status_poker == 'Tutorial':
            print('Vai fazer tutorial')
            entrou_corretamente, stataus_facebook = Seleniun.teste_logado()
            if entrou_corretamente is False:  # se nao entrou no face
                return False
            time.sleep(2)
            if Limpa.limpa_pequeno(x_origem, y_origem) == "sair da conta":
                return False
            Limpa.faz_tutorial(x_origem, y_origem)
            if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                return False
        elif status_poker == 'Atualizar':
            return False
    entrou_corretamente, stataus_facebook = Seleniun.teste_logado()
    if not entrou_corretamente:  # se nao entrou no face
        return False

    if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
        return False
    print("\nIniciado corretamente\n")
    return True


def roletas():
    global x_origem, y_origem, roleta, hora_que_rodou, entrou_corretamente, stataus_facebook, conta_upada, pontuacao_tarefas
    global level_conta, valor_fichas_perfil, dia_da_semana

    roleta, hora_que_rodou, time_rodou = Roletas.roletas(x_origem, y_origem)
    print("Esta fazendo a roleta: ", roleta)

    if hora_que_rodou is None:
        hora_que_rodou = datetime.datetime.now().strftime('%H:%M:%S')

    if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
        return

    entrou_corretamente, stataus_facebook = Seleniun.teste_logado()
    if not entrou_corretamente:  # se nao entrou no face
        return

    if roleta == 'roleta_1':  # saber se roleta R1 ja terminou de rodar para sair da conta

        # para pegar os pontos das tarefas
        conta_upada = Limpa.limpa_abre_tarefa(x_origem, y_origem)  # retorna se a conta ta upada ou nao
        if conta_upada:
            IP.f5_quando_internete_ocila()
            entrou_corretamente, stataus_facebook = Seleniun.teste_logado()
            if not entrou_corretamente:  # se nao entrou no face
                return
            pontuacao_tarefas = OCR_tela.pontuacao_tarefas(x_origem, y_origem)
            Limpa.fecha_tarefa(x_origem, y_origem)

        level_conta, valor_fichas_perfil = OCR_tela.level_conta(x_origem, y_origem)
        print('Level_conta: ', level_conta)
        print('Valor_fichas_perfil: ', valor_fichas_perfil)

        for _ in range(50):
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

        level_conta, valor_fichas_perfil = Mesa.dia_de_jogar_mesa(x_origem, y_origem, level_conta, valor_fichas_perfil, conta_upada, dia_da_semana)

    elif roleta == 'roleta_2':
        for _ in range(20):
            pyautogui.doubleClick(x_origem + 683, y_origem + 14)  # clica no icone roleta, ja roda sozinho
            time_sair = time.perf_counter()
            tempo_total = time_sair - time_rodou
            print('tempo que ja clicou no rodou', tempo_total)
            if tempo_total >= 0.5:
                print('ja pode sair do r2')
                break
            time.sleep(0.3)

    # level_conta, valor_fichas_perfil = Mesa.dia_de_jogar_mesa(x_origem, y_origem, level_conta, valor_fichas_perfil, conta_upada, dia_da_semana)
    return


def tarefas():
    print('Entrou nas tarefas')
    global x_origem, y_origem, roleta, hora_que_rodou, entrou_corretamente, stataus_facebook, pontuacao_tarefas
    global level_conta, valor_fichas_perfil, valor_fichas, hora_fim_tarefa

    pontuacao_tarefas = 0
    valor_fichas = 0
    parar_tarefas = False
    lista_tarefas_fazer = []

    if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
        return
    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
        return

    for j in range(2):
        Aneis.recolhe_aneis(x_origem, y_origem)
        print('procura tarefa, tentativa: ', j)
        for _ in range(3):
            print('\n TAREFAS \n')

            (parar_tarefas, valor_fichas, pontuacao_tarefas, lista_tarefas_fazer,
             hora_fim_tarefa) = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, dia_da_semana)

            if parar_tarefas:
                break

            print("--------------parte 1---------------")
            for item_tarefa in lista_tarefas_fazer:
                if 'Jogar o caca-niquel da mesa' in item_tarefa:
                    print("\n\n Jogar o caca-niquel da mesa vezes \n\n")

                    Mesa.joga(x_origem, y_origem, 200)

                    (parar_tarefas, valor_fichas, pontuacao_tarefas, lista_tarefas_fazer,
                     hora_fim_tarefa) = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, dia_da_semana)

            print("--------------parte 2---------------")
            if parar_tarefas:
                break
            for item_tarefa in lista_tarefas_fazer:
                if 'vezes nas Cartas Premiadas' in item_tarefa:
                    print("\n\n Jogar vezes nas Cartas Premiadas \n\n")
                    Cartas.cartas_premidas_joga_vezes(x_origem, y_origem)

                    (parar_tarefas, valor_fichas, pontuacao_tarefas, lista_tarefas_fazer,
                     hora_fim_tarefa) = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, dia_da_semana)

            print("--------------parte 3---------------")
            if parar_tarefas:
                break
            for item_tarefa in lista_tarefas_fazer:
                if 'fichas nas Cartas Premiadas' in item_tarefa:
                    print("\n\n Ganhar fichas nas Cartas Premiadas \n\n")
                    Cartas.cartas_premidas_joga_valor(x_origem, y_origem, lista_tarefas_fazer, valor_fichas)

                    (parar_tarefas, valor_fichas, pontuacao_tarefas, lista_tarefas_fazer,
                     hora_fim_tarefa) = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, dia_da_semana)

            print("--------------parte 4---------------")
            if parar_tarefas:
                break
            for item_tarefa in lista_tarefas_fazer:
                if 'Jogar no Casino Genius Pro' in item_tarefa:
                    print("\n\n Jogar no Casino Genius Pro vezes \n\n")
                    Genius.genius_joga_vezes(x_origem, y_origem)
                    (parar_tarefas, valor_fichas, pontuacao_tarefas, lista_tarefas_fazer,
                     hora_fim_tarefa) = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, dia_da_semana)

            print("--------------parte 5---------------")
            if parar_tarefas:
                break
            for item_tarefa in lista_tarefas_fazer:
                if 'fichas no Casino Genius Pro' in item_tarefa:
                    print("\n\n Ganhar fichas no Casino Genius Pro \n\n")
                    Genius.genius_joga_valor(x_origem, y_origem, lista_tarefas_fazer)
                    (parar_tarefas, valor_fichas, pontuacao_tarefas, lista_tarefas_fazer,
                     hora_fim_tarefa) = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, dia_da_semana)

            print("--------------parte 6---------------")
            if parar_tarefas:
                break
            for item_tarefa in lista_tarefas_fazer:
                if 'Apostar 20 fichas ou mais em 9 linhas do caca' in item_tarefa:
                    print("\n\n Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot vezes \n\n")
                    Slot.solot_joga_vezes(x_origem, y_origem, True)
                    (parar_tarefas, valor_fichas, pontuacao_tarefas, lista_tarefas_fazer,
                     hora_fim_tarefa) = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, dia_da_semana)

            print("--------------parte 7---------------")
            if parar_tarefas:
                break
            for item_tarefa in lista_tarefas_fazer:
                if 'fichas no caca niquel Slot Poker' in item_tarefa:
                    print("\n\n Ganhar fichas no caca niquel slot poker \n\n")
                    Slot.solot_joga_vezes(x_origem, y_origem, False)
                    (parar_tarefas, valor_fichas, pontuacao_tarefas, lista_tarefas_fazer,
                     hora_fim_tarefa) = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, dia_da_semana)

            print("--------------parte 8---------------")
            if parar_tarefas:
                break
            for item_tarefa in lista_tarefas_fazer:
                if 'fichas no caca niquel da mesa' in item_tarefa:
                    print("\n\n Ganhar fichas no caca niquel da mesa \n\n")
                    Mesa.joga(x_origem, y_origem, 2000)
                    (parar_tarefas, valor_fichas, pontuacao_tarefas, lista_tarefas_fazer,
                     hora_fim_tarefa) = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, dia_da_semana)

            print("--------------parte 9---------------")
            if parar_tarefas:
                break

    hora_que_rodou = datetime.datetime.now().strftime('%H:%M:%S')
    return


def recolher():
    global blind, lugares, valor_fichas, posi_lista, hora_que_rodou, valor_fichas_perfil

    recebido1 = "padrao"
    recebido2 = "padrao"
    comando = None
    status_comando_anterior = None
    sorte = True
    valor_fichas = 0

    Firebase.confirmacao_comando_resposta('Iniciou o recolher')

    if blind == '':
        blind = '1K/2K'
    if lugares == '':
        lugares = 9

    if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
        return

    for i in range(4):
        if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
            return
        time.sleep(2)

    Firebase.confirmacao_comando_resposta('Terminou de limpa')

    valor_fichas = OCR_tela.valor_fichas(x_origem, y_origem, fichas)
    status_comando = 'Valor ficha: ' + str(valor_fichas)
    Firebase.confirmacao_comando_resposta(status_comando)

    # status_comando = 'Aguardando comando'
    status_comando = Mesa.escolher_blind(x_origem, y_origem, blind, lugares, posi_lista)
    Firebase.confirmacao_comando_resposta(status_comando)

    while True:
        time.sleep(1)
        # Limpa.limpa_total(x_origem, y_origem)

        recebido1 = str(Firebase.comando_escravo())
        if (recebido1 != recebido2) and (recebido1 is not None):
            recebido2 = recebido1
            comando = recebido1.strip().title()  # remove espaços vasiao e coloca a primeira letra amiusculo
            Firebase.confirmacao_comando_resposta(comando)
        print('comando :', comando)

        Tarefas.recolher_tarefa_upando(x_origem, y_origem)

        if comando == "Sair":
            break

        if comando == 'Trocarip':
            status_comando = "Trocando ip"
            IP.ip_troca_agora()

        elif comando == "Limpa":
            status_comando = "Limpando"
            comando = 'Executado'
            for i in range(3):
                Limpa.limpa_total(x_origem, y_origem)
                time.sleep(1)

        elif comando == 'Levanta':
            Mesa.levantar_mesa(x_origem, y_origem)
            Limpa.limpa_jogando(x_origem, y_origem)
            valor_fichas = OCR_tela.valor_fichas(x_origem, y_origem, fichas)
            status_comando = 'Valor ficha: ' + str(valor_fichas)

        elif comando == 'Cofre':
            Cofre.cofre_abrir(x_origem, y_origem)
            Cofre.cofre_sacar(x_origem, y_origem)

        elif 'Posi_' in comando:
            if comando == 'Posi_0':
                posi_lista = 0
            elif comando == 'Posi_1':
                posi_lista = 1
            else:
                posi_lista = 0
            status_comando = 'Posição ' + str(posi_lista)

        elif 'Lugar_' in comando:
            if comando == 'Lugar_9':
                lugares = 9
            elif comando == 'Lugar_5':
                lugares = 5
            else:
                lugares = 9
            status_comando = "Escolhido " + str(lugares)

        elif '/' in comando:
            blind = comando
            Limpa.limpa_total(x_origem, y_origem)
            status_comando = Mesa.escolher_blind(x_origem, y_origem, blind, lugares, posi_lista)

        elif comando == "Senta":
            comando = 'Executado'
            if Mesa.cadeiras_livres(x_origem, y_origem, lugares=lugares):
                sentou = Mesa.sentar_mesa(x_origem, y_origem, True, blind, True)
                if sentou:
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

        if comando != 'Executado':
            comando = 'Executado'

        if status_comando_anterior != status_comando:
            Firebase.confirmacao_comando_resposta(status_comando)
            status_comando_anterior = status_comando

    Firebase.confirmacao_comando_resposta('Saindo da conta')

    hora_que_rodou = datetime.datetime.now().strftime('%H:%M:%S')

    valor_fichas_perfil = OCR_tela.valor_fichas_perfil(x_origem, y_origem)

    print('\nValor_fichas', valor_fichas, '\n')
    return


def recolher_autometico():
    global x_origem, y_origem, blind_recolher_auto, hora_que_rodou, fichas, valor_fichas, valor_fichas_perfil
    print('main recolher_autometico. Blid blind_recolher_auto:', blind_recolher_auto)
    Limpa.limpa_total(x_origem, y_origem)
    time.sleep(1)
    Limpa.limpa_total(x_origem, y_origem)
    valor_fichas = OCR_tela.valor_fichas(x_origem, y_origem, fichas)
    valor_minimo_mesa = Mesa.dicionario_salas[blind_recolher_auto][3]
    Limpa.limpa_total(x_origem, y_origem)
    Mesa.atualizar_estatos_mesa('Fichas: ', valor_fichas)
    print('\nFichas Disponiveis: ', valor_fichas, '.Mínimo para o blide: ', valor_minimo_mesa,'\n')

    if valor_minimo_mesa < valor_fichas:
        Mesa.mesa_upar_jogar(x_origem, y_origem, blind_mesa=blind_recolher_auto, apostar=False, recolher=True)
        Limpa.limpa_total(x_origem, y_origem)
    else:
        print('Fichas insuficiente para recolher: ', valor_fichas, '.Mínimo para o blide é: ', valor_minimo_mesa)

    hora_que_rodou = datetime.datetime.now().strftime('%H:%M:%S')
    valor_fichas_perfil = OCR_tela.valor_fichas_perfil(x_origem, y_origem)

def identifica_funcao():
    global guia_anterior, id, guia, confg_funcao_anterior, confg_funcao, blind_recolher_auto
    try:
        confg_funcao, config_tempo_roleta, blind_recolher_auto = ler_configuracao()
        print(confg_funcao, config_tempo_roleta, blind_recolher_auto)
    except Exception as e:
        print(e)
        print('Sera usado o pradrao roleta_auto')
        confg_funcao = 'roleta_auto'
        config_tempo_roleta = '4:40:5'

    print(confg_funcao, config_tempo_roleta, blind_recolher_auto)

    if confg_funcao == 'roleta_auto':
        guia = HoraT.mudar_guia(id, guia, config_tempo_roleta)
    elif confg_funcao in ('Face', 'Remover', 'Recolher', 'Recolher_automatico', 'T1', 'R1', 'R2', 'R3', 'R4', 'R5'):
        if confg_funcao == 'Face':
            guia = 'Remover'
        elif confg_funcao == 'Recolher_automatico':
            guia = 'Recolher'
        else:
            guia = confg_funcao
    else:
        print(' Padrão de configuração não esperado, será usado o -roleta_auto- ')
        confg_funcao = 'roleta_auto'
        config_tempo_roleta = '4:40:5'
        guia = HoraT.mudar_guia(id, guia, config_tempo_roleta)

    if confg_funcao_anterior != confg_funcao and confg_funcao_anterior != '':
        Telegran.monta_mensagem(f'código alterado para modo {str(confg_funcao)}.  ⚙️', True)
    confg_funcao_anterior = confg_funcao

    print('identifica_funcao.  guia:', guia, 'confg_funcao: ', confg_funcao, 'blind_recolher_auto: ', blind_recolher_auto)


# Obter a guia a ser utilizada
identifica_funcao()

print('Guia: ', guia)
guia_anterior = guia
# Obter as credenciais da conta do facebook
id, senha, fichas, linha, cont_IP = Google.credenciais(guia)

Telegran.monta_mensagem(f'código iniciado com sucesso no modo {str(guia)}.  🚀', True)

while True:
    # ip = ""
    # hora_que_rodou = 0
    # valor_fichas = ""
    # valor_fichas_perfil = ""
    # pontuacao_tarefas = ""
    # level_conta = ""
    # roleta = 'roleta_1'
    # conta_upada = True
    # hora_atual = ""
    # status_poker = None
    # valores = [""]
    # entrou_corretamente = True
    # stataus_facebook = 'Carregada'
    # hora_fim_tarefa = False

    valores = [""]

    dia_da_semana = int(datetime.datetime.now().weekday())  # 0 segunda, 1 terça, 2 quarta, 3 quinta, 4 sexta, 5 sábado, 6 domingo
    print('dia_da_semana: ', dia_da_semana)
    # ################################################################################################################################################
    if logar_carregar():
        if confg_funcao == 'roleta_auto':
            # Roletas
            if guia in ["R1", "R2", "R3", "R4", "R5"]:
                print('Inicia a execução das Roletas')
                roletas()
            # Tarefas
            elif guia == "T1":
                print('Inicia a execução das Tarefas')
                tarefas()
        # Recolher
        elif confg_funcao == 'Recolher':
            print('Inicia a execução do Recolher')
            recolher()
        # Recolher automático
        elif confg_funcao == 'Recolher_automatico':
            print('Inicia a execução do Recolher automático')
            recolher_autometico()
        # Remover
        elif confg_funcao == 'Remover' or confg_funcao == 'Face':
            print('Inicia a execução do remover Poker')
            roletas()

        Tarefas.recolher_tarefa_upando(x_origem, y_origem)
        Aneis.recolhe_aneis(x_origem, y_origem)
        valor_fichas = OCR_tela.valor_fichas(x_origem, y_origem, fichas, valor_fichas_perfil)

        print('\nTerminou as atividades\n')
    # ################################################################################################################################################
    ip, com_internet = IP.meu_ip()  # obtem meu endereço de IP
    valores = [valor_fichas, pontuacao_tarefas, hora_que_rodou, ip, level_conta]
    print('Valores [valor_fichas, pontuacao_tarefas, hora_que_rodou, ip, level_conta]: ', valores)
    Seleniun.sair_face(url)

    print('\n Espera terminar tarefa independente loop\n')
    tarefa_concluida.acquire()

    print('\n Tarefa independente liberada loop\n')

    while True:
        if not continuar_tarefa:
            break
        time.sleep(0.3)

    print('\n Tarefa independente terminada loop\n')

    if entrou_corretamente is False:  # se nao entrou no face

        print("Conta não entrou, o Statos é: ", stataus_facebook)
        Google.marca_caida(stataus_facebook, guia, linha)

    elif status_poker == 'Banida' or status_poker == 'Bloqueado Temporariamente':
        print("Conta não entrou, o Statos é: ", status_poker)
        Google.marca_caida(status_poker, guia, linha)

    elif entrou_corretamente:  # se nao entrou no face
        if hora_fim_tarefa:
            valores = [""]
            #  apaga os valore quando da a hoara de sair do tarefas
            Google.apagar_numerodo_pc(valores, guia, linha)  # apaga o nume do pc
            Google.apagar_numerodo_pc(valores, guia, linha_novo)  # apaga o nume do pc
        else:
            # escreve os valores na planilha
            Google.escrever_valores_lote(valores, guia, linha)  # escreve as informaçoes na planilha apartir da coluna E

    identifica_funcao()

    if guia != guia_anterior:
        Telegran.monta_mensagem(f'mudou para a guia {str(guia)}.  🗂️', False)

        if (nome_computador == "PC-I5-9400A") and (nome_usuario == "PokerIP"):
            Seleniun.busca_link()
        elif nome_computador == "PC-I7-9700KF":
            Seleniun.busca_link()

        if guia in ('Remover', 'Recolher', 'T1', 'R1', 'R2', 'R3', 'R4', 'R5'):
            url = str(Google.pega_valor('Dados', 'F1'))

        guia_anterior = guia
        id, senha, fichas, linha, cont_IP = Google.credenciais(guia)  # pega id e senha par o proximo login

    else:
        id, senha, fichas, linha, cont_IP = id_novo, senha_novo, fichas_novo, linha_novo, cont_IP_novo
