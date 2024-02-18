import datetime
import random
import socket
import time

import pyautogui

# Desabilitar o fail-safe
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0
import Limpa
import OCR_tela
import IP
import Tarefas
import HoraT
import xp2
from UparAuto import upar

# import Firebase
# from Firebase import confirmacao_comando_resposta, comando_escravo, comando_coleetivo_escravo_escravo

nome_computador = socket.gethostname()

indice_inicial = 0

blinb_rolagem = {
    '1/2': (534, 478, 2, 4), '2/4': (534, 504, 4, 8), '5/10': (534, 530, 10, 20), '10/20': (534, 556, 20, 40), '20/40': (534, 582, 40, 80),
    '25/50': (548, 478, 50, 100), '50/100': (548, 504, 100, 200), '100/200': (548, 530, 200, 400), '200/400': (548, 556, 400, 800),
    '500/1K': (548, 582, 1000, 2000), '1K/2K': (563, 478, 2000, 4000), '2K/4K': (563, 504, 4000, 8000), '5K/10K': (563, 530, 10000, 20000),
    '10K/20K': (563, 556, 20000, 40000), '20K/40K': (563, 582, 40000, 80000), '50K/100K': (571, 530, 100000, 200000),
    '100K/200K': (571, 556, 200000, 400000), '500K/1M': (571, 582, 1000000, 2000000)
}

lista_salas_niquel = [
    # 5 lugares
    {'1025': ('2040', 80, 40)}, {'1026': ('2040', 80, 40)}, {'1027': ('2040', 80, 40)}, {'1028': ('2040', 80, 40)}, {'1236': ('2040', 80, 40)},
    {'1266': ('2040', 80, 40)}, {'1645': ('2040', 80, 40)}, {'1646': ('2040', 80, 40)}, {'1647': ('2040', 80, 40)}, {'1648': ('2040', 80, 40)},
    {'1649': ('2040', 80, 40)}, {'1650': ('2040', 80, 40)}, {'1651': ('2040', 80, 40)}, {'1652': ('2040', 80, 40)},
    # 3 lugares
    {'435': ('2040', 80, 40)}, {'1540': ('2040', 80, 40)}, {'1541': ('2040', 80, 40)}, {'1542': ('2040', 80, 40)}, {'1543': ('2040', 80, 40)},
    {'1767': ('2040', 80, 40)}, {'1768': ('2040', 80, 40)}, {'1769': ('2040', 80, 40)},
    # 2 lugares
    {'1535': ('2040', 80, 40)}, {'1536': ('2040', 80, 40)}, {'1537': ('2040', 80, 40)}, {'1538': ('2040', 80, 40)},
    # nao sei
    {'1546': ('2040', 80, 40)}, {'1765': ('2040', 80, 40)}, {'1766': ('2040', 80, 40)}, {'1545': ('2040', 80, 40)}
]

# lista_salas_jogar = [{'12': ('12', 2, 4)}, {'296': ('12', 2, 4)}, {'4': ('12', 2, 4)}, {'297': ('12', 2, 4)},
#                      {'295': ('12', 2, 4)}, {'294': ('12', 2, 4)}, {'293': ('12', 2, 4)},
#                      {'52': ('24', 4, 8)},
#                      {'1537': ('2040', 80, 40)}, {'1538': ('2040', 80, 40)}, {'1546': ('2040', 80, 40)},
#                      {'1542': ('2040', 80, 40)}, {'1545': ('2040', 80, 40)}, {'1543': ('2040', 80, 40)},
#                      {'1542': ('2040', 80, 40)}, {'1541': ('2040', 80, 40)}, {'1540': ('2040', 80, 40)},
#                      {'1538': ('2040', 80, 40)}, {'1536': ('2040', 80, 40)}, {'1535': ('2040', 80, 40)},
#                      {'1769': ('2040', 80, 40)}, {'1768': ('2040', 80, 40)}, {'1767': ('2040', 80, 40)},
#                      {'1766': ('2040', 80, 40)}, {'1765': ('2040', 80, 40)}]

# lista_salas_jogar = [{'435': ('2040', 80, 40)}, {'1027': ('2040', 80, 40)}, {'1028': ('2040', 80, 40)}, {'1236': ('2040', 80, 40)},
#                       {'1535': ('2040', 80, 40)}, {'1536': ('2040', 80, 40)}, {'1537': ('2040', 80, 40)}, {'1537': ('2040', 80, 40)},
#                       {'1538': ('2040', 80, 40)}, {'1538': ('2040', 80, 40)}, {'1540': ('2040', 80, 40)}, {'1541': ('2040', 80, 40)},
#                       {'1542': ('2040', 80, 40)}, {'1543': ('2040', 80, 40)}, {'1545': ('2040', 80, 40)}, {'1546': ('2040', 80, 40)},
#                       {'1648': ('2040', 80, 40)}, {'1649': ('2040', 80, 40)}, {'1650': ('2040', 80, 40)}, {'1651': ('2040', 80, 40)},
#                       {'1652': ('2040', 80, 40)}, {'1765': ('2040', 80, 40)}, {'1766': ('2040', 80, 40)}, {'1767': ('2040', 80, 40)},
#                       {'1768': ('2040', 80, 40)}, {'1769': ('2040', 80, 40)}]


lista_salas_jogar = [
    {'134': ('2550', 100, 50)}, {'135': ('2550', 100, 50)}, {'999': ('2550', 100, 50)}, {'1003': ('2550', 100, 50)}, {'1004': ('2550', 100, 50)},
    {'1243': ('2550', 100, 50)}, {'1245': ('2550', 100, 50)}, {'1246': ('2550', 100, 50)}, {'1247': ('2550', 100, 50)}, {'1673': ('2550', 100, 50)},
    {'1674': ('2550', 100, 50)}, {'1675': ('2550', 100, 50)}, {'1676': ('2550', 100, 50)}, {'1677': ('2550', 100, 50)}, {'1678': ('2550', 100, 50)}
]

lista_salas_jogar2 = [
    {'1586': ('50100', 200, 100)}, {'1587': ('50100', 200, 100)}, {'1588': ('50100', 200, 100)}, {'1589': ('50100', 200, 100)},
    {'1590': ('50100', 200, 100)}, {'1591': ('50100', 200, 100)}, {'1592': ('50100', 200, 100)}, {'1593': ('50100', 200, 100)},
    {'1683': ('50100', 200, 100)}, {'1684': ('50100', 200, 100)}, {'1685': ('50100', 200, 100)}, {'1686': ('50100', 200, 100)},
    {'1687': ('50100', 200, 100)}, {'1688': ('50100', 200, 100)}, {'1689': ('50100', 200, 100)}
]

lista_salas_jogar3 = [
    {'172': ('100200', 200, 400)}, {'1690': ('100200', 200, 400)}, {'1691': ('100200', 200, 400)}, {'1692': ('100200', 200, 400)},
    {'1693': ('100200', 200, 400)}, {'1694': ('100200', 200, 400)}, {'1695': ('100200', 200, 400)}, {'1696': ('100200', 200, 400)},
    {'1697': ('100200', 200, 400)}, {'1698': ('100200', 200, 400)}, {'1699': ('100200', 200, 400)}, {'1700': ('100200', 200, 400)},
    {'1701': ('100200', 200, 400)}, {'1702': ('100200', 200, 400)}, {'1703': ('100200', 200, 400)}
]

dicionari_PC_cadeira = {
    'PC-I5-8600K': {'cadeira_1': (659, 127), 'cadeira_2': (828, 211), 'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_5': (495, 452),
                    'cadeira_6': (276, 451), 'cadeira_7': (118, 360), 'cadeira_8': (134, 194), 'cadeira_9': (312, 131)},
    'PC-I5-9400A': {'cadeira_2': (828, 211), 'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_5': (495, 452), 'cadeira_6': (276, 451),
                    'cadeira_7': (118, 360), 'cadeira_8': (134, 194), 'cadeira_9': (312, 131), 'cadeira_1': (659, 127)},
    'PC-I5-9400B': {'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_5': (495, 452), 'cadeira_6': (276, 451), 'cadeira_7': (118, 360),
                    'cadeira_8': (134, 194), 'cadeira_9': (312, 131), 'cadeira_1': (659, 127), 'cadeira_2': (828, 211)},
    'PC-I5-9400C': {'cadeira_4': (690, 451), 'cadeira_5': (495, 452), 'cadeira_6': (276, 451), 'cadeira_7': (118, 360), 'cadeira_8': (134, 194),
                    'cadeira_9': (312, 131), 'cadeira_1': (659, 127), 'cadeira_2': (828, 211), 'cadeira_3': (847, 366)},
    'PC-R5-7600A': {'cadeira_5': (495, 452), 'cadeira_6': (276, 451), 'cadeira_7': (118, 360), 'cadeira_8': (134, 194), 'cadeira_9': (312, 131),
                    'cadeira_1': (659, 127), 'cadeira_2': (828, 211), 'cadeira_3': (847, 366), 'cadeira_4': (690, 451)},
    'PC-I5-13400A': {'cadeira_6': (276, 451), 'cadeira_7': (118, 360), 'cadeira_8': (134, 194), 'cadeira_9': (312, 131), 'cadeira_1': (659, 127),
                     'cadeira_2': (828, 211), 'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_5': (495, 452)},
    'PC-I5-13400B': {'cadeira_7': (118, 360), 'cadeira_8': (134, 194), 'cadeira_9': (312, 131), 'cadeira_1': (659, 127), 'cadeira_2': (828, 211),
                     'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_5': (495, 452), 'cadeira_6': (276, 451)},
    'PC-I5-13400C': {'cadeira_8': (134, 194), 'cadeira_9': (312, 131), 'cadeira_1': (659, 127), 'cadeira_2': (828, 211), 'cadeira_3': (847, 366),
                     'cadeira_4': (690, 451), 'cadeira_5': (495, 452), 'cadeira_6': (276, 451), 'cadeira_7': (118, 360)},
    'PC-I5-13400D': {'cadeira_9': (312, 131), 'cadeira_1': (659, 127), 'cadeira_2': (828, 211), 'cadeira_3': (847, 366), 'cadeira_4': (690, 451),
                     'cadeira_5': (495, 452), 'cadeira_6': (276, 451), 'cadeira_7': (118, 360), 'cadeira_8': (134, 194)},
    'PC-R5-5600G': {'cadeira_1': (659, 127), 'cadeira_2': (828, 211), 'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_5': (495, 452),
                    'cadeira_6': (276, 451), 'cadeira_7': (118, 360), 'cadeira_8': (134, 194), 'cadeira_9': (312, 131)},
    'PC-I5-13400E': {'cadeira_2': (828, 211), 'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_5': (495, 452), 'cadeira_6': (276, 451),
                     'cadeira_7': (118, 360), 'cadeira_8': (134, 194), 'cadeira_9': (312, 131), 'cadeira_1': (659, 127)},
    'PC-i3-8145U': {'cadeira_1': (659, 127), 'cadeira_2': (828, 211), 'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_5': (495, 452),
                    'cadeira_6': (276, 451), 'cadeira_7': (118, 360), 'cadeira_8': (134, 194), 'cadeira_9': (312, 131)},
    'PC-I7-9700KF': {'cadeira_1': (659, 127), 'cadeira_2': (828, 211), 'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_5': (495, 452),
                     'cadeira_6': (276, 451), 'cadeira_7': (118, 360), 'cadeira_8': (134, 194), 'cadeira_9': (312, 131)}
}

dicionario_cadeira = {'cadeira_1': (659, 127), 'cadeira_2': (828, 211), 'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_5': (495, 452),
                      'cadeira_6': (276, 451), 'cadeira_7': (118, 360), 'cadeira_8': (134, 194), 'cadeira_9': (312, 131)}

dicionario_cadeira5 = {'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_5': (495, 452), 'cadeira_6': (276, 451), 'cadeira_7': (118, 360)}

dicionario_celular = {'cadeira_1': (645, 135), 'cadeira_2': (818, 217), 'cadeira_3': (814, 377), 'cadeira_4': (675, 473), 'cadeira_5': (484, 473),
                      'cadeira_6': (290, 473), 'cadeira_7': (144, 377), 'cadeira_8': (156, 217), 'cadeira_9': (334, 135)}

prioridade_cadeira = dicionari_PC_cadeira[nome_computador]


def localizar_imagem(imagem, regiao, precisao):
    try:
        posicao = pyautogui.locateOnScreen(imagem, region=regiao, confidence=precisao, grayscale=True)
        return posicao
    except:
        print("Ocorreu um erro ao localizar a imagem")
        time.sleep(2)
        return None


# def conta_cadeiras_livres(x_origem, y_origem, cor_cadeira=(254, 207, 0), tolerancia=10):
#     """
#     Conta o número de cadeiras livres ao redor de uma mesa.
#
#     Parâmetros:
#     - x_origem: A coordenada X da origem da mesa.
#     - y_origem: A coordenada Y da origem da mesa.
#     - cor_cadeira: A cor da cadeira em formato RGB.
#     - tolerancia: A tolerância para correspondência de cor.
#
#     Retorna:
#     - O número de cadeiras livres ao redor da mesa.
#     """
#
#     # Usando uma list comprehension e a função sum para contar cadeiras livres
#     cadeiras_livres = sum(
#         1 for valor in dicionario_cadeira.values()
#         if pyautogui.pixelMatchesColor(x_origem + valor[0], y_origem + valor[1], cor_cadeira, tolerance=tolerancia)
#     )
#
#     # Exibindo a mensagem com o número de cadeiras livres
#     print(f"Esta mesa tem {cadeiras_livres} cadeiras livres.")
#     return cadeiras_livres


def cadeiras_livres(x_origem, y_origem, cor_cadeira=(254, 207, 0), tolerancia=10, lugares=9):
    """
    Verifica se todas as cadeiras em torno de uma mesa estão livres.

    Parâmetros:
    - x_origem: A coordenada X da origem da mesa.
    - y_origem: A coordenada Y da origem da mesa.
    - cor_cadeira: A cor da cadeira em formato RGB.
    - tolerancia: A tolerância para correspondência de cor.

    Retorna:
    - True se todas as cadeiras estiverem livres, False se pelo menos uma cadeira estiver ocupada.
    """
    print('cadeiras_livres')
    if lugares == 9:
        for x, y in dicionario_cadeira.values():
            if not pyautogui.pixelMatchesColor(x_origem + x, y_origem + y, cor_cadeira, tolerance=tolerancia):
                print('Pelo menos uma cadeira está ocupada.')
                return False
        print('Todas as cadeiras estão livres.')
    else:
        for x, y in dicionario_cadeira5.values():
            if not pyautogui.pixelMatchesColor(x_origem + x, y_origem + y, cor_cadeira, tolerance=tolerancia):
                print('Pelo menos uma cadeira está ocupada.')
                return False
        print('Todas as cadeiras estão livres.')
    return True


# def conta_cadeiras_livres_celular(x_origem, y_origem, cor_celular=(136, 137, 137), tolerancia=8):
#     """
#     Conta o número de cadeiras livres ao redor de uma mesa.
#
#     Parâmetros:
#     - x_origem: A coordenada X da origem da mesa.
#     - y_origem: A coordenada Y da origem da mesa.
#     - cor_cadeira: A cor da cadeira em formato RGB.
#     - tolerancia: A tolerância para correspondência de cor.
#
#     Retorna:
#     - O número de cadeiras livres ao redor da mesa.
#     """
#
#     # Usando uma list comprehension e a função sum para contar cadeiras livres
#     cadeiras_livres = sum(
#         1 for valor in dicionario_celular.values()
#         if pyautogui.pixelMatchesColor(x_origem + valor[0], y_origem + valor[1], cor_celular, tolerance=tolerancia)
#     )
#
#     # Exibindo a mensagem com o número de cadeiras livres
#     print(f"Esta mesa tem {cadeiras_livres} cadeiras com celular.")
#     return cadeiras_livres


def cadeiras_celular(x_origem, y_origem, cor_celular=(136, 137, 137), tolerancia=8):
    """
    Verifica se todas as cadeiras em torno de uma mesa estão livres.

    Parâmetros:
    - x_origem: A coordenada X da origem da mesa.
    - y_origem: A coordenada Y da origem da mesa.
    - cor_cadeira: A cor da cadeira em formato RGB.
    - tolerancia: A tolerância para correspondência de cor.

    Retorna:
    - True se todas as cadeiras estiverem livres, False se pelo menos uma cadeira estiver ocupada.
    """
    # print('cadeiras_livres')
    for x, y in dicionario_celular.values():
        if pyautogui.pixelMatchesColor(x_origem + x, y_origem + y, cor_celular, tolerance=tolerancia):
            print('\nPelo menos uma cadeira está com celular.\n')
            return False
    # print('Todas as cadeiras estão livres de celular.')
    return True


def clica_seta_sentar(x_origem, y_origem):
    """
    Clica na seta de uma cadeira com base nas coordenadas de origem fornecidas.

    Parameters:
    - x_origem (int): Coordenada x de origem na tela.
    - y_origem (int): Coordenada y de origem na tela.

    Returns:
    - bool: Retorna True se encontrar e clicar na seta de uma cadeira livre, caso contrário, retorna False.
    """

    print('clica_seta_sentar')
    # Itera sobre as cadeiras na ordem de prioridade
    for cadeira_id, offset in prioridade_cadeira.items():
        # Verifica se a cor do pixel corresponde à cor da cadeira livre
        if pyautogui.pixelMatchesColor((x_origem + offset[0]), (y_origem + offset[1]), (254, 207, 0), tolerance=10):
            # Clique na cadeira e imprima que está livre
            pyautogui.click((x_origem + offset[0]), (y_origem + offset[1]))
            print(cadeira_id, "livre")
            return True
    # Retorna False se nenhuma cadeira estiver livre
    return False


def sentar_mesa(x_origem, y_origem, senta_com_maximo=False, blind='2040', teste_celular=False):
    """
    Tenta sentar em uma mesa de poker virtual com base nas coordenadas fornecidas.

    Parameters:
    - x_origem (int): Coordenada x de origem na tela.
    - y_origem (int): Coordenada y de origem na tela.
    - senta_com_maximo (bool): Indica se deve tentar sentar com o máximo de fichas.
    - blind (str): Valor do blind desejado. Padrão é '2040'.

    Returns:
    - bool: Retorna True se for bem-sucedido em sentar, False caso contrário.
    """

    print('sentar_mesa')
    sentou = False
    if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 674), (19, 65, 109), tolerance=5):
        print('possivel aviso so sistema, roda um limpa jogando')
        Limpa.limpa_jogando(x_origem, y_origem)
        Limpa.limpa_promocao(x_origem, y_origem)
        # time.sleep(0.5)

    # testa se esta aparecendo o botao azul "Jogar agora"
    if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 674), (27, 92, 155), tolerance=5):
        # testa se esta dentro da mesa

        # print("Está dentro da mesa")

        if not (pyautogui.pixelMatchesColor(495 + x_origem, 627 + y_origem, (15, 160, 220), tolerance=10)):
            # testa se tem o botao jogar agoar apara seber se ja ta sentado
            # print('Já está sentado')
            sentou = True
            return sentou
        else:
            blind_sala = OCR_tela.blind_sala(x_origem, y_origem)
            try:
                blind = blind.replace("/", "")
            except:
                print('erro blind')

            if blind == blind_sala:
                print("Sentar mesa: Está na sala certa")
            else:
                print("Sentar mesa: Está na sala errada")
                return False

            if teste_celular:
                if not cadeiras_celular(x_origem, y_origem):
                    print('Sai da mesa pq tem humanos')
                    sentou = False
                    return sentou

            for _ in range(2):
                print('Tentando sentar')

                if (pyautogui.pixelMatchesColor((x_origem + 534), (y_origem + 357), (70, 126, 56), tolerance=10)
                        or pyautogui.pixelMatchesColor((x_origem + 534), (y_origem + 357), (23, 121, 166), tolerance=10)):
                    print('mesa esta limpa')
                else:
                    Limpa.fecha_tarefa(x_origem, y_origem)
                    Limpa.limpa_jogando(x_origem, y_origem)
                    Limpa.limpa_promocao(x_origem, y_origem)

                clica_seta = clica_seta_sentar(x_origem, y_origem)

                if clica_seta:
                    posicao_comprar_x = 490 + x_origem
                    posicao_comprar_y = 480 + y_origem
                    cor_comprar = (30, 140, 206)
                    avisodo_sistema_x = 490 + x_origem
                    avisodo_sistema_y = 400 + y_origem
                    cor_nao_possui_fichas = (209, 211, 213)
                    cor_nao_possui_fichas2 = (30, 138, 218)
                    compra_ajustada = False

                    for _ in range(20):
                        # Testa se o botão azul do comprar está visível # testa algumas vezes
                        if pyautogui.pixelMatchesColor(posicao_comprar_x, posicao_comprar_y, cor_comprar, 35):
                            print("Tem comprar")
                            # testa o tipo de caixa de comprar ficha, testa se a caixa é mais larga, olha uma mao cinsa segurando um dinheiro
                            if pyautogui.pixelMatchesColor((x_origem + 313), (y_origem + 445), (55, 57, 62), 20):
                                # print("janela mais alta")
                                if pyautogui.pixelMatchesColor((x_origem + 520), (y_origem + 407), (255, 255, 255), 10):
                                    # testa se a recompra nao esta marcada
                                    pyautogui.click((x_origem + 522), (y_origem + 405))  # Marca a re-compra automatica
                                posicao_valor_minimo_x = 324 + x_origem
                                posicao_valor_minimo_y = 354 + y_origem
                                posicao_valor_maximo_x = 659 + x_origem
                                posicao_valor_maximo_y = 354 + y_origem
                            else:
                                # print("janela mais baixa")
                                if pyautogui.pixelMatchesColor((x_origem + 520), (y_origem + 427), (255, 255, 255), 10):
                                    # testa se a recompra nao esta marcada
                                    pyautogui.click((x_origem + 522), (y_origem + 424))  # Marca a re-compra automatica
                                posicao_valor_minimo_x = 324 + x_origem
                                posicao_valor_minimo_y = 372 + y_origem
                                posicao_valor_maximo_x = 659 + x_origem
                                posicao_valor_maximo_y = 372 + y_origem

                            if senta_com_maximo:
                                pyautogui.doubleClick(posicao_valor_maximo_x, posicao_valor_maximo_y)  # clica no ajuste maximo de fichas
                                time.sleep(0.6)

                                for _ in range(500):  # testa algumas vezes

                                    if pyautogui.pixelMatchesColor(posicao_comprar_x, posicao_comprar_y, cor_comprar, tolerance=35):
                                        # testa se o botao ta azul
                                        compra_ajustada = True
                                        break
                                    pyautogui.click((x_origem + 290), (y_origem + 363))  # clina no diminuir ate o botao ficar azul

                            else:
                                pyautogui.doubleClick(posicao_valor_minimo_x, posicao_valor_minimo_y)  # clica no ajuste minimo de fichas
                                compra_ajustada = True

                            if compra_ajustada:

                                for _ in range(15):
                                    pyautogui.mouseDown(posicao_comprar_x, posicao_comprar_y)  # clica no comprar
                                    print("Clicou no comprar")
                                    time.sleep(0.7)
                                    pyautogui.mouseUp(posicao_comprar_x, posicao_comprar_y)  # clica no comprar

                                    if not (pyautogui.pixelMatchesColor(posicao_comprar_x, posicao_comprar_y, cor_comprar, tolerance=35)):
                                        break

                                time.sleep(0.5)

                                if pyautogui.pixelMatchesColor(avisodo_sistema_x, avisodo_sistema_y, cor_nao_possui_fichas, tolerance=5):
                                    print('Aviso do sistema')
                                    # testa se tem aviso do sistema

                                    if pyautogui.pixelMatchesColor((x_origem + 337), (y_origem + 337), (33, 66, 103), tolerance=5):
                                        # Desculpex vocês nao possui fichas suficientes para senter. Favor ir a uma sala ou faça uma recarga
                                        pyautogui.click((x_origem + 641), (y_origem + 278))  # fecha aviso do sistema
                                        print('Desculpex vocês nao possui fichas suficientes para senter. Favor ir a uma sala ou faça uma recarga')
                                        sentou = False
                                        return sentou

                                    elif pyautogui.pixelMatchesColor((x_origem + 373), (y_origem + 339), (63, 92, 123), tolerance=5):
                                        pyautogui.click((x_origem + 641), (y_origem + 278))  # fecha aviso do sistema
                                        print('Desculpe! Não possui fichas suficientes')
                                        sentou = False
                                        return sentou

                                    elif pyautogui.pixelMatchesColor((x_origem + 340), (y_origem + 336), (33, 66, 103), tolerance=5):
                                        # Você não pode jogar com duas contas ao mesmo tempo
                                        pyautogui.click((x_origem + 641), (y_origem + 278))  # fecha aviso do sistema
                                        print('Você não pode jogar com duas contas ao mesmo tempo')
                                        sentou = False
                                        return sentou

                                    elif pyautogui.pixelMatchesColor((x_origem + 369), (y_origem + 341), (33, 66, 103), tolerance=5):
                                        # Este lugar ja foi ocupado
                                        pyautogui.click((x_origem + 641), (y_origem + 278))  # fecha aviso do sistema
                                        print("Este lugar ja foi ocupado")
                                        sentou = False
                                        # tenta sentar em outra cadeira
                                        break
                                    else:
                                        pyautogui.click((x_origem + 641), (y_origem + 278))  # fecha aviso do sistema
                                        print('outro amensagem com aviso do sistema')
                                        break

                                else:
                                    print('sentar_mesa: Sentou')
                                    sentou = True
                                    return sentou

                        elif (pyautogui.pixelMatchesColor(avisodo_sistema_x, avisodo_sistema_y, cor_nao_possui_fichas, tolerance=10)
                              or pyautogui.pixelMatchesColor(avisodo_sistema_x, avisodo_sistema_y, cor_nao_possui_fichas2, tolerance=10)):
                            # se assim que clicar na setinha nao ter fichas suficiente
                            pyautogui.click((x_origem + 641), (y_origem + 278), button='left')  # clica no fechar mensagem de nao tem fichas
                            print("Não possui fichas suficiente")
                            sentou = False
                            return sentou

    print('Não está dentro da mesa')
    return sentou


def escolher_blind(x_origem, y_origem, blind, lugares=9, posi_lista=0):
    """
    Escolhe o valor do blind em uma mesa de poker virtual com base nas coordenadas fornecidas.

    Parameters:
    - x_origem (int): Coordenada x de origem na tela.
    - y_origem (int): Coordenada y de origem na tela.
    - blind (str): Valor do blind desejado.

    Returns:
    - int: Retorna o número da sala se bem-sucedido, 0 caso contrário.
    """

    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
        return "sair da conta"

    Limpa.aviso_canto_lobby(x_origem, y_origem)

    for _ in range(20):  # abrir o menu blind
        # testa se a caixa de escolha do blind esta aberta, olha a barra preta
        if pyautogui.pixelMatchesColor((x_origem + 200), (y_origem + 450), (0, 0, 0), tolerance=1):
            pyautogui.click(268 + x_origem, 571 + y_origem, button='left')  # clica no aptualizar blind
            print("Blind aberto")
            break
        else:
            pyautogui.click(71 + x_origem, 619 + y_origem, button='left')  # clica para abrir o blind
            print("Clicar para abrir o blind")
            time.sleep(0.3)

    for _ in range(10):  # Abrir a barra de rolagem de valores
        if pyautogui.pixelMatchesColor((x_origem + 200), (y_origem + 475), (0, 0, 0), tolerance=1):
            # testa se a barra de rolagem esta aberta
            print("Barra de rolagem aberta")
            break
        else:
            pyautogui.click(293 + x_origem, 450 + y_origem, button='left')  # clica para abrir o blind
            print("Clicar para abrir a barra de rolagem")
            time.sleep(0.3)

    posicao_barra, posicao_lista = list(blinb_rolagem[blind])[:2]

    pyautogui.doubleClick(300 + x_origem, posicao_barra + y_origem, button='left')  # clica para rolar
    time.sleep(0.2)
    pyautogui.doubleClick(200 + x_origem, posicao_lista + y_origem, button='left')  # clica no valor dentro da lista
    time.sleep(0.2)

    for _ in range(30):  # Marcar apenas as salas de 9 lugares
        if pyautogui.pixelMatchesColor((x_origem + 139), (y_origem + 492), (201, 201, 201), tolerance=2):
            if lugares == 9:
                print('Sala de 9 lugares marcada')
                break
            else:
                pyautogui.click(x_origem + 139, y_origem + 492)  # Marcar sala de nove
                time.sleep(0.3)
                print("Desmarca sala de 9 lugares")
        else:
            if lugares == 9:
                pyautogui.click(x_origem + 139, y_origem + 492)  # Marcar sala de nove
                time.sleep(0.3)
                print("Marcar sala de 9 lugares")
            else:
                print('Sala de 9 lugares desmarcada')
                break
    for _ in range(30):
        if pyautogui.pixelMatchesColor((x_origem + 186), (y_origem + 492), (201, 201, 201), tolerance=2):
            if lugares == 9:
                pyautogui.click(x_origem + 186, y_origem + 492)  # Desmarcar sala de 5
                time.sleep(0.3)
                print("Desmarcar sala de 5 lugares")
            else:
                print('Sala de 5 lugares marcada')
                break
        else:
            if lugares == 9:
                print('Sala de 5 lugares marcada')
                break
            else:
                pyautogui.click(x_origem + 186, y_origem + 492)  # Desmarcar sala de 5
                time.sleep(0.3)
                print("Marcar sala de 5 lugares")

    for _ in range(30):
        if pyautogui.pixelMatchesColor((x_origem + 233), (y_origem + 492), (201, 201, 201), tolerance=2):
            pyautogui.click(x_origem + 233, y_origem + 492)  # Desmarcar sala de 3
            time.sleep(0.3)
            print("Desmarcar sala de 3 lugares")
        else:
            print('Sala de 3 lugares desmarcada')
            break

    for _ in range(30):
        if pyautogui.pixelMatchesColor((x_origem + 280), (y_origem + 492), (201, 201, 201), tolerance=2):
            pyautogui.click(x_origem + 280, y_origem + 492)  # Desmarcar sala de 2
            time.sleep(0.3)
            print("Desmarcar sala de 2 lugares")
        else:
            print('Sala de 2 lugares desmarcada')
            break

    pyautogui.click(71 + x_origem, 619 + y_origem, button='left')  # clica para fechar o blind

    pyautogui.doubleClick(405 + x_origem, 233 + y_origem)  # clica em organizar vazias para cima
    blind_sala = None
    time.sleep(1)
    cont_erro_entrar_mesa = 0

    dicionari_posi_lista_mesa = {0: 264, 1: 298, 2: 332, 3: 366, 4: 400, 5: 434, 6: 468}
    posi = dicionari_posi_lista_mesa[posi_lista]

    for j in range(20):

        if pyautogui.pixelMatchesColor((x_origem + 310), (y_origem + 264), (95, 106, 122), tolerance=5):
            # erro ao buscar sala, fica uma faixa cinza na linha da sala
            print('Erro ao buscar sala, vai ser dado um F5')
            pyautogui.press('f5')
            time.sleep(35)
            return "Erro ao buscar sala, vai ser dado um F5"

        if pyautogui.pixelMatchesColor((x_origem + 358), (y_origem + posi), (29, 32, 37), tolerance=5):
            # testa se tem sala com todos lugares vazios, olha se tem preto no inicio da barra de ocupação
            pyautogui.doubleClick(358 + x_origem, posi + y_origem)  # clica para entar na sala vazia

            for i in range(40):
                if pyautogui.pixelMatchesColor((x_origem + 358), (y_origem + posi), (29, 32, 37), tolerance=5):
                    # testa se tem sala com todos lugares vazios, olha se tem preto no inicio da barra de ocupação
                    pyautogui.doubleClick(358 + x_origem, posi + y_origem)  # clica para entar na sala vazia
                    cont_erro_entrar_mesa += 1

                Limpa.limpa_jogando(x_origem, y_origem)
                Limpa.limpa_promocao(x_origem, y_origem)

                if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 674), (27, 92, 155), tolerance=19):
                    # testa se esta dentro da mesa
                    # Limpa.limpa_jogando(x_origem, y_origem)
                    blind_sala = OCR_tela.blind_sala(x_origem, y_origem)
                    try:
                        blind = blind.replace("/", "")
                    except:
                        print('erro blind')

                    num_sala = OCR_tela.numero_sala(x_origem, y_origem)
                    print("num_sala", num_sala)

                    if blind == blind_sala:
                        print("Esta na sala certa")
                        return num_sala
                    else:
                        print("Esta na sala errada")
                        return num_sala

                time.sleep(1)
                if cont_erro_entrar_mesa >= 5:
                    Limpa.limpa_total(x_origem, y_origem)
                    break

        elif (pyautogui.pixelMatchesColor((x_origem + 435), (y_origem + 264), (246, 126, 0), tolerance=5)
              or pyautogui.pixelMatchesColor((x_origem + 435), (y_origem + 264), (80, 178, 0), tolerance=5)):
            # barra verde ou barra laranja
            print("Não tem sala vazia")
            return "Não tem sala vazia"

        elif pyautogui.pixelMatchesColor((x_origem + 205), (y_origem + 265), (46, 87, 132), tolerance=3):  # testa se existe sala com este numero
            print("Não existe sala com esse numero")
            if j > 15:
                return "Não existe sala com esse numero"
        time.sleep(0.1)
    return "Não entrou na sala"


def ajuste_valor_niquel(x_origem, y_origem, ajusta_aposta):
    """
    Ajusta o valor da aposta no jogo de Niquel em uma máquina virtual.

    Parameters:
    - x_origem (int): Coordenada x de origem na tela.
    - y_origem (int): Coordenada y de origem na tela.
    - ajusta_aposta (int): Valor da aposta desejada (200 ou 2000).

    Returns:
    - tuple: Retorna uma tupla com dois booleanos indicando se a aposta e o modo automático foram ajustados.
    """
    print("ajuste_valor_niquel :", ajusta_aposta)
    aposta, auto10 = False, False

    for _ in range(20):
        posicao_200 = None
        Limpa.aviso_canto_lobby(x_origem, y_origem)

        if ajusta_aposta == 2000:
            # se deve jogar apostando 2000
            imagem = r'Imagens\Niquel\niquel2000.png'
            escolhe_aposta = 614  # coodenada do 2000
        else:
            # se deve jogar apostando 200
            imagem = r'Imagens\Niquel\niquel200.png'
            escolhe_aposta = 636  # coodenada do 200

        regiao = (77 + x_origem, 651 + y_origem, 50, 16)  # (x, y, largura, altura)
        precisao = 0.9
        posicao_200 = localizar_imagem(imagem, regiao, precisao)

        if posicao_200 is not None:
            # Verifica se a imagem foi encontrada
            print("Foi encontrado o valor de:", ajusta_aposta)
            aposta = True
            break
        elif posicao_200 is None:  # Verifica se a imagem foi encontrada
            print("Não foi encontrado o valor de:", ajusta_aposta)
            pyautogui.click(x_origem + 161, y_origem + 658)  # clica na setinha para abrir a lista de valores a serem apostados
            time.sleep(0.3)
            pyautogui.click(x_origem + 161, y_origem + escolhe_aposta)  # clica no valor de 200
            time.sleep(0.3)

    for _ in range(20):
        posicao_10auto = None
        Limpa.aviso_canto_lobby(x_origem, y_origem)  # fecha propaganda

        regiao = (207 + x_origem, 652 + y_origem, 58, 13)  # (x, y, largura, altura)
        precisao = 0.9
        imagem = r'Imagens\Niquel\10auto.png'
        posicao_10auto = localizar_imagem(imagem, regiao, precisao)

        if posicao_10auto is not None:
            # Verifica se a imagem foi encontrada
            print("Foi encontrado 10 AUTO")
            auto10 = True
            break
        elif posicao_10auto is None:
            # Verifica se a imagem foi encontrada
            print("Não foi encontrado 10 AUTO")
            pyautogui.mouseDown(x_origem + 234, y_origem + 659)  # aperta e segura 10auto
            time.sleep(0.5)
            pyautogui.mouseUp(x_origem + 234, y_origem + 659)  # aperta e segura 10auto
            time.sleep(0.3)
            pyautogui.click(x_origem + 234, y_origem + 615)  # escolhe 10auto na lista
            time.sleep(0.3)
            pyautogui.click(x_origem + 641, y_origem + 278)  # clica para fechar a mensagem vc so pode jogar depois de estar sentado

    return aposta, auto10


def sala_minima_niquel(x_origem, y_origem, num_mesa, blind_mesa):
    if blind_mesa == "12":
        pyautogui.doubleClick(130 + x_origem, 200 + y_origem)  # clica na lista de iniciantes
    elif blind_mesa == "2040" or blind_mesa == "24":
        pyautogui.doubleClick(280 + x_origem, 200 + y_origem)  # clica na lista de aprendizes
        # if not pyautogui.pixelMatchesColor((x_origem + 280), (y_origem + 210), (73, 177, 9), tolerance=5):
    #     pyautogui.click(280 + x_origem, 200 + y_origem)  # clica na lista de aprendizes

    time.sleep(0.3)
    # if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
    #     return "sair da conta"
    Limpa.aviso_canto_lobby(x_origem, y_origem)
    pyautogui.doubleClick(310 + x_origem, 617 + y_origem)  # clica FORA caixa de busca de salas para apagar o valor
    time.sleep(0.2)
    pyautogui.doubleClick(190 + x_origem, 617 + y_origem)  # clica na caixa de busca de salas
    time.sleep(0.2)
    pyautogui.write(num_mesa)  # escreve o numero da sala na barra de busca
    time.sleep(0.2)
    pyautogui.press('enter')  # Pressiona a tecla Enter
    pyautogui.click(99 + x_origem, 238 + y_origem)  # clica na primeira coluna do id
    time.sleep(0.2)
    pyautogui.click(99 + x_origem, 238 + y_origem)  # clica na primeira coluna do id
    time.sleep(0.2)

    print('mesa: ', num_mesa)
    # time.sleep(0.5)
    cont_erro_entrar_mesa = 0
    blind_sala = None

    if pyautogui.pixelMatchesColor((x_origem + 685), (y_origem + 360), (215, 234, 244), tolerance=1):
        print("teste_limpo: Esta no Lobby, ta limpo")
    else:
        Limpa.limpa_promocao(x_origem, y_origem)

    for j in range(20):
        # print(j)
        if pyautogui.pixelMatchesColor((x_origem + 310), (y_origem + 264), (95, 106, 122), tolerance=5):
            # erro ao buscar sala, fica uma faixa cinza na linha da sala
            print('Erro ao buscar sala, vai ser dado um F5')
            pyautogui.press('f5')
            time.sleep(25)
            break

        if pyautogui.pixelMatchesColor((x_origem + 435), (y_origem + 264), (26, 29, 33), tolerance=5):
            # testa se tem sala com pelo menos um lugar vazio, olha se tem preto no fim da barra de ocupação
            pyautogui.doubleClick(490 + x_origem, 263 + y_origem)  # clica para entar na sala vazia

            for i in range(40):
                if pyautogui.pixelMatchesColor((x_origem + 435), (y_origem + 264), (26, 29, 33), tolerance=5):
                    # testa se tem sala com pelo menos um lugar vazio, olha se tem preto no fim da barra de ocupação
                    pyautogui.doubleClick(490 + x_origem, 263 + y_origem)  # clica para entar na sala vazia
                    cont_erro_entrar_mesa += 1

                Limpa.limpa_jogando(x_origem, y_origem)
                Limpa.limpa_promocao(x_origem, y_origem)

                if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 674), (27, 92, 155), tolerance=19):
                    # testa se esta dentro da mesa
                    # Limpa.limpa_jogando(x_origem, y_origem)

                    num_sala = OCR_tela.numero_sala(x_origem, y_origem)
                    print("num_sala", num_sala)
                    print('num_mesa', num_mesa)

                    if num_sala == num_mesa:
                        print("Esta na sala certa")
                        if not cadeiras_celular(x_origem, y_origem):
                            print('Sai da mesa pq tem humanos')
                            return False, True
                        return True, True
                    else:
                        print("Esta na sala errada")
                        return False, True

                time.sleep(1)
                if cont_erro_entrar_mesa >= 5:
                    Limpa.limpa_total(x_origem, y_origem)
                    break

        elif pyautogui.pixelMatchesColor((x_origem + 435), (y_origem + 264), (203, 107, 7), tolerance=5):
            print("Não tem sala vazia")
            return False, True

        elif pyautogui.pixelMatchesColor((x_origem + 205), (y_origem + 265), (46, 87, 132), tolerance=3):  # testa se existe sala com este numero
            print("Não existe sala com esse numero")
            if j > 15:
                return False, False
        time.sleep(0.1)
    Limpa.limpa_total(x_origem, y_origem)
    print("alguma outra falha para achar mesa")
    return False, True


def gira_niquel(x_origem, y_origem):
    posicao_10auto = None
    regiao = (207 + x_origem, 652 + y_origem, 58, 13)  # (x, y, largura, altura)
    imagem = r'Imagens\Niquel\10auto.png'
    precisao = 0.9
    posicao_10auto = localizar_imagem(imagem, regiao, precisao)
    if posicao_10auto is not None:  # Verifica se a imagem foi encontrada
        pyautogui.click((x_origem + 233), (y_origem + 660))  # clica no 10auto
        print("foi encontado 10 AUTO")
        gira = True
        return gira
    else:
        print("não tem 10 auto")
        gira = False
        return gira


def gira_10auto(x_origem, y_origem):
    posicao_10auto = None
    regiao = (207 + x_origem, 652 + y_origem, 58, 13)  # (x, y, largura, altura)
    imagem = r'Imagens\Niquel\10auto.png'
    precisao = 0.9
    posicao_10auto = localizar_imagem(imagem, regiao, precisao)
    if posicao_10auto is not None:  # Verifica se a imagem foi encontrada
        print("foi encontado 10 AUTO")
        gira = True
        return gira
    else:
        print("não tem 10 auto")
        gira = False
        return gira


def joga(x_origem, y_origem, ajusta_aposta):
    global lista_salas_niquel
    blind_mesa = None
    sentou = False

    if ajusta_aposta == 200:
        tarefas_fazer = ('Jogar o caca-niquel da mesa 150 vezes',
                         'Jogar o caca-niquel da mesa 70 vezes',
                         'Jogar o caca-niquel da mesa 10 vezes')

    elif ajusta_aposta == 2000:
        tarefas_fazer = ('Ganhar 100.000 fichas no caca niquel da mesa',
                         'Ganhar 30.000 fichas no caca niquel da mesa',
                         'Ganhar 10.000 fichas no caca niquel da mesa')

    continua_jogando = True
    meta_atigida = False

    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
        return "sair da conta"

    while continua_jogando:  # permanece joghando
        senta_com_maximo = False
        # print('joga mesa')
        if (pyautogui.pixelMatchesColor((x_origem + 534), (y_origem + 357), (70, 126, 56), tolerance=10)
                or pyautogui.pixelMatchesColor((x_origem + 534), (y_origem + 357), (23, 121, 166), tolerance=10)):
            print('mesa esta limpa')
        else:
            Limpa.fecha_tarefa(x_origem, y_origem)
            Limpa.limpa_jogando(x_origem, y_origem)
            Limpa.limpa_promocao(x_origem, y_origem)

        sentou = sentar_mesa(x_origem, y_origem, senta_com_maximo, blind_mesa)
        # print("Sentou : ", sentou)

        if sentou:
            # print("esta sentado")
            passa_corre_joga(x_origem, y_origem, valor_aposta1, valor_aposta2)
            auto10 = gira_10auto(x_origem, y_origem)
            if auto10:
                # Limpa.limpa_abre_tarefa2(x_origem, y_origem)
                Limpa.limpa_abre_tarefa(x_origem, y_origem)
                print('manda recolher')
                Tarefas.recolher_tarefa(x_origem, y_origem)
                print('procura se aidna tem tarefa')

                continua_jogando, tarefa = Tarefas.comparar_listas_fazendo_tarefa(tarefas_fazer, x_origem, y_origem)

                meta_atigida, pontos = Tarefas.meta_tarefas(x_origem, y_origem)

                if Limpa.limpa_total_fazendo_tarefa(x_origem, y_origem) == "sair da conta":
                    return "sair da conta"

                if HoraT.fim_tempo_tarefa():
                    continua_jogando = False
                    return
                IP.testa_trocar_IP()  # ve se tem que trocar ip

            Limpa.fecha_tarefa(x_origem, y_origem)
            # continua_jogando = True
            print("conmtinua jogando ", continua_jogando)
        else:
            print("ainda nao esta sentado")
            for i in range(2):
                # for dicionario in lista_salas_niquel:
                for indice, dicionario in enumerate(lista_salas_niquel):
                    num_mesa = list(dicionario.keys())[0]  # Obtendo a chave do dicionário
                    valor_tupla = dicionario[num_mesa]  # Obtendo a tupla associada à chave
                    blind_mesa = valor_tupla[0]  # Obtendo a string da tupla
                    valor_aposta1 = valor_tupla[1]  # Obtendo o primeiro número da tupla
                    valor_aposta2 = valor_tupla[2]  # Obtendo o segundo número da tupla

                    print('Mumero da mesa para tentar sentar: ', num_mesa)
                    IP.tem_internet()
                    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                        return "sair da conta"
                    # blind_certo = escolher_blind(x_origem, y_origem, '20/40')
                    blind_certo, sala_existe = sala_minima_niquel(x_origem, y_origem, num_mesa, blind_mesa)
                    if not sala_existe:
                        # Remova o item da posição específica
                        item_removido = lista_salas_niquel.pop(indice)
                        # Adicione o item ao final da lista
                        lista_salas_niquel.append(item_removido)

                    if blind_certo:
                        aposta, auto10 = ajuste_valor_niquel(x_origem, y_origem, ajusta_aposta)

                        sentou = sentar_mesa(x_origem, y_origem, senta_com_maximo, blind_mesa)

                        if sentou and aposta and auto10:
                            print('esta tudo ok, slote e sentado')
                            break
                if sentou and aposta and auto10:
                    print('esta tudo ok, slote e sentado')
                    break
            if not sentou:
                print("rodou a lista de mesas 2x, da um F5 para recarregar as mesas")
                IP.tem_internet()
                print('f5')
                pyautogui.press('f5')
                time.sleep(15)

        meta, pontos = Tarefas.tem_tarefa_para_recolher(x_origem, y_origem)
        if meta:
            meta_atigida = True

        if HoraT.fim_tempo_tarefa():
            continua_jogando = False

        if (not continua_jogando) or meta_atigida:
            Limpa.limpa_abre_tarefa(x_origem, y_origem)
            continua_jogando, tarefa = Tarefas.comparar_listas_fazendo_tarefa(tarefas_fazer, x_origem, y_origem)
            meta_atigida, pontos = Tarefas.meta_tarefas(x_origem, y_origem)
            if (not continua_jogando) or meta_atigida:
                print("FIM")
                if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                    return "sair da conta"
                break
        if sentou:
            gira_niquel(x_origem, y_origem)
        time.sleep(0.5)
    return


def mesa_upar_jogar(x_origem, y_origem, numero_jogadas=3, upar=False, blind_mesa='2550'):
    print('mesa_upar_jogar')

    global lista_salas_jogar, lista_salas_jogar2, lista_salas_jogar3, lista_salas_niquel, indice_inicial
    valor_aposta1 = 100
    valor_aposta2 = 50
    # blind_mesa = '2550'
    sentou = False
    continua_jogando = True
    jogou_uma_vez = False
    humano = False
    cont_jogou = 0
    senta_com_maximo = False
    cont_limpa_jogando = 0
    sala_atual = None
    pular_sala = False

    # Use a lista apropriada com base no valor da variável blind_mesa

    if blind_mesa == '100200':
        lista_salas = lista_salas_jogar3
    elif blind_mesa == '50100':
        lista_salas = lista_salas_jogar2
    elif blind_mesa == '2550':
        lista_salas = lista_salas_jogar
    else:
        lista_salas = lista_salas_jogar

    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
        return "sair da conta"

    if upar:
        xp2.pega_2xp(x_origem, y_origem)

    Limpa.fecha_tarefa(x_origem, y_origem)
    Limpa.limpa_jogando(x_origem, y_origem)
    Limpa.limpa_promocao(x_origem, y_origem)
    sentou = sentar_mesa(x_origem, y_origem, senta_com_maximo, blind_mesa, True)

    time_comecou = time_entrou = time.perf_counter()

    while continua_jogando:  # permanece joghando

        if cont_limpa_jogando > 40:
            cont_limpa_jogando = 0
            # testa se a mesa esta limpa
            if (pyautogui.pixelMatchesColor((x_origem + 534), (y_origem + 357), (70, 126, 56), tolerance=10)
                    or pyautogui.pixelMatchesColor((x_origem + 534), (y_origem + 357), (23, 121, 166), tolerance=10)):
                print('mesa esta limpa')
                if pyautogui.pixelMatchesColor((x_origem + 38), (y_origem + 526), (187, 153, 111), tolerance=19):
                    pyautogui.click(x_origem + 38, y_origem + 526)
                    print("Presentinho de dentro da mesa")

            else:
                Limpa.fecha_tarefa(x_origem, y_origem)
                Limpa.limpa_jogando(x_origem, y_origem)
                Limpa.limpa_promocao(x_origem, y_origem)
            sentou = sentar_mesa(x_origem, y_origem, senta_com_maximo, blind_mesa, True)

            # Cálculo do tempo decorrido desde que o jogador entrou no jogo
            tempo_decorrido = time.perf_counter() - time_comecou

            # Conversão de segundos para horas, minutos e segundos
            horas = int(tempo_decorrido // 3600)
            minutos = int((tempo_decorrido % 3600) // 60)
            segundos = int(tempo_decorrido % 60)

            # Impressão do tempo decorrido
            print(f"Tempo jogando: {horas:02d}:{minutos:02d}:{segundos:02d}")

            if (tempo_decorrido >= 300) and (not upar):
                print('Limite de tempo jogando mesa.')
                break

        cont_limpa_jogando += 1

        if jogou_uma_vez:
            if pyautogui.pixelMatchesColor((x_origem + 663), (y_origem + 538), (86, 169, 68), tolerance=20):
                # testa se apareceu as mensagens verdes na parte de baixo
                print('Fim da partida')
                cont_jogou += 1
                if upar:
                    print("Esta upando a conta. Jogou vezes igua a: ", cont_jogou)
                    level_conta, valor_fichas_perfil = OCR_tela.level_conta(x_origem, y_origem)
                    if level_conta >= 10:
                        level_conta, valor_fichas_perfil = OCR_tela.level_conta(x_origem, y_origem)
                        if level_conta >= 10:
                            break

                    if cont_jogou % 10 == 0:  # testa se tem que trocar ip a casa 5 jogadas
                        xp2.pega_2xp(x_origem, y_origem)
                        IP.testa_trocar_IP()  # ve se tem que trocar ip
                else:
                    print('Não esta upando. Jogou vezes igua a: ', cont_jogou, ' .Limite de jogadas: ', numero_jogadas)
                    if cont_jogou >= numero_jogadas:
                        break

                jogou_uma_vez = False
                time_entrou = time.perf_counter()
                if not cadeiras_celular(x_origem, y_origem):
                    print('Sair da mesa fim da jogada com humanos na mesa')
                    humano = True
        else:
            if pyautogui.pixelMatchesColor((x_origem + 663), (y_origem + 538), (86, 169, 68), tolerance=20):
                for i in range(20):
                    time.sleep(0.3)
                    if not cadeiras_celular(x_origem, y_origem):
                        print('Sair da mesa fim da jogada com humanos na mesa')
                        humano = True
                        break
        # print('tempo que esta esperando', tempo_total)
        if (time.perf_counter() - time_entrou) > 60:  # troica de mesa se ficar muito tempo parado sem entrar alguem para jogar
            time_entrou = time.perf_counter()
            cont_limpa_jogando = 45
            print("tempo limite atingido sem outro jogador, sai da mesa para tentar em outra")
            Limpa.limpa_total(x_origem, y_origem)
            Limpa.limpa_jogando(x_origem, y_origem)
            pular_sala = True

        if humano:
            print('Jogador humano na mesa, troca de mesa')
            jogou_uma_vez = False
            humano = False
            pular_sala = True
            Limpa.limpa_total(x_origem, y_origem)
            Limpa.limpa_jogando(x_origem, y_origem)

        if sentou:
            # print("esta sentado")
            (jogou, humano) = passa_corre_joga(x_origem, y_origem, valor_aposta1, valor_aposta2)
            if jogou:
                jogou_uma_vez = True

        else:
            humano = False
            print("ainda nao esta sentado")
            for i in range(3):
                print('indice_inicial', indice_inicial)

                for indice, dicionario in enumerate(lista_salas):

                    print('indice', indice)

                    if indice_inicial > indice:
                        print('pula: ', indice)
                        # faz o for interagir ate chegar na ultima sala que foi usada anteriormente
                        # troca o valor para que na proxima interação possamos iniciar do inicios da lista
                        continue

                    if indice == sala_atual and pular_sala:
                        continue  # Pule a primeira iteração, começando pelo segundo item

                    num_mesa = list(dicionario.keys())[0]  # Obtendo a chave do dicionário
                    valor_tupla = dicionario[num_mesa]  # Obtendo a tupla associada à chave
                    blind_mesa = valor_tupla[0]  # Obtendo a string da tupla
                    valor_aposta1 = valor_tupla[1]  # Obtendo o primeiro número da tupla
                    valor_aposta2 = valor_tupla[2]  # Obtendo o segundo número da tupla

                    print('Mumero da mesa para tentar sentar: ', num_mesa)
                    IP.tem_internet()
                    Limpa.limpa_jogando(x_origem, y_origem)
                    Limpa.limpa_total(x_origem, y_origem)
                    blind_certo, sala_existe = sala_minima_niquel(x_origem, y_origem, num_mesa, blind_mesa)

                    if not sala_existe:
                        # Remova o item da posição específica
                        item_removido = lista_salas.pop(indice)
                        # Adicione o item ao final da lista
                        lista_salas.append(item_removido)

                    if blind_certo:
                        sentou = sentar_mesa(x_origem, y_origem, senta_com_maximo, blind_mesa, True)
                        if sentou:
                            time_entrou = time.perf_counter()
                            print('esta tudo ok, sentado', indice)
                            sala_atual = indice
                            indice_inicial = 0
                            pular_sala = False
                            break
                        else:
                            time_entrou = 0

                    if indice_inicial == indice and indice_inicial != 0:
                        indice_inicial = 0
                        i = 0
                        break

                    indice_inicial = 0

                if i == 1:
                    pular_sala = False

                if sentou:
                    break
                else:
                    time_entrou = 0

            if not sentou:
                indice_inicial = 0
                time_entrou = 0
                print("rodou a lista de mesas 2x, da um F5 para recarregar as mesas")
                IP.tem_internet()
                print('f5')
                pyautogui.press('f5')
                time.sleep(25)

    indice_inicial = sala_atual

    # # Ao final da função, atribui o valor da lista utilizada dentro da função à lista global
    if blind_mesa == '100200':
        lista_salas_jogar3 = lista_salas
    elif blind_mesa == '50100':
        lista_salas_jogar2 = lista_salas
    elif blind_mesa == '2550':
        lista_salas_jogar = lista_salas
    else:
        lista_salas_jogar = lista_salas

    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
        return "sair da conta"

    Limpa.limpa_jogando(x_origem, y_origem)
    return


def dia_de_jogar_mesa(x_origem, y_origem, roleta, level_conta=1, valor_fichas_perfil=0, conta_upada=True, dia_da_semana=0):
    if roleta != 'roleta_1':
        return level_conta, valor_fichas_perfil

    if datetime.datetime.now().time() < datetime.time(23, 0, 0):
        if level_conta == "":
            level_conta, valor_fichas_perfil = OCR_tela.level_conta(x_origem, y_origem)
    else:
        return level_conta, valor_fichas_perfil

    if dia_da_semana in [3]:
        print("O dia da semana é 100/200.")
        blind_mesa = '100200'
        num_vezes_maximo = 5
        num_vezes_minimo = 2

    elif dia_da_semana in [0, 2, 5]:
        print("O dia da semana é 50/100.")
        blind_mesa = '50100'
        num_vezes_maximo = 5
        num_vezes_minimo = 2
    else:
        print("O dia da semana é 25/50.")
        blind_mesa = '2550'
        num_vezes_maximo = 5
        num_vezes_minimo = 2

    Limpa.fecha_tarefa(x_origem, y_origem)
    Limpa.limpa_promocao(x_origem, y_origem)
    print('level_conta', level_conta)
    print('valor_fichas_perfil', valor_fichas_perfil)
    time.sleep(2)
    Limpa.limpa_total(x_origem, y_origem)

    if not conta_upada:
        upar(x_origem, y_origem)
        level_conta, valor_fichas_perfil = OCR_tela.level_conta(x_origem, y_origem)
        Limpa.limpa_total(x_origem, y_origem)

    if level_conta >= 10:
        print('conta para jogar mesa')
        numero_aleatorio = random.randint(num_vezes_minimo, num_vezes_maximo)
        print('Joga vezes: ', numero_aleatorio)
        mesa_upar_jogar(x_origem, y_origem, numero_aleatorio, False, blind_mesa)

    elif 4 <= level_conta < 10:
        mesa_upar_jogar(x_origem, y_origem, 0, True, blind_mesa)
        level_conta, valor_fichas_perfil = OCR_tela.level_conta(x_origem, y_origem)

    elif 1 <= level_conta < 4:
        print('conta para jogar mesa')
        numero_aleatorio = random.randint(num_vezes_minimo, num_vezes_maximo)
        print('Joga vezes: ', numero_aleatorio)
        mesa_upar_jogar(x_origem, y_origem, numero_aleatorio, False, blind_mesa)
        level_conta, valor_fichas_perfil = OCR_tela.level_conta(x_origem, y_origem)

    else:
        print('conta para jogar mesa')
        numero_aleatorio = random.randint(num_vezes_minimo, num_vezes_maximo)
        print('Joga vezes: ', numero_aleatorio)
        mesa_upar_jogar(x_origem, y_origem, numero_aleatorio, False, blind_mesa)

    print('level_conta', level_conta)
    print('valor_fichas_perfil', valor_fichas_perfil)
    Limpa.limpa_total(x_origem, y_origem)
    return level_conta, valor_fichas_perfil


def passa_corre_joga(x_origem, y_origem, valor_aposta1=40, valor_aposta2=80):  # para se fazer tarefas
    # print("passa_corre_joga")
    jogou_uma_vez = False, False
    # se esta com v azul dentro do quadrado branco
    if pyautogui.pixelMatchesColor((x_origem + 333), (y_origem + 610), (59, 171, 228), 3):
        return jogou_uma_vez

    # se esta com quadrado branco
    elif pyautogui.pixelMatchesColor((x_origem + 333), (y_origem + 610), (255, 255, 255), 3):
        pyautogui.click((x_origem + 337), (y_origem + 605))
        time.sleep(0.3)
        print("Passar")
        jogou_uma_vez = True, False
        return jogou_uma_vez
    # testa se tem a area de valores apostar
    elif pyautogui.pixelMatchesColor((x_origem + 480), (y_origem + 650), (255, 255, 255), 5):  # testa se tem area branca
        # print("area de valor branco")
        valor = OCR_tela.valor_apostar(x_origem, y_origem)
        print('Valor da aposta: ', valor)
        if (valor == valor_aposta1) or (valor == valor_aposta2):
            pyautogui.click((x_origem + 337), (y_origem + 605))  # clica no passar
            print("Valor esprado, Paga")
            jogou_uma_vez = True, False
            return jogou_uma_vez
        else:
            # pyautogui.click((x_origem + 528), (y_origem + 605))  # clica no correr
            print("Valor diferente do esperado")
            # time.sleep(3)
            jogou_uma_vez = True, True
            return jogou_uma_vez

    #  nao tem a area branca do apostar mas tem Pagar
    # se tem o pagar com um valor ja escrito
    elif (pyautogui.pixelMatchesColor((x_origem + 343), (y_origem + 598), (255, 255, 255), 5)
          and (not pyautogui.pixelMatchesColor((x_origem + 480), (y_origem + 650), (255, 255, 255), 5))):
        print('Tem o botao de pagar sem o a area de ajuste de valor')
        jogou_uma_vez = True, True
        return jogou_uma_vez

    return jogou_uma_vez


def apostar_pagar(x_origem, y_origem, sorte=True):
    jogou_uma_vez = False
    if sorte:
        # quando se tem que apostar, testa se tem a barra de ajustar a aposta
        if pyautogui.pixelMatchesColor((x_origem + 513), (y_origem + 647), (180, 202, 224), 5):
            print('barra de ajustar valor')
            # se tem a barra de ajustar a aposta
            # testar se é a ultima carta
            if pyautogui.pixelMatchesColor((x_origem + 652), (y_origem + 327), (249, 249, 249), 5):
                print('ultima carta')
                # cliaca no final da barra
                pyautogui.click((x_origem + 660), (y_origem + 647))

            else:
                print('NÂO é a ultima carta')
                # clicar no meio da barra de ajuste
                pyautogui.click((x_origem + 595), (y_origem + 647))

            for _ in range(150):
                #  teste se a barra foi deslocada, nao esta mais na posição inicial
                if not pyautogui.pixelMatchesColor((x_origem + 652), (y_origem + 327), (184, 212, 237), 5):
                    break
                time.sleep(0.01)
            # clica no apostar
            print('tem que aposta')
            pyautogui.click((x_origem + 380), (y_origem + 650))

            jogou_uma_vez = True
            return jogou_uma_vez

        elif pyautogui.pixelMatchesColor((x_origem + 342), (y_origem + 601), (255, 255, 255), 5):
            # branco de interceção de pagar e passar sem o quadrado brando
            print('clicou no Passar ou no Pagar')
            # se nao tem a barra de ajusta a posta e se tem o pagar
            pyautogui.click((x_origem + 380), (y_origem + 604))
            jogou_uma_vez = True
            return jogou_uma_vez
        return jogou_uma_vez

    else:
        # vai perder de proposito
        # testar se é a ultima carta
        print('perde')
        # quando se tem que apostar, testa se tem a barra de ajustar a aposta
        if pyautogui.pixelMatchesColor((x_origem + 513), (y_origem + 647), (180, 202, 224), 5):
            print('barra de ajustar valor')
            # se tem a barra de ajustar a aposta
            # testar se é a ultima carta

            if (pyautogui.pixelMatchesColor((x_origem + 652), (y_origem + 327), (249, 249, 249), 5)
                    or pyautogui.pixelMatchesColor((x_origem + 512), (y_origem + 232), (234, 239, 233), 5)):
                # testa se é a ultima carta ou se a a aposta do river
                print('ultima carta')
                # cliaca no correr
                pyautogui.click((x_origem + 600), (y_origem + 600))

            elif ((pyautogui.pixelMatchesColor((x_origem + 585), (y_origem + 327), (249, 249, 249), 5)
                   and not pyautogui.pixelMatchesColor((x_origem + 652), (y_origem + 327), (249, 249, 249), 5))
                  or pyautogui.pixelMatchesColor((x_origem + 517), (y_origem + 233), (234, 239, 233), 5)):
                # (tem a penultima carta e nao tem a ultima) ou aposta do Turn
                print('penultima carta')
                # cliaca no final da barra
                pyautogui.click((x_origem + 660), (y_origem + 647))
                time.sleep(0.3)
                # clica para voltar a barra um pouquinho de nada
                pyautogui.click((x_origem + 509), (y_origem + 647))
                time.sleep(0.3)

            else:
                print('NÂO é a ultima carta nem a penultima')
                # clicar no meio da barra de ajuste
                pyautogui.click((x_origem + 595), (y_origem + 647))

            for _ in range(150):
                #  teste se a barra foi deslocada, nao esta mais na posição inicial
                if not pyautogui.pixelMatchesColor((x_origem + 652), (y_origem + 327), (184, 212, 237), 5):
                    break
                time.sleep(0.01)
            # clica no apostar
            print('tem que aposta')
            pyautogui.click((x_origem + 380), (y_origem + 650))

        elif pyautogui.pixelMatchesColor((x_origem + 342), (y_origem + 601), (255, 255, 255), 5):
            # branco de interceção de pagar e passar sem o quadrado brando

            if (pyautogui.pixelMatchesColor((x_origem + 652), (y_origem + 327), (249, 249, 249), 5)
                    or pyautogui.pixelMatchesColor((x_origem + 512), (y_origem + 232), (234, 239, 233), 5)):
                # testa se é a ultima carta ou se a a aposta do river
                print('ultima carta')
                print('clicou no Correr')
                # cliaca no correr
                pyautogui.click((x_origem + 600), (y_origem + 600))
            else:
                print('Não é a ultima carta')
                print('clicou no Passar ou no Pagar')
                # se nao tem a barra de ajusta a posta e se tem o pagar
                pyautogui.click((x_origem + 380), (y_origem + 604))
            jogou_uma_vez = True
            return jogou_uma_vez
        return jogou_uma_vez


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
                or pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 674), (19, 64, 109), tolerance=19)):
            # testa se esta dentro da mesa

            pyautogui.click(947 + x_origem, 78 + y_origem)  # setinha
            time.sleep(0.3)
            pyautogui.click(925 + x_origem, 204 + y_origem)  # Levantar

            if pyautogui.pixelMatchesColor((x_origem + 455), (y_origem + 417), (25, 116, 184), tolerance=19):
                # aviso do sistema "tem certesa de que quer sair da mesa?"
                pyautogui.click(641 + x_origem, 278 + y_origem)  # clica no x do aviso do sistema "tem certesa de que quer sair da mesa?"
                print("aviso do sistema")
                time.sleep(0.3)
                pyautogui.click(947 + x_origem, 78 + y_origem)  # setinha
                time.sleep(0.3)
                pyautogui.click(925 + x_origem, 204 + y_origem)  # Levantar

    return sentado

# x_origem, y_origem = Origem_pg.x_y()
# escolher_blind(x_origem, y_origem, blind='2K/4K', lugares=5)
# sentar_mesa(x_origem, y_origem, True, '20/40', True)
# mesa_recolher(x_origem, y_origem, 2, '20/40')
# x_origem, y_origem = Origem_pg.x_y()
# cadeiras_celular(x_origem, y_origem)
# conta_cadeiras_livres_celular(x_origem, y_origem)
# joga_uma_vez(x_origem, y_origem)
# cadeiras_livres_resultado = cadeiras_livres(x_origem, y_origem )
# print("Resultado:", cadeiras_livres_resultado)
# conta_cadeiras_livres(x_origem, y_origem )
# joga_uma_vez(x_origem, y_origem)
# joga_uma_vez(x_origem, y_origem)
# Limpa.fecha_tarefa(x_origem, y_origem)
# levantar_mesa(x_origem, y_origem)
# blind_escolha = '500/1K'
# blind_escolha = '1K/2K'
# escolher_blind(x_origem, y_origem, '1K/2K')
# escolher_blind(x_origem, y_origem, blind_escolha)
# senta_com_maximo = False
# sentou = sentar_mesa(x_origem, y_origem, senta_com_maximo, blind_escolha)
# joga(x_origem, y_origem, 0, 0, 0, 0)
# passa_corre_joga(x_origem, y_origem)
# x_origem, y_origem = Origem_pg.x_y()
# senta_com_maximo = False
# sentou = sentar_mesa(x_origem, y_origem, senta_com_maximo, '200/400')
# print(sentou)
# ajuste_valor_niquel(x_origem, y_origem)
# x_origem, y_origem = Origem_pg.x_y()
# gira_niquel(x_origem, y_origem)
# sala_minima_niquel(x_origem, y_origem)
# tem_tarefa = Tarefas.comparar_imagens_tarefa(tarefas_fazer_niquel, x_origem, y_origem)
# print(tem_tarefa)
