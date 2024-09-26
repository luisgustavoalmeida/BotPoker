import time

import pyautogui

# import Google
import IP
from F5_navegador import atualizar_navegador
# from ListaIpFirebase import escrever_IP_banido
from Requerimentos import nome_computador, nome_usuario
from Seleniun import teste_logado

# Desabilitar o fail-safe
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0

# Define o nome do arquivo da imagem a ser buscada
origem = r'Imagens\Origem.png'
origem1 = r'Imagens\Origem1.png'
origemB = r'Imagens\OrigemB.png'
origem2 = r'Imagens\OrigemAvisoDoSistema.png'

# Define a região da tela onde a imagem será buscada
regiao_busca = (0, 210, 120, 290)  # (x, y, largura, altura)
precisao_origem = 0.997


def localizar_imagem(imagem, regiao, precisao):
    try:
        posicao = pyautogui.locateOnScreen(imagem, region=regiao, confidence=precisao, grayscale=True)
        return posicao
    except:
        print("Ocorreu um erro ao localizar a imagem")
        time.sleep(2)
        return None


def carregado_origem():  # navegador
    status_conta = None
    cont_erro = 0
    cont_erro_fundo_preto = 0

    for i in range(3):

        posicao = None
        # Faz x buscas com um intervalo de x segundos entre cada busca
        # print(" 0 x 0...")

        # JanelaSuperior.encontrar_janela_navegador()
        # pyautogui.click(10, 1020)  # clica bobo para nao hibernar

        print("carregado_orige Procurando coodenada 0 x 0...")
        for i in range(80):

            # Procura a imagem na região definida com 99,5% de tolerância, em escala de cinza e retorna a posição

            posicao = localizar_imagem(origem, regiao_busca, precisao_origem)
            if posicao is not None:  # Verifica se a imagem foi encontrada
                x_origem, y_origem = posicao.left, posicao.top
                x_origem = int(x_origem)
                y_origem = int(y_origem)
                print("x_origem: ", x_origem)
                print("y_origem: ", y_origem)
                if status_conta != 'Tutorial':
                    status_conta = 'Carregada'
                return x_origem, y_origem, status_conta
            posicao = localizar_imagem(origem1, regiao_busca, precisao_origem)
            if posicao is not None:  # Verifica se a imagem foi encontrada
                x_origem, y_origem = posicao.left, posicao.top
                x_origem = int(x_origem)
                y_origem = int(y_origem)
                print("x_origem: ", x_origem)
                print("y_origem: ", y_origem)
                if status_conta != 'Tutorial':
                    status_conta = 'Carregada'
                return x_origem, y_origem, status_conta
            else:

                localizado = localizar_imagem(imagem=r'Imagens\Aceite.png', regiao=(380, 400, 250, 350), precisao=0.8)
                if localizado is not None:
                    centro = pyautogui.center(localizado)
                    pyautogui.doubleClick(centro.x, centro.y, button='left')
                    print("clica no aceite")
                    status_conta = 'Tutorial'
                    time.sleep(2)

                localizado = localizar_imagem(imagem=r'Imagens\Banida.png', regiao=(250, 400, 300, 300), precisao=0.8)
                if localizado is not None:
                    print("comta banida para o poker")
                    status_conta = 'Banida'
                    return 0, 0, status_conta

                localizado = localizar_imagem(imagem=r'Imagens\Temporariamente.png', regiao=(540, 180, 200, 80), precisao=0.8)
                if localizado is not None:
                    print("Você está bloquadao temporariamente imagem reconhecida")
                    status_conta = 'Bloqueado Temporariamente'
                    return 0, 0, status_conta

                if (pyautogui.pixelMatchesColor(700, 130, (66, 103, 178), tolerance=5)
                        and pyautogui.pixelMatchesColor(700, 300, (242, 242, 242), tolerance=5)):
                    # testa se tem a barra azul do facebook e testa se tem uma barra cinza da mensagem do temporarimente bloqueado
                    print("Você está bloquadao temporariamente cor reconhecida")
                    status_conta = 'Bloqueado Temporariamente'
                    return 0, 0, status_conta

                localizado = localizar_imagem(imagem=r'Imagens\Continuar2.png', regiao=(440, 480, 330, 270), precisao=0.8)
                if localizado is not None:
                    centro = pyautogui.center(localizado)
                    pyautogui.doubleClick(centro.x, centro.y, button='left')
                    print("clica no continuar")
                    time.sleep(7)

                localizado = localizar_imagem(imagem=r'Imagens\Continuar3.png', regiao=(620, 640, 360, 170), precisao=0.8)
                if localizado is not None:
                    centro = pyautogui.center(localizado)
                    pyautogui.doubleClick(centro.x, centro.y, button='left')
                    print("clica no continuar")
                    time.sleep(7)

                localizado = localizar_imagem(imagem=r'Imagens\Atualizar.png', regiao=(410, 400, 580, 300), precisao=0.8)
                if localizado is not None:
                    print("Erro ao entrar no Lobby, tente atualizar a pagina")
                    status_conta = 'Atualizar'
                    return 0, 0, status_conta

                localizado = localizar_imagem(imagem=r'Imagens\CarosJogadores.png', regiao=(340, 800, 385, 105), precisao=0.995)
                if localizado is not None:

                    print("\n\nCaros jogadores, para garantir um ambiente de jogo mais estável e melhor, o servidor esta em "
                          "manutenção. Durante esse período, talvez voçê não consiga acessar o jogo. Pedimos desculpas "
                          "por qualquer inconveniente. E obrigado pelo seu apoio e compreensão!\n")

                    if (nome_usuario == "PokerIP") or (nome_computador == "PC-I7-9700KF"):
                        # teste se o usuario do computador é o que troca IP se nao for fica esperando esta livre
                        print('computador principarl vai marcar o IP banido')
                        # ip, com_internet = IP.meu_ip()
                        # Google.escrever_IP_banido(ip)
                        # escrever_IP_banido(ip)
                        print('manda trocar IP')
                        IP.ip_troca_agora()
                    else:
                        print('Não é um computador prncipal, apenas espera liberar um novo ip')
                        time.sleep(30)

                    print('origem da um f5 e espera 15 segundos ')
                    # navegador.get(url)
                    # clica no atualizar
                    atualizar_navegador()
                    # pyautogui.press('f5')
                    time.sleep(25)
                    continue

                # Permitir que o Facebook use cookies e tecnologias semelhantes inseridos em outros apps e sites?
                if (pyautogui.pixelMatchesColor(830, 466, (27, 116, 228), tolerance=5)
                        or pyautogui.pixelMatchesColor(830, 466, (26, 110, 216), tolerance=5)):
                    print('Permitir que o Facebook use cookies e tecnologias semelhantes inseridos em outros apps e sites?')
                    pyautogui.click(830, 466)
                # Você entrou anteriormente no poker brasil com o facebook
                if (pyautogui.pixelMatchesColor(640, 688, (27, 116, 228), tolerance=5)
                        or pyautogui.pixelMatchesColor(640, 688, (26, 110, 216), tolerance=5)):
                    print('Você entrou anteriormente no poker brasil com o facebook')
                    pyautogui.click(640, 688, )

                recolhe_fan()

                cont_erro_fundo_preto += 1
                if cont_erro_fundo_preto > 20:
                    cont_erro_fundo_preto = 0
                    if pyautogui.pixelMatchesColor(493, 602, (17, 16, 16), tolerance=2):
                        print('Esta com fundo preto da um F5')
                        # clica no atualizar
                        atualizar_navegador()
                    else:
                        print('Pagina esta carregando')

            # Espera x segundos antes da próxima tentativa
            # time.sleep(1)
            IP.f5_quando_internete_ocila()
            teste_logado()
            if not pyautogui.pixelMatchesColor(500, 670, (27, 116, 228), tolerance=10):
                # testa se nao tem o botao azul de continuar
                try:
                    # if (pyautogui.pixelMatchesColor(215, 1000, (36, 37, 38), tolerance=5)  # mensagem do canto inferior esquedo " Você esta offiline no momento."
                    if (pyautogui.pixelMatchesColor(700, 650, (32, 33, 36), tolerance=5)  # fundo cinza com o dinoçauro
                            or pyautogui.pixelMatchesColor(700, 640, (255, 255, 255), tolerance=2)  # retangulo branco no meio da tela quando esta sem internete
                            or pyautogui.pixelMatchesColor(700, 640, (221, 221, 221), tolerance=7)  # tela cinza clara com cara triste
                            or pyautogui.pixelMatchesColor(700, 640, (238, 238, 238), tolerance=7)):  # tela cinza clara com cara triste
                        print("aguarda 7 segundos e faz um novo teste se a pagina nao carregou")
                        time.sleep(7)
                        try:
                            # if (pyautogui.pixelMatchesColor(215, 1000, (36, 37, 38),tolerance=5)  # mensagem do canto inferior esquedo " Você esta offiline no momento."
                            if ( pyautogui.pixelMatchesColor(700, 650, (32, 33, 36), tolerance=5)  # fundo cinza com o dinoçauro
                                    or pyautogui.pixelMatchesColor(700, 640, (255, 255, 255), tolerance=2)  # retangulo branco no meio da tela quando esta sem internete
                                    or pyautogui.pixelMatchesColor(700, 640, (221, 221, 221), tolerance=7)  # tela cinza clara com cara triste
                                    or pyautogui.pixelMatchesColor(700, 640, (238, 238, 238), tolerance=7)):  # tela cinza clara com cara triste
                                print("Falha na pagina e a tela esta branca, da um F5")
                                IP.tem_internet()
                                atualizar_navegador()
                                time.sleep(15)
                        except Exception as e:
                            # Lide com o erro aqui, por exemplo, exiba uma mensagem de erro ou registre-o em um arquivo de log
                            print(f'Erro: {e}')
                except Exception as e:
                    # Lide com o erro aqui, por exemplo, exiba uma mensagem de erro ou registre-o em um arquivo de log
                    print(f'Erro: {e}')

        if posicao is None:

            cont_erro += 1
            if cont_erro >= 2:
                # se tiverem algumasa tentativas fracaçadas troca o ip
                cont_erro = 0
                print('troca o IP para ver se entra')
                IP.ip_troca_agora()

            print("Não foi encontado a imagem de referencia para determinar a posição de origem")
            # Seleniun.atualizar_pagina(navegador, url)
            IP.tem_internet()
            print('origem da um f5 ')
            # navegador.get(url)
            # clica no atualizar
            atualizar_navegador()
            # pyautogui.press('f5')
            time.sleep(15)

    return 0, 0, status_conta


def recolhe_fan(x_origem=4, y_origem=266):
    if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 435), (173, 23, 18), tolerance=15):
        pyautogui.click(x_origem + 490, y_origem + 435)
        print("voce ja recebeu seu premio, deixe um pouco para os outros")

    # voce ganhou 2500
    elif pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 179), (71, 0, 148), tolerance=15):
        pyautogui.click(x_origem + 490, y_origem + 480, button='left')
        print("Voce ganhou 2500")

    # if pyautogui.pixelMatchesColor((x_origem + 681), (y_origem + 12), (254, 254, 42), tolerance=15):
    #     print('\nClica para abrir a roleta\n')
    #     pyautogui.doubleClick(x_origem + 683, y_origem + 14)  # clica no icone da roleta para abir


def x_y():  # apenas para testes
    while True:
        posicao = None
        print("Procurando coodenada 0 x 0...")
        for i in range(50):
            posicao = localizar_imagem(origem, regiao_busca, precisao_origem)
            if posicao is not None:  # Verifica se a imagem foi encontrada
                x_origem, y_origem = posicao.left, posicao.top
                x_origem = int(x_origem)
                y_origem = int(y_origem)
                print("x_origem: ", x_origem)
                print("y_origem: ", y_origem)

                return x_origem, y_origem

            # posicao = localizar_imagem(origemB, regiao_busca, precisao_origem)
            # if posicao is not None:# Verifica se a imagem foi encontrada
            #     x_origem, y_origem = posicao.left, posicao.top
            #     x_origem = int(x_origem)
            #     y_origem = int(y_origem)
            #
            #     return x_origem, y_origem


def x_y_aviso_sistema():
    print("Procurando aviso do sistema")
    for i in range(3):
        # Procura a imagem na região definida com 99,5% de tolerância, em escala de cinza e retorna a posição
        try:
            posicao = pyautogui.locateOnScreen(origem2, region=regiao_busca, confidence=0.993, grayscale=True)  # limite maximo de precisao é 0.997
            # Verifica se a imagem foi encontrada
            if posicao is not None:
                # print("Imagem encontrada na posição:", posicao)
                # Obtém as coordenadas x e o da imagem encontrada
                x_origem, y_origem = posicao.left, posicao.top
                x_origem = int(x_origem)
                y_origem = int(y_origem)
                # pyautogui.click(x_origem, y_origem ) #clica com mouse na origem so para ajudar a visualizar
                # print(f"Coordenadas origem: x={x_origem}, y={y_origem}")
                return x_origem, y_origem
        except:
            print("Ocorreu um erro ao localizar a imagem")
            time.sleep(2)
            continue

    return None, None
