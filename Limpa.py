import time

import pyautogui

from F5_navegador import atualizar_navegador
from IP import tem_internet, f5_quando_internete_ocila
from OCR_tela import aviso_sistema as ocr_aviso_sistema, mensagem_aviso_do_sistema
from Seleniun import teste_logado

# Desabilitar o fail-safe
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0


def teste_limpo(x_origem, y_origem):
    print('teste_limpo')
    # pyautogui.click(490 + x_origem, 70 + y_origem)  # clique bobo para passar alguma naimação
    pyautogui.click(640 + x_origem, 70 + y_origem)  # clique bobo para passar alguma naimação
    # barra azul do looby
    if pyautogui.pixelMatchesColor((x_origem + 685), (y_origem + 360), (215, 234, 244), tolerance=1):
        print("teste_limpo: Esta no Lobby, ta limpo")
        return True
    else:
        print('\nteste_limpo: Não esta limpo!!!\n ')
        return False


def ja_esta_logado(x_origem, y_origem):
    print('ja_esta_logado')
    teste_aviso_sistema = mensagem_aviso_do_sistema(x_origem, y_origem)
    # print(resultado_aviso_sistema)
    if teste_aviso_sistema:
        mensagen, coodenada_x, coodenada_y = teste_aviso_sistema
        # pyautogui.click((x_origem + coodenada_x), (y_origem + coodenada_y))  # fecha aviso do sistema
        if 'Logado outra pagina' in mensagen:
            print("sair da conta")
            return "sair da conta"
    return False


def limpa_jogando(x_origem, y_origem):
    print('limpa_jogando')
    pyautogui.click(640 + x_origem, 70 + y_origem)  # clique bobo para passar alguma animação

    if (not pyautogui.pixelMatchesColor((x_origem + 43), (y_origem + 388), (76, 37, 30), tolerance=10)
            and not pyautogui.pixelMatchesColor((x_origem + 43), (y_origem + 388), (64, 34, 8), tolerance=10)):
        pyautogui.click(x_origem + 43, y_origem + 388)  # clica no anel

    if (pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 117), (72, 71, 76), tolerance=5) or
            pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 117), (22, 21, 23), tolerance=5)):
        pyautogui.click(821 + x_origem, 138 + y_origem)  # clica no fechar tarefa
        print('fecha lista tarefas dentro do limpa jogando')

    # voce ganhou 2500
    if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 179), (71, 0, 148), tolerance=6):
        pyautogui.click(x_origem + 490, y_origem + 480)
        print("Voce ganhou 2500")

    # Subiu de nivel
    if (pyautogui.pixelMatchesColor((x_origem + 492), (y_origem + 443), (25, 118, 188), tolerance=6)
          or pyautogui.pixelMatchesColor((x_origem + 492), (y_origem + 443), (29, 139, 200), tolerance=6)):
        pyautogui.click(x_origem + 492, y_origem + 443)
        print("Subiu de nivel")

    # Quebou seu recorde
    if pyautogui.pixelMatchesColor((x_origem + 639), (y_origem + 270), (255, 138, 32), tolerance=20):
        pyautogui.click(x_origem + 703, y_origem + 170)
        print("Quebou seu recorde")

    # Você avançou para broinse II e ganhou 100 fichas
    if pyautogui.pixelMatchesColor((x_origem + 365), (y_origem + 235), (255, 237, 151), tolerance=20):
        pyautogui.click(x_origem + 490, y_origem + 435)  # continuar
        print("Você avançou para broinse II e ganhou 100 fichas")

    # nivel 2
    if pyautogui.pixelMatchesColor((x_origem + 492), (y_origem + 390), (237, 105, 0), tolerance=10):
        pyautogui.click(x_origem + 492, y_origem + 390)
        print("nivel 2")

    # Presentinho de dentro da mesa
    if pyautogui.pixelMatchesColor((x_origem + 38), (y_origem + 526), (187, 153, 111), tolerance=19):
        pyautogui.click(x_origem + 38, y_origem + 526)
        print("Presentinho de dentro da mesa")

    # aviso do sistema dentro da mesa
    if pyautogui.pixelMatchesColor((x_origem + 455), (y_origem + 417), (25, 116, 184), tolerance=19):
        # clica no x do aviso do sistema "tem certesa de que quer sair da mesa?"
        pyautogui.click(641 + x_origem, 278 + y_origem)
        print("aviso do sistema dentro da mesa")

    # Laranja
    if (pyautogui.pixelMatchesColor((x_origem + 235), (y_origem + 158), (235, 52, 3), tolerance=20)
          or pyautogui.pixelMatchesColor((x_origem + 238), (y_origem + 163), (227, 18, 5), tolerance=20)
          or pyautogui.pixelMatchesColor((x_origem + 241), (y_origem + 159), (236, 55, 4), tolerance=20)):

        pyautogui.click(768 + x_origem, 160 + y_origem)
        print("promoçao laranja")

    # Fecha promoçoes
    # elif pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 118), (72, 71, 76), tolerance=10):
    if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 118), (62, 71, 76), tolerance=20):
        pyautogui.click(821 + x_origem, 138 + y_origem)
        print("Promoção padrão, limpa_jogando, clica no fechar")

    # clica no Normal
    if pyautogui.pixelMatchesColor((x_origem + 162), (y_origem + 160), (12, 72, 108), tolerance=5):
        pyautogui.click(x_origem + 164, y_origem + 161)
        print("Clica no Normal")

    # Gostaria de começar a Liga do Finde?
    if pyautogui.pixelMatchesColor((x_origem + 538), (y_origem + 408), (217, 184, 50), tolerance=5):
        if pyautogui.pixelMatchesColor((x_origem + 538), (y_origem + 408), (31, 24, 73), tolerance=10):
            pyautogui.click(x_origem + 407, y_origem + 354)  # não mostar novamente hoje
            time.sleep(0.8)
        pyautogui.click(x_origem + 407, y_origem + 408)  # clica no NÃO
        print("Gostaria de começar a Liga do Finde?")

    # clica na casinha par voltar par o lob quando esta dentro de uma mesa
    if pyautogui.pixelMatchesColor(x_origem + 859, y_origem + 40, (116, 139, 171), tolerance=15):
        pyautogui.click(x_origem + 859, y_origem + 40)
        print('Voltar ao Lobby')


def limpa_pequeno(x_origem, y_origem):
    print('limpa_pequeno')
    pyautogui.click(640 + x_origem, 70 + y_origem)  # clique bobo para passar alguma animação
    if ja_esta_logado(x_origem, y_origem) == "sair da conta":
        return "sair da conta"

    # pyautogui.click(490 + x_origem, 70 + y_origem)  # clique bobo para passar alguma naimação
    # pyautogui.click(686 + x_origem, 70 + y_origem)  # clique bobo para passar alguma naimação
    # voce ja recebeu seu premio, deixe um pouco para os outros
    if pyautogui.pixelMatchesColor((x_origem + 470), (y_origem + 530), (183, 25, 19), tolerance=15):
        pyautogui.click(x_origem + 470, y_origem + 530)
        print("voce ja recebeu seu premio, deixe um pouco para os outros")

    # voce ganhou 2500
    elif pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 179), (71, 0, 148), tolerance=15):
        pyautogui.click(x_origem + 490, y_origem + 480)
        print("Voce ganhou 2500")

    # Subiu de nivel
    elif (pyautogui.pixelMatchesColor((x_origem + 492), (y_origem + 443), (25, 118, 188), tolerance=15)
          or pyautogui.pixelMatchesColor((x_origem + 492), (y_origem + 443), (29, 139, 200), tolerance=15)):
        pyautogui.click(x_origem + 492, y_origem + 443)
        print("Subiu de nivel")

    # Resutado da temporada - Bronse 1
    elif pyautogui.pixelMatchesColor((x_origem + 705), (y_origem + 216), (150, 104, 177), tolerance=10):
        pyautogui.click(x_origem + 721, y_origem + 218)
        print("Subiu de nivel")

    # nivel 2
    elif pyautogui.pixelMatchesColor((x_origem + 492), (y_origem + 390), (237, 105, 0), tolerance=10):
        pyautogui.click(x_origem + 492, y_origem + 390)
        print("nivel 2")

    # Quebou seu recorde
    elif pyautogui.pixelMatchesColor((x_origem + 772), (y_origem + 170), (242, 246, 0), tolerance=15):
        pyautogui.click(x_origem + 703, y_origem + 170)
        print("Quebou seu recorde")

    # Você avançou para broinse II e ganhou 100 fichas
    elif pyautogui.pixelMatchesColor((x_origem + 365), (y_origem + 235), (255, 237, 151), tolerance=20):
        pyautogui.click(x_origem + 490, y_origem + 435)  # continuar
        print("Você avançou para broinse II e ganhou 100 fichas")

    # clica no Normal
    elif pyautogui.pixelMatchesColor((x_origem + 162), (y_origem + 160), (12, 72, 108), tolerance=15):
        pyautogui.click(x_origem + 164, y_origem + 161)
        print("Clica no Normal")


    # Genius Muito tempo desde a sua unlima aposta
    elif pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 612), (80, 73, 76), tolerance=15):
        if (pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 415), (25, 118, 188), tolerance=15)
                or pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 415), (29, 139, 200), tolerance=15)):
            # Genius Muito tempo desde a sua unlima aposta
            pyautogui.mouseDown(x_origem + 490, y_origem + 415)
            print("Genius Muito tempo desde a sua unlima apostar")
            time.sleep(1)
            pyautogui.mouseUp(x_origem + 490, y_origem + 415)

    # testa se o torneino semanal esta no loob
    elif pyautogui.pixelMatchesColor((x_origem + 154), (y_origem + 105), (70, 70, 71), tolerance=15):
        # Slot Classico testa se esta no slot com ele limpo ou com alguma mensagem, quando tem alguma messagem fica um pouco escuro
        if not (pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 668), (46, 22, 9), tolerance=15)
                or pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 668), (18, 9, 4), tolerance=5)):
            print("Torneio semanal de forma errada no loby")
            limpo = teste_limpo(x_origem, y_origem)
            if limpo:
                tem_internet()
                print("erro no torneio semanal, Da um F5")
                # pyautogui.press('f5')
                # clica no atualizar
                atualizar_navegador()
                time.sleep(25)
    # encontre o martelo para o goblin
    elif pyautogui.pixelMatchesColor((x_origem + 378), (y_origem + 197), (10, 126, 120), tolerance=15):
        pyautogui.click(x_origem + 490, y_origem + 520)
        print("encontre o martelo para o goblin")

    # voce esta convidado a participar de uma festa em las vegasuma surpresa esta esperando por vc
    elif pyautogui.pixelMatchesColor((x_origem + 520), (y_origem + 480), (64, 37, 165), tolerance=15):
        pyautogui.click(490 + x_origem, 485 + y_origem)
        print("Festa em lasvegas")

    elif pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 370), (224, 227, 229), tolerance=15):
        aviso_sistema, resposta = ocr_aviso_sistema(x_origem, y_origem)
        if aviso_sistema:
            if resposta == "sair da conta":
                print("sair da conta")
                return "sair da conta"

    # aviso do sistema
    teste_aviso_sistema = mensagem_aviso_do_sistema(x_origem, y_origem)
    if teste_aviso_sistema:
        mensagen, coodenada_x, coodenada_y = teste_aviso_sistema
        pyautogui.click((x_origem + coodenada_x), (y_origem + coodenada_y))  # fecha aviso do sistema
        if 'Logado outra pagina' in mensagen:
            print("sair da conta")
            return "sair da conta"

    # o novo banco esta aberto"
    if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 195), (124, 77, 27), tolerance=20):
        pyautogui.click(495 + x_origem, 400 + y_origem)
        print("o novo banco esta aberto")

    if not teste_limpo(x_origem, y_origem):  # se ta limpo nem entra

        # Valete ou mais
        if (pyautogui.pixelMatchesColor((x_origem + 400), (y_origem + 70), (7, 4, 25), tolerance=10)
                or pyautogui.pixelMatchesColor((x_origem + 400), (y_origem + 70), (20, 10, 69), tolerance=10)):
            return

        teste_logado()
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
                    if (pyautogui.pixelMatchesColor(700, 650, (32, 33, 36), tolerance=5)  # fundo cinza com o dinoçauro
                            or pyautogui.pixelMatchesColor(700, 640, (255, 255, 255), tolerance=2)  # retangulo branco no meio da tela quando esta sem internete
                            or pyautogui.pixelMatchesColor(700, 640, (221, 221, 221), tolerance=7)  # tela cinza clara com cara triste
                            or pyautogui.pixelMatchesColor(700, 640, (238, 238, 238), tolerance=7)):  # tela cinza clara com cara triste
                        print("Falha na pagina e a tela esta branca, da um F5")
                        tem_internet()
                        atualizar_navegador()
                        time.sleep(15)
                except Exception as e:
                    # Lide com o erro aqui, por exemplo, exiba uma mensagem de erro ou registre-o em um arquivo de log
                    print(f'Erro: {e}')
        except Exception as e:
            # Lide com o erro aqui, por exemplo, exiba uma mensagem de erro ou registre-o em um arquivo de log
            print(f'Erro: {e}')


def limpa_tarefas(x_origem, y_origem):  # fecha todas as tarefas que sao feitas
    print('limpa_tarefas')

    limpa_pequeno(x_origem, y_origem)

    # pyautogui.click(490 + x_origem, 70 + y_origem)  # clique bobo para passar alguma naimação
    # pyautogui.click(686 + x_origem, 70 + y_origem)  # clique bobo para passar alguma naimação

    if teste_limpo(x_origem, y_origem):  # se ta limpo nem entra
        return

    # Cartas premiadas
    elif pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 213), (18, 42, 91), tolerance=19):
        pyautogui.click(763 + x_origem, 193 + y_origem, button='left')
        print("Cartas premiadas")

    # Mesa
    elif (pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 674), (27, 92, 155), tolerance=19)
          or pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 674), (19, 64, 109), tolerance=19)):
        # testa se esta dentro da mesa

        if not pyautogui.pixelMatchesColor((x_origem + 893), (y_origem + 71), (50, 20, 10), tolerance=10):
            # cor de fundo marrom do lado da setinh apara baixo
            # testa se nao esta limpo a regiao
            print("Desafios do alvo vermelho")
            for _ in range(30):
                pyautogui.click(895 + x_origem, 22 + y_origem)
                time.sleep(0.3)
                if pyautogui.pixelMatchesColor((x_origem + 893), (y_origem + 100), (21, 6, 45), tolerance=10):
                    pyautogui.click(919 + x_origem, 105 + y_origem)
                    print("Desafios do alvo aberto")
                    time.sleep(0.5)
                    break

        pyautogui.click(947 + x_origem, 78 + y_origem)  # setinha
        time.sleep(0.3)
        pyautogui.click(925 + x_origem, 204 + y_origem)  # Levantar
        time.sleep(0.2)
        pyautogui.click(947 + x_origem, 78 + y_origem)  # setinha
        time.sleep(0.2)
        pyautogui.click(925 + x_origem, 111 + y_origem)  # Lobby

        # aviso do sistema
        teste_aviso_sistema = mensagem_aviso_do_sistema(x_origem, y_origem)
        if teste_aviso_sistema:
            mensagen, coodenada_x, coodenada_y = teste_aviso_sistema
            pyautogui.click((x_origem + coodenada_x), (y_origem + coodenada_y))  # fecha aviso do sistema

        print("Sai da Mesa")

    # Casino Genius
    elif pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 612), (111, 100, 105), tolerance=19):
        if ((not pyautogui.pixelMatchesColor((x_origem + 893), (y_origem + 71), (96, 85, 110), tolerance=10))
                and (not pyautogui.pixelMatchesColor((x_origem + 893), (y_origem + 71), (61, 53, 75), tolerance=10))):

            # testa se nao esta limpo a regiao
            print("Desafios do alvo vermelho")
            for _ in range(30):
                pyautogui.click(895 + x_origem, 22 + y_origem)
                time.sleep(0.3)
                if pyautogui.pixelMatchesColor((x_origem + 893), (y_origem + 100), (21, 6, 45), tolerance=10):
                    pyautogui.click(919 + x_origem, 105 + y_origem)
                    print("Desafios do alvo aberto")
                    time.sleep(0.5)
                    break

        pyautogui.click(910 + x_origem, 80 + y_origem)
        print("Casino Genius")

    # Slot Classico
    elif (pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 668), (46, 22, 9), tolerance=5)
          or pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 668), (18, 9, 4), tolerance=5)):

        if not pyautogui.pixelMatchesColor((x_origem + 893), (y_origem + 71), (234, 225, 228), tolerance=10):
            # testa se nao esta limpo a regiao
            print("Desafios do alvo vermelho")
            for _ in range(30):
                pyautogui.click(895 + x_origem, 22 + y_origem)
                time.sleep(0.3)
                if pyautogui.pixelMatchesColor((x_origem + 893), (y_origem + 100), (21, 6, 45), tolerance=10):
                    pyautogui.click(919 + x_origem, 105 + y_origem)
                    print("Desafios do alvo aberto")
                    time.sleep(0.5)
                    break

        pyautogui.click(910 + x_origem, 80 + y_origem)
        print("Slot Classico")

    # clica na casinha par voltar par o lob quando esta dentro de uma mesa
    elif pyautogui.pixelMatchesColor(x_origem + 859, y_origem + 40, (116, 139, 171), tolerance=5):
        pyautogui.click(x_origem + 859, y_origem + 40)
        print('Voltar ao Lobby')

    fecha_tarefa(x_origem, y_origem)


def fecha_tarefa(x_origem, y_origem, jogando=False):  # fecha a lista de tarefas diarias
    print('fecha_tarefa')
    # pyautogui.click(490 + x_origem, 70 + y_origem, button='left')  # clique bobo para passar alguma naimação
    # Tarefas diarias
    for i in range(20):
        if pyautogui.pixelMatchesColor((x_origem + 495), (y_origem + 133), (71, 2, 128), tolerance=5):
            pyautogui.click(821 + x_origem, 138 + y_origem)  # fecha tarefa
            time.sleep(0.5)
            print("fecha Tarefas diarias")
        else:
            return

        # o novo banco esta aberto"
        if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 195), (124, 77, 27), tolerance=20):
            pyautogui.click(495 + x_origem, 400 + y_origem)
            print("o novo banco esta aberto")

        time.sleep(0.3)
    if not jogando:
        limpa_total(x_origem, y_origem)


def limpa_promocao(x_origem, y_origem):
    '''Limpa as promoções exceto as tarefas que são feitas'''
    print('limpa_promocao')

    # pyautogui.click(490 + x_origem, 70 + y_origem)  # clique bobo para passar alguma naimação
    # pyautogui.click(686 + x_origem, 70 + y_origem)  # clique bobo para passar alguma naimação

    # limpa_pequeno(x_origem, y_origem)
    if ja_esta_logado(x_origem, y_origem) == "sair da conta":
        return "sair da conta"

    if teste_limpo(x_origem, y_origem):  # se ta limpo nem entra
        return None

    # amigos on line e opiçoes
    if pyautogui.pixelMatchesColor((x_origem + 879), (y_origem + 190), (235, 237, 239), tolerance=19):
        pyautogui.click(909 + x_origem, 84 + y_origem, button='left')
        print("amigos on line e opiçoes")

    # o novo banco esta aberto"
    if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 195), (124, 77, 27), tolerance=20):
        pyautogui.click(495 + x_origem, 400 + y_origem)
        print("o novo banco esta aberto")

    # Fique milionario jogando
    if pyautogui.pixelMatchesColor((x_origem + 545), (y_origem + 105), (167, 100, 48), tolerance=10):
        pyautogui.click(812 + x_origem, 240 + y_origem)
        print("Fique milionario jogando")

    # Vip
    if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 100), (46, 29, 21), tolerance=5):
        pyautogui.click(921 + x_origem, 89 + y_origem, button='left')
        print("vip")

    # Desafios do Rallyaces
    if pyautogui.pixelMatchesColor((x_origem + 920), (y_origem + 105), (150, 138, 220), tolerance=10):
        pyautogui.click(920 + x_origem, 105 + y_origem)
        print("Desafios do Rallyaces")

    # Mega Giro e roleta2
    if pyautogui.pixelMatchesColor((x_origem + 473), (y_origem + 120), (204, 113, 29), tolerance=10):
        pyautogui.click(884 + x_origem, 135 + y_origem)
        print("Mega Giro e roleta2")

    # Festa dos grandes apostadores
    if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 118), (29, 28, 31), tolerance=5):
        pyautogui.click(821 + x_origem, 138 + y_origem)
        print("Festa dos grandes apostadores")
        time.sleep(0.5)
        if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 118), (29, 28, 31), tolerance=5):
            pyautogui.click(821 + x_origem, 138 + y_origem)
            print("Festa dos grandes apostadores")
            time.sleep(0.5)

    # Fecha promoçoes exceto tarefas (72, 71, 76) padrao 100% . usado (62, 71, 76) para pegar outrasd propaganas mais claras
    if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 118), (62, 71, 76), tolerance=20):
        print("Promoção padrão")
        if pyautogui.pixelMatchesColor((x_origem + 495), (y_origem + 133), (71, 2, 128), tolerance=5):
            print("Tarefas diarias, se fecha no limpa")
        else:
            pyautogui.click(821 + x_origem, 138 + y_origem)
            print("Promoção padrão clica no fechar")

    # # A carta final 8
    # if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 118), (67, 35, 10), tolerance=20):
    #     pyautogui.click(823 + x_origem, 137 + y_origem)
    #     print("A carta final 8")

    # # TEMA DE PARCOA
    # if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 103), (72, 71, 75), tolerance=20):
    #     pyautogui.click(827 + x_origem, 109 + y_origem)
    #     print("Promoção Tema de pascoa")

    # Oferta de primeira recarga
    if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 176), (252, 123, 0), tolerance=20):
        pyautogui.click(826 + x_origem, 176 + y_origem)
        print("Oferta de primeira recarga")

    # Banco do poker regras aberto
    if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 118), (46, 38, 26), tolerance=20):
        pyautogui.click(777 + x_origem, 217 + y_origem)
        time.sleep(0.5)
        pyautogui.click(821 + x_origem, 138 + y_origem)
        print("Banco do poker regras aberto")
        time.sleep(1)

    # Banco do poker
    if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 118), (115, 96, 64), tolerance=20):
        pyautogui.click(821 + x_origem, 138 + y_origem)
        print("Banco do poker")
        time.sleep(1)

    # # VS pegar a carta
    # if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 118), (29, 28, 30), tolerance=8):
    #     pyautogui.click(477 + x_origem, 500 + y_origem)
    #     print("VS pegar a carta")

    # Roleta 1
    if pyautogui.pixelMatchesColor((x_origem + 495), (y_origem + 315), (211, 110, 12), tolerance=25):
        pyautogui.click(882 + x_origem, 171 + y_origem)
        print("limpa Roleta1")

    # Roleta depois da roleta e Mega giro
    if pyautogui.pixelMatchesColor((x_origem + 472), (y_origem + 120), (218, 106, 4), tolerance=20):
        pyautogui.click(884 + x_origem, 136 + y_origem)
        print("Roleta depois da roleta e Mega giro")

    # Laranja
    if (pyautogui.pixelMatchesColor((x_origem + 235), (y_origem + 158), (235, 52, 3), tolerance=20)
            or pyautogui.pixelMatchesColor((x_origem + 238), (y_origem + 163), (227, 18, 5), tolerance=20)
            or pyautogui.pixelMatchesColor((x_origem + 241), (y_origem + 159), (236, 55, 4), tolerance=20)
            or pyautogui.pixelMatchesColor((x_origem + 220), (y_origem + 180), (233, 24, 6), tolerance=20)):
        # area dos campeoes
        # comprar
        # meus objetos
        # Voce perdeu tudo
        pyautogui.click(771 + x_origem, 160 + y_origem)
        print("promoçao laranja")
        time.sleep(0.5)

    # raliacesses
    if (pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 167), (255, 204, 125), tolerance=19) or
            pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 167), (53, 27, 14), tolerance=19) or
            pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 167), (74, 40, 12), tolerance=19) or
            pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 167), (66, 66, 68), tolerance=19)):  # aneis
        pyautogui.click(811 + x_origem, 168 + y_origem)
        print("aneis")

    # Voce Noa Jogou Nehum Jogo De Poker Essasemana
    if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 225), (13, 17, 41), tolerance=6):
        pyautogui.click(x_origem + 722, y_origem + 219)
        print("Voce Noa Jogou Nehum Jogo De Poker Essasemana")

    # Gostaria de começar a Liga do Finde?
    if pyautogui.pixelMatchesColor((x_origem + 538), (y_origem + 408), (217, 184, 50), tolerance=5):
        if pyautogui.pixelMatchesColor((x_origem + 538), (y_origem + 408), (31, 24, 73), tolerance=10):
            pyautogui.click(x_origem + 407, y_origem + 354)  # não mostar novamente hoje
            time.sleep(0.8)
        pyautogui.click(x_origem + 407, y_origem + 408)  # clica no NÃO
        print("Gostaria de começar a Liga do Finde?")

    # Valete ou mais
    if (pyautogui.pixelMatchesColor((x_origem + 400), (y_origem + 70), (7, 4, 25), tolerance=10)
            or pyautogui.pixelMatchesColor((x_origem + 400), (y_origem + 70), (20, 10, 69), tolerance=10)):
        pyautogui.mouseDown(895 + x_origem, 82 + y_origem)  # aperta e segura
        time.sleep(0.4)
        pyautogui.mouseUp(895 + x_origem, 82 + y_origem)  # aperta e segura
        print("Valete ou mais")

    # chave de saque diario
    if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 122), (62, 71, 76), tolerance=20):
        print("Chave de saque diario")
        pyautogui.click(819 + x_origem, 140 + y_origem)

    # chave de saque diario
    if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 122), (29, 28, 30), tolerance=20):
        print("Chave de saque diario 2")
        pyautogui.click(498 + x_origem, 454 + y_origem)
        time.sleep(2)
        pyautogui.click(819 + x_origem, 140 + y_origem)


def limpa_total(x_origem, y_origem):
    cont_erro_limpa = 0
    for i in range(50):
        print('limpa_total:', i)

        cont_erro_limpa += 1
        if cont_erro_limpa >= 20:
            cont_erro_limpa = 0
            print('clica no atualizar')
            # pyautogui.press('f5')
            # clica no atualizar
            atualizar_navegador()
            print('espera 25 segundos')
            time.sleep(25)
            print('esperou 25 segundos')

        if ja_esta_logado(x_origem, y_origem) == "sair da conta":
            return "sair da conta"
        limpa_pequeno(x_origem, y_origem)
        if teste_limpo(x_origem, y_origem):  # se ta limpo nem entra
            return None
        limpa_tarefas(x_origem, y_origem)  # fecha as tarefas que sao feitas cartas genius slote mesa ...
        if teste_limpo(x_origem, y_origem):  # se ta limpo nem entra
            return None
        fecha_tarefa(x_origem, y_origem)  # fecha a lista de tarefas diarias
        if teste_limpo(x_origem, y_origem):  # se ta limpo nem entra
            return None
        limpa_promocao(x_origem, y_origem)
        if teste_limpo(x_origem, y_origem):  # se ta limpo nem entra
            return None
        iniciantes(x_origem, y_origem)
        if teste_limpo(x_origem, y_origem):  # se ta limpo nem entra
            return None
        limpa_jogando(x_origem, y_origem)
        if teste_limpo(x_origem, y_origem):  # se ta limpo nem entra
            return None
        teste_logado()

    return None


def limpa_total_fazendo_tarefa(x_origem, y_origem):
    print('limpa_total_fazendo_tarefa')

    if ja_esta_logado(x_origem, y_origem) == "sair da conta":
        return "sair da conta"
    limpa_pequeno(x_origem, y_origem)
    limpa_promocao(x_origem, y_origem)
    # fecha_tarefa(x_origem, y_origem) # fecha a lista de tarefas diarias


def limpa_abre_tarefa(x_origem, y_origem, com_pausa=True):  # abre o tarefas
    print('limpa_abre_tarefa')
    pyautogui.click(640 + x_origem, 70 + y_origem)  # clique bobo para passar alguma animação

    # if pyautogui.pixelMatchesColor((x_origem + 802), (y_origem + 38), (245, 218, 96), tolerance=10):
    #     print("Tarefas diarias conta upada com o cadeado level menor que 4")
    #     return False

    cont_limpa_tarefas = 0
    for _ in range(20):
        for _ in range(15):
            f5_quando_internete_ocila()
            pyautogui.doubleClick(x_origem + 635, y_origem + 25)  # clica no tarefas diarias
            print("Limpa Tarefas diarias")
            time.sleep(0.5)
            pyautogui.doubleClick(x_origem + 193, y_origem + 172)  # clica dentro do tarefas diarias
            limpa_pequeno(x_origem, y_origem)

            # testa se tarefa diariaria esta aberta e limpa
            if (pyautogui.pixelMatchesColor((x_origem + 495), (y_origem + 133), (71, 2, 128), tolerance=5)
                    and pyautogui.pixelMatchesColor((x_origem + 495), (y_origem + 117), (72, 71, 76), tolerance=5)):
                print("Tarefas diarias pausa")
                if com_pausa:
                    time.sleep(1.5)
                if (pyautogui.pixelMatchesColor((x_origem + 495), (y_origem + 133), (71, 2, 128), tolerance=5)
                        and pyautogui.pixelMatchesColor((x_origem + 495), (y_origem + 117), (72, 71, 76), tolerance=5)):
                    print("Tarefas diarias limpo conta upada, missoes padroes")
                    return True
            # testa se a tarefa diaria é de conta sem upar
            elif pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 133), (1, 49, 243), tolerance=5):
                pyautogui.click(821 + x_origem, 138 + y_origem)  # clique para fechar
                print("Tarefas diarias, missoes iniciais")
                return False

        limpa_promocao(x_origem, y_origem)

        cont_limpa_tarefas += 1
        if cont_limpa_tarefas >= 3:
            cont_limpa_tarefas = 0
            # da um F5
            tem_internet()
            print("limpa tarefa Da um F5")
            atualizar_navegador()
            time.sleep(25)
            teste_logado()
            limpa_total(x_origem, y_origem)

        time.sleep(1)
    return False


# def forca_iniciante(x_origem, y_origem):
#     print('forca_iniciante')
#     limpa_total(x_origem, y_origem)
#     # testa se esta visivel o começar ja
#     for i in range(30):
#         print('procura começar ja')
#         if pyautogui.pixelMatchesColor((x_origem + 672), (y_origem + 146), (179, 216, 127), tolerance=5):
#             print('clique começar ja ')
#             pyautogui.click(672 + x_origem, 146 + y_origem)  # clica no começar ja
#             time.sleep(4)
#             limpa_tarefas(x_origem, y_origem)
#             time.sleep(1)
#             iniciantes(x_origem, y_origem)
#             limpa_total(x_origem, y_origem)
#             return
#         time.sleep(1)
#     return


def iniciantes(x_origem, y_origem):
    print("iniciantes")
    if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 173), (34, 0, 109), tolerance=20):
        for i in range(10):
            print("Recompensa de logim para iniciantes")
            if pyautogui.pixelMatchesColor((x_origem + 310), (y_origem + 326), (234, 114, 32), tolerance=20):
                pyautogui.click(310 + x_origem, 326 + y_origem)  # pega o 2xp
                print("Primeiro dia, EXPX2")
                time.sleep(2)
                pyautogui.click(777 + x_origem, 173 + y_origem)  # clica no fechar
                time.sleep(1)

            if pyautogui.pixelMatchesColor((x_origem + 424), (y_origem + 326), (234, 114, 32), tolerance=20):
                pyautogui.click(424 + x_origem, 326 + y_origem)  # pega o anel
                print("Segundo dia, anel")
                time.sleep(2)
                pyautogui.click(777 + x_origem, 173 + y_origem)  # clica no fechar
                time.sleep(1)
            if pyautogui.pixelMatchesColor((x_origem + 534), (y_origem + 326), (234, 114, 32), tolerance=20):
                pyautogui.click(534 + x_origem, 326 + y_origem)  # pega o anel
                print("Terceiro  dia, 2.000")
                time.sleep(2)
                pyautogui.click(478 + x_origem, 529 + y_origem)  # clica no pegar
                time.sleep(2)

            if pyautogui.pixelMatchesColor((x_origem + 310), (y_origem + 475), (234, 114, 32), tolerance=20):
                pyautogui.click(310 + x_origem, 475 + y_origem)  # pega o 2xp
                print("Qarto dia, Caixa102")
                time.sleep(2)
                pyautogui.click(777 + x_origem, 173 + y_origem)  # clica no fechar
                time.sleep(1)
            if pyautogui.pixelMatchesColor((x_origem + 424), (y_origem + 475), (234, 114, 32), tolerance=20):
                pyautogui.click(424 + x_origem, 475 + y_origem)  # pega o anel
                print("Quinto dia, 5.000")
                time.sleep(2)
                pyautogui.click(478 + x_origem, 529 + y_origem)  # clica no pegar
                time.sleep(2)
            if pyautogui.pixelMatchesColor((x_origem + 534), (y_origem + 475), (234, 114, 32), tolerance=20):
                pyautogui.click(534 + x_origem, 475 + y_origem)  # pega o anel
                print("Sexto dia, Bilhete")
                time.sleep(2)
                pyautogui.click(777 + x_origem, 173 + y_origem)  # clica no fechar
                time.sleep(1)

            if pyautogui.pixelMatchesColor((x_origem + 716), (y_origem + 470), (172, 70, 2), tolerance=20):
                pyautogui.click(743 + x_origem, 465 + y_origem)  # pega o anel
                print("Setimo dia, 10.000")
                time.sleep(2)
                pyautogui.click(478 + x_origem, 529 + y_origem)  # clica no pegar
                time.sleep(2)
            # time.sleep(1)
        pyautogui.click(777 + x_origem, 173 + y_origem)  # clica no fechar
    return


def faz_tutorial(x_origem, y_origem):
    print('Tutorial.')
    for i in range(100):
        print('Tutorial...')

        # testa se esta aparecendo o 500 Fichas
        if pyautogui.pixelMatchesColor((x_origem + 280), (y_origem + 260), (47, 6, 71), tolerance=20):
            print("5000 fichas, clica no OK")
            pyautogui.click(x_origem + 550, y_origem + 500)  # clica no ok
            # time.sleep(1)

        if pyautogui.pixelMatchesColor((x_origem + 484), (y_origem + 325), (255, 254, 104), tolerance=10):
            print('Girar roleta gratis')
            pyautogui.doubleClick(x_origem + 490, y_origem + 380)  # clica no girar gratis da roleta
            time.sleep(15)

        if pyautogui.pixelMatchesColor((x_origem + 475), (y_origem + 475), (38, 1, 61), tolerance=10):
            print('clica no sim jogar agora')
            pyautogui.mouseDown(x_origem + 470, y_origem + 420)  # Sim, jogar agora
            time.sleep(0.3)
            pyautogui.mouseUp(x_origem + 470, y_origem + 420)  # Sim, jogar agora
            time.sleep(1)

        limpa_pequeno(x_origem, y_origem)
        limpa_tarefas(x_origem, y_origem)
        limpa_promocao(x_origem, y_origem)

        time.sleep(1)

        if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 173), (34, 0, 109), tolerance=20):
            for _ in range(40):
                print("Recompensa de logim para iniciantes")
                time.sleep(0.5)
                if pyautogui.pixelMatchesColor((x_origem + 310), (y_origem + 326), (234, 114, 32), tolerance=30):
                    pyautogui.click(310 + x_origem, 326 + y_origem)  # pega o 2xp
                    print("Primeiro dia, EXPX2")
                    time.sleep(2)
                    pyautogui.click(777 + x_origem, 173 + y_origem)  # clica no fechar
                    time.sleep(1)
                    print('fim do tutorial')
                    break

            pyautogui.click(777 + x_origem, 173 + y_origem)  # clica no fechar
            time.sleep(2)
            break


# def premio_r1(x_origem, y_origem):
#     print('premio_r1')
#     fecha_tarefa(x_origem, y_origem)
#     for i in range(100):
#         # print('espera...')
#         # Roleta 1 aberta esperando bater o premio
#         if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 611), (255, 196, 255), tolerance=20):
#             # testa de roleta 1 ta aberta
#             print("terminou de rodar o R1 da um time")
#             time.sleep(2)
#             print("sai do R1")
#             return True
#         time.sleep(0.05)
#         fecha_tarefa(x_origem, y_origem)
#         limpa_pequeno(x_origem, y_origem)
#         limpa_promocao(x_origem, y_origem)
#         limpa_tarefas(x_origem, y_origem)
#         if teste_limpo(x_origem, y_origem):  # se ta limpo nem entra
#             return True
#     print('deu o tempo')
#     return True


# def premio_r2(x_origem, y_origem):
#     print('premio_r2')
#     for i in range(100):
#         if pyautogui.pixelMatchesColor((x_origem + 365), (y_origem + 580), (22, 0, 100), tolerance=20):
#             # espera o premio sair
#             print("roleta 2 aberta pegou o pemio pode sair")
#             return True
#         time.sleep(0.05)
#         fecha_tarefa(x_origem, y_origem)
#         limpa_pequeno(x_origem, y_origem)
#         limpa_promocao(x_origem, y_origem)
#         limpa_tarefas(x_origem, y_origem)
#         iniciantes(x_origem, y_origem)
#         if teste_limpo(x_origem, y_origem):  # se ta limpo nem entra
#             return True
#     print('deu o tempo')
#     return True


def aviso_canto_lobby(x_origem, y_origem):
    '''Fecha propaganda'''
    # fecha mnsagem no canto inferior da tela
    if pyautogui.pixelMatchesColor((x_origem + 281), (y_origem + 561), (255, 255, 255), tolerance=5):
        pyautogui.click(x_origem + 281, y_origem + 561)
        print("fechou aviso canto da tela")

# #
# x_origem, y_origem = Origem_pg.x_y()
# limpa_pequeno(x_origem, y_origem)
# # limpa_jogando(x_origem, y_origem)
# limpa_total(x_origem, y_origem)
# # faz_tutorial(x_origem,y_origem)
# # # # # #iniciantes(x_origem, y_origem)
# # # # # # # # # # aviso_canto_lobby(x_origem, y_origem)
# # # limpa_total(x_origem, y_origem)
# # limpa_abre_tarefa2(x_origem, y_origem)
# limpa_promocao(x_origem, y_origem)
