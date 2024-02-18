import datetime
import time

import pyautogui

import Aneis
import IP
import Limpa
import Seleniun
from OCR_tela import tempo_roleta

pyautogui.FAILSAFE = False  # Desabilitar o fail-safe
pyautogui.PAUSE = 0


def roletas(x_origem, y_origem):
    cont_roleta1 = 0
    TEMPO_ESPERA = 1200  # tempo de tolerancia para esperar em, segundos
    roleta = "sem_roleta"
    tempo2 = 1200
    while True:
        print('roletas')

        pyautogui.click(490 + x_origem, 70 + y_origem, button='left')  # clique bobo para passar alguma naimação

        if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
            break

        # testa se tem a barra vermelha ou #testa se tem a barra amarela ou
        # #testa se tem a barra amarelo meio cinza # se tem siguinifica que ja fez o R1
        if (pyautogui.pixelMatchesColor((x_origem + 702), (y_origem + 41), (153, 3, 86), tolerance=20) or
                pyautogui.pixelMatchesColor((x_origem + 673), (y_origem + 41), (254, 191, 35), tolerance=20) or
                pyautogui.pixelMatchesColor((x_origem + 673), (y_origem + 41), (166, 113, 35), tolerance=20)):
            roleta = 'roleta_2'
            print("Jarodou a roleta 1, tem que fazer a roleta 2")
            # faz roleta 2# se tem roleta 2 tem que ta com o icone da roleta amarelo
            if ((not pyautogui.pixelMatchesColor((x_origem + 680), (y_origem + 14), (227, 235, 248), tolerance=20))
                    and (not pyautogui.pixelMatchesColor((x_origem + 680), (y_origem + 14), (146, 172, 208), tolerance=20))):
                # testa se o icone da roleta NÃO esta cinsa
                # ricone da roleta esta mamarelo
                print("espera abrir a roleta 2")
                for i in range(100):
                    print("espera abrir a roleta 2")
                    pyautogui.doubleClick(x_origem + 683, y_origem + 14)  # clica no icone roleta, ja roda sozinho

                    if (pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 107), (39, 22, 74), tolerance=10)
                            or pyautogui.pixelMatchesColor((x_origem + 290), (y_origem + 107), (39, 22, 74), tolerance=10)):
                        pyautogui.doubleClick(x_origem + 486, y_origem + 335)  # clica no meio da roleta para rodar, mas a R2 roda sozinho
                        pyautogui.doubleClick(x_origem + 683, y_origem + 14)  # clica no icone roleta, ja roda sozinho
                        print("clicou na roleta 2")
                        time_rodou = time.perf_counter()
                        roleta = 'roleta_2'
                        return roleta, None, time_rodou

                    if Limpa.limpa_pequeno(x_origem, y_origem) == "sair da conta":
                        roleta = 'sair da conta'
                        return roleta, None, 0

                    time.sleep(0.5)
                    pyautogui.click(490 + x_origem, 70 + y_origem, )  # clique bobo para passar alguma naimação
                    IP.f5_quando_internete_ocila()

                IP.f5_quando_internete_ocila()

            elif (pyautogui.pixelMatchesColor((x_origem + 680), (y_origem + 14), (227, 235, 248), tolerance=20)
                  or pyautogui.pixelMatchesColor((x_origem + 680), (y_origem + 14), (146, 172, 208), tolerance=20)):
                pyautogui.click(490 + x_origem, 70 + y_origem)  # clique bobo para passar alguma naimação
                time.sleep(0.5)
                # testa se o icone da roleta  esta cinsa
                print('icone da roleta nao esta amarelo')
                # OCR para saber quanto tempo falta para rodar
                tempo = tempo_roleta(x_origem, y_origem)
                print("tempo restante: ", tempo)
                # converte o tempo que esta escrito na roleta para segundos
                tempo = tempo // 10000 * 3600 + (tempo % 10000) // 100 * 60 + (tempo % 100)
                print(tempo)

                if tempo < tempo2:
                    tempo2 = tempo
                    cont_roleta1 = 0

                if tempo > TEMPO_ESPERA:  # testa se o tempo é maior que o predeterminado se sim si fora
                    pyautogui.click(490 + x_origem, 70 + y_origem)  # clique bobo para passar alguma naimação
                    time.sleep(2)
                    tempo = tempo_roleta(x_origem, y_origem)
                    print("tempo restante: ", tempo)
                    # converte o tempo que esta escrito na roleta para segundos
                    tempo = tempo // 10000 * 3600 + (tempo % 10000) // 100 * 60 + (tempo % 100)

                    if tempo > TEMPO_ESPERA:  # testa se o tempo é maior que o predeterminado se sim si fora
                        print("não espera, tempo para a roleta maior que o determindao")

                        hora_atual = datetime.datetime.now().time()
                        hora_atual_segundos = hora_atual.hour * 3600 + hora_atual.minute * 60 + hora_atual.second
                        print(hora_atual_segundos)

                        segundos = hora_atual_segundos - (18000 - tempo)
                        print(segundos)

                        horas = segundos // 3600
                        minutos = (segundos % 3600) // 60
                        segundos = segundos % 60

                        hora_que_rodou = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
                        print(hora_que_rodou)
                        roleta = 'roleta_2'
                        time_rodou = 0
                        return roleta, hora_que_rodou, time_rodou

                else:
                    print("esperando pela roleta 2")
                    IP.testa_trocar_IP()
                    time.sleep(5)

        # faz roleta 1 # se tem roleta 1 tem que ta com o icone da roleta amarelo e nao pode ter barra vermelha nem amarela nem amerela mio cinza
        else:
            print('nao tem roleta 2')
            roleta = 'roleta_1'
            if ((not pyautogui.pixelMatchesColor((x_origem + 680), (y_origem + 14), (227, 235, 248), tolerance=15))
                    and (not pyautogui.pixelMatchesColor((x_origem + 680), (y_origem + 14), (146, 172, 208), tolerance=15))):
                # testa se o icone da roleta NÃO esta cinsa

                print("espera abrir a roleta 1")
                for i in range(50):
                    pyautogui.doubleClick(x_origem + 683, y_origem + 14)  # clica no icone da roleta para abir
                    if Limpa.limpa_pequeno(x_origem, y_origem) == "sair da conta":
                        roleta = 'sair da conta'
                        return roleta, None

                    pyautogui.click(490 + x_origem, 70 + y_origem)  # clique bobo para passar alguma naimação

                    if pyautogui.pixelMatchesColor((x_origem + 495), (y_origem + 315), (211, 110, 12), tolerance=25):
                        # testa de roleta 1 ta aberta Pino dourado apontando para cima

                        pyautogui.doubleClick(x_origem + 492, y_origem + 383)  # clica no meio da roleta para rodar
                        print("roleta 1 aberta")
                        time.sleep(0.3)
                        pyautogui.doubleClick(x_origem + 492, y_origem + 383)  # clica no meio da roleta para rodar
                        # time.sleep(0.8)
                        roleta = 'roleta_1'
                        time_rodou = time.perf_counter()
                        return roleta, None, time_rodou

                    IP.f5_quando_internete_ocila()
                    time.sleep(1)
                IP.f5_quando_internete_ocila()

        # testa se apareceu os premios
        if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 612), (255, 196, 255), tolerance=20):
            print("Ja saiu os premios")
            break

        if roleta == 'roleta_1':
            # testa se tem a barra vermelha ou #testa se tem a barra amarela
            if (pyautogui.pixelMatchesColor((x_origem + 702), (y_origem + 41), (161, 6, 93), tolerance=20)) or \
                    (pyautogui.pixelMatchesColor((x_origem + 673), (y_origem + 41), (253, 195, 44), tolerance=20)):
                print("Jarodou a roleta 1 esta com barra vermelha ou amarela")
                break
            elif pyautogui.pixelMatchesColor((x_origem + 680), (y_origem + 14), (227, 235, 248), tolerance=20):
                print("Jarodou a roleta 1 esta com icone cinza")
                break
            # se fez todas as roletas do dia
            elif pyautogui.pixelMatchesColor((x_origem + 680), (y_origem + 14), (227, 235, 248),
                                             tolerance=20):  # testa se o icone da roleta ta branco
                print("Jarodou todas as roletas do dia")
                break
            # se fez todas as roletas do dia
            elif pyautogui.pixelMatchesColor((x_origem + 680), (y_origem + 14), (146, 172, 208),
                                             tolerance=20):  # testa se o icone da roleta ta branco
                print("Jarodou todas as roletas do dia")
                break

        entrou_corretamente, stataus = Seleniun.teste_logado()
        # fazer restes se tem mesagem de duas pessoas logado

        Aneis.recolhe_aneis(x_origem, y_origem)

        cont_roleta1 += 1
        time.sleep(2)
        print("cont tentativa: ", cont_roleta1)
        # testar se tem que trocar IP par alibera computador
        if cont_roleta1 >= 5:
            print("da um atualizar na pagina")
            IP.tem_internet()
            Seleniun.atualizar_pagina()
            cont_roleta1 = 0
            time.sleep(15)
            # da um F5

        IP.f5_quando_internete_ocila()
        Limpa.limpa_total(x_origem, y_origem)
    return roleta, "00:00:00", 0
