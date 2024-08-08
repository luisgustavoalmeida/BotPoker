import random
import time

import pyautogui

import HoraT
import IP
import Limpa
import Tarefas
from F5_navegador import atualizar_navegador
import OCR_tela
# Desabilitar o fail-safe
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0


def abre_cartas_premidas(x_origem, y_origem):
    for _ in range(3):
        for _ in range(30):
            # testa se ta aberto o trofel azul claro do cartas pemidas
            if pyautogui.pixelMatchesColor((x_origem + 686), (y_origem + 222), (73, 124, 181), tolerance=5):
                # testa se  o valor escolhido é o 200
                if pyautogui.pixelMatchesColor((x_origem + 379), (y_origem + 481), (217, 28, 18), tolerance=5):
                    pyautogui.doubleClick(x_origem + 270, y_origem + 425)  # clica no limpar
                    return True
                else:
                    pyautogui.click(x_origem + 346, y_origem + 472)  # setinha para cima
                    time.sleep(0.3)
                    # pyautogui.click(x_origem + 407, y_origem + 432)  # setinha para cima
                    # time.sleep(0.5)
            pyautogui.doubleClick(x_origem + 737, y_origem + 22)  # abre o cartas premidas
            time.sleep(0.2)
        atualizar_navegador()
    return False


def cartas_premidas_joga_vezes(x_origem, y_origem):
    tarefas_fazer = ('Jogar 100 vezes nas Cartas Premiadas',
                     'Gioca la Carta Scommessa per 100 volte',
                     'Jogar 50 vezes nas Cartas Premiadas',
                     'Gioca la Carta Scommessa per 50 volte',
                     'Jogar 10 vezes nas Cartas Premiadas',
                     'Gioca la Carta Scommessa per 10 volte')

    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
        return "sair da conta"

    abre_cartas_premidas(x_origem, y_origem)

    continua_jogando = True

    cont_jogadas_troca_ip = 0

    while continua_jogando:  # permanece joghando cartas premiadas ate nao ter mais a mição jogar x vezes

        if Limpa.limpa_total_fazendo_tarefa(x_origem, y_origem) == "sair da conta":
            return "sair da conta"
        if HoraT.fim_tempo_tarefa():
            return
        if cont_jogadas_troca_ip >= 5:
            cont_jogadas_troca_ip = 0
            IP.testa_trocar_IP()
        cont_jogadas_troca_ip += 1

        cartas_aberto = abre_cartas_premidas(x_origem, y_origem)  # abre o cartas premidas
        confirmar = False
        if cartas_aberto:
            print("tem cartas vezes")
            for i in range(100):
                print('espera as cartas virado para baixo')
                # espera ter as cartas virado para baixo lado marrom para cima
                if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 239), (111, 26, 37), tolerance=10):
                    print("ta com as cartas viradas para baixo")
                    print("Faz uma aposta aletoria ente cartas vermelhar ou pretas")
                    valor_aleatorio = random.choice([True, False])
                    if valor_aleatorio:
                        pyautogui.click(x_origem + 686, y_origem + 353)  # clica nas cartas vermelhas
                        print('vermelhas')
                        for _ in range(100):
                            # testa se tem a ficha de 200 verde na posição correta
                            if pyautogui.pixelMatchesColor((x_origem + 641), (y_origem + 344), (193, 46, 47), tolerance=10):
                                print('200 fichas no lugar')
                                pyautogui.doubleClick(x_origem + 711, y_origem + 422)  # clica em comfirmar
                                confirmar = True
                                break
                    else:
                        pyautogui.click(x_origem + 714, y_origem + 291)  # clica nas cartas pretas
                        print('pretas')
                        for _ in range(100):
                            # testa se tem a ficha de 200 verde na posição correta
                            if pyautogui.pixelMatchesColor((x_origem + 678), (y_origem + 295), (190, 42, 42), tolerance=10):
                                print('200 fichas no lugar')
                                pyautogui.doubleClick(x_origem + 711, y_origem + 422)  # clica em comfirmar
                                confirmar = True
                                break

                if confirmar:
                    break

                time.sleep(0.3)
        # time.sleep(3)
        # espera ate as cartas virartem para cima, ficar brancas
        for i in range(20):
            if pyautogui.pixelMatchesColor((x_origem + 440), (y_origem + 200), (252, 253, 253), tolerance=5):
                break
            time.sleep(0.3)
        # se nao virou as cartas da um limpa todal para desagarrar possivel falhar na hora de trocar ip
        if not (pyautogui.pixelMatchesColor((x_origem + 440), (y_origem + 200), (252, 253, 253), tolerance=5)):
            if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                return "sair da conta"

        # Limpa.limpa_abre_tarefa2(x_origem, y_origem)
        Limpa.limpa_abre_tarefa(x_origem, y_origem, com_pausa=False)
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
        abre_cartas_premidas(x_origem, y_origem)
        valor_fichas_ = OCR_tela.valor_fichas(x_origem, y_origem)
        if valor_fichas_ < 5000:
            valor_fichas_ = OCR_tela.valor_fichas(x_origem, y_origem)
            if valor_fichas_ < 5000:
                print('Quantidade de fichas baixa')
                return
    return


def cartas_premidas_joga_valor(x_origem, y_origem, lista_tarefas_disponivel, valor_fichas):
    tarefas_fazer = ('Ganhar 100.000 fichas nas Cartas Premiadas',
                     'Ganhar 30.000 fichas nas Cartas Premiadas',
                     'Ganhar 4.000 fichas nas Cartas Premiadas')

    tarefa = ""
    cliques = 0

    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
        return "sair da conta"

    continua_jogando = False

    for item in tarefas_fazer:
        if item in lista_tarefas_disponivel:
            print('comparar_listas_fazendo_tarefa', item)
            continua_jogando = True
            tarefa = item
            break

    if continua_jogando is False:
        return

    abre_cartas_premidas(x_origem, y_origem)
    cont_jogadas_troca_ip = 0

    while continua_jogando:  # permanece joghando cartas premiadas ate nao ter mais a mição jogar x vezes
        if Limpa.limpa_total_fazendo_tarefa(x_origem, y_origem) == "sair da conta":
            return "sair da conta"
        if HoraT.fim_tempo_tarefa():
            return
        if cont_jogadas_troca_ip >= 5:
            cont_jogadas_troca_ip = 0
            IP.testa_trocar_IP()
        cont_jogadas_troca_ip += 1

        cartas_aberto = abre_cartas_premidas(x_origem, y_origem)  # abre o cartas premidas
        confirmar = False
        if cartas_aberto:

            print("tem cartas vezes")
            for i in range(100):
                print('espera as cartas virado para baixo')
                # espera ter as cartas virado para baixo lado marrom para cima
                if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 239), (111, 26, 37), tolerance=10):
                    print("ta com as cartas viradas para baixo")
                    if tarefa == 'Ganhar 100.000 fichas nas Cartas Premiadas':
                        print('cartas 100k')
                        if valor_fichas <= 8560:
                            print(f'valor de fichas muito baixo: {valor_fichas}')
                            return
                        # valor_fichas = OCR_tela.valor_fichas(x_origem, y_origem)
                        # para se ganhar 100 k se perde 5440 / 5280 fichas

                        if valor_fichas > 106600:  # joga 1 vez
                            cliques = 264
                        elif valor_fichas > 56440:  # joga 2 vez
                            cliques = 132
                        elif valor_fichas > 31360:  # joga 4 vez
                            cliques = 66
                        elif valor_fichas > 18820:  # joga 8 vez
                            cliques = 33
                        elif valor_fichas > 12520:  # joga 17 vez
                            cliques = 16
                        elif valor_fichas > 9320:  # joga 33 vez
                            cliques = 8
                        elif valor_fichas > 8560:  # joga 44 vez
                            cliques = 6
                        # elif valor_fichas > 8200:  # joga 53 vez
                        #     cliques = 5
                        # elif valor_fichas > 7800:  # joga 66 vez
                        #     cliques = 4
                        # elif valor_fichas > 7420:  # joga 88 vez
                        #     cliques = 3
                        # elif valor_fichas > 7040:  # joga 132 vez
                        #     cliques = 2
                        # elif valor_fichas > 6660:  # joga 264 vez
                        #     cliques = 1

                    elif tarefa == 'Ganhar 30.000 fichas nas Cartas Premiadas':
                        # para se ganhar 30 k se perde 1600 fichas
                        print('cartas 30k')
                        if valor_fichas <= 4120:
                            print(f'valor de fichas muito baixo: {valor_fichas}')
                            return

                        if valor_fichas > 32600:  # joga 1 vez
                            cliques = 79
                        elif valor_fichas > 17800:  # joga 2 vez
                            cliques = 40
                        elif valor_fichas > 10200:  # joga 4 vez
                            cliques = 20
                        elif valor_fichas > 6400:  # joga 8 vez
                            cliques = 10
                        elif valor_fichas > 4500:  # joga 16 vez
                            cliques = 5
                        elif valor_fichas > 4120:  # joga 20 vez
                            cliques = 4
                        # elif valor_fichas > 3360:  # joga 40 vez
                        #     cliques = 2
                        # elif valor_fichas > 2980:  # joga 80 vez
                        #     cliques = 1

                    elif tarefa == 'Ganhar 4.000 fichas nas Cartas Premiadas':
                        # para se ganhar 4 k se perde 240 fichas
                        print('cartas 4k')
                        if valor_fichas > 5400:  # joga 1 vez
                            cliques = 11
                        elif valor_fichas > 3520:  # joga 2 vez
                            cliques = 6
                        elif valor_fichas > 2760:  # joga 3 vez
                            cliques = 4
                        elif valor_fichas > 2380:  # joga 4 vez
                            cliques = 3
                        elif valor_fichas > 1600:  # joga 11 vez
                            cliques = 1

                    for _ in range(cliques):
                        pyautogui.click(x_origem + 658, y_origem + 341)  # clica nas cartas vermelhas
                        time.sleep(0.01)
                    for _ in range(cliques):
                        pyautogui.click(x_origem + 690, y_origem + 279)  # clica nas cartas prestas
                        time.sleep(0.01)
                    time.sleep(1)
                    pyautogui.doubleClick(x_origem + 711, y_origem + 422)  # clica em comfirmar
                    break

                time.sleep(0.3)
        # time.sleep(3)
        # espera ate as cartas virartem para cima, ficar brancas
        for i in range(20):
            if pyautogui.pixelMatchesColor((x_origem + 440), (y_origem + 200), (252, 253, 253), tolerance=5):
                break
            time.sleep(0.3)
        # se nao virou as cartas da um limpa todal para desagarrar possivel falhar na hora de trocar ip
        if not (pyautogui.pixelMatchesColor((x_origem + 440), (y_origem + 200), (252, 253, 253), tolerance=5)):
            if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                return "sair da conta"

        # Limpa.limpa_abre_tarefa2(x_origem, y_origem)
        Limpa.limpa_abre_tarefa(x_origem, y_origem, com_pausa=False)
        Tarefas.recolher_tarefa(x_origem, y_origem)
        meta_atigida, pontos = Tarefas.meta_tarefas(x_origem, y_origem)

        continua_jogando, tarefa = Tarefas.comparar_listas_fazendo_tarefa(tarefas_fazer, x_origem, y_origem)  # procura com ocr

        if (not continua_jogando) or meta_atigida:
            time.sleep(0.5)
            Limpa.limpa_abre_tarefa(x_origem, y_origem)
            continua_jogando, tarefa = Tarefas.comparar_listas_fazendo_tarefa(tarefas_fazer, x_origem, y_origem)  # procura com ocr
            meta_atigida, pontos = Tarefas.meta_tarefas(x_origem, y_origem)
            if (not continua_jogando) or meta_atigida:
                print("FIM")
                if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                    return "sair da conta"
                return

        Limpa.fecha_tarefa(x_origem, y_origem)  # fecha a lista de tarefas diarias
        abre_cartas_premidas(x_origem, y_origem)
        valor_fichas_ = OCR_tela.valor_fichas(x_origem, y_origem)
        if valor_fichas_ < 5000:
            valor_fichas_ = OCR_tela.valor_fichas(x_origem, y_origem)
            if valor_fichas_ < 5000:
                print('Quantidade de fichas baixa')
                return
    return


def cartas_premidas_joga_vezes_upando(x_origem, y_origem):
    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
        return "sair da conta"

    abre_cartas_premidas(x_origem, y_origem)

    continua_jogando = True

    while continua_jogando:  # permanece joghando cartas premiadas ate nao ter mais a mição jogar x vezes
        cartas_aberto = abre_cartas_premidas(x_origem, y_origem)  # abre o cartas premidas
        confirmar = False
        if cartas_aberto:

            print("tem cartas vezes")
            for i in range(100):
                print('espera as cartas virado para baixo')
                # espera ter as cartas virado para baixo lado marrom para cima
                if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 239), (111, 26, 37), tolerance=10):
                    print("ta com as cartas viradas para baixo")
                    if pyautogui.pixelMatchesColor((x_origem + 394), (y_origem + 483), (239, 231, 212), tolerance=10):
                        # Teste se tem 1000 fichas gratis
                        for i in range(10):
                            pyautogui.click(x_origem + 658, y_origem + 341)  # clica nas cartas vermelhas
                            time.sleep(0.1)

                    valor_aleatorio = random.choice([True, False])
                    if valor_aleatorio:
                        pyautogui.click(x_origem + 686, y_origem + 353)  # clica nas cartas vermelhas
                        print('vermelhas')
                        for _ in range(100):
                            # testa se tem a ficha de 200 verde na posição correta
                            if pyautogui.pixelMatchesColor((x_origem + 641), (y_origem + 344), (193, 46, 47), tolerance=10):
                                print('200 fichas no lugar')
                                pyautogui.doubleClick(x_origem + 711, y_origem + 422)  # clica em comfirmar
                                confirmar = True
                                break
                    else:
                        pyautogui.click(x_origem + 714, y_origem + 291)  # clica nas cartas pretas
                        print('pretas')
                        for _ in range(100):
                            # testa se tem a ficha de 200 verde na posição correta
                            if pyautogui.pixelMatchesColor((x_origem + 678), (y_origem + 295), (190, 42, 42), tolerance=10):
                                print('200 fichas no lugar')
                                pyautogui.doubleClick(x_origem + 711, y_origem + 422)  # clica em comfirmar
                                confirmar = True
                                break

                if confirmar:
                    break

                time.sleep(0.3)

        # espera ate as cartas virartem para cima, ficar brancas
        for i in range(20):
            if pyautogui.pixelMatchesColor((x_origem + 440), (y_origem + 200), (252, 253, 253), tolerance=5):
                break
            time.sleep(0.3)
        # se nao virou as cartas da um limpa todal para desagarrar possivel falhar na hora de trocar ip
        if not (pyautogui.pixelMatchesColor((x_origem + 440), (y_origem + 200), (252, 253, 253), tolerance=5)):
            if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                return "sair da conta"

        status_tarefa = Tarefas.recolher_tarefa_upando(x_origem, y_origem)
        print(status_tarefa)
        if status_tarefa == "Não tem missão":
            continua_jogando = True
        elif status_tarefa == "Recolhido":
            continua_jogando = False
        else:
            continua_jogando = False

        if not continua_jogando:
            print("FIM")
            if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                return "sair da conta"
            return
    return

# x_origem, y_origem = Origem_pg.x_y()
# cartas_premidas_joga_vezes_upando(x_origem, y_origem)
# #abre_cartas_premidas(x_origem, y_origem) # abre o cartas premidas
# #
# cartas_premidas_joga_vezes(x_origem, y_origem)

# cartas_premidas_joga_valor(x_origem, y_origem)
