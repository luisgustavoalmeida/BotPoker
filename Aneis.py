import time

import pyautogui

import Limpa

# Desabilitar o fail-safe
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0


def recolhe_aneis(x_origem, y_origem):
    # testa se tem aneis para serem recolhidos

    for i in range(2):
        if (pyautogui.pixelMatchesColor((x_origem + 954), (y_origem + 288), (33, 145, 18), tolerance=30)
                or (not pyautogui.pixelMatchesColor((x_origem + 954), (y_origem + 288), (32, 17, 20), tolerance=30))):
            # testa se tem o verde do anel ou se nao esta visivel a parte atras do verde
            print("Tem aneis para recolhar")
            Limpa.limpa_total(x_origem, y_origem)
            for i in range(20):
                pyautogui.doubleClick((x_origem + 928), (y_origem + 323))
                # espera abrir os anis
                if pyautogui.pixelMatchesColor((x_origem + 650), (y_origem + 118), (72, 72, 74), tolerance=20):
                    print('aneis aberto')
                    time.sleep(0.5)
                    # se esta aberto
                    pyautogui.doubleClick((x_origem + 195), (y_origem + 307))  # 1
                    pyautogui.doubleClick((x_origem + 275), (y_origem + 307))  # 2
                    pyautogui.doubleClick((x_origem + 355), (y_origem + 307))  # 3

                    pyautogui.doubleClick((x_origem + 235), (y_origem + 408))  # 4
                    pyautogui.doubleClick((x_origem + 315), (y_origem + 408))  # 5

                    pyautogui.doubleClick((x_origem + 630), (y_origem + 307))  # 6
                    pyautogui.doubleClick((x_origem + 710), (y_origem + 307))  # 7
                    pyautogui.doubleClick((x_origem + 788), (y_origem + 307))  # 8

                    pyautogui.doubleClick((x_origem + 670), (y_origem + 408))  # 9
                    pyautogui.doubleClick((x_origem + 750), (y_origem + 408))  # 10

                    time.sleep(3)

                    Limpa.limpa_promocao(x_origem, y_origem)
                    return
                time.sleep(0.5)
    return

#
# x_origem, y_origem = Origem_pg.x_y()
# # #
# recolhe_aneis(x_origem, y_origem)
