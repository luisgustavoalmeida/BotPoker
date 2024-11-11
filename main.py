import datetime
import threading
import time

# import IP
from Google import (apagar_numerodo_pc, escrever_valores_lote, marca_caida, credenciais, pega_valor_endereco, escrever_celula,
                    retona_para_inicio_planilha, obter_id_proxy)
from IP import testa_contagem_ip, f5_quando_internete_ocila, ip_troca_agora, meu_ip, tem_internet, iniciando_testando_conexao_internet

import pyautogui
from colorama import Fore
import Aneis
import Cartas
import Cofre
import Firebase
import Firebase_cookies
import Genius
import HoraT
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
import Tratar_url
# from Firebase import ler_configuracao
from UparAuto import upar

from apagar_dados_navegador import limpar_todos_perfis

from Requerimentos import nome_computador, nome_usuario, tipo_conexao
from Sub_processo import fecha_cmd_atualisa_codigo, fecha_cmd_subistitui_codigo
from BancoDadosIP import incrementa_contagem_ip, decrementa_contagem_ip, indicar_pc_desativo
from Horario_atual import horario, dia_semana
from ListaIpFirebase import escolher_configuracao_e_db
from webshare_proxy import adicionar_ip_ao_servidor_proxy

adicionar_ip_ao_servidor_proxy()



print('\n\n         I N I C I A N D O \n\n')
iniciando_testando_conexao_internet()
escolher_configuracao_e_db()
# Firebase.sincronizar_cookies_com_firebase()
url = str(pega_valor_endereco('Dados!F1'))
url_link = str(pega_valor_endereco('Dados!F2'))
dic_links = Tratar_url.rodar_links(url_link)


Telegran.monta_mensagem(f'inicializando o codigo.  ⚡🤑', False)

LIMITE_IP = 6

x_origem = 4
y_origem = 266

id = "x"
guia = ""
guia_anterior = ""
guia_velha = ""
confg_funcao = 'roleta_auto'
confg_secundaria = 'auto'
confg_funcao_anterior = 'roleta_auto'
blind_recolher_auto = ''

cont_IP = 10
LEVEL_UPAR = 0.0280
blind = ""
lugares = ""
posi_lista = 0

time_id = 0
id_novo = "x"
senha_novo = ''
fichas_planilha_novo = ''
linha_novo = ''
level_novo = ''
continuar_tarefa = False

status_fim = None
entrou_corretamente_fim = True
hora_fim_tarefa_fim = False
guia_fim = ''
ip_fim = ''
linha_fim = ''
linha_novo_fim = ''
valores_fim = ['']

limpar_todos_perfis()

adicionar_ip_ao_servidor_proxy()

Firebase_cookies.sincronizar_cookies_com_firebase()

# Semaphore para iniciar a tarefa independente
iniciar_tarefa = threading.Semaphore(0)
# Semaphore para a tarefa independente indicar que terminou e aguardar novo comando
tarefa_concluida = threading.Semaphore(0)

# Função que será executada na tarefa independente
def tarefa_independente():
    global continuar_tarefa, guia, id_novo, senha_novo, fichas_planilha_novo, linha_novo, level_novo, time_id
    global status_fim, guia_fim, linha_fim, hora_fim_tarefa_fim, linha_novo_fim, valores_fim, entrou_corretamente_fim, ip_fim
    print(Fore.BLUE + "Executando tarefa independente... inicio" + Fore.RESET)

    while True:
        # Aguardar o comando para iniciar a execução
        iniciar_tarefa.acquire()
        print(Fore.BLUE + "Executando tarefa independente..." + Fore.RESET)
        # Verificar se a tarefa deve continuar executando ou parar
        if continuar_tarefa:
            print(status_fim, guia_fim, linha_fim, valores)
            if guia_fim:
                if entrou_corretamente_fim:  # se nao entrou no face
                    if hora_fim_tarefa_fim:
                        #  apaga os valore quando da a hoara de sair do tarefas
                        apagar_numerodo_pc([""], guia_fim, linha_fim)  # apaga o nume do pc
                    else:
                        # escreve os valores na planilha
                        escrever_valores_lote(valores_fim, guia_fim, linha_fim)  # escreve as informaçoes na planilha apartir da coluna E
                else:  # se nao entrou no face
                    marca_caida(status_fim, guia_fim, linha_fim, ip_fim)

            # Atualizar as variáveis
            id_novo, senha_novo, fichas_planilha_novo, linha_novo, level_novo = credenciais(guia)
            # pega id e senha para o proximo login
            time_id = time.perf_counter()
            continuar_tarefa = False
            # Indicar que a tarefa terminou e está pronta para aguardar novo comando
            print(Fore.BLUE + "Tarefa independente finalizada" + Fore.RESET)
            tarefa_concluida.release()
        else:
            print(Fore.BLUE + "Tarefa independente parada.\n" + Fore.RESET)
            # Indicar que a tarefa terminou de executar
            tarefa_concluida.release()


# # Iniciar a execução da tarefa independente
# tarefa = threading.Thread(target=tarefa_independente)
# tarefa.start()

# Função para iniciar a execução da tarefa independente em uma thread separada
def iniciar_tarefa_em_thread():
    thread = threading.Thread(target=tarefa_independente)
    thread.daemon = True  # Permite que a thread termine quando o programa principal terminar
    thread.start()


iniciar_tarefa_em_thread()

def logar_carregar():
    print('logar_carregar')
    global entrou_corretamente, stataus_facebook, continuar_tarefa, x_origem, y_origem, status_poker  # , confg_funcao, guia, url,

    print(Fore.GREEN + f'Entando em uma nova conta...' + Fore.RESET)

    proxy = None
    if tipo_conexao == 'proxy':
        print('Conexão tipo Proxy', id)

        proxy = dic_id_proxy.get(str(id), None)
        print(proxy)
        if proxy is None:
            print(f"O ID {id} não foi encontrado no dicionário.")
            return False
        else:
            print(f"logar_carregar - O proxy para o ID {id} é: {proxy}")

    else:
        testa_contagem_ip(LIMITE_IP, confg_funcao)  # testa se o numero de contas esta dentro do limite antes de trocar ip
        incrementa_contagem_ip()


    if confg_funcao in ('roleta_auto', 'R1', 'R2', 'R3', 'R4', 'R5'):
        if guia in ('R1', 'R2', 'R3', 'R4', 'R5'):
            numero = int(guia[1:]) - 1
            link_url = dic_links[numero]

        else:
            link_url = url

        print("logar_carregar", link_url)

        # loga nomamente no jogo
        Seleniun.iniciar_pefil(id, proxy, link_url)
        entrou_corretamente, stataus_facebook = Seleniun.fazer_login(id, senha, link_url, True, False,)
    elif confg_funcao in ('Recolher_automatico', 'Recolher', 'T1',):
        # loga nomamente no jogo
        Seleniun.iniciar_pefil(id, proxy)
        entrou_corretamente, stataus_facebook = Seleniun.fazer_login(id, senha, url, True, False)
    elif confg_funcao in ('Remover', 'Face'):
        url_remove_app = 'https://www.facebook.com/login.php?next=https%3A%2F%2Fwww.facebook.com%2Fsettings%3Ftab%3Dapplications%26ref%3Dsettings'
        if confg_funcao == 'Face':
            print('\n Loga apenas o Fecebook \n')
            Seleniun.iniciar_pefil(id, proxy)
            entrou_corretamente, stataus_facebook = Seleniun.fazer_login(id, senha, url_remove_app, False, True)
        elif confg_funcao == 'Remover':
            print('\n Inicia o remover poker Brasil \n')
            Seleniun.iniciar_pefil(id, proxy)
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

    if stataus_facebook == "Logou so face":
        return False

    if not entrou_corretamente:  # se nao entrou no face
        print("Conta não entrou no Facebook")
        return False

    while True:
        if entrou_corretamente:
            x_origem, y_origem, status_poker = Origem_pg.carregado_origem()
            print("Estatus correto da conta", status_poker)

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
        hora_que_rodou = horario().strftime('%H:%M:%S')

    if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
        return

    entrou_corretamente, stataus_facebook = Seleniun.teste_logado()
    if not entrou_corretamente:  # se nao entrou no face
        return

    if roleta == 'roleta_1':  # saber se roleta R1 ja terminou de rodar para sair da conta

        # para pegar os pontos das tarefas
        conta_upada = Limpa.limpa_abre_tarefa(x_origem, y_origem)  # retorna se a conta ta upada ou nao
        if conta_upada:
            f5_quando_internete_ocila()
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
            print(f'Tempo que ja clicou no girar: {tempo_total}')
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

    elif roleta == 'roleta_2':

        for _ in range(20):
            pyautogui.doubleClick(x_origem + 683, y_origem + 14)  # clica no icone roleta, ja roda sozinho
            time_sair = time.perf_counter()
            tempo_total = time_sair - time_rodou
            print('tempo que ja clicou no rodou', tempo_total)
            if tempo_total >= 2:
                print('ja pode sair do r2')
                break
            pyautogui.doubleClick(x_origem + 492, y_origem + 383)  # clica no meio da roleta para rodar
            time.sleep(0.3)

    return


def upar_t1():
    global x_origem, y_origem, conta_upada, level_conta, valor_fichas_perfil, dia_da_semana, hora_fim_tarefa, hora_que_rodou

    conta_upada = Limpa.limpa_abre_tarefa(x_origem, y_origem)  # retorna se a conta ta upada ou nao
    level_conta, valor_fichas_perfil = OCR_tela.level_conta(x_origem, y_origem)
    if level_conta < 10:
        print('Level_conta: ', level_conta)
        print('Valor_fichas_perfil: ', valor_fichas_perfil)
        if not HoraT.fim_tempo_tarefa():
            if (4 >= level_conta) or (not conta_upada):
                upar(x_origem, y_origem)

        conta_upada = Limpa.limpa_abre_tarefa(x_origem, y_origem)  # retorna se a conta ta upada ou nao
        level_conta, valor_fichas_perfil = OCR_tela.level_conta(x_origem, y_origem)

        if not HoraT.fim_tempo_tarefa():
            if (level_conta < 10) and (valor_fichas_perfil > 5000) and conta_upada:
                Mesa.mesa_upar_jogar_recolher_slote(x_origem, y_origem, funcoes='subir_level')

        level_conta, valor_fichas_perfil = OCR_tela.level_conta(x_origem, y_origem)
        hora_que_rodou = horario().strftime('%H:%M:%S')
        if HoraT.fim_tempo_tarefa():
            Limpa.limpa_total(x_origem, y_origem)
            print('Fim do horario destinado a tarefas')
            hora_fim_tarefa = True
    return


def tarefas():
    print('Entrou nas tarefas')
    global x_origem, y_origem, roleta, hora_que_rodou, entrou_corretamente, stataus_facebook, pontuacao_tarefas
    global level_conta, valor_fichas, hora_fim_tarefa, dia_da_semana

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

            print("--------------parte 1---------------")
            if parar_tarefas:
                break
            missao_encontrada = False
            for item_tarefa in lista_tarefas_fazer:
                print(item_tarefa)
                if 'Jogar o caca-niquel da mesa' in item_tarefa:
                    print('Jogar o caca-niquel da mesa')
                    missao_encontrada = True
                elif 'Gioca alla Slot machine al tavolo' in item_tarefa:
                    print('Gioca alla Slot machine al tavolo')
                    missao_encontrada = True

                if missao_encontrada:
                    print("\n\n Jogar o caca-niquel da mesa vezes.", item_tarefa)
                    Mesa.mesa_upar_jogar_recolher_slote(x_origem, y_origem, funcoes='slot', ajusta_aposta=200)
                    (parar_tarefas, valor_fichas, pontuacao_tarefas, lista_tarefas_fazer,
                     hora_fim_tarefa) = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, dia_da_semana)
                    missao_encontrada = False
            print("--------------parte 2---------------")
            if parar_tarefas:
                break
            missao_encontrada = False
            for item_tarefa in lista_tarefas_fazer:
                if ('maos em uma mesa com blinds acima de' in item_tarefa) or ('maos em qualquer mesa' in item_tarefa):
                    missao_encontrada = True
                elif ('mani su un tavolo con bui maggiori di' in item_tarefa) or ('mani su un tavolo qualsiasi' in item_tarefa):
                    missao_encontrada = True
                if missao_encontrada:
                    print("\n\n Jogar mão em uma mesa vezes.", item_tarefa)
                    Mesa.mesa_upar_jogar_recolher_slote(x_origem, y_origem, funcoes='tarefa_mesa')
                    (parar_tarefas, valor_fichas, pontuacao_tarefas, lista_tarefas_fazer,
                     hora_fim_tarefa) = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, dia_da_semana)
                    missao_encontrada = False

            print("--------------parte 3---------------")
            if parar_tarefas:
                break
            missao_encontrada = False
            for item_tarefa in lista_tarefas_fazer:
                if 'vezes nas Cartas Premiadas' in item_tarefa:
                    missao_encontrada = True
                elif 'la Carta Scommessa per' in item_tarefa:
                    missao_encontrada = True
                if missao_encontrada:
                    print("\n\n Jogar vezes nas Cartas Premiadas.", item_tarefa)
                    Cartas.cartas_premidas_joga_vezes(x_origem, y_origem)

                    (parar_tarefas, valor_fichas, pontuacao_tarefas, lista_tarefas_fazer,
                     hora_fim_tarefa) = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, dia_da_semana)
                    missao_encontrada = False

            print("--------------parte 4---------------")
            if parar_tarefas:
                break
            missao_encontrada = False
            for item_tarefa in lista_tarefas_fazer:
                if 'fichas nas Cartas Premiadas' in item_tarefa:
                    missao_encontrada = False
                elif 'fiches con la Carta Scommessa' in item_tarefa:
                    missao_encontrada = False

                if missao_encontrada:
                    print("\n\n Ganhar fichas nas Cartas Premiadas.", item_tarefa)
                    Cartas.cartas_premidas_joga_valor(x_origem, y_origem, lista_tarefas_fazer, valor_fichas)

                    (parar_tarefas, valor_fichas, pontuacao_tarefas, lista_tarefas_fazer,
                     hora_fim_tarefa) = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, dia_da_semana)
                    missao_encontrada = False

            print("--------------parte 5---------------")
            if parar_tarefas:
                break
            missao_encontrada = False
            for item_tarefa in lista_tarefas_fazer:
                if 'Jogar no Casino Genius Pro' in item_tarefa:
                    missao_encontrada = True
                elif 'Gioca la Carta Genio del Casino per' in item_tarefa:
                    missao_encontrada = True

                if missao_encontrada:
                    print("\n\n Jogar no Casino Genius Pro vezes.", item_tarefa)
                    Genius.genius_joga_vezes(x_origem, y_origem)
                    (parar_tarefas, valor_fichas, pontuacao_tarefas, lista_tarefas_fazer,
                     hora_fim_tarefa) = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, dia_da_semana)
                    missao_encontrada = False

            print("--------------parte 6---------------")
            if parar_tarefas:
                break
            missao_encontrada = False
            for item_tarefa in lista_tarefas_fazer:
                if 'fichas no Casino Genius Pro' in item_tarefa:
                    missao_encontrada = True
                elif 'fiches con la Carta Genio del Casino' in item_tarefa:
                    missao_encontrada = True
                if missao_encontrada:
                    print("\n\n Ganhar fichas no Casino Genius Pro.", item_tarefa)
                    Genius.genius_joga_valor(x_origem, y_origem, lista_tarefas_fazer, valor_fichas)
                    (parar_tarefas, valor_fichas, pontuacao_tarefas, lista_tarefas_fazer,
                     hora_fim_tarefa) = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, dia_da_semana)
                    missao_encontrada = False

            print("--------------parte 7---------------")
            if parar_tarefas:
                break
            missao_encontrada = False
            for item_tarefa in lista_tarefas_fazer:
                if 'Apostar 20 fichas ou mais em 9 linhas do caca' in item_tarefa:
                    missao_encontrada = True
                elif 'Scommetti 20 o piu su 9 linee della Poker Slot per ' in item_tarefa:
                    missao_encontrada = True

                if missao_encontrada:
                    print("\n\n Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot vezes.", item_tarefa)
                    Slot.solot_joga_vezes(x_origem, y_origem, True)
                    (parar_tarefas, valor_fichas, pontuacao_tarefas, lista_tarefas_fazer,
                     hora_fim_tarefa) = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, dia_da_semana)
                    missao_encontrada = False

            print("--------------parte 8---------------")
            if parar_tarefas:
                break
            missao_encontrada = False
            for item_tarefa in lista_tarefas_fazer:
                if 'fichas no caca niquel Slot Poker' in item_tarefa:
                    missao_encontrada = True
                elif 'fiches alla Poker Slot' in item_tarefa:
                    missao_encontrada = True

                if missao_encontrada:
                    print("\n\n Ganhar fichas no caca niquel slot poker.", item_tarefa)
                    Slot.solot_joga_vezes(x_origem, y_origem, False)
                    (parar_tarefas, valor_fichas, pontuacao_tarefas, lista_tarefas_fazer,
                     hora_fim_tarefa) = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, dia_da_semana)
                    missao_encontrada = False

            print("--------------parte 9---------------")
            if parar_tarefas:
                break
            missao_encontrada = False
            for item_tarefa in lista_tarefas_fazer:
                if 'fichas no caca niquel da mesa' in item_tarefa:
                    missao_encontrada = True
                elif 'fiches alla Slot machine al tavolo' in item_tarefa:
                    missao_encontrada = True

                if missao_encontrada:
                    print("\n\n Ganhar fichas no caca niquel da mesa.", item_tarefa)
                    Mesa.mesa_upar_jogar_recolher_slote(x_origem, y_origem, funcoes='slot', ajusta_aposta=2000)
                    # Mesa.mesa_upar_jogar(x_origem, y_origem, numero_jogadas=40, upar=False, blind_mesa='100200', apostar=False, recolher=False,
                    #                      level_conta=4, subir_level=False, jogar=False, slot=True, ajusta_aposta=2000)
                    (parar_tarefas, valor_fichas, pontuacao_tarefas, lista_tarefas_fazer,
                     hora_fim_tarefa) = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, dia_da_semana)
                    missao_encontrada = False

            print("--------------parte 10---------------")
            if parar_tarefas:
                break
            missao_encontrada = False

    hora_que_rodou = horario().strftime('%H:%M:%S')
    return


def recolher():
    global blind, lugares, valor_fichas, posi_lista, hora_que_rodou, valor_fichas_perfil, fichas_planilha

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

    valor_fichas = OCR_tela.valor_fichas(x_origem, y_origem, fichas_planilha)
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
            ip_troca_agora()

        elif comando == "Limpa":
            status_comando = "Limpando"
            comando = 'Executado'
            for i in range(3):
                Limpa.limpa_total(x_origem, y_origem)
                time.sleep(1)

        elif comando == 'Levanta':
            Mesa.levantar_mesa(x_origem, y_origem)
            Limpa.limpa_jogando(x_origem, y_origem)
            valor_fichas = OCR_tela.valor_fichas(x_origem, y_origem, fichas_planilha)
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
                sentou, ficha_suficiente = Mesa.sentar_mesa(x_origem, y_origem, True, blind, True)
                if sentou:
                    Recolher.mesa_recolher(x_origem, y_origem, 2, blind, sorte)
                else:
                    status_comando = "Não sentou"
            else:
                status_comando = "Mesa ocupada"
            time.sleep(2)
            valor_fichas = OCR_tela.valor_fichas(x_origem, y_origem, fichas_planilha)
            status_comando = 'Valor ficha: ' + str(valor_fichas)

        elif comando == "Senta2":
            # Começa ja apostando na primeira jogada
            comando = 'Executado'
            if Mesa.cadeiras_livres(x_origem, y_origem, lugares=lugares):
                sentou, ficha_suficiente = Mesa.sentar_mesa(x_origem, y_origem, True, blind, True)
                if sentou:
                    Recolher.mesa_recolher(x_origem, y_origem, 1, blind, sorte)
                else:
                    status_comando = "Não sentou"
            else:
                status_comando = "Mesa ocupada"
            time.sleep(2)
            valor_fichas = OCR_tela.valor_fichas(x_origem, y_origem, fichas_planilha)
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

    hora_que_rodou = horario().strftime('%H:%M:%S')

    valor_fichas_perfil = OCR_tela.valor_fichas_perfil(x_origem, y_origem)

    print('\nValor_fichas', valor_fichas, '\n')
    return


def recolher_automatico():
    global x_origem, y_origem, blind_recolher_auto, hora_que_rodou, fichas_planilha, valor_fichas, valor_fichas_perfil
    print('main recolher_autometico. Blid blind_recolher_auto:', blind_recolher_auto)
    Limpa.limpa_total(x_origem, y_origem)
    time.sleep(1)
    Limpa.limpa_total(x_origem, y_origem)
    time.sleep(1)
    Limpa.limpa_total(x_origem, y_origem)
    time.sleep(1)
    valor_minimo_mesa = Mesa.dicionario_salas[blind_recolher_auto][3]
    valor_fichas_perfil = OCR_tela.valor_fichas_perfil(x_origem, y_origem)
    valor_fichas_inicial = valor_fichas = OCR_tela.valor_fichas(x_origem, y_origem, fichas_planilha, valor_fichas_perfil)

    for _ in range(10):

        if valor_minimo_mesa >= valor_fichas:
            print(f'Fichas insuficiente para recolher:  {valor_fichas}. Mínimo para o blide é: {valor_minimo_mesa}')
            break
        elif (valor_fichas_inicial * 3) < valor_fichas:
            print(f'Conta ganhou no recolher automático: {valor_fichas}')
            break
        elif (valor_fichas_inicial / 3) > valor_fichas:
            print(f'Conta perdeu no recolher automático: {valor_fichas}')
            break

        # Mesa.mesa_upar_jogar(x_origem, y_origem, blind_mesa=blind_recolher_auto, apostar=False, recolher=True)
        Mesa.mesa_upar_jogar_recolher_slote(x_origem, y_origem, funcoes='recolher', blind_mesa=blind_recolher_auto)
        valor_fichas_perfil = OCR_tela.valor_fichas_perfil(x_origem, y_origem)
        valor_fichas = OCR_tela.valor_fichas(x_origem, y_origem, fichas_perfil=valor_fichas_perfil)
        try:
            blind_recolher_auto = Firebase.ler_configuracao()[2]
            valor_minimo_mesa = Mesa.dicionario_salas[blind_recolher_auto][3]
            print(blind_recolher_auto)
        except Exception as e:
            print(e)

    Limpa.limpa_total(x_origem, y_origem)
    hora_que_rodou = horario().strftime('%H:%M:%S')


def identifica_funcao():
    global id_novo, guia, guia_velha, confg_funcao_anterior, confg_funcao, blind_recolher_auto, guia_fim, linha_novo_fim, valores_fim, confg_secundaria

    try:
        confg_funcao, config_tempo_roleta, blind_recolher_auto, confg_secundaria = Firebase.ler_configuracao()
        print(confg_funcao, config_tempo_roleta, blind_recolher_auto)
    except Exception as e:
        print(e)
        print('Sera usado o pradrao roleta_auto')
        confg_funcao = 'roleta_auto'
        config_tempo_roleta = '3:50:5'

    if id_novo == "" and confg_funcao != 'roleta_auto':
        # Se a planilha chegou no final força atualização do fire base para o padrao
        print("Fim das atividades escolhidas manualmente, o programa retornara para o padrão Role'roleta_auto'")
        novos_dados = {'confg_funcao': 'roleta_auto', 'confg_secundaria': 'auto'}
        Firebase.atualizar_configuracao_pc(novos_dados)
        confg_funcao = 'roleta_auto'

    if confg_funcao == 'roleta_auto':
        guia = HoraT.mudar_guia(id_novo, guia, config_tempo_roleta)
        if ((guia == "R2") or (guia == "T1")) and (confg_secundaria != 'auto'):
            novos_dados = {'confg_funcao': confg_secundaria, 'confg_secundaria': 'auto'}
            Firebase.atualizar_configuracao_pc(novos_dados)
            confg_funcao, config_tempo_roleta, blind_recolher_auto, confg_secundaria = Firebase.ler_configuracao()
            if confg_funcao == 'Face':
                guia = 'Remover'
            elif confg_funcao == 'Recolher_automatico':
                guia = 'Recolher'
            else:
                guia = confg_funcao

    elif confg_funcao in ('Face', 'Remover', 'Recolher', 'Recolher_automatico', 'T1', 'R1', 'R2', 'R3', 'R4', 'R5'):
        if confg_funcao == 'Face':
            guia = 'Remover'
        elif confg_funcao == 'Recolher_automatico':
            guia = 'Recolher'
        else:
            guia = confg_funcao

    elif confg_funcao == "Atualizar_codigo":
        escrever_valores_lote(valores_fim, guia_fim, linha_fim)
        apagar_numerodo_pc([""], guia_fim, linha_novo_fim)
        Telegran.monta_mensagem(f'Atualização local de codigo {str(confg_funcao)}.  ⚙️', False)
        Seleniun.finaliza_navegador()
        print("Este script será interrompido e inicializado novamente!")
        fecha_cmd_atualisa_codigo()
        exit(0)

    elif confg_funcao == "Substituir_codigo":
        escrever_valores_lote(valores_fim, guia_fim, linha_fim)
        apagar_numerodo_pc([""], guia_fim, linha_novo_fim)
        Telegran.monta_mensagem(f'Atualização local de codigo {str(confg_funcao)}.  ⚙️', False)
        Seleniun.finaliza_navegador()
        print("Este script será interrompido e inicializado novamente!")
        fecha_cmd_subistitui_codigo()
        exit(0)

    elif confg_funcao == "Parar_codigo":
        escrever_valores_lote(valores_fim, guia_fim, linha_fim)
        apagar_numerodo_pc([""], guia_fim, linha_novo_fim)
        Telegran.monta_mensagem(f'A execução do programa foi interrompida {str(confg_funcao)}.  ⚙️', False)
        print("Este script será interrompido!")
        exit(0)

    elif confg_funcao == "Pausar_codigo":
        escrever_valores_lote(valores_fim, guia_fim, linha_fim)
        apagar_numerodo_pc([""], guia_fim, linha_novo_fim)
        retona_para_inicio_planilha()

        while confg_funcao == "Pausar_codigo":
            Telegran.monta_mensagem(f'A execução do programa foi pausada {str(confg_funcao)}.  ⚙️', False)
            print("Este script está pausado!")
            time.sleep(60)
            confg_funcao, config_tempo_roleta, blind_recolher_auto, confg_secundaria = Firebase.ler_configuracao()

        Telegran.monta_mensagem(f'A execução do programa foi retomada {str(confg_funcao)}.  ⚙️', False)
        if confg_funcao == 'roleta_auto':
            guia = HoraT.mudar_guia(id_novo, guia, config_tempo_roleta)

        elif confg_funcao == 'Face':
            guia = 'Remover'
        elif confg_funcao == 'Recolher_automatico':
            guia = 'Recolher'
        else:
            guia = confg_funcao

    else:
        Telegran.monta_mensagem(f'Padrão de configuração não esperado {str(confg_funcao)}.  ⚙️', False)
        print(f'Padrão de configuração não esperado {str(confg_funcao)}.')
        confg_funcao = confg_funcao_anterior
        guia = guia_velha

    if confg_funcao_anterior != confg_funcao and confg_funcao_anterior != '':
        Telegran.monta_mensagem(f'código alterado para modo {str(confg_funcao)}.  ⚙️', True)

    confg_funcao_anterior = confg_funcao
    guia_velha = guia
    print('identifica_funcao.  guia:', guia, 'confg_funcao: ', confg_funcao, 'blind_recolher_auto: ', blind_recolher_auto)


# Obter a guia a ser utilizada
identifica_funcao()

print('Guia: ', guia)
guia_anterior = guia

if guia != 'R1':
    url = 'https://apps.facebook.com/poker_italia'

# Obter as credenciais da conta do facebook
id, senha, fichas_planilha, linha, level_conta = credenciais(guia)

if id == '':
    id_novo = id
    apagar_numerodo_pc([""], guia, linha)  # apaga o nume do pc
    identifica_funcao()
    id, senha, fichas_planilha, linha, level_conta = credenciais(guia)

Telegran.monta_mensagem(f'Código iniciado com sucesso no modo {str(guia)}.  🚀', True)

dia_da_semana = dia_semana()  # 0 segunda, 1 terça, 2 quarta, 3 quinta, 4 sexta, 5 sábado, 6 domingo

print(Fore.GREEN + f'Novos dados...'
                   f'\nID: {id},'
                   f'\nSenha: {senha},'
                   f'\nFichas planilha: {fichas_planilha},'
                   f'\nLevel da conta {level_conta},' + Fore.RESET)

# indicar_pc_desativo()

while True:
    ip = ""
    hora_que_rodou = 0
    valor_fichas = ""
    valor_fichas_perfil = ""
    pontuacao_tarefas = ""
    roleta = 'roleta_1'
    conta_upada = True
    hora_atual = ""
    status_poker = None
    valores = [""]
    entrou_corretamente = True
    stataus_facebook = 'Carregada'
    hora_fim_tarefa = False

    # ################################################################################################################################################
    # Comando para iniciar a tarefa independente
    continuar_tarefa = True
    iniciar_tarefa.release()

    if logar_carregar():

        if confg_funcao == 'roleta_auto':
            # Roletas
            if guia in ["R1", "R2", "R3", "R4", "R5"]:
                print('Inicia a execução das Roletas')
                roletas()

            # Tarefas
            elif guia == "T1":
                print('Inicia a execução das Tarefas')
                upar_t1()
                tarefas()

        # Recolher
        elif confg_funcao == 'Recolher':
            print('Inicia a execução do Recolher')
            recolher()
        # Recolher automático
        elif confg_funcao == 'Recolher_automatico':
            print('Inicia a execução do Recolher automático')
            recolher_automatico()
        # Remover
        elif confg_funcao == 'Remover' or confg_funcao == 'Face':
            print('Inicia a execução do remover Poker')
            roletas()

        elif confg_funcao == "T1":
            print('Inicia a execução das Tarefas')
            upar_t1()
            tarefas()

        elif confg_funcao in ["R1", "R2", "R3", "R4", "R5"]:
            print('Inicia a execução das Roletas')
            roletas()

        Tarefas.recolher_tarefa_upando(x_origem, y_origem)
        Aneis.recolhe_aneis(x_origem, y_origem)
        valor_fichas = OCR_tela.valor_fichas(x_origem, y_origem, fichas_planilha, valor_fichas_perfil)
        if guia in 'R2':
            for numero in range(3, 10):
                link_url = dic_links[numero]
                feito = False
                for _ in range(3):
                    Seleniun.colocar_url_link(link_url)
                    print(f'link: {numero}\n{link_url}')
                    for _ in range(80):
                        if pyautogui.pixelMatchesColor((x_origem + 470), (y_origem + 530), (183, 25, 19), tolerance=15):
                            pyautogui.click(x_origem + 470, y_origem + 530)
                            print('link encontado')
                            feito = True
                            break
                        if pyautogui.pixelMatchesColor(429, 894, (17, 16, 16), tolerance=10):
                            print('Preto encontrado')
                            break
                        if pyautogui.pixelMatchesColor(429, 894, (255, 255, 255), tolerance=1):
                            pyautogui.click(x_origem + 470, y_origem + 530)
                            print('Branco encontrado...')
                            feito = True
                            break
                        time.sleep(0.1)
                    if feito:
                        break
                    for _ in range(80):
                        if pyautogui.pixelMatchesColor((x_origem + 470), (y_origem + 530), (183, 25, 19), tolerance=15):
                            pyautogui.click(x_origem + 470, y_origem + 530)
                            print('link encontado')
                            feito = True
                            break
                        if pyautogui.pixelMatchesColor(429, 894, (255, 255, 255), tolerance=1):
                            pyautogui.click(x_origem + 470, y_origem + 530)
                            print('Branco encontrado')
                            feito = True
                            break
                        time.sleep(0.1)
                    if feito:
                        break
                    # tem_internet()

        print(Fore.GREEN + '\nTerminou as atividades\n' + Fore.RESET)
    # ################################################################################################################################################
    ip, com_internet = meu_ip()  # obtem meu endereço de IP
    valores = [valor_fichas, pontuacao_tarefas, hora_que_rodou, ip, level_conta]
    print('Valores [valor_fichas, pontuacao_tarefas, hora_que_rodou, ip, level_conta]: ', valores)

    # Seleniun.sair_face()
    Seleniun.fechar_navegador(id)

    if not entrou_corretamente:  # se nao entrou no face
        decrementa_contagem_ip()
        status_fim = stataus_facebook
        print("Conta não entrou, o Statos é: ", stataus_facebook)

    elif status_poker == 'Banida' or status_poker == 'Bloqueado Temporariamente':

        status_fim = status_poker
        entrou_corretamente = False
        print("Conta não entrou, o Statos é: ", status_poker)


    # print('\n Espera terminar tarefa independente loop\n')
    tarefa_concluida.acquire()
    # print('\n Tarefa independente liberada loop\n')
    while True:
        if not continuar_tarefa:
            break
        time.sleep(0.3)
    # print('\n Tarefa independente terminada loop\n')

    guia_fim = guia
    linha_fim = linha
    linha_novo_fim = linha_novo
    valores_fim = valores
    ip_fim = ip
    entrou_corretamente_fim = entrou_corretamente
    hora_fim_tarefa_fim = hora_fim_tarefa

    identifica_funcao()
    if guia != guia_anterior:
        dia_da_semana = dia_semana()  # 0 segunda, 1 terça, 2 quarta, 3 quinta, 4 sexta, 5 sábado, 6 domingo
        print(Fore.CYAN + 'Mudando de guia' + Fore.RESET)
        Telegran.monta_mensagem(f'mudou para a guia {str(guia)}.  🗂️', True)

        # if ((nome_computador == "PC-I5-9400A") and (nome_usuario == "PokerIP")) or (nome_computador == "PC-I7-9700KF"):
        #     encontrado, link = Seleniun.busca_link()
        #     if encontrado:
        #         escrever_celula(link, 'Dados', 'F2')
        #         data_hora_atual = str(datetime.datetime.now())
        #         print('escreve a data da atialização: ', data_hora_atual)
        #         escrever_celula(data_hora_atual, 'Dados', 'F3')
        #         Telegran.monta_mensagem(f'Link fan page feito com sucesso. ', False)
        #     else:
        #         escrever_celula(link, 'Dados', 'F3')
        #         Telegran.monta_mensagem(f'  FALHA LINK FAN PAGE.    A T E N Ç Ã O !!! ', False)

        if guia in ('R1', 'R2', 'R3'):
            url_link = str(pega_valor_endereco('Dados!F2'))
            dic_links = Tratar_url.rodar_links(url_link)
        # elif guia in ('Remover', 'Recolher', 'T1'):
        #     url = 'https://apps.facebook.com/poker_italia'

        apagar_numerodo_pc([""], guia_fim, linha_novo_fim)  # apaga o nume do pc

        guia_anterior = guia
        id, senha, fichas_planilha, linha, level_conta = credenciais(guia)  # pega id e senha par o proximo login

    else:
        id, senha, fichas_planilha, linha, level_conta = id_novo, senha_novo, fichas_planilha_novo, linha_novo, level_novo

        print(Fore.GREEN + f'Novos dados...'
                           f'\nID: {id},'
                           f'\nSenha: {senha},'
                           f'\nFichas planilha: {fichas_planilha},'
                           f'\nLevel da conta {level_conta},' + Fore.RESET)
