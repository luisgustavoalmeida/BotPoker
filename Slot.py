import time

import pyautogui

import HoraT
import IP
import Limpa
import Tarefas

# Desabilitar o fail-safe
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0


def localizar_imagem(imagem, regiao, precisao):
    try:
        posicao = pyautogui.locateOnScreen(imagem, region=regiao, confidence=precisao, grayscale=True)
        return posicao
    except:
        print("Ocorreu um erro ao localizar a imagem")
        time.sleep(2)
        return None


def abre_slot(x_origem, y_origem, joga_vezes=True):
    print('abre_slot')
    while True:
        for i in range(40):

            if Limpa.teste_limpo(x_origem, y_origem):
                pyautogui.click(x_origem + 920, y_origem + 150)
                print('clica para abrir o slot 777')
                time.sleep(1)

            # Slot Classico testa se esta no slot com ele limpo ou com alguma mensagem, quando tem alguma messagem fica um pouco escuro
            if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 668), (46, 22, 9), tolerance=5) \
                    or pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 668), (18, 9, 4), tolerance=5):
                print("slote aberto")

                if testa_slot_lipo(x_origem, y_origem):
                    print('manda limpara total fazendo tarefas')
                    if Limpa.limpa_total_fazendo_tarefa(x_origem, y_origem) == "sair da conta":
                        return "sair da conta"

                print("Slot Classico, entrou")

                if ajustar_valor(x_origem, y_origem, joga_vezes):
                    return True

            time.sleep(0.2)

        print('limite de tentativas manda limpara total')
        if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
            return "sair da conta"


def testa_slot_lipo(x_origem, y_origem):
    print('testa_slot_lipo')
    cont_erro = 0

    while True:
        Limpa.aviso_canto_lobby(x_origem, y_origem)  # fecha propaganda
        Limpa.fecha_tarefa(x_origem, y_origem)

        if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 668), (46, 22, 9), tolerance=5) \
                and pyautogui.pixelMatchesColor((x_origem + 624), (y_origem + 336), (0, 0, 0), tolerance=5):
            print("testa_slot_lipo: slote limpo")
            # testa se esta limpo, se esta com a cor clara sem foco na mensagem e se a lista preta de divisão esta apatecendo
            return False
        else:
            print("slote NÂO limpo")
            if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 668), (18, 9, 4),
                                           tolerance=5):  # esta com alguma mensagem de bonus, fica mais escuro com foco na mensagem
                pyautogui.click(x_origem + 684, y_origem + 258)  # rodada bonus
                pyautogui.click(x_origem + 716, y_origem + 256)  # mega win
                pyautogui.click(x_origem + 681, y_origem + 199)  # outra mensagem nao sei qual é nesse lugar

            elif pyautogui.pixelMatchesColor((x_origem + 491), (y_origem + 417), (25, 118, 188), tolerance=20):
                print('Erro de comunicação, favor atualizar a página para continuar com o processo')
                pyautogui.press('f5')
                print('espera 25 segundos')
                time.sleep(25)
                print('continua')
                return True

            elif not (pyautogui.pixelMatchesColor((x_origem + 624), (y_origem + 336), (0, 0, 0),
                                                  tolerance=5)):  # testa se tem a lista preta de divisão das colunas
                Limpa.limpa_pequeno(x_origem, y_origem)
                Limpa.limpa_promocao(x_origem, y_origem)
                pyautogui.click(x_origem + 684, y_origem + 258)  # rodada bonus
                pyautogui.click(x_origem + 716, y_origem + 256)  # mega win
                pyautogui.click(x_origem + 681, y_origem + 199)  # outra mensagem nao sei qual é nesse lugar

        cont_erro += 1
        if cont_erro > 50:
            print('numero de tentativas superadas vai da um F5')
            pyautogui.press('f5')
            print('espera 25 segundos')
            time.sleep(25)
            print('continua')
            return True
        time.sleep(0.3)


def ajustar_valor(x_origem, y_origem, joga_vezes):
    print('ajustar_valor')

    Limpa.aviso_canto_lobby(x_origem, y_origem)  # fecha propaganda
    imagem1 = r'Imagens\Slot\linhas9.png'
    regiao1 = (230 + x_origem, 591 + y_origem, 55, 19)  # (x, y, largura, altura)
    regiao2 = (379 + x_origem, 591 + y_origem, 55, 18)  # (x, y, largura, altura)
    precisao = 0.98

    if joga_vezes:
        imagem2 = r'Imagens\Slot\aposta20.png'
    else:
        imagem2 = r'Imagens\Slot\aposta200.png'

    for i in range(20):
        print('procura numero linha')

        posicao = localizar_imagem(imagem1, regiao1, precisao)
        if posicao is not None:  # Verifica se a imagem foi encontrada
            print("Linhas 9")

            for i in range(20):
                print('procura valor aposta')

                posicao = localizar_imagem(imagem2, regiao2, precisao)
                if posicao is not None:  # Verifica se a imagem foi encontrada
                    print("Aposta 20")
                    return True
                else:
                    pyautogui.click(x_origem + 445, y_origem + 601)  # mudar numero de linhas
                    time.sleep(0.2)
        else:
            pyautogui.click(x_origem + 289, y_origem + 601)  # mudar numero de linhas
            time.sleep(0.2)
    return False


def solot_joga_vezes(x_origem, y_origem, joga_vezes):
    if joga_vezes:
        tarefas_fazer = ('Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 150 vezes',
                         'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 70 vezes',
                         'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 10 vezes')
    else:
        tarefas_fazer = ('Ganhar 100.000 fichas no caca niquel Slot Poker',
                         'Ganhar 30.000 fichas no caca niquel Slot Poker',
                         'Ganhar 10.000 fichas no caca niquel Slot Poker')

    continua_jogando = True

    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
        return "sair da conta"

    abre_slot(x_origem, y_origem, joga_vezes)
    cont_jogadas_troca_ip = 0

    while continua_jogando:  # permanece joghando cartas premiadas ate nao ter mais a mição jogar x vezes
        if HoraT.fim_tempo_tarefa():
            return
        if Limpa.limpa_total_fazendo_tarefa(x_origem, y_origem) == "sair da conta":
            return "sair da conta"
        if cont_jogadas_troca_ip >= 5:
            cont_jogadas_troca_ip = 0
            IP.testa_trocar_IP()
        cont_jogadas_troca_ip += 1
        slot_aberto = abre_slot(x_origem, y_origem, joga_vezes)
        if slot_aberto == True:
            print('espera girar na cor certa')
            for i in range(20):
                # espera poder clicar no girar
                if pyautogui.pixelMatchesColor((x_origem + 922), (y_origem + 609), (216, 17, 2), tolerance=5):
                    print("clicar no girar")
                    pyautogui.doubleClick(x_origem + 922, y_origem + 609)  # clica em girar
                    break
                time.sleep(0.3)

        # Limpa.limpa_abre_tarefa2(x_origem, y_origem)
        Limpa.limpa_abre_tarefa(x_origem, y_origem)
        Tarefas.recolher_tarefa(x_origem, y_origem)
        meta_atigida, pontos = Tarefas.meta_tarefas(x_origem, y_origem)
        continua_jogando, tarefa = Tarefas.comparar_listas_fazendo_tarefa(tarefas_fazer, x_origem, y_origem)  # procura com ocr

        if (not continua_jogando) or (meta_atigida):
            time.sleep(0.5)
            # Limpa.limpa_abre_tarefa2(x_origem, y_origem)
            Limpa.limpa_abre_tarefa(x_origem, y_origem)
            continua_jogando, tarefa = Tarefas.comparar_listas_fazendo_tarefa(tarefas_fazer, x_origem, y_origem)  # procura com ocr
            meta_atigida, pontos = Tarefas.meta_tarefas(x_origem, y_origem)
            if (not continua_jogando) or (meta_atigida):
                print("FIM")
                if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                    return "sair da conta"
                return
        # cartas_vezes = True
        Limpa.fecha_tarefa(x_origem, y_origem)  # fecha a lista de tarefas diarias
        abre_slot(x_origem, y_origem, joga_vezes)
    return

# def solot_joga_vezes_upando(x_origem, y_origem, joga_vezes = True):
#
#     continua_jogando = True
#
#     if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
#         return "sair da conta"
#
#     abre_slot(x_origem, y_origem, joga_vezes)
#
#     while continua_jogando: # permanece joghando cartas premiadas ate nao ter mais a mição jogar x vezes
#
#         slot_aberto = abre_slot(x_origem, y_origem, joga_vezes)
#         if slot_aberto:
#             print('espera girar na cor certa')
#             for i in range(20):
#                 #espera poder clicar no girar
#                 if pyautogui.pixelMatchesColor((x_origem + 922), (y_origem + 609), (216, 17, 2), tolerance=5):
#                     pyautogui.doubleClick(x_origem + 922, y_origem + 609)  # clica em girar
#                     print("clicar no girar")
#                     break
#                 time.sleep(0.3)
#
#         status_tarefa = Tarefas.recolher_tarefa_upando(x_origem, y_origem)
#         print(status_tarefa)
#         if status_tarefa == "Não tem missão":
#             continua_jogando = True
#         elif status_tarefa == "Recolhido":
#             continua_jogando = False
#         else:
#             continua_jogando = False
#
#         if not continua_jogando:
#             print("FIM")
#             if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
#                 return "sair da conta"
#             return
#     return


# solot_joga_vezes_upando(x_origem, y_origem)
# # #solot_joga_vezes(x_origem, y_origem)
# #abre_slot(x_origem, y_origem, False)
# ajustar_valor(x_origem, y_origem, False)
