import datetime
import time

import pyautogui

import Aneis
import HoraT
import Limpa
import OCR_tela
from F5_navegador import atualizar_navegador
from Horario_atual import dia_semana

# Desabilitar o fail-safe
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0

posicao_recolher_presentes = (215, 400, 585, 770)

# import Origem_pg
# from fuzzywuzzy import fuzz #pip install fuzzywuzzy
# import Levenshtein #pip install python-Levenshtein

dicionario_tarefas_fazer = {
    # caça-níquel da mesa
    'Jogar o caca-niquel da mesa 150 vezes': 30,
    'Gioca alla Slot machine al tavolo 150 volte': 30,
    'Gioca alla Slot machine al tavolo 120 volte': 30,
    'Jogar o caca-niquel da mesa 70 vezes': 20,
    'Gioca alla Slot machine al tavolo 70 volte': 20,
    'Gioca alla Slot machine al tavolo 50 volte': 20,
    'Jogar o caca-niquel da mesa 10 vezes': 10,
    'Gioca alla Slot machine al tavolo 10 volte': 10,
    # Casino Genius
    'Jogar no Casino Genius Pro 100 vezes': 30,
    'Gioca la Carta Genio del Casino per 100 volte': 30,
    'Jogar no Casino Genius Pro 50 vezes': 20,
    'Gioca la Carta Genio del Casino per 50 volte': 20,
    'Jogar no Casino Genius Pro 10 vezes': 10,
    'Gioca la Carta Genio del Casino per 10 volte': 10,
    'Ganhar 100.000 fichas no Casino Genius Pro': 30,
    'Vinci 100.000 fiches con la Carta Genio del Casino': 30,
    'Ganhar 30.000 fichas no Casino Genius Pro': 20,
    'Vinci 30.000 fiches con la Carta Genio del Casino': 20,
    'Ganhar 4.000 fichas no Casino Genius Pro': 10,
    'Vinci 4.000 fiches con la Carta Genio del Casino': 10,
    # Cartas Premiadas
    'Jogar 100 vezes nas Cartas Premiadas': 30,
    'Gioca la Carta Scommessa per 100 volte': 30,
    'Jogar 50 vezes nas Cartas Premiadas': 20,
    'Gioca la Carta Scommessa per 50 volte': 20,
    'Jogar 10 vezes nas Cartas Premiadas': 10,
    'Gioca la Carta Scommessa per 10 volte': 10,
    'Ganhar 100.000 fichas nas Cartas Premiadas': 30,
    'Ganhar 30.000 fichas nas Cartas Premiadas': 20,
    'Ganhar 4.000 fichas nas Cartas Premiadas': 10,
    # Poker Slot
    'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 150 vezes': 30,
    'Scommetti 20 o piu su 9 linee della Poker Slot per 150 volte': 30,
    'Scommetti 20 o piu su 9 linee della Poker Slot per 120 volte': 30,
    'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 70 vezes': 20,
    'Scommetti 20 o piu su 9 linee della Poker Slot per 70 volte': 20,
    'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 10 vezes': 10,
    'Scommetti 20 o piu su 9 linee della Poker Slot per 10 volte': 10,
    # Tarefa de mesa
    'Jogar 40 maos em uma mesa com blinds acima de 100': 30,
    'Gioca 40 mani su un tavolo con bui maggiori di 100': 30,
    'Jogar 40 maos em uma mesa com blinds acima de 50': 30,
    'Gioca 40 mani su un tavolo con bui maggiori di 50': 30,
    'Jogar 20 maos em uma mesa com blinds acima de 100': 20,
    'Gioca 20 mani su un tavolo con bui maggiori di 100': 20,
    'Jogar 20 maos em uma mesa com blinds acima de 50': 20,
    'Gioca 20 mani su un tavolo con bui maggiori di 50': 20,
    'Jogar 20 maos em uma mesa com blinds acima de 25': 20,
    'Gioca 20 mani su un tavolo con bui maggiori di 25': 20,
    'Jogar 10 maos em qualquer mesa': 10,
    'Gioca 10 mani su un tavolo qualsiasi': 10,
    'Jogar 5 maos em qualquer mesa': 10,
    'Gioca 5 mani su un tavolo qualsiasi': 10,
}

dicionario_tarefas_fazer_sabado = {
    # caça-níquel da mesa
    'Jogar o caca-niquel da mesa 150 vezes': 30,
    'Gioca alla Slot machine al tavolo 150 volte': 30,
    'Gioca alla Slot machine al tavolo 120 volte': 30,
    'Jogar o caca-niquel da mesa 70 vezes': 20,
    'Gioca alla Slot machine al tavolo 70 volte': 20,
    'Gioca alla Slot machine al tavolo 50 volte': 20,
    'Jogar o caca-niquel da mesa 10 vezes': 10,
    'Gioca alla Slot machine al tavolo 10 volte': 10,
    'Ganhar 100.000 fichas no caca niquel da mesa': 30,
    'Vinci 100.000 fiches alla Slot machine al tavolo': 30,
    'Vinci 50.000 fiches alla Slot machine al tavolo': 30,
    'Ganhar 30.000 fichas no caca niquel da mesa': 20,
    'Vinci 30.000 fiches alla Slot machine al tavolo': 20,
    'Ganhar 10.000 fichas no caca niquel da mesa': 10,
    'Vinci 10.000 fiches alla Slot machine al tavolo': 20,
    'Vinci 2.000 fiches alla Slot machine al tavolo': 10,
    # Casino Genius
    'Jogar no Casino Genius Pro 100 vezes': 30,
    'Gioca la Carta Genio del Casino per 100 volte': 30,
    'Jogar no Casino Genius Pro 50 vezes': 20,
    'Gioca la Carta Genio del Casino per 50 volte': 20,
    'Jogar no Casino Genius Pro 10 vezes': 10,
    'Gioca la Carta Genio del Casino per 10 volte': 10,
    'Ganhar 100.000 fichas no Casino Genius Pro': 30,
    'Vinci 100.000 fiches con la Carta Genio del Casino': 30,
    'Ganhar 30.000 fichas no Casino Genius Pro': 20,
    'Vinci 30.000 fiches con la Carta Genio del Casino': 20,
    'Ganhar 4.000 fichas no Casino Genius Pro': 10,
    'Vinci 4.000 fiches con la Carta Genio del Casino': 10,
    # Cartas Premiadas
    'Jogar 100 vezes nas Cartas Premiadas': 30,
    'Gioca la Carta Scommessa per 100 volte': 30,
    'Jogar 50 vezes nas Cartas Premiadas': 20,
    'Gioca la Carta Scommessa per 50 volte': 20,
    'Jogar 10 vezes nas Cartas Premiadas': 10,
    'Gioca la Carta Scommessa per 10 volte': 10,
    'Ganhar 100.000 fichas nas Cartas Premiadas': 30,
    'Ganhar 30.000 fichas nas Cartas Premiadas': 20,
    'Ganhar 4.000 fichas nas Cartas Premiadas': 10,
    # Poker Slot
    'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 150 vezes': 30,
    'Scommetti 20 o piu su 9 linee della Poker Slot per 150 volte': 30,
    'Scommetti 20 o piu su 9 linee della Poker Slot per 120 volte': 30,
    'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 70 vezes': 20,
    'Scommetti 20 o piu su 9 linee della Poker Slot per 70 volte': 20,
    'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 10 vezes': 10,
    'Scommetti 20 o piu su 9 linee della Poker Slot per 10 volte': 10,
    'Ganhar 100.000 fichas no caca niquel Slot Poker': 30,
    'Vinci 100.000 fiches alla Poker Slot': 30,
    'Ganhar 30.000 fichas no caca niquel Slot Poker': 20,
    'Vinci 30.000 fiches alla Poker Slot': 20,
    'Ganhar 10.000 fichas no caca niquel Slot Poker': 10,
    'Vinci 10.000 fiches alla Poker Slot': 10,
    'Vinci 4.000 fiches alla Poker Slot': 10,
    'Vinci 2.000 fiches alla Poker Slot': 10,
    # Tarefa de mesa
    'Jogar 40 maos em uma mesa com blinds acima de 100': 30,
    'Gioca 40 mani su un tavolo con bui maggiori di 100': 30,
    'Jogar 40 maos em uma mesa com blinds acima de 50': 30,
    'Gioca 40 mani su un tavolo con bui maggiori di 50': 30,
    'Jogar 20 maos em uma mesa com blinds acima de 100': 20,
    'Gioca 20 mani su un tavolo con bui maggiori di 100': 20,
    'Jogar 20 maos em uma mesa com blinds acima de 50': 20,
    'Gioca 20 mani su un tavolo con bui maggiori di 50': 20,
    'Jogar 20 maos em uma mesa com blinds acima de 25': 20,
    'Gioca 20 mani su un tavolo con bui maggiori di 25': 20,
    'Jogar 10 maos em qualquer mesa': 10,
    'Gioca 10 mani su un tavolo qualsiasi': 10,
    'Jogar 5 maos em qualquer mesa': 10,
    'Gioca 5 mani su un tavolo qualsiasi': 10,
}


def comparar_listas(x_origem, y_origem, dia_da_semana):
    lista = OCR_tela.tarefas_diarias(x_origem, y_origem)
    lista_do_dia = []

    pontos_disponiveis = 0
    if dia_da_semana == 5:
        for chave in dicionario_tarefas_fazer_sabado:
            if chave in lista:
                pontos_disponiveis += dicionario_tarefas_fazer_sabado[chave]
                lista_do_dia.append(chave)
    else:
        for chave in dicionario_tarefas_fazer:
            if chave in lista:
                pontos_disponiveis += dicionario_tarefas_fazer[chave]
                lista_do_dia.append(chave)

    print(lista_do_dia)
    print("Pontos disponiveis para serem feritos: ", pontos_disponiveis)

    return lista_do_dia, pontos_disponiveis


def comparar_listas_fazendo_tarefa(tarefas_fazer, x_origem, y_origem):
    continua_jogando = False
    # print('tarefas_fazer', tarefas_fazer)
    lista_tarefas_disponivel, tarefa_extra = OCR_tela.tarefas_diaris_posicao1(x_origem, y_origem)
    print('lista_tarefas_disponivel', lista_tarefas_disponivel)
    for chave in tarefas_fazer:
        if chave in lista_tarefas_disponivel:
            print('comparar_listas_fazendo_tarefa: ', chave)
            continua_jogando = True
            return continua_jogando, chave

    lista_tarefas_disponivel = OCR_tela.tarefas_diaris_posicao2(x_origem, y_origem, tarefa_extra)

    for chave in tarefas_fazer:
        if chave in lista_tarefas_disponivel:
            print('comparar_listas_fazendo_tarefa: ', chave)
            continua_jogando = True
            return continua_jogando, chave

    return continua_jogando, None


def recolher_tarefa(x_origem, y_origem):
    posicao_recolher_tarefa_y = (542, 463, 384, 305)

    for i in range(10):
        print("recolher_tarefa", i)
        clique_recolher = []

        if pyautogui.pixelMatchesColor((x_origem + 670), (y_origem + 305), (48, 154, 17), tolerance=40):
            # testa se tem que recolher "verde" apartir da primeira linha
            print("Tem missão para recolher")
            for recolher_y in posicao_recolher_tarefa_y:
                # print(recolher_y)
                if pyautogui.pixelMatchesColor((x_origem + 670), (y_origem + recolher_y), (48, 154, 17), tolerance=40):
                    # testa se tem que recolher "verde" (48, 154, 17)
                    clique_recolher.append(recolher_y)  # adiciona as coordenada de y que deve ser clicadas

        elif pyautogui.pixelMatchesColor((x_origem + 590), (y_origem + 280), (171, 13, 143), tolerance=40):
            # testa se tem que recolher tendo missão extra
            print('Missão extra')
            if pyautogui.pixelMatchesColor((x_origem + 670), (y_origem + 384), (48, 154, 17), tolerance=40):
                # testa se tem que recolher "verde" apartir da segunda linha
                print("Tem missão para recolher")
                for recolher_y in posicao_recolher_tarefa_y:
                    # print(recolher_y)
                    if pyautogui.pixelMatchesColor((x_origem + 670), (y_origem + recolher_y), (48, 154, 17), tolerance=40):
                        # testa se tem que recolher "verde"
                        clique_recolher.append(recolher_y)  # adiciona as coordenada de y que deve ser clicadas
            else:
                print('Não foi encontrado missão para recolher')
                return

        else:
            print('Não foi encontrado missão para recolher')
            return

        if len(clique_recolher) > 0:
            for recolhe in clique_recolher:
                pyautogui.doubleClick(x_origem + 670, y_origem + recolhe)  # clica no recolher
                pyautogui.click(x_origem + 670, y_origem + recolhe)
            time.sleep(1)
    return


def meta_tarefas(x_origem, y_origem):
    pyautogui.doubleClick(x_origem + 635, y_origem + 25)  # clica no tarefas diarias
    # chma a funçao para ver a pontuação acumilada nas tarefas
    pontuacao_tarefas = int(OCR_tela.pontuacao_tarefas(x_origem, y_origem))

    # Obter o dia da semana (0 segunda, 1 terça, 2 quarta, 3 quinta, 4 sexta, 5 sabado, 6 domingo)
    dia_da_semana = dia_semana()

    # dicionarios com os dias da semana e com os valores de meta de cada dia
    metas = {0: 150, 1: 160, 2: 170, 3: 180, 4: 190, 5: 200, 6: 140}
    # busca os objetivos basenado no dia da semana
    meta_dia = metas[dia_da_semana]
    # compara a pontuação atual com o objetivo do dia para saber se foi batido ou nao
    print("meta do dia:", meta_dia, ",pontos atigidos:", pontuacao_tarefas)
    # dicionarios com os dias da semana e com os valores de meta de cada dia
    if pontuacao_tarefas >= meta_dia:
        print("Meta atingida")
        return True, pontuacao_tarefas
    else:
        print('Meta não atingida')
        return False, pontuacao_tarefas


def tem_tarefa_para_recolher(x_origem, y_origem):
    if pyautogui.pixelMatchesColor((x_origem + 627), (y_origem + 35), (228, 194, 31), tolerance=30):
        # testa se tem que recolher icone das tarefas amarelo
        Limpa.limpa_abre_tarefa(x_origem, y_origem)
        recolher_tarefa(x_origem, y_origem)
        Limpa.limpa_abre_tarefa(x_origem, y_origem)
        meta, pontos = meta_tarefas(x_origem, y_origem)
        return meta, pontos
    else:
        return False, 0


def testa_continuar_fazendo_tarefa(x_origem, y_origem, dia_da_semana):
    parar_tarefas = False
    hora_fim_tarefa = False
    lista_tarefas_fazer = []
    pontuacao_tarefas = 0
    pontos_disponiveis = 0
    meta_atingida = False
    valor_fichas = 0
    conta_upada = False

    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
        parar_tarefas = True
        return parar_tarefas, valor_fichas, pontuacao_tarefas, lista_tarefas_fazer, hora_fim_tarefa

    valor_fichas = OCR_tela.valor_fichas(x_origem, y_origem)
    Aneis.recolhe_aneis(x_origem, y_origem)
    conta_upada = Limpa.limpa_abre_tarefa(x_origem, y_origem)  # retorna se a conta ta upada ou nao
    if conta_upada:
        recolher_tarefa(x_origem, y_origem)  # recolhe se tiver alguma tarefa batida
        Limpa.limpa_abre_tarefa(x_origem, y_origem)  # retorna se a conta ta upada ou nao
        OCR_tela.tarefas_diaris_trocar(x_origem, y_origem)
        Limpa.limpa_abre_tarefa(x_origem, y_origem)
        meta_atingida, pontuacao_tarefas = meta_tarefas(x_origem, y_origem)
        lista_tarefas_fazer, pontos_disponiveis = comparar_listas(x_origem, y_origem, dia_da_semana)

    print('__________________________________________________________________')
    print("Valor fichas :", valor_fichas)
    print('Numero de tarefas disponiveis: ', len(lista_tarefas_fazer))
    print('lista de tarefas para se fazer: ', lista_tarefas_fazer)
    print('Pontuação tarefas:', pontuacao_tarefas)
    print('Pontos disponiveis :', pontos_disponiveis)
    print("Meta atigida :", meta_atingida)
    print("Conta upada: ", conta_upada)
    print('__________________________________________________________________')

    if HoraT.fim_tempo_tarefa():
        Limpa.limpa_total(x_origem, y_origem)
        print('Fim do horario destinado a tarefas')
        hora_fim_tarefa = True
        parar_tarefas = True
    elif conta_upada is False:
        print('Conta não esta upada')
        parar_tarefas = True
    elif Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
        print('Ja esta logado')
        parar_tarefas = True
    elif valor_fichas < 5000:  # se a conta tem menos de 110K vai para a proxima
        print('Quantidade de fichas insuficiente para jogar')
        parar_tarefas = True
    elif not lista_tarefas_fazer:
        print("Lista de trarefas vazia")
        parar_tarefas = True
    elif meta_atingida:
        print("Meta do dia atigida")
        parar_tarefas = True
    elif dia_da_semana == 5:  # testa se é sabado ultimo dia das tarefas
        print('Ultimo dia das tarefas, continua somente se for possivel atigir 150 ou 200 pontos')
        print('pontuacao_tarefas + pontos_disponiveis :', pontuacao_tarefas + pontos_disponiveis)

        if ((pontuacao_tarefas + pontos_disponiveis) < 150) and (pontuacao_tarefas < 150):
            print(
                '\n\nA soma dos pontos disponiveis e os pontos feitos não atigem 150, o máximo que pode atingir é: ',
                pontuacao_tarefas + pontos_disponiveis)
            parar_tarefas = True
        if ((pontuacao_tarefas + pontos_disponiveis) < 200) and (pontuacao_tarefas >= 150):
            print(
                '\n\nA soma dos pontos disponiveis e os pontos feitos não atigem 200, o máximo que pode atingir é: ',
                pontuacao_tarefas + pontos_disponiveis)
            parar_tarefas = True

    return parar_tarefas, valor_fichas, pontuacao_tarefas, lista_tarefas_fazer, hora_fim_tarefa


def recolher_tarefa_upando(x_origem, y_origem):
    posicao_recolher_tarefa_y = (361, 457, 553)
    print('recolher_tarefa_upando')
    status_tarefas = "Não tem missão"
    # print("recolher_tarefa_upando")
    if (pyautogui.pixelMatchesColor((x_origem + 627), (y_origem + 35), (228, 194, 31), tolerance=5)
            and not pyautogui.pixelMatchesColor((x_origem + 627), (y_origem + 35), (119, 168, 219), tolerance=5)):
        # testa se tem que recolher icone das tarefas amarelo
        print('Tem missão para recolher, aguarda um tempo pequeno')
        status_tarefas = "Recolhido"
        time.sleep(4)

        for i in range(8):
            pyautogui.doubleClick(x_origem + 635, y_origem + 25)  # clica no tarefas diarias para abrir
            print('Click para abrir o tarefas')
            time.sleep(0.5)

            if (pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 118), (73, 71, 76), tolerance=20)
                    or pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 118), (22, 21, 23), tolerance=20)):
                # testa se ja abriu a janela bora cinza da janela
                print('Tarefas abertas')
                time.sleep(0.5)

                if pyautogui.pixelMatchesColor((x_origem + 495), (y_origem + 125), (0, 51, 248), tolerance=10):
                    # testa se esta aberto a lista de tarefas
                    print('Tarefas abertas, conta sem Upar')
                    time.sleep(3)

                    clique_recolher = []

                    for recolher_y in posicao_recolher_tarefa_y:
                        if (pyautogui.pixelMatchesColor((x_origem + 767), (y_origem + recolher_y), (240, 249, 240), tolerance=25)
                                or pyautogui.pixelMatchesColor((x_origem + 722), (y_origem + recolher_y), (34, 170, 33), tolerance=25)):
                            # testa se tem "Retirar" em braco ou se a tela ta verde
                            clique_recolher.append(recolher_y)  # adiciona as coordenada de y que deve ser clicadas

                    if len(clique_recolher) > 0:
                        for recolhe in clique_recolher:
                            pyautogui.click(x_origem + 767, y_origem + recolhe)  # clica no recolher
                        print("Recoulheu as missões")
                        time.sleep(3)
                    else:
                        print('Não conseguiu reconhecer o recolhecer escrito em branco')

                    for recolhe in posicao_recolher_presentes:
                        pyautogui.click(x_origem + recolhe, y_origem + 246)  # clica nos presentes
                    print('Cricou no presentes')
                    time.sleep(2)

                    if (not pyautogui.pixelMatchesColor((x_origem + 627), (y_origem + 35), (228, 194, 31), tolerance=5)
                            and pyautogui.pixelMatchesColor((x_origem + 627), (y_origem + 35), (119, 168, 219), tolerance=5)):
                        # testa se NÂO tem que recolher icone das tarefas amarelo
                        pyautogui.click(821 + x_origem, 138 + y_origem)  # fecha tarefa
                        status_tarefas = "Recolhido"
                        time.sleep(1)
                        break
                else:
                    print('Tarefas abertas, conta Upada limpa tarefa...')
                    conta_upada = Limpa.limpa_abre_tarefa(x_origem, y_origem, com_pausa=False)  # retorna se a conta ta upada ou nao
                    if conta_upada:
                        print('Tarefas abertas, conta Upada')
                        recolher_tarefa(x_origem, y_origem)  # recolhe se tiver alguma tarefa batida
                    pyautogui.click(821 + x_origem, 138 + y_origem)  # fecha tarefa
                    time.sleep(1)
                    status_tarefas = "Recolhido"
                    break

        if (pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 118), (73, 71, 76), tolerance=20)
                or pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 118), (22, 21, 23), tolerance=20)):
            # testa se ja abriu a janela borda cinza da janela
            # testa se nao fechou a janela

            # pyautogui.press('f5')
            print('espera 30 segundos clica no atualizar')
            atualizar_navegador()
            time.sleep(30)
            Limpa.limpa_total(x_origem, y_origem)

        return status_tarefas

    else:
        # print(status_tarefas)
        # pyautogui.click(821 + x_origem, 138 + y_origem)  # fecha tarefa
        return status_tarefas
#
# #

# recolher_tarefa(1, 128)
# recolher_tarefa_upando(x_origem, y_origem)
#
# comparar_listas(x_origem, y_origem)

# tarefas_fazer_vezes2 = ('Jogar 100 vezes nas Cartas Premiadas',
#                            'Jogar 50 vezes nas Cartas Premiadas',
#                            'Jogar 10 vezes nas Cartas Premiadas')
# # tarefas_fazer2 = ('Jogar o caca-niquel da mesa 150 vezes', 'Jogar o caca-niquel da mesa 70 vezes', 'Jogar o caca-niquel da mesa 10 vezes')
# continua_jogando, tarefa = comparar_imagens_tarefa(tarefas_fazer_vezes2, x_origem, y_origem)
# print(tarefa)
# # # # #meta_tarefas(x_origem, y_origem)
# # # #
# # # #
# # # #
# # # # # recolher_tarefa(x_origem, y_origem)
# # # meta_tarefas(x_origem, y_origem)
# # # # x_origem, y_origem = Origem_pg.x_y()
# # # # # # # # Comparar as listas e obter os itens em comum
# comparar_listas(x_origem, y_origem)


# # # # # #
# # # itens_comuns= comparar_imagens(tarefas_fazer, x_origem, y_origem)
# # # print("Itens em comum:")
# # # print(itens_comuns)
# # for item in itens_comuns:
# #     print(item)
