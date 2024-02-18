import time

import pyautogui

import Limpa


def cofre_abrir(x_origem, y_origem):
    cofre_fechado = True
    # Limpa.limpa_total(x_origem, y_origem)
    while cofre_fechado:
        pyautogui.doubleClick(x_origem + 214, y_origem + 25)  # clica no no icone do cofre para abrir a janela
        Limpa.limpa_pequeno(x_origem, y_origem)
        if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 170), (111, 79, 51), tolerance=10):
            # testa se esta visivel o cofre
            print("Janela do cobre visivel")

            if pyautogui.pixelMatchesColor((x_origem + 420), (y_origem + 340), (76, 56, 39), tolerance=10):
                # testa se esta diponivel para digitar senha
                pyautogui.doubleClick(x_origem + 450, y_origem + 340)  # clica no campo para digirta senha
                time.sleep(0.5)
                pyautogui.typewrite("020996Pa")  # coloca a senha no canpo destinado
                time.sleep(0.5)
                pyautogui.press('enter')  # Pressione a tecla "Enter"
                time.sleep(0.5)

            if pyautogui.pixelMatchesColor((x_origem + 148), (y_origem + 237), (120, 35, 23), tolerance=10):
                # testa se esta diponivel para digitar senha
                print('Cofre aberto')
                cofre_fechado = False
                return True

            if pyautogui.pixelMatchesColor((x_origem + 286), (y_origem + 186), (255, 248, 246), tolerance=5):
                # testa se tem que criar o cofre
                print('Cofre ainda naofoicriado')
                cofre_criar(x_origem, y_origem)


def cofre_depositar(x_origem, y_origem):
    if cofre_abrir(x_origem, y_origem):
        pyautogui.doubleClick(x_origem + 330, y_origem + 140)  # clica para abrir a tela de depositar
        time.sleep(0.5)
        pyautogui.doubleClick(x_origem + 490, y_origem + 280)  # clica na area para escrever o valor da fichas
        time.sleep(0.5)
        pyautogui.typewrite("40000")  # escreve o valor a ser depositado
        time.sleep(0.5)
        pyautogui.click(x_origem + 490, y_origem + 500)  # clica no botao depositar
        for i in range(30):
            if (pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 475), (14, 134, 7), tolerance=10)
                    or pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 475), (17, 146, 9), tolerance=10)):
                # testa se esta diponivel para digitar senha
                pyautogui.doubleClick(x_origem + 490, y_origem + 470)  # clica no botao OK de confirmação de deposito
                print('Valor depositado corretamente')
                return True
            time.sleep(0.2)
        return False

    else:
        print('Cofre não foi aberto')
        return False


def cofre_sacar(x_origem, y_origem):
    if cofre_abrir(x_origem, y_origem):
        pyautogui.doubleClick(x_origem + 660, y_origem + 140)  # clica para abrir a tela de sacara
        time.sleep(0.5)
        pyautogui.doubleClick(x_origem + 490, y_origem + 280)  # clica na area para escrever o valor da fichas
        time.sleep(0.5)
        pyautogui.typewrite("999999999")  # escreve o valor para sacar tudo
        time.sleep(0.5)
        pyautogui.click(x_origem + 490, y_origem + 500)  # clica no botao depositar
        for i in range(30):
            if (pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 475), (14, 134, 7), tolerance=10)
                    or pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 475), (17, 146, 9), tolerance=10)):
                # testa se esta diponivel para digitar senha
                pyautogui.doubleClick(x_origem + 490, y_origem + 470)  # clica no botao OK de confirmação de deposito
                print('Valor sacado corretamente')
                return True
            time.sleep(0.2)
        print('Cofre ja estava vazio')
        return True

    else:
        print('Cofre não foi aberto')
        return False


def cofre_criar(x_origem, y_origem):
    # pyautogui.doubleClick(x_origem + 214, y_origem + 25)  # clica no no icone do cofre para abrir a janela
    # time.sleep(0.5)
    pyautogui.click(x_origem + 490, y_origem + 480)  # clica no botao confirmar para criaro cofre
    time.sleep(0.5)
    if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 150), (106, 30, 230), tolerance=5):
        # testa se aoareceu o cadastrar
        time.sleep(0.5)
        pyautogui.click(x_origem + 490, y_origem + 240)  # clica no campo para digitar a senha
        time.sleep(0.5)
        pyautogui.typewrite("020996Pa")  # coloca a senha no canpo destinado
        time.sleep(0.5)
        pyautogui.click(x_origem + 490, y_origem + 307)  # clica no campo para Repita a senha
        time.sleep(0.5)
        pyautogui.typewrite("020996Pa")  # coloca a senha no canpo destinado
        time.sleep(0.5)
        pyautogui.click(x_origem + 490, y_origem + 417)  # clica no campo resposta
        time.sleep(0.5)
        pyautogui.typewrite("Ale")  # coloca a senha no canpo destinado
        time.sleep(0.5)
        pyautogui.click(x_origem + 340, y_origem + 500)  # clica fora da caixa de digitar
        time.sleep(0.5)
        if (pyautogui.pixelMatchesColor((x_origem + 634), (y_origem + 243), (0, 153, 0), tolerance=5)
                and pyautogui.pixelMatchesColor((x_origem + 634), (y_origem + 312), (0, 153, 0), tolerance=5)
                and pyautogui.pixelMatchesColor((x_origem + 776), (y_origem + 420), (0, 153, 0), tolerance=5)):
            # testa se tem os 3 V's verdes
            pyautogui.click(x_origem + 490, y_origem + 500)  # clica no botao conformar para criaro cofre
            time.sleep(1)
            if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 170), (111, 79, 51), tolerance=10):
                # testa se esta visivel o cofre
                print("Cofre criado com sucesso")
                return True
            else:
                print("Falha ao criar")
                pyautogui.click(x_origem + 816, y_origem + 142)  # clica no x para fechar o cofre
                time.sleep(1)
                return False

# cofre_abrir(x_origem, y_origem)
# cofre_sacar(x_origem, y_origem)
# cofre_depositar(x_origem, y_origem)
