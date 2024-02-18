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


def localizar_imagem(imagem, regiao, precisao):
    try:
        posicao = pyautogui.locateOnScreen(imagem, region=regiao, confidence=precisao, grayscale=True)
        return posicao
    except:
        print("Ocorreu um erro ao localizar a imagem")
        time.sleep(2)
        return None


def abre_genius(x_origem, y_origem):
    while True:

        for i in range(50):

            limpo = Limpa.teste_limpo(x_origem, y_origem)
            if limpo:
                pyautogui.click(x_origem + 792, y_origem + 21)
                print('clica para abrir Genius')
                time.sleep(1)

            elif pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 612), (111, 100, 105), tolerance=5):

                if pyautogui.pixelMatchesColor((x_origem + 449), (y_origem + 655), (193, 119, 70), tolerance=5):
                    # Testa se tem uma setinha para cima

                    print("Genius, entrou")
                    valor = 200
                    if ajustar_valor(x_origem, y_origem, valor):
                        return True
                else:
                    print("Genius, entrou. Conta sendo upada")
                    return True

            elif pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 612), (78, 70, 74), tolerance=5):
                # genius com foco na mensagem
                # mensagem par aclicar no ok de muito tempo desde a sua ultima aposta
                if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 415), (25, 118, 188), tolerance=5) \
                        or pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 415), (29, 139, 200), tolerance=5):
                    ## Genius Muito tempo desde a sua unlima aposta
                    pyautogui.mouseDown(x_origem + 490, y_origem + 415, button='left')
                    print("Genius Muito tempo desde a sua unlima apostar")
                    time.sleep(1)
                    pyautogui.mouseUp()
            else:
                if Limpa.limpa_pequeno(x_origem, y_origem) == "sair da conta":
                    return "sair da conta"
                if Limpa.limpa_promocao(x_origem, y_origem) == "sair da conta":
                    return "sair da conta"

            time.sleep(0.25)

        if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
            return "sair da conta"

        if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
            return "sair da conta"


def ajustar_valor(x_origem, y_origem, valor=200):
    Limpa.aviso_canto_lobby(x_origem, y_origem)  # fecha propaganda
    regiao = (304 + x_origem, 637 + y_origem, 88, 30)  # (x, y, largura, altura)
    imagem1 = r'Imagens\Genius\valor200.png'
    imagem2 = r'Imagens\Genius\valor2000.png'
    precisao = 0.9

    if valor == 200:

        for i in range(50):
            posicao = localizar_imagem(imagem1, regiao, precisao)
            if posicao is not None:  # Verifica se a imagem foi encontrada
                print("valor 200 escolhido no genius")
                return True
            else:
                if pyautogui.pixelMatchesColor((x_origem + 449), (y_origem + 622), (107, 98, 100), tolerance=5):
                    # testa se a lista esta fechada
                    pyautogui.click(x_origem + 449, y_origem + 654)  # clica na setinha para abrir a lista
                    time.sleep(0.8)
                    pyautogui.click(x_origem + 449, y_origem + 608)  # escolhe o valor 200
                elif (pyautogui.pixelMatchesColor((x_origem + 449), (y_origem + 622), (61, 55, 57), tolerance=5)
                      or pyautogui.pixelMatchesColor((x_origem + 449), (y_origem + 622), (61, 55, 57), tolerance=5)):
                    # testa se a lista esta aberta
                    pyautogui.click(x_origem + 449, y_origem + 608)  # escolhe o valor 200
            time.sleep(0.25)

    elif valor == 2000:

        for i in range(50):
            posicao = localizar_imagem(imagem2, regiao, precisao)
            if posicao is not None:  # Verifica se a imagem foi encontrada
                print("valor 2000 escolhido no genius")
                return True
            else:
                if pyautogui.pixelMatchesColor((x_origem + 449), (y_origem + 622), (107, 98, 100), tolerance=5):
                    # testa se a lista esta fechada
                    pyautogui.click(x_origem + 449, y_origem + 654)  # clica na setinha para abrir a lista
                    time.sleep(0.8)
                    pyautogui.click(x_origem + 449, y_origem + 568)  # escolhe o valor 2000
                elif (pyautogui.pixelMatchesColor((x_origem + 449), (y_origem + 622), (61, 55, 57), tolerance=5)
                      or pyautogui.pixelMatchesColor((x_origem + 449), (y_origem + 622), (61, 55, 57), tolerance=5)):
                    # testa se a lista esta aberta
                    pyautogui.click(x_origem + 449, y_origem + 568)  # escolhe o valor 2000
            time.sleep(0.25)
    return False


def genius_joga_vezes(x_origem, y_origem):
    regiao = (473 + x_origem, 101 + y_origem, 20, 32)  # (x, y, largura, altura)
    imagem1 = r'Imagens\Genius\tempo6.png'
    precisao = 0.9

    tarefas_fazer = ('Jogar no Casino Genius Pro 100 vezes',
                     'Jogar no Casino Genius Pro 50 vezes',
                     'Jogar no Casino Genius Pro 10 vezes')

    continua_jogando = True

    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
        return "sair da conta"

    abre_genius(x_origem, y_origem)
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

        genius_aberto = abre_genius(x_origem, y_origem)

        if genius_aberto:
            print('espera espera pelo valor de tempo certo')

            for i in range(80):
                # espera o time
                posicao = localizar_imagem(imagem1, regiao, precisao)
                if posicao is not None:  # Verifica se a imagem foi encontrada
                    print("Faz uma aposta aletoria ente Stace e David")
                    valor_aleatorio = random.choice([True, False])
                    if valor_aleatorio:
                        pyautogui.click(x_origem + 603, y_origem + 223)  # clica em Staci ganha
                        print('Stace')
                    else:
                        pyautogui.click(x_origem + 366, y_origem + 223)  # clica em David ganha
                        print('David')
                    print('Espera o tempo passar ate sair o premio')
                    time.sleep(10)
                    break
                time.sleep(0.3)

        Limpa.limpa_abre_tarefa(x_origem, y_origem)
        # Limpa.limpa_abre_tarefa2(x_origem, y_origem)
        Tarefas.recolher_tarefa(x_origem, y_origem)
        meta_atigida, pontos = Tarefas.meta_tarefas(x_origem, y_origem)

        continua_jogando, tarefa = Tarefas.comparar_listas_fazendo_tarefa(tarefas_fazer, x_origem, y_origem)  # procura com ocr

        if (not continua_jogando) or meta_atigida:
            time.sleep(0.5)

            # Limpa.limpa_abre_tarefa2(x_origem, y_origem)
            Limpa.limpa_abre_tarefa(x_origem, y_origem)
            continua_jogando, tarefa = Tarefas.comparar_listas_fazendo_tarefa(tarefas_fazer, x_origem, y_origem)  # procura com ocr
            meta_atigida, pontos = Tarefas.meta_tarefas(x_origem, y_origem)
            if (not continua_jogando) or meta_atigida:
                print("FIM")
                if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                    return "sair da conta"
                return

        Limpa.fecha_tarefa(x_origem, y_origem)  # fecha a lista de tarefas diarias
        abre_genius(x_origem, y_origem)
    return


def genius_joga_valor(x_origem, y_origem, lista_tarefas_disponivel):
    regiao = (473 + x_origem, 101 + y_origem, 20, 32)  # (x, y, largura, altura)
    imagem1 = r'Imagens\Genius\tempo6.png'
    precisao = 0.9

    tarefas_fazer = ('Ganhar 100.000 fichas no Casino Genius Pro',
                     'Ganhar 30.000 fichas no Casino Genius Pro',
                     'Ganhar 4.000 fichas no Casino Genius Pro')

    continua_jogando = False

    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
        return "sair da conta"

    for item in tarefas_fazer:
        if item in lista_tarefas_disponivel:
            print('comparar_listas_fazendo_tarefa', item)
            continua_jogando = True
            tarefa = item
            break

    if continua_jogando is False:
        return

    abre_genius(x_origem, y_origem)
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

        genius_aberto = abre_genius(x_origem, y_origem)

        if genius_aberto == True:
            print('espera espera pelo valor de tempo certo')
            for i in range(80):
                # espera o time
                posicao = localizar_imagem(imagem1, regiao, precisao)
                if posicao is not None:  # Verifica se a imagem foi encontrada
                    print("faz a aposta")
                    if tarefa == 'Ganhar 100.000 fichas no Casino Genius Pro':

                        # valor = 2000
                        # ajustar_valor(x_origem, y_origem, valor)
                        # pyautogui.click(x_origem + 370, y_origem + 223)  # 2000 lado esquedo
                        # time.sleep(0.25)
                        # pyautogui.click(x_origem + 370, y_origem + 223)  # 2000 lado esquedo
                        # time.sleep(0.25)
                        # pyautogui.click(x_origem + 370, y_origem + 223)  # 2000 lado esquedo
                        # time.sleep(0.15)
                        # pyautogui.moveTo(x_origem + 955, y_origem + 245)  # move o mouse
                        # time.sleep(0.15)
                        # pyautogui.click(x_origem + 603, y_origem + 223)  # 2000 lado direito
                        # time.sleep(0.25)
                        # pyautogui.click(x_origem + 603, y_origem + 223)  # 2000 lado direito
                        # time.sleep(0.25)
                        # pyautogui.click(x_origem + 603, y_origem + 223)  # 2000 lado direito
                        # time.sleep(0.25)

                        valor = 200
                        ajustar_valor(x_origem, y_origem, valor)
                        pyautogui.click(x_origem + 370, y_origem + 223)  # 200 lado esquedo
                        time.sleep(0.5)
                        pyautogui.moveTo(x_origem + 955, y_origem + 245)  # move o mouse
                        time.sleep(0.25)
                        pyautogui.click(x_origem + 603, y_origem + 223)  # 200 lado direito
                        time.sleep(0.25)
                        pyautogui.click(x_origem + 686, y_origem + 655)  # aperta no 8 vezes
                        time.sleep(0.5)
                        pyautogui.click(x_origem + 608, y_origem + 655)  # aperta no 4 vezes
                        time.sleep(0.01)

                    elif tarefa == 'Ganhar 30.000 fichas no Casino Genius Pro':

                        valor = 2000
                        ajustar_valor(x_origem, y_origem, valor)
                        pyautogui.click(x_origem + 370, y_origem + 223)  # 2000 lado esquedo
                        time.sleep(0.5)
                        pyautogui.moveTo(x_origem + 955, y_origem + 245)  # move o mouse
                        time.sleep(0.25)
                        pyautogui.click(x_origem + 603, y_origem + 223)  # 2000 lado direito
                        time.sleep(0.5)
                        pyautogui.click(x_origem + 686, y_origem + 655)  # aperta no 8 vezes
                        time.sleep(0.01)

                    elif tarefa == 'Ganhar 4.000 fichas no Casino Genius Pro':

                        valor = 200
                        ajustar_valor(x_origem, y_origem, valor)
                        pyautogui.click(x_origem + 370, y_origem + 223)  # 200 lado esquedo
                        time.sleep(0.5)
                        pyautogui.moveTo(x_origem + 955, y_origem + 245)  # move o mouse
                        time.sleep(0.25)
                        pyautogui.click(x_origem + 603, y_origem + 223)  # 200 lado direito
                        time.sleep(0.25)
                        valor = 2000
                        ajustar_valor(x_origem, y_origem, valor)
                        pyautogui.click(x_origem + 370, y_origem + 223)  # 2000 lado esquedo
                        time.sleep(0.5)
                        pyautogui.moveTo(x_origem + 955, y_origem + 245)  # move o mouse
                        time.sleep(0.25)
                        pyautogui.click(x_origem + 603, y_origem + 223)  # 2000 lado direito
                        time.sleep(0.01)

                    print('espera o tempo passar ate sair o premio')
                    time.sleep(10)
                    break
                time.sleep(0.3)

        Limpa.limpa_abre_tarefa(x_origem, y_origem)
        # Limpa.limpa_abre_tarefa2(x_origem, y_origem)
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
        abre_genius(x_origem, y_origem)
    return

# def genius_joga_vezes_upando(x_origem, y_origem):
#     abre_genius(x_origem, y_origem)
#     continua_jogando = True
#     regiao = (473 + x_origem, 101 + y_origem, 20, 32)  # (x, y, largura, altura)
#     imagem1 = r'Imagens\Genius\tempo6.png'
#     precisao = 0.9
#
#     while continua_jogando:  # permanece joghando cartas premiadas ate nao ter mais a mição jogar x vezes
#
#         genius_aberto = abre_genius(x_origem, y_origem)
#
#         if genius_aberto:
#             print('espera espera pelo valor de tempo certo')
#
#             for i in range(80):
#                 # espera o time
#                 posicao = localizar_imagem(imagem1, regiao, precisao)
#                 if posicao is not None:  # Verifica se a imagem foi encontrada
#                     print("faz a aposta")
#                     if pyautogui.pixelMatchesColor((x_origem + 449), (y_origem + 655), (193, 119, 70), tolerance=5):
#                         # Testa se tem uma setinha para cima
#                         print("Faz uma aposta aletoria ente Stace e David")
#                         valor_aleatorio = random.choice([True, False])
#                         if valor_aleatorio:
#                             pyautogui.click(x_origem + 603, y_origem + 223)  # clica em Staci ganha
#                             print('Stace')
#                         else:
#                             pyautogui.click(x_origem + 366, y_origem + 223)  # clica em David ganha
#                             print('David')
#                         print('Espera o tempo passar ate sair o premio')
#
#                     else:
#                         for i in range(5):
#                             pyautogui.click(x_origem + 603, y_origem + 223)  # clica em Staci ganha
#                             time.sleep(0.1)
#
#                     time.sleep(10)
#                     break
#
#                 time.sleep(0.3)
#
#             status_tarefa = Tarefas.recolher_tarefa_upando(x_origem, y_origem)
#             print(status_tarefa)
#             if status_tarefa == "Não tem missão":
#                 continua_jogando = True
#             elif status_tarefa == "Recolhido":
#                 continua_jogando = False
#             else:
#                 continua_jogando = False
#
#             if not continua_jogando:
#                 print("FIM")
#                 if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
#                     return "sair da conta"
#                 return
#     return

# x_origem, y_origem = Origem_pg.x_y()
# genius_joga_vezes_upando(x_origem, y_origem)
# genius_joga_valor(x_origem, y_origem)
# genius_joga_vezes(x_origem, y_origem)
