# import Firebase
from time import sleep

import pyautogui

from Cartas import abre_cartas_premidas
from Genius import abre_genius, localizar_imagem
from Limpa import limpa_total
from OCR_tela import tarefas_diaris_upando
from Slot import abre_slot
from Tarefas import recolher_tarefa_upando


def slot_joga_vezes_upando(x_origem, y_origem):
    """
    Joga repetidamente em um caça-níqueis para completar a missão de 'Gire 10 vezes no caça-níqueis'.

    Parameters:
    - x_origem (int): Coordenada x da origem da janela do jogo.
    - y_origem (int): Coordenada y da origem da janela do jogo.

    Returns:
    - str: Mensagem indicando se a missão foi concluída.
    """
    print('slot_joga_vezes_upando')
    joga_vezes = True
    cont_jogadas = 0
    continua_jogando = True

    limpa_total(x_origem, y_origem)

    while continua_jogando:  # Permanece jogando cartas premiadas até não ter mais a missão de jogar x vezes

        slot_aberto = abre_slot(x_origem, y_origem, joga_vezes)

        if slot_aberto:
            print('Esperando girar na cor certa')
            for i in range(20):
                # Espera poder clicar no girar
                if pyautogui.pixelMatchesColor((x_origem + 922), (y_origem + 609), (216, 17, 2), tolerance=5):
                    pyautogui.doubleClick(x_origem + 922, y_origem + 609)  # Clica em girar
                    print("Clicou em girar")
                    cont_jogadas += 1
                    status_upando = 'Jogando Slot ' + str(cont_jogadas)
                    print(status_upando)
                    break
                sleep(0.3)

        status_tarefa = recolher_tarefa_upando(x_origem, y_origem)
        print(status_tarefa)
        lista_tarefa_upar = tarefas_diaris_upando(x_origem, y_origem)

        if 'Gire 10 vezes no caça-níqueis' in lista_tarefa_upar:
            continua_jogando = True
        else:
            print("Terminou Slot")
            limpa_total(x_origem, y_origem)
            return "Terminou Slot"
    return "Terminou Slot"


def genius_joga_vezes_upando(x_origem, y_origem):
    """
    Joga no jogo Genius Pro até atingir a quantidade de jogadas necessárias.

    Parameters:
    - x_origem (int): Coordenada x da origem da janela.
    - y_origem (int): Coordenada y da origem da janela.

    Returns:
    - str: Mensagem indicando o término da execução da função.
    """

    print('genius_joga_vezes_upando')

    cont_jogadas = 0
    continua_jogando = True
    regiao = (473 + x_origem, 101 + y_origem, 20, 32)  # (x, y, largura, altura)
    imagem1 = r'Imagens\Genius\tempo6.png'
    precisao = 0.9

    limpa_total(x_origem, y_origem)

    while continua_jogando:  # Permanece jogando Genius Pro até atingir a quantidade de jogadas

        genius_aberto = abre_genius(x_origem, y_origem)

        if genius_aberto:
            print('Esperando o valor de tempo certo')

            for _ in range(80):
                # Espera o tempo correto
                posicao = localizar_imagem(imagem1, regiao, precisao)
                if posicao is not None:  # Verifica se a imagem foi encontrada
                    print("Faz a aposta")
                    if pyautogui.pixelMatchesColor((x_origem + 449), (y_origem + 655), (193, 119, 70), tolerance=5):
                        # Testa se há uma seta para cima
                        pyautogui.click(x_origem + 603, y_origem + 223)  # Clica em Staci ganha
                        cont_jogadas += 1
                        status_upando = 'Jogando Genius ' + str(cont_jogadas)
                        print(status_upando)
                    else:
                        for _ in range(5):
                            pyautogui.click(x_origem + 603, y_origem + 223)  # Clica em Staci ganha
                            sleep(0.1)
                        print('Jogou a quantia gratuita')

                    sleep(10)
                    break

                sleep(0.3)

            status_tarefa = recolher_tarefa_upando(x_origem, y_origem)
            print(status_tarefa)
            lista_tarefa_upar = tarefas_diaris_upando(x_origem, y_origem)

            if 'Jogar no Casino Genius Pro 5 vezes' in lista_tarefa_upar:
                continua_jogando = True
            else:
                print("Terminou Genius")
                limpa_total(x_origem, y_origem)
                return "Terminou Genius"

    return "Terminou Genius"


def cartas_premidas_joga_vezes_upando(x_origem, y_origem):
    print('cartas_premidas_joga_vezes_upando')

    cont_jogadas = 0
    continua_jogando = True
    limpa_total(x_origem, y_origem)

    while continua_jogando:
        # permanece joghando cartas premiadas ate nao ter mais a mição jogar x vezes
        cartas_aberto = abre_cartas_premidas(x_origem, y_origem)  # abre o cartas premidas
        confirmar = False
        if cartas_aberto:

            print("tem cartas vezes")
            for _ in range(100):
                print('espera as cartas virado para baixo')
                # espera ter as cartas virado para baixo lado marrom para cima
                if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 239), (111, 26, 37), tolerance=10):
                    print("ta com as cartas viradas para baixo")
                    if pyautogui.pixelMatchesColor((x_origem + 394), (y_origem + 483), (239, 231, 212),
                                                   tolerance=10):  # Teste se tem 1000 fichas gratis
                        for i in range(10):
                            pyautogui.click(x_origem + 658, y_origem + 341)  # clica nas cartas vermelhas
                            sleep(0.1)
                        print('Jogou a quantia gatis')

                    pyautogui.click(x_origem + 658, y_origem + 341)  # clica nas cartas vermelhas
                    for _ in range(100):
                        # testa se tem a ficha de 200 verde na posição correta
                        if pyautogui.pixelMatchesColor((x_origem + 641), (y_origem + 344), (193, 46, 47), tolerance=5):
                            print('200 fichas no lugar')
                            pyautogui.doubleClick(x_origem + 711, y_origem + 422)  # clica em comfirmar
                            cont_jogadas += 1
                            status_upando = 'Jogando Cartas ' + str(cont_jogadas)
                            print(status_upando)
                            confirmar = True
                            break

                if confirmar:
                    break

                sleep(0.3)

        # espera ate as cartas virartem para cima, ficar brancas
        for _ in range(20):
            if pyautogui.pixelMatchesColor((x_origem + 440), (y_origem + 200), (252, 253, 253), tolerance=5):
                break
            sleep(0.3)
        # se nao virou as cartas da um limpa todal para desagarrar possivel falhar na hora de trocar ip
        if not pyautogui.pixelMatchesColor((x_origem + 440), (y_origem + 200), (252, 253, 253), tolerance=5):
            if limpa_total(x_origem, y_origem) == "sair da conta":
                return "sair da conta"

        status_tarefa = recolher_tarefa_upando(x_origem, y_origem)
        print(status_tarefa)
        lista_tarefa_upar = tarefas_diaris_upando(x_origem, y_origem)
        if 'Jogar o Casino Poker Genius 5 vezes' in lista_tarefa_upar:
            continua_jogando = True
        else:
            print("Terminou Cartas Premiadas")
            limpa_total(x_origem, y_origem)
            return "Terminou Cartas Premiadas"
    return "Terminou Cartas Premiadas"


def levantar_mesa(x_origem, y_origem):
    print('levantar_mesa')
    sentado = "manda levantar"
    for i in range(50):
        if pyautogui.pixelMatchesColor((x_origem + 619), (y_origem + 631), (67, 89, 136), tolerance=1):  # testa se esta dentro da mesa
            print('Não esta sentado')
            sentado = "levantou da mesa"
            # Firebase.confirmacao_comando_resposta(sentado)
            break

        if (pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 674), (27, 92, 155), tolerance=19)
                or pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 674), (19, 64, 109), tolerance=19)):  # testa se esta dentro da mesa

            pyautogui.click(947 + x_origem, 78 + y_origem)  # setinha
            sleep(0.3)
            pyautogui.click(925 + x_origem, 204 + y_origem)  # Levantar

            if pyautogui.pixelMatchesColor((x_origem + 455), (y_origem + 417), (25, 116, 184),
                                           tolerance=19):  # aviso do sistema "tem certesa de que quer sair da mesa?"
                pyautogui.click(641 + x_origem, 278 + y_origem)  # clica no x do aviso do sistema "tem certesa de que quer sair da mesa?"
                print("aviso do sistema")
                sleep(0.3)
                pyautogui.click(947 + x_origem, 78 + y_origem)  # setinha
                sleep(0.3)
                pyautogui.click(925 + x_origem, 204 + y_origem)  # Levantar

    return sentado

# def passa_ate_lv7(x_origem, y_origem):  # para se fazer tarefas
#     print('passa_ate_lv7')
#     # Firebase.confirmacao_comando_resposta("Jogando mesa")
#     level = 0
#     status_comando = "Jogando mesa"
#
#     while True:
#         # comando = Firebase.comando_escravo
#         # if comando == "Levanta":
#         #     status_comando = levantar_mesa(x_origem, y_origem)
#         #     return
#         #
#         # Firebase.confirmacao_comando_resposta(status_comando)
#
#         limpa_jogando(x_origem, y_origem)
#
#         status_tarefas = recolher_tarefa_upando(x_origem, y_origem)
#
#         if status_tarefas == "Recolhido":
#             lista, so_tem_gire = tarefas_diaris_upando(x_origem, y_origem)
#
#         if pyautogui.pixelMatchesColor((x_origem + 480), (y_origem + 650), (43, 16, 9), tolerance=3):
#             pyautogui.click((x_origem + 640), (y_origem + 72))  # clica para passar animação de recolher
#
#         if pyautogui.pixelMatchesColor((x_origem + 619), (y_origem + 631), (67, 89, 136), tolerance=1):  # testa se esta sentado
#             print("Levantou")
#             print("Emvia um comando para levantar os outros escravos")
#             # Firebase.comando_coleetivo_escravo_escravo("Levanta")
#             return
#
#         else:
#
#             if level < 7:
#                 # se nao esta com v azul dentro do quadrado branco e se esta com quadrado branco
#                 if ((not pyautogui.pixelMatchesColor((x_origem + 333), (y_origem + 610), (59, 171, 228), tolerance=1))
#                         and (pyautogui.pixelMatchesColor((x_origem + 333), (y_origem + 610), (255, 255, 255), tolerance=1))):
#                     pyautogui.click((x_origem + 337), (y_origem + 605))
#                     # sleep(0.3)
#                     print("Passou")
#                     try:
#                         level = level_conta(x_origem, y_origem)
#                     except:
#                         print("erro level")
#                     status_comando = "Passou" + " " + so_tem_gire
#
#                 elif pyautogui.pixelMatchesColor((x_origem + 480), (y_origem + 650), (255, 255, 255), tolerance=1):  # testa se tem area branca
#                     pyautogui.click((x_origem + 337), (y_origem + 605))
#                     print("Pagou")
#                     try:
#                         level = level_conta(x_origem, y_origem)
#                     except:
#                         print("erro level")
#                     status_comando = "Pagou" + " " + so_tem_gire
#
#             else:
#                 if pyautogui.pixelMatchesColor((x_origem + 480), (y_origem + 650), (255, 255, 255), tolerance=1):  # testa se tem area branca
#                     pyautogui.click((x_origem + 528), (y_origem + 605))  # clica no correr
#                     print("Correu")
#                     status_comando = "Correu" + " " + so_tem_gire
#                     if limpa_abre_tarefa2(x_origem, y_origem):
#                         so_tem_gire = 'caonta Upada'
#                     else:
#                         so_tem_gire = 'upando'
#                     pyautogui.click(821 + x_origem, 138 + y_origem)  # fecha tarefa
