import random
import time

import pyautogui

import HoraT
import IP
import Limpa
import Tarefas

# Desabilitar o fail-safe
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0


def abre_cartas_premidas(x_origem, y_origem):
    for i in range(30):
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


def cartas_premidas_joga_vezes(x_origem, y_origem):
    tarefas_fazer = ('Jogar 100 vezes nas Cartas Premiadas',
                     'Jogar 50 vezes nas Cartas Premiadas',
                     'Jogar 10 vezes nas Cartas Premiadas')

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
        if cartas_aberto == True:

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
        abre_cartas_premidas(x_origem, y_origem)
    return


def cartas_premidas_joga_valor(x_origem, y_origem, lista_tarefas_disponivel, valor_fichas):
    tarefas_fazer = ('Ganhar 100.000 fichas nas Cartas Premiadas',
                     'Ganhar 30.000 fichas nas Cartas Premiadas',
                     'Ganhar 4.000 fichas nas Cartas Premiadas')

    tarefa = ""

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
        if cartas_aberto == True:

            print("tem cartas vezes")
            for i in range(100):
                print('espera as cartas virado para baixo')
                # espera ter as cartas virado para baixo lado marrom para cima
                if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 239), (111, 26, 37), tolerance=10):
                    print("ta com as cartas viradas para baixo")
                    if tarefa == 'Ganhar 100.000 fichas nas Cartas Premiadas':
                        print('cartas 100k')
                        # valor_fichas = OCR_tela.valor_fichas(x_origem, y_origem)
                        if valor_fichas > 110000:
                            for i in range(264):
                                pyautogui.click(x_origem + 658, y_origem + 341)  # clica nas cartas vermelhas
                                time.sleep(0.01)
                            for i in range(264):
                                pyautogui.click(x_origem + 690, y_origem + 279)  # clica nas cartas prestas
                                time.sleep(0.01)
                            time.sleep(1)
                            pyautogui.doubleClick(x_origem + 711, y_origem + 422)  # clica em comfirmar
                            break

                        else:  # quando nao tem ficha par ajogar de uma so vez
                            for i in range(90):
                                pyautogui.click(x_origem + 658, y_origem + 341)  # clica nas cartas vermelhas
                                time.sleep(0.01)
                            for i in range(90):
                                pyautogui.click(x_origem + 690, y_origem + 279)  # clica nas cartas prestas
                                time.sleep(0.01)
                            time.sleep(1)
                            pyautogui.doubleClick(x_origem + 711, y_origem + 422)  # clica em comfirmar
                            break

                    elif tarefa == 'Ganhar 30.000 fichas nas Cartas Premiadas':
                        print('cartas 30k')
                        for i in range(79):
                            pyautogui.click(x_origem + 658, y_origem + 341)  # clica nas cartas vermelhas
                            time.sleep(0.01)
                        for i in range(79):
                            pyautogui.click(x_origem + 690, y_origem + 279)  # clica nas cartas prestas
                            time.sleep(0.01)
                        time.sleep(1)
                        pyautogui.doubleClick(x_origem + 711, y_origem + 422)  # clica em comfirmar
                        break

                    elif tarefa == 'Ganhar 4.000 fichas nas Cartas Premiadas':
                        print('cartas 4k')
                        for i in range(11):
                            pyautogui.click(x_origem + 658, y_origem + 341)  # clica nas cartas vermelhas
                            time.sleep(0.01)
                        for i in range(11):
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

        Limpa.fecha_tarefa(x_origem, y_origem)  # fecha a lista de tarefas diarias
        abre_cartas_premidas(x_origem, y_origem)
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
