import pyautogui

import Limpa
from Firebase import confirmacao_comando_resposta, comando_escravo, comando_coleetivo_escravo_escravo, confirmacao_escravo
from Mesa import blinb_rolagem, levantar_mesa, apostar_pagar, passa_corre_joga


def mesa_recolher(x_origem, y_origem, numero_jogadas=2, blind='2K/4K', sorte=True):
    print('mesa_recolher')
    print(sorte)

    sentou = False
    continua_jogando = True
    jogou_uma_vez = False
    apostar = False
    cont_jogou = 0
    status_comando = 'Iniciado o recolhimento'
    humano = False
    status_comando_anterior = None
    recebido1 = "padrao"
    recebido2 = "padrao"

    if not sorte:
        apostar = True

    cont_limpa_jogando = 0

    valor_aposta1, valor_aposta2 = list(blinb_rolagem[blind])[-2:]
    print('Valores das apostas')
    print(valor_aposta1, valor_aposta2)

    while continua_jogando:  # permanece joghando

        if status_comando_anterior != status_comando:
            confirmacao_comando_resposta(status_comando)
            status_comando_anterior = status_comando

        recebido1 = str(comando_escravo())
        if recebido1 != recebido2:
            recebido2 = recebido1
            comando = recebido1.strip().title()  # remove espaços vasiao e coloca a primeira letra amiusculo
            print('comando :', comando)

        if comando == 'Levanta':
            levantar_mesa(x_origem, y_origem)
            Limpa.limpa_jogando(x_origem, y_origem)
            confirmacao_escravo('Levantou')
            # Firebase.comando_coleetivo_escravo_escravo("Levanta")
            return
        elif comando == 'Limpa':
            Limpa.limpa_jogando(x_origem, y_origem)
            Limpa.limpa_total(x_origem, y_origem)
            Limpa.limpa_jogando(x_origem, y_origem)
            return
        elif comando == 'Aposta':
            apostar = True
            cont_jogou = numero_jogadas
        elif comando == "Senta3":
            status_comando = 'Vai correr'
            sorte = False
            apostar = True

        if cont_limpa_jogando > 20:
            cont_limpa_jogando = 0
            Limpa.fecha_tarefa(x_origem, y_origem)
            Limpa.limpa_jogando(x_origem, y_origem)
        cont_limpa_jogando += 1

        if jogou_uma_vez:
            if pyautogui.pixelMatchesColor((x_origem + 663), (y_origem + 538), (86, 169, 68), tolerance=20):
                # testa se apareceu as mensagens verdes na parte de baixo
                jogou_uma_vez = False
                cont_jogou += 1
                print("Jogou vezes igua a: ", cont_jogou)
                status_comando = 'Jogada: ' + str(cont_jogou)

                if cont_jogou == numero_jogadas:
                    apostar = True
                    status_comando = 'Hora de apostar'

                if apostar and cont_jogou > numero_jogadas:
                    apostar = False
                    status_comando = 'Hora de jogar sem apostar'

                if cont_jogou >= numero_jogadas + 3:
                    print('Fim do recolher')
                    comando_coleetivo_escravo_escravo("Levanta")
                    levantar_mesa(x_origem, y_origem)
                    Limpa.limpa_jogando(x_origem, y_origem)
                    return

        if apostar:
            jogou = apostar_pagar(x_origem, y_origem, sorte)
            if jogou:
                jogou_uma_vez = True
        else:
            (jogou, apostar) = passa_corre_joga(x_origem, y_origem, valor_aposta1, valor_aposta2)
            if apostar:
                cont_jogou = numero_jogadas + 1
            if jogou:
                jogou_uma_vez = True

    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
        return "sair da conta"

    levantar_mesa(x_origem, y_origem)
    Limpa.limpa_jogando(x_origem, y_origem)
    return
