import datetime
import random
import time

import pyautogui
from colorama import Fore

import HoraT
import IP
import Limpa
import OCR_tela
import Tarefas
import Telegran
import xp2
from F5_navegador import atualizar_navegador
from Firebase import contar_pessoas_mesa, atualizar_estatos_mesa, ler_configuracao
from Requerimentos import nome_computador
from UparAuto import upar
from BancoDadosIP import indicar_pc_desativo, indicar_pc_ativo

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0

indice_inicial = 0

blinb_rolagem = {'1/2': (534, 478, 2, 4), '2/4': (534, 504, 4, 8), '5/10': (534, 530, 10, 20), '10/20': (534, 556, 20, 40),
                 '20/40': (534, 582, 40, 80), '25/50': (548, 478, 50, 100), '50/100': (548, 504, 100, 200), '100/200': (548, 530, 200, 400),
                 '200/400': (548, 556, 400, 800), '500/1K': (548, 582, 1000, 2000), '1K/2K': (563, 478, 2000, 4000), '2K/4K': (563, 504, 4000, 8000),
                 '5K/10K': (563, 530, 10000, 20000), '10K/20K': (563, 556, 20000, 40000), '20K/40K': (563, 582, 40000, 80000),
                 '50K/100K': (571, 530, 100000, 200000), '100K/200K': (571, 556, 200000, 400000), '500K/1M': (571, 582, 1000000, 2000000)}

lista_salas_niquel = [  # 5 lugares
    {'1025': ('2040', 80, 40)}, {'1026': ('2040', 80, 40)}, {'1027': ('2040', 80, 40)}, {'1028': ('2040', 80, 40)}, {'1236': ('2040', 80, 40)},
    {'1266': ('2040', 80, 40)}, {'1645': ('2040', 80, 40)}, {'1646': ('2040', 80, 40)}, {'1647': ('2040', 80, 40)}, {'1648': ('2040', 80, 40)},
    {'1649': ('2040', 80, 40)}, {'1650': ('2040', 80, 40)}, {'1651': ('2040', 80, 40)}, {'1652': ('2040', 80, 40)},  # 3 lugares
    {'435': ('2040', 80, 40)}, {'1540': ('2040', 80, 40)}, {'1541': ('2040', 80, 40)}, {'1542': ('2040', 80, 40)}, {'1543': ('2040', 80, 40)},
    {'1767': ('2040', 80, 40)}, {'1768': ('2040', 80, 40)}, {'1769': ('2040', 80, 40)},  # 2 lugares
    {'1535': ('2040', 80, 40)}, {'1536': ('2040', 80, 40)}, {'1537': ('2040', 80, 40)}, {'1538': ('2040', 80, 40)},  # nao sei
    {'1546': ('2040', 80, 40)}, {'1765': ('2040', 80, 40)}, {'1766': ('2040', 80, 40)}, {'1545': ('2040', 80, 40)}]

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


lista_salas_jogar = [{'134': ('2550', 100, 50)}, {'135': ('2550', 100, 50)}, {'999': ('2550', 100, 50)}, {'1003': ('2550', 100, 50)},
                     {'1004': ('2550', 100, 50)}, {'1243': ('2550', 100, 50)}, {'1245': ('2550', 100, 50)}, {'1246': ('2550', 100, 50)},
                     {'1247': ('2550', 100, 50)}, {'1673': ('2550', 100, 50)}, {'1674': ('2550', 100, 50)}, {'1675': ('2550', 100, 50)},
                     {'1676': ('2550', 100, 50)}, {'1677': ('2550', 100, 50)}, {'1678': ('2550', 100, 50)}]

lista_salas_jogar2 = [{'1586': ('50100', 200, 100)}, {'1587': ('50100', 200, 100)}, {'1588': ('50100', 200, 100)}, {'1589': ('50100', 200, 100)},
                      {'1590': ('50100', 200, 100)}, {'1591': ('50100', 200, 100)}, {'1592': ('50100', 200, 100)}, {'1593': ('50100', 200, 100)},
                      {'1683': ('50100', 200, 100)}, {'1684': ('50100', 200, 100)}, {'1685': ('50100', 200, 100)}, {'1686': ('50100', 200, 100)},
                      {'1687': ('50100', 200, 100)}, {'1688': ('50100', 200, 100)}, {'1689': ('50100', 200, 100)}]

lista_salas_jogar3 = [{'172': ('100200', 200, 400)}, {'1690': ('100200', 200, 400)}, {'1691': ('100200', 200, 400)}, {'1692': ('100200', 200, 400)},
                      {'1693': ('100200', 200, 400)}, {'1694': ('100200', 200, 400)}, {'1695': ('100200', 200, 400)}, {'1696': ('100200', 200, 400)},
                      {'1697': ('100200', 200, 400)}, {'1698': ('100200', 200, 400)}, {'1699': ('100200', 200, 400)}, {'1700': ('100200', 200, 400)},
                      {'1701': ('100200', 200, 400)}, {'1702': ('100200', 200, 400)}, {'1703': ('100200', 200, 400)}]
# dicionariao numero das salas, valores das salas , e id das salas

# 100200 maximo de 40k
# 200400 maximo de 80k
# 5001k maximo de 200k
# 1k2k maximo de 400k
dicionario_salas = {
    '2550': [100, 50, ['134', '135', '999', '1003', '1004', '1243', '1245', '1246', '1247', '1673', '1674', '1675', '1676', '1677', '1678'], 500],
    '50100': [200, 100, ['1586', '1587', '1588', '1589', '1590', '1591', '1592', '1593', '1681', '1682', '1683', '1684', '1685', '1686', '1687',
                         '1688', '1689'], 1000],
    '100200': [400, 200, ['172', '472', '1690', '1691', '1692', '1693', '1694', '1695', '1696', '1697', '1698', '1699', '1700', '1701', '1702',
                          '1703'], 2000],
    '200400': [800, 400, ['1044', '1045', '1046', '1047', '1048', '1268', '1269', '1270', '1271', '1272', '1273', '1274', '1275', '1276', '1705',
                          '1706', '1707', '1708', '1709', '1710', '1711', '1712', '1713', '1714'], 4000],
    '5001K': [2000, 1000, ['192', '492', '1741', '1742', '1743', '1744', '1745', '1746', '1747', '1748', '1749'], 10000],
    '1K2K': [4000, 2000, ['1287', '1288', '1289', '1290', '1752', '1753', '1754', '1756', '1757', '1758', '1759', '1760'], 20000],
    '2K4K': [8000, 4000, ['1154', '1155', '1298', '1299', '1300', '1301', '1302', '1303', '1304', '1305'], 40000],
    '5K10K': [20000, 10000, ['1206', '1207', '1208', '1160', '1158', '1159'], 100000]
}

dicionari_PC_cadeira = {
    'PC-I5-8600K': {'cadeira_1': (659, 127), 'cadeira_2': (828, 211), 'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_5': (495, 452),
                    'cadeira_6': (276, 451), 'cadeira_7': (118, 360), 'cadeira_8': (134, 194), 'cadeira_9': (312, 131)},
    'PC-I5-9400A': {'cadeira_2': (828, 211), 'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_5': (495, 452), 'cadeira_6': (276, 451),
                    'cadeira_7': (118, 360), 'cadeira_8': (134, 194), 'cadeira_9': (312, 131), 'cadeira_1': (659, 127)},
    'PC-I5-9400B': {'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_5': (495, 452), 'cadeira_6': (276, 451), 'cadeira_7': (118, 360),
                    'cadeira_8': (134, 194), 'cadeira_9': (312, 131), 'cadeira_1': (659, 127), 'cadeira_2': (828, 211)},
    'PC-I5-9400C': {'cadeira_4': (690, 451), 'cadeira_5': (495, 452), 'cadeira_6': (276, 451), 'cadeira_7': (118, 360), 'cadeira_8': (134, 194),
                    'cadeira_9': (312, 131), 'cadeira_1': (659, 127), 'cadeira_2': (828, 211), 'cadeira_3': (847, 366)},
    'PC-I5-13400H': {'cadeira_5': (495, 452), 'cadeira_6': (276, 451), 'cadeira_7': (118, 360), 'cadeira_8': (134, 194), 'cadeira_9': (312, 131),
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
    'PC-I5-13400F': {'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_5': (495, 452), 'cadeira_6': (276, 451), 'cadeira_7': (118, 360),
                     'cadeira_8': (134, 194), 'cadeira_9': (312, 131), 'cadeira_1': (659, 127), 'cadeira_2': (828, 211)},
    'PC-I5-13400G': {'cadeira_4': (690, 451), 'cadeira_5': (495, 452), 'cadeira_6': (276, 451), 'cadeira_7': (118, 360), 'cadeira_8': (134, 194),
                     'cadeira_9': (312, 131), 'cadeira_1': (659, 127), 'cadeira_2': (828, 211), 'cadeira_3': (847, 366)},
    'PC-I5-13400I': {'cadeira_5': (495, 452), 'cadeira_6': (276, 451), 'cadeira_7': (118, 360), 'cadeira_8': (134, 194), 'cadeira_9': (312, 131),
                     'cadeira_1': (659, 127), 'cadeira_2': (828, 211), 'cadeira_3': (847, 366), 'cadeira_4': (690, 451)},
    'PC-R5-7600': {'cadeira_6': (276, 451), 'cadeira_7': (118, 360), 'cadeira_8': (134, 194), 'cadeira_9': (312, 131), 'cadeira_1': (659, 127),
                   'cadeira_2': (828, 211), 'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_5': (495, 452)},
    'PC-i3-8145U': {'cadeira_1': (659, 127), 'cadeira_2': (828, 211), 'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_5': (495, 452),
                    'cadeira_6': (276, 451), 'cadeira_7': (118, 360), 'cadeira_8': (134, 194), 'cadeira_9': (312, 131)},
    'PC-I7-9700KF': {'cadeira_1': (659, 127), 'cadeira_2': (828, 211), 'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_5': (495, 452),
                     'cadeira_6': (276, 451), 'cadeira_7': (118, 360), 'cadeira_8': (134, 194), 'cadeira_9': (312, 131)}
}

dicionario_cadeira = {'cadeira_1': (659, 127), 'cadeira_2': (828, 211), 'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_5': (495, 452),
                      'cadeira_6': (276, 451), 'cadeira_7': (118, 360), 'cadeira_8': (134, 194), 'cadeira_9': (312, 131)}

dicionario_cadeira5 = {'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_5': (495, 452), 'cadeira_6': (276, 451), 'cadeira_7': (118, 360)}

# dicionario_celular = {'cadeira_1': (645, 135), 'cadeira_2': (818, 217), 'cadeira_3': (814, 377), 'cadeira_4': (675, 473), 'cadeira_5': (484, 473),
#                       'cadeira_6': (290, 473), 'cadeira_7': (144, 377), 'cadeira_8': (156, 217), 'cadeira_9': (334, 135)}

# lista de tuplas conde se tem a coordenada de interesse e a cor da coodenada que identifica se é um humano
lista_humano_9 = [
    # # celuar
    (645, 138, 2, (96, 160, 249)), (817, 220, 2, (96, 160, 249)), (814, 380, 2, (96, 160, 249)), (675, 476, 2, (96, 160, 249)),
    (484, 476, 2, (96, 160, 249)), (292, 476, 2, (134, 179, 242)), (146, 380, 2, (134, 179, 242)), (158, 220, 2, (134, 179, 242)),
    (336, 138, 2, (134, 179, 242)),
    # # hoemem claro
    (667, 104, 2, (255, 193, 161)), (839, 186, 2, (255, 193, 161)), (836, 346, 2, (255, 193, 161)), (697, 442, 2, (255, 193, 161)),
    (506, 442, 2, (255, 193, 161)), (276, 442, 2, (255, 193, 161)), (130, 346, 2, (255, 193, 161)), (142, 186, 2, (255, 193, 161)),
    (320, 104, 2, (255, 193, 161)),
    # homem escuro
    (667, 104, 2, (128, 97, 81)), (839, 186, 2, (128, 97, 81)), (836, 346, 2, (128, 97, 81)), (697, 442, 2, (128, 97, 81)),
    (506, 442, 2, (128, 97, 81)), (276, 442, 2, (128, 97, 81)), (130, 346, 2, (128, 97, 81)), (142, 186, 2, (128, 97, 81)),
    (320, 104, 2, (128, 97, 81)),
    # # mulher claro
    (667, 104, 2, (255, 220, 185)), (839, 186, 2, (255, 220, 185)), (836, 346, 2, (255, 220, 185)), (697, 442, 2, (255, 220, 185)),
    (506, 442, 2, (255, 220, 185)), (276, 442, 2, (255, 220, 185)), (130, 346, 2, (255, 220, 185)), (142, 186, 2, (255, 220, 185)),
    (320, 104, 2, (255, 220, 185)),
    # # mulher escuro
    (667, 104, 2, (128, 110, 93)), (839, 186, 2, (128, 110, 93)), (836, 346, 2, (128, 110, 93)), (697, 442, 2, (128, 110, 93)),
    (506, 442, 2, (128, 110, 93)), (276, 442, 2, (128, 110, 93)), (130, 346, 2, (128, 110, 93)), (142, 186, 2, (128, 110, 93)),
    (320, 104, 2, (128, 110, 93))
]

lista_humano_5 = [
    # celuar
    (814, 380, 2, (96, 160, 249)), (675, 476, 2, (95, 159, 247)), (484, 476, 2, (96, 160, 249)), (292, 476, 2, (134, 179, 242)),
    (146, 380, 2, (134, 179, 242)),
    # # hoemem claro
    (836, 346, 2, (255, 193, 161)), (697, 442, 2, (255, 193, 161)), (506, 442, 2, (255, 193, 161)), (276, 442, 2, (255, 193, 161)),
    (130, 346, 2, (255, 193, 161)),
    # homem escuro
    (836, 346, 2, (128, 97, 81)), (697, 442, 2, (128, 97, 81)), (506, 442, 2, (128, 97, 81)), (276, 442, 2, (128, 97, 81)),
    (130, 346, 2, (128, 97, 81)),
    # # mulher claro
    (836, 346, 2, (255, 220, 185)), (697, 442, 2, (255, 220, 185)), (506, 442, 2, (255, 220, 185)), (276, 442, 2, (255, 220, 185)),
    (130, 346, 2, (255, 220, 185)),
    # # mulher escuro
    (836, 346, 2, (128, 110, 93)), (697, 442, 2, (128, 110, 93)), (506, 442, 2, (128, 110, 93)), (276, 442, 2, (128, 110, 93)),
    (130, 346, 2, (128, 110, 93)),
]  # +32 +11

cadeiras_vazias_quando_sentado_azul_9 = [
    (661, 148, 1, (23, 21, 20)), (831, 232, 1, (20, 19, 18)), (849, 388, 1, (20, 19, 18)), (671, 451, 1, (20, 19, 18)),
    (476, 451, 1, (21, 19, 18)), (257, 451, 1, (14, 14, 14)), (120, 381, 1, (33, 31, 30)), (136, 216, 1, (21, 19, 18)),
    (314, 152, 1, (18, 17, 16))
]

cadeiras_vazias_quando_sentado_azul_5 = [
    (849, 388, 1, (20, 19, 18)), (671, 451, 1, (20, 19, 18)), (476, 451, 1, (21, 19, 18)), (257, 451, 1, (14, 14, 14)), (120, 381, 1, (33, 31, 30))
]

cadeiras_vazias_quando_sentado_verde_9 = [
    (661, 148, 1, (22, 13, 10)), (831, 232, 1, (16, 12, 8)), (838, 386, 1, (33, 22, 20)), (671, 451, 1, (57, 50, 47)),
    (476, 451, 1, (27, 24, 22)), (257, 451, 1, (60, 52, 49)), (120, 381, 1, (30, 23, 21)), (136, 216, 1, (16, 11, 8)),
    (314, 152, 1, (17, 12, 8))
]

cadeiras_vazias_quando_sentado_verde_5 = [
    (838, 386, 1, (33, 22, 20)), (671, 451, 1, (57, 50, 47)), (476, 451, 1, (27, 24, 22)), (257, 451, 1, (60, 52, 49)), (120, 381, 1, (30, 23, 21))
]

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


def mesa_sem_humanos(x_origem, y_origem, lugares=9):
    # print('Testa humanos')
    """
    Verifica se todas as cadeiras em torno de uma mesa nao tem celular ou avata do jogo indicado humano.

    Parâmetros:
    - x_origem: A coordenada X da origem da mesa.
    - y_origem: A coordenada Y da origem da mesa.
    - cor_cadeira: A cor da cadeira em formato RGB.
    - tolerancia: A tolerância para correspondência de cor.

    Retorna:
    - True se todas as cadeiras estiverem livres, False se pelo menos uma cadeira estiver ocupada.
    """

    if lugares == 9:
        for x, y, tolerancia, cor_celular in lista_humano_9:

            if pyautogui.pixelMatchesColor(x_origem + x, y_origem + y, cor_celular, tolerance=tolerancia):
                print('\nPelo menos um humano esta na mesa posição: ', x, y, ' , cor: ', cor_celular, '.\n')
                return False
    else:
        for x, y, tolerancia, cor_celular in lista_humano_5:

            if pyautogui.pixelMatchesColor(x_origem + x, y_origem + y, cor_celular, tolerance=tolerancia):
                print('\nPelo menos um humano esta na mesa posição: ', x, y, ' , cor: ', cor_celular, '.\n')
                return False
    # print('Todas as cadeiras estão livres de celular.')
    return True


def testa_mesa_completa(x_origem, y_origem, lugares=9, cor_da_mesa='verde'):
    print('Testa mesa completa')
    """
    Verifica se todas as cadeiras em torno de uma mesa estao ocupadas.

    Parâmetros:
    - x_origem: A coordenada X da origem da mesa.
    - y_origem: A coordenada Y da origem da mesa.
    - cor_cadeira: A cor da cadeira em formato RGB.
    - tolerancia: A tolerância para correspondência de cor.

    Retorna:
    - True se todas as cadeiras estiverem estiver ocupada e False se pelo menso uma estiver vazia.
    """
    if cor_da_mesa == 'verde':
        for indece, (x, y, tolerancia, cor_celular) in enumerate(cadeiras_vazias_quando_sentado_verde_9):
            if indece in (0, 1, 7, 8) and lugares == 5:
                continue

            if pyautogui.pixelMatchesColor(x_origem + x, y_origem + y, cor_celular, tolerance=tolerancia):
                print('\nPelo uma cadeira vazia.\n')
                return False

    else:
        for indece, (x, y, tolerancia, cor_celular) in enumerate(cadeiras_vazias_quando_sentado_azul_9):
            if indece in (0, 1, 7, 8) and lugares == 5:
                continue

            if pyautogui.pixelMatchesColor(x_origem + x, y_origem + y, cor_celular, tolerance=tolerancia):
                print('\nPelo uma cadeira vazia.\n')
                return False
    print('Todas as cadeiras estão ocupadas.')
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
    print('sentar_mesa')
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
    ficha_suficiente = True
    if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 674), (19, 65, 109), tolerance=5):
        print('possivel aviso so sistema, roda um limpa jogando')
        Limpa.limpa_jogando(x_origem, y_origem)
        Limpa.limpa_promocao(x_origem, y_origem)  # time.sleep(0.5)

    # testa se esta aparecendo o botao azul "Jogar agora"
    if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 674), (27, 92, 155), tolerance=5):
        # testa se esta dentro da mesa

        # print("Está dentro da mesa")

        if not (pyautogui.pixelMatchesColor(495 + x_origem, 627 + y_origem, (15, 160, 220), tolerance=10)):
            # testa se tem o botao jogar agoar apara seber se ja ta sentado
            # print('Já está sentado')
            sentou = True
            ficha_suficiente = True
            return sentou, ficha_suficiente
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
                sentou = False
                ficha_suficiente = True
                return sentou, ficha_suficiente

            if teste_celular:
                if not mesa_sem_humanos(x_origem, y_origem):
                    print('Sai da mesa pq tem humanos')
                    sentou = False
                    ficha_suficiente = True
                    return sentou, ficha_suficiente

            for _ in range(9):
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
                                        ficha_suficiente = False
                                        return sentou, ficha_suficiente

                                    elif pyautogui.pixelMatchesColor((x_origem + 373), (y_origem + 339), (63, 92, 123), tolerance=5):
                                        pyautogui.click((x_origem + 641), (y_origem + 278))  # fecha aviso do sistema
                                        print('Desculpe! Não possui fichas suficientes')
                                        sentou = False
                                        ficha_suficiente = False
                                        return sentou, ficha_suficiente

                                    elif pyautogui.pixelMatchesColor((x_origem + 340), (y_origem + 336), (33, 66, 103), tolerance=5):
                                        # Você não pode jogar com duas contas ao mesmo tempo
                                        pyautogui.click((x_origem + 641), (y_origem + 278))  # fecha aviso do sistema
                                        print('Você não pode jogar com duas contas ao mesmo tempo')
                                        sentou = False
                                        ficha_suficiente = False
                                        return sentou, ficha_suficiente

                                    elif pyautogui.pixelMatchesColor((x_origem + 369), (y_origem + 341), (33, 66, 103), tolerance=5):
                                        # Este lugar ja foi ocupado
                                        pyautogui.click((x_origem + 641), (y_origem + 278))  # fecha aviso do sistema
                                        print("Este lugar ja foi ocupado")
                                        sentou = False
                                        ficha_suficiente = True
                                        break
                                    else:
                                        pyautogui.click((x_origem + 641), (y_origem + 278))  # fecha aviso do sistema
                                        print('outro amensagem com aviso do sistema')
                                        ficha_suficiente = True
                                        break

                                else:
                                    print('sentar_mesa: Sentou')
                                    sentou = True
                                    ficha_suficiente = True
                                    return sentou, ficha_suficiente

                        elif (pyautogui.pixelMatchesColor(avisodo_sistema_x, avisodo_sistema_y, cor_nao_possui_fichas,
                                                          tolerance=10) or pyautogui.pixelMatchesColor(avisodo_sistema_x, avisodo_sistema_y,
                                                                                                       cor_nao_possui_fichas2, tolerance=10)):
                            # se assim que clicar na setinha nao ter fichas suficiente
                            pyautogui.click((x_origem + 641), (y_origem + 278), button='left')  # clica no fechar mensagem de nao tem fichas
                            print("Não possui fichas suficiente")
                            sentou = False
                            ficha_suficiente = False
                            return sentou, ficha_suficiente
                else:
                    print('Não tem cadeira livre')
                    break

    print('Não está dentro da mesa')
    return sentou, ficha_suficiente


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

    for _ in range(30):  # Marcar apenas as salas de 9 lugares ou 5 lugares
        if pyautogui.pixelMatchesColor((x_origem + 139), (y_origem + 492), (201, 201, 201), tolerance=2):
            if lugares == 9:
                print('Sala de 9 lugares marcada')
                break
            else:
                pyautogui.click(x_origem + 139, y_origem + 492)
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
            atualizar_navegador()
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

        elif (pyautogui.pixelMatchesColor((x_origem + 435), (y_origem + 264), (246, 126, 0), tolerance=5) or pyautogui.pixelMatchesColor(
                (x_origem + 435), (y_origem + 264), (80, 178, 0), tolerance=5)):
            # barra verde ou barra laranja
            print("Não tem sala vazia")
            return "Não tem sala vazia"

        elif pyautogui.pixelMatchesColor((x_origem + 205), (y_origem + 265), (46, 87, 132), tolerance=3):  # testa se existe sala com este numero
            print("Não existe sala com esse numero")
            if j > 15:
                return "Não existe sala com esse numero"
        time.sleep(0.1)
    return "Não entrou na sala"


def ajuste_valor_niquel(x_origem, y_origem, ajusta_aposta=200):
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


def escolher_sala_por_numero(x_origem, y_origem, num_mesa, blind_mesa, lugares=9):
    print('sala_minima_niquel')
    if blind_mesa == "12":
        pyautogui.doubleClick(130 + x_origem, 200 + y_origem)  # clica na lista de iniciantes
    elif blind_mesa == "2040" or blind_mesa == "24":
        pyautogui.doubleClick(280 + x_origem, 200 + y_origem)
        # clica na lista de aprendizes  # if not pyautogui.pixelMatchesColor((x_origem + 280), (y_origem + 210), (73, 177, 9), tolerance=5):
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

    if pyautogui.pixelMatchesColor((x_origem + 685), (y_origem + 360), (215, 234, 244), tolerance=1):
        print("teste_limpo: Esta no Lobby, ta limpo")
    else:
        Limpa.limpa_promocao(x_origem, y_origem)
    print('j')
    for j in range(20):
        print(j)
        if pyautogui.pixelMatchesColor((x_origem + 310), (y_origem + 264), (95, 106, 122), tolerance=5):
            # erro ao buscar sala, fica uma faixa cinza na linha da sala
            print('Erro ao buscar sala, vai ser dado um F5')
            # pyautogui.press('f5')
            atualizar_navegador()
            time.sleep(25)
            break

        if pyautogui.pixelMatchesColor((x_origem + 435), (y_origem + 264), (26, 29, 33), tolerance=5):
            # testa se tem sala com pelo menos um lugar vazio, olha se tem preto no fim da barra de ocupação
            pyautogui.doubleClick(490 + x_origem, 263 + y_origem)  # clica para entar na sala vazia
            print('Clica para entrar em uma sala com lugar disponível')
            print('i')
            for i in range(40):
                print(i)
                if pyautogui.pixelMatchesColor((x_origem + 435), (y_origem + 264), (26, 29, 33), tolerance=5):
                    # testa se tem sala com pelo menos um lugar vazio, olha se tem preto no fim da barra de ocupação
                    pyautogui.doubleClick(490 + x_origem, 263 + y_origem)  # clica para entar na sala vazia
                    cont_erro_entrar_mesa += 1

                Limpa.limpa_jogando(x_origem, y_origem)
                Limpa.limpa_promocao(x_origem, y_origem)

                if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 674), (27, 92, 155), tolerance=19):
                    # testa se esta dentro da mesa
                    # Limpa.limpa_jogando(x_origem, y_origem)

                    if not mesa_sem_humanos(x_origem, y_origem, lugares):
                        print('Sai da mesa pq tem humanos')
                        return False, True

                    num_sala = OCR_tela.numero_sala(x_origem, y_origem)
                    print("num_sala", num_sala, 'num_mesa', num_mesa)

                    if num_sala == num_mesa:
                        print("Esta na sala certa")
                        return True, True
                    else:
                        print("Esta na sala errada")
                        return False, True

                time.sleep(1)
                if cont_erro_entrar_mesa >= 5:
                    print('cont_erro_entrar_mesa')
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
        # print("não tem 10 auto")
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
        # print("não tem 10 auto")
        gira = False
        return gira


def joga(x_origem, y_origem, ajusta_aposta):
    global lista_salas_niquel
    blind_mesa = None
    sentou = False

    if ajusta_aposta == 200:
        tarefas_fazer = ('Jogar o caca-niquel da mesa 150 vezes', 'Jogar o caca-niquel da mesa 70 vezes', 'Jogar o caca-niquel da mesa 10 vezes')

    elif ajusta_aposta == 2000:
        tarefas_fazer = (
            'Ganhar 100.000 fichas no caca niquel da mesa', 'Ganhar 30.000 fichas no caca niquel da mesa',
            'Ganhar 10.000 fichas no caca niquel da mesa')

    continua_jogando = True
    meta_atigida = False

    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
        return "sair da conta"

    while continua_jogando:  # permanece joghando
        senta_com_maximo = False
        # print('joga mesa')
        if (pyautogui.pixelMatchesColor((x_origem + 534), (y_origem + 357), (70, 126, 56), tolerance=10) or pyautogui.pixelMatchesColor(
                (x_origem + 534), (y_origem + 357), (23, 121, 166), tolerance=10)):
            print('mesa esta limpa')
        else:
            Limpa.fecha_tarefa(x_origem, y_origem)
            Limpa.limpa_jogando(x_origem, y_origem)
            Limpa.limpa_promocao(x_origem, y_origem)

        sentou, ficha_suficiente = sentar_mesa(x_origem, y_origem, senta_com_maximo, blind_mesa)
        # print("Sentou : ", sentou)

        if sentou:
            # print("esta sentado")
            passa_corre_joga(x_origem, y_origem, valor_aposta1, valor_aposta2)
            auto10 = gira_10auto(x_origem, y_origem)
            if auto10:
                # Limpa.limpa_abre_tarefa2(x_origem, y_origem)
                Limpa.limpa_abre_tarefa(x_origem, y_origem, com_pausa=False)
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
                    blind_certo, sala_existe = escolher_sala_por_numero(x_origem, y_origem, num_mesa, blind_mesa, lugares=5)
                    if not sala_existe:
                        # Remova o item da posição específica
                        item_removido = lista_salas_niquel.pop(indice)
                        # Adicione o item ao final da lista
                        lista_salas_niquel.append(item_removido)

                    if blind_certo:
                        aposta, auto10 = ajuste_valor_niquel(x_origem, y_origem, ajusta_aposta)

                        sentou, ficha_suficiente = sentar_mesa(x_origem, y_origem, senta_com_maximo, blind_mesa)

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
                # pyautogui.press('f5')
                atualizar_navegador()
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


def mesa_upar_jogar(x_origem, y_origem, numero_jogadas=40, upar=False, blind_mesa='100200', apostar=True, recolher=False, level_conta=4,
                    subir_level=False, jogar=False, slot=False, ajusta_aposta=200):
    print('mesa_upar_jogar')

    global dicionario_salas, indice_inicial
    sentou = False
    teste_humano = False
    continua_jogando = True
    jogou_uma_vez = False
    jogou_uma_vez_mesa_completa = False
    humano = False
    mesa_completa = False
    num_mesa = ''
    cont_jogou = 0
    cont_limpa_jogando = 0

    cont_total_jogadas = 0
    cont_slot = 0
    JOGADAS_UPAR = 280
    SLOT_UPAR = 200
    LEVEL_UPAR = 7
    JOGADAS_SLOT_SOMA = 511
    indice_atual = None
    pular_sala = False
    reinicia_variaveis = True
    if recolher:
        senta_com_maximo = True
    else:
        senta_com_maximo = False

    meta_atigida = False

    # Use a lista apropriada com base no valor da variável blind_mesa
    # Captura os valores do dicionário em função dos blindes das mesas
    valor_aposta1 = dicionario_salas[blind_mesa][0]
    valor_aposta2 = dicionario_salas[blind_mesa][1]
    lista_salas = dicionario_salas[blind_mesa][2]

    print('\nlista_salas', lista_salas, '\n')
    print('valores', valor_aposta1, valor_aposta2, '\n')

    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
        return "sair da conta"

    if upar:
        cont_total_jogadas = (level_conta - int(level_conta)) * 10000
        xp2.pega_2xp(x_origem, y_origem)

    if slot:
        if ajusta_aposta == 200:
            tarefas_fazer = ('Jogar o caca-niquel da mesa 150 vezes', 'Jogar o caca-niquel da mesa 70 vezes', 'Jogar o caca-niquel da mesa 10 vezes')

        elif ajusta_aposta == 2000:
            tarefas_fazer = (
                'Ganhar 100.000 fichas no caca niquel da mesa', 'Ganhar 30.000 fichas no caca niquel da mesa',
                'Ganhar 10.000 fichas no caca niquel da mesa')

    Limpa.fecha_tarefa(x_origem, y_origem)
    Limpa.limpa_jogando(x_origem, y_origem)
    Limpa.limpa_promocao(x_origem, y_origem)
    sentou, ficha_suficiente = sentar_mesa(x_origem, y_origem, senta_com_maximo, blind_mesa, True)

    time_encher_mesa = time_comecou = time_fazer_jogada = time.perf_counter()

    print('entra no loop do mesa_upar_jogar')
    print('status do sentar : ', sentou)

    if datetime.datetime.now().time() > datetime.time(23, 00, 0):
        continua_jogando = False

    if not ficha_suficiente:
        continua_jogando = False

    if subir_level:
        xp2.pega_2xp(x_origem, y_origem)
        LEVEL_UPAR = 19.0511
        cont_slot = 0
        if datetime.datetime.now().time() > datetime.time(23, 50, 0):
            continua_jogando = False

    while continua_jogando:  # permanece joghando

        if not ficha_suficiente:
            print('Não tem fichas suficientes')
            break

        if reinicia_variaveis:
            print('reiniciando as variaveis')
            if recolher:
                atualizar_estatos_mesa('Ainda não sentado ' + num_mesa)
                indicar_pc_desativo()
            Limpa.limpa_total(x_origem, y_origem)
            Limpa.limpa_jogando(x_origem, y_origem)
            jogou_uma_vez = False
            humano = False
            teste_humano = False
            pular_sala = True
            mesa_completa = False
            sentou = False
            cont_limpa_jogando = 45
            time_encher_mesa = time_fazer_jogada = time.perf_counter()
            reinicia_variaveis = False
            if not recolher:
                IP.testa_trocar_IP()  # ve se tem que trocar ip

        cont_limpa_jogando += 1
        if cont_limpa_jogando > 10:
            cont_limpa_jogando = 0
            # testa se a mesa esta limpa
            if (pyautogui.pixelMatchesColor((x_origem + 534), (y_origem + 357), (70, 126, 56), tolerance=10)
                    or pyautogui.pixelMatchesColor((x_origem + 534), (y_origem + 357), (23, 121, 166), tolerance=10)):
                print('Mesa esta limpa')

            else:
                print('Mesa nao esta limpa')
                Limpa.fecha_tarefa(x_origem, y_origem, jogando=True)
                Limpa.limpa_jogando(x_origem, y_origem)
                Limpa.limpa_promocao(x_origem, y_origem)

            if pyautogui.pixelMatchesColor((x_origem + 38), (y_origem + 526), (187, 153, 111), tolerance=19):
                print("Presentinho de dentro da mesa")
                pyautogui.click(x_origem + 38, y_origem + 526)

            if not pyautogui.pixelMatchesColor((x_origem + 637), (y_origem + 68), (43, 14, 10), tolerance=19):
                print("Presente de fazer tarefa")
                pyautogui.click(x_origem + 637, y_origem + 68)

            if pyautogui.pixelMatchesColor(495 + x_origem, 627 + y_origem, (15, 160, 220), tolerance=10):
                print('Não esta sentado')
                reinicia_variaveis = True
                continue

            sentou, ficha_suficiente = sentar_mesa(x_origem, y_origem, senta_com_maximo, blind_mesa, True)
            if (not sentou) and recolher:
                atualizar_estatos_mesa('Ainda não sentado ' + num_mesa)
                indicar_pc_desativo()

            # Cálculo do tempo decorrido desde que o jogador entrou no jogo
            tempo_decorrido = time.perf_counter() - time_comecou
            # Conversão de segundos para horas, minutos e segundos
            horas = int(tempo_decorrido // 3600)
            minutos = int((tempo_decorrido % 3600) // 60)
            segundos = int(tempo_decorrido % 60)

            # Impressão do tempo decorrido
            print(f"Tempo jogando: {horas:02d}:{minutos:02d}:{segundos:02d}")

            if not ficha_suficiente:
                print('Não tem fichas suficientes')
                break

            if (tempo_decorrido >= 300) and (not upar) and (not recolher) and (not jogar) and (not slot):
                print('\nLimite de tempo jogando mesa, abandona tentativa e pega uma nova conta.\n')
                break

            if ((time.perf_counter() - time_encher_mesa) > 120) and recolher and (not mesa_completa):
                print('\nLimite de tempo esperando a mesa ficar completa durante o recolhimento, muda de mesa\n')
                reinicia_variaveis = True
                continue

            if (time.perf_counter() - time_fazer_jogada > 100) and (not jogar) and (not slot):
                print('\nLimite de tempo sem jogar, 100 segundos\n')
                reinicia_variaveis = True
                continue

            # if datetime.datetime.now().time() > datetime.time(23, 50, 0):
            #     print('\nPara de jogar atingiu o limite de 23:30\n')
            #     break

            if not recolher:
                if HoraT.fim_tempo_tarefa():
                    Limpa.limpa_total(x_origem, y_origem)
                    print('Fim do horario destinado a tarefas')
                    break

            if upar and (cont_slot < SLOT_UPAR):
                if gira_niquel(x_origem, y_origem):
                    cont_slot += 10

        if slot or jogar:

            meta_atigida, pontos = Tarefas.tem_tarefa_para_recolher(x_origem, y_origem)

            if gira_10auto(x_origem, y_origem):
                Limpa.limpa_abre_tarefa(x_origem, y_origem, com_pausa=False)
                print('manda recolher')
                Tarefas.recolher_tarefa(x_origem, y_origem)
                print('procura se ainda tem tarefa')

                continua_jogando, tarefa = Tarefas.comparar_listas_fazendo_tarefa(tarefas_fazer, x_origem, y_origem)
                meta_atigida, pontos = Tarefas.meta_tarefas(x_origem, y_origem)

                if Limpa.limpa_total_fazendo_tarefa(x_origem, y_origem) == "sair da conta":
                    return "sair da conta"
                IP.testa_trocar_IP()  # ve se tem que trocar ip

            if (not continua_jogando) or meta_atigida:
                Limpa.limpa_abre_tarefa(x_origem, y_origem, com_pausa=False)
                print('manda recolher')
                Tarefas.recolher_tarefa(x_origem, y_origem)
                print('procura se ainda tem tarefa')
                continua_jogando, tarefa = Tarefas.comparar_listas_fazendo_tarefa(tarefas_fazer, x_origem, y_origem)
                meta_atigida, pontos = Tarefas.meta_tarefas(x_origem, y_origem)
                if (not continua_jogando) or meta_atigida:
                    Limpa.limpa_total(x_origem, y_origem)
                    print('Atingiu a meta de pontos do dia')
                    break

            if (pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 117), (72, 71, 76), tolerance=5) or
                    pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 117), (22, 21, 23), tolerance=5)):
                pyautogui.click(821 + x_origem, 138 + y_origem)  # clica no fechar tarefa
                print('fecha lista tarefas jogando')

            gira_niquel(x_origem, y_origem)

        if jogou_uma_vez:
            if pyautogui.pixelMatchesColor((x_origem + 663), (y_origem + 538), (86, 169, 68), tolerance=20):
                # testa se apareceu as mensagens verdes na parte de baixo
                print('Fim da partida')
                cont_jogou += 1
                if jogou_uma_vez_mesa_completa and recolher:
                    print('Jogou uma partida com a mesa completa')
                    break
                if upar:
                    print(Fore.YELLOW + f"Esta upando a conta. Jogou vezes igua a: {cont_jogou}."
                                        f"\nSlote vezes: {cont_slot}."
                                        f"\n Jogadas total: {cont_total_jogadas}" + Fore.RESET)
                    if cont_jogou % 5 == 0:  # testa se tem que trocar ip a casa 5 jogadas
                        level_conta, valor_fichas_perfil = OCR_tela.level_conta(x_origem, y_origem)
                        cont_total_jogadas = (level_conta - int(level_conta)) * 10000
                        if subir_level:
                            xp2.pega_2xp(x_origem, y_origem)
                        IP.testa_trocar_IP()  # ve se tem que trocar ip
                        if level_conta >= LEVEL_UPAR:
                            level_conta, valor_fichas_perfil = OCR_tela.level_conta(x_origem, y_origem)

                    if level_conta >= LEVEL_UPAR:
                        if subir_level:
                            break
                        if (cont_total_jogadas >= JOGADAS_UPAR) and (cont_slot >= SLOT_UPAR):
                            print(Fore.YELLOW + f"Terminou de upoar. "
                                                f"\nJogou vezes igua a: {cont_jogou}."
                                                f"\nSlote vezes: {cont_slot}."
                                                f"\n Jogadas total: {cont_total_jogadas}."
                                                f"\nJogadas + Slote" + Fore.RESET)
                            break

                        if (cont_total_jogadas + cont_slot) >= JOGADAS_SLOT_SOMA:
                            print(Fore.YELLOW + f"Terminou de upoar. "
                                                f"\nJogou vezes igua a: {cont_jogou}."
                                                f"\nSlote vezes: {cont_slot}."
                                                f"\n Jogadas total: {cont_total_jogadas}."
                                                f"\nJogadas + Slote" + Fore.RESET)
                            break

                else:
                    print('Não esta upando. Jogou vezes igua a: ', cont_jogou, ' .Limite de jogadas: ', numero_jogadas)
                    if (cont_jogou >= numero_jogadas) and (not recolher) and (not jogar) and (not slot):
                        break

                jogou_uma_vez = False
                if not mesa_sem_humanos(x_origem, y_origem, 5):
                    print('Sair da mesa fim da jogada com humanos na mesa')
                    humano = True
                else:
                    humano = False

        else:
            # mensagem verde
            if pyautogui.pixelMatchesColor((x_origem + 663), (y_origem + 538), (86, 169, 68), tolerance=20):
                print('Mensagem verde fim da jogada')
                for i in range(10):
                    time.sleep(0.3)
                    if not mesa_sem_humanos(x_origem, y_origem, 5):
                        print('Sair da mesa fim da jogada com humanos na mesa')
                        humano = True
                        reinicia_variaveis = True
                        break
                    else:
                        humano = False
                print('Terminou o for humanos :', humano)

                if (not humano) and recolher:
                    mesa_completa = testa_mesa_completa(x_origem, y_origem, 5)
                    print('Reconhecimenteo de mesa completa: ', mesa_completa)
                    lugares_ocupados = contar_pessoas_mesa(num_mesa)
                    print('Firebase mesa com lugares ocupadas:', lugares_ocupados)

                    if mesa_completa and (lugares_ocupados < 5):
                        # testa se a mesa esta completa porem no firebase nao tem 5 pessoas
                        if teste_humano:  # para levantar so na segunada rodada
                            humano = True
                            print('\nJogador humano na mesa, troca de mesa\n')
                            reinicia_variaveis = True
                            continue
                        teste_humano = True
                    else:
                        teste_humano = False

                    if lugares_ocupados >= 5:
                        mesa_completa = True
                        time_encher_mesa = time_fazer_jogada = time.perf_counter()
                    elif lugares_ocupados == 4:
                        time_encher_mesa = time_fazer_jogada = time.perf_counter()
                        mesa_completa = False
                    else:
                        mesa_completa = False
                    print('Mesa esta com todas as caderas completas: ', mesa_completa)

            else:
                if not mesa_sem_humanos(x_origem, y_origem, 5):
                    print('Sair da mesa, humanos na mesa')
                    humano = True
                    print('\nJogador humano na mesa, troca de mesa\n')
                    reinicia_variaveis = True
                    continue
                else:
                    humano = False

        if humano:
            print('\nJogador humano na mesa, troca de mesa\n')
            reinicia_variaveis = True
            continue

        if sentou:
            if not humano:
                if recolher:
                    atualizar_estatos_mesa(num_mesa)
                    indicar_pc_ativo()
                    if mesa_completa:
                        jogou = apostar_pagar(x_origem, y_origem)
                        if jogou:
                            jogou_uma_vez_mesa_completa = True
                    else:
                        lugares_ocupados = contar_pessoas_mesa(num_mesa)
                        if lugares_ocupados < 5:
                            lento = True
                        else:
                            lento = False
                        (jogou, humano) = passa_corre_joga(x_origem, y_origem, valor_aposta1, valor_aposta2, lento)
                else:
                    if apostar:
                        jogou = apostar_pagar_jogar_mesa(x_origem, y_origem)
                    else:
                        (jogou, humano) = passa_corre_joga(x_origem, y_origem, valor_aposta1, valor_aposta2, lento=False)
                if jogou:
                    time_fazer_jogada = time.perf_counter()
                    jogou_uma_vez = True

        else:
            humano = False
            reinicia_variaveis = False
            print("ainda nao esta sentado")
            if recolher:
                indicar_pc_desativo()
            for i in range(3):
                print('indice_inicial', indice_inicial)
                if not indice_inicial:
                    indice_inicial = 0
                if not indice_atual:
                    indice_atual = 0
                for indice, num_mesa in enumerate(lista_salas):
                    try:
                        if indice_inicial > indice:
                            print('Porcurando o indece / mesa: ', indice, num_mesa)
                            # faz o for interagir ate chegar na ultima sala que foi usada anteriormente
                            # troca o valor para que na proxima interação possamos iniciar do inicios da lista
                            continue

                        if (indice == indice_atual) and pular_sala:
                            print('Pula o indice / mesa: ', indice, num_mesa)
                            continue  # Pule a primeira iteração, começando pelo segundo item
                    except Exception as e:
                        print(e)

                    print('Continuar, indece / mesa para tentar sentar: ', indice, num_mesa)
                    IP.tem_internet()
                    Limpa.limpa_jogando(x_origem, y_origem)
                    Limpa.limpa_total(x_origem, y_origem)
                    blind_certo, sala_existe = escolher_sala_por_numero(x_origem, y_origem, num_mesa, blind_mesa, lugares=5)

                    if not sala_existe:
                        # Remova o item da posição específica
                        item_removido = lista_salas.pop(indice)
                        # Adicione o item ao final da lista
                        lista_salas.append(item_removido)

                    if blind_certo:
                        if upar or joga or slot:
                            aposta, auto10 = ajuste_valor_niquel(x_origem, y_origem, ajusta_aposta=200)
                        else:
                            aposta, auto10 = True, True
                        sentou, ficha_suficiente = sentar_mesa(x_origem, y_origem, senta_com_maximo, blind_mesa, True)
                        if sentou and aposta and auto10 and ficha_suficiente:
                            if recolher:
                                atualizar_estatos_mesa(num_mesa)
                                indicar_pc_ativo()
                                mesa_completa = testa_mesa_completa(x_origem, y_origem, 5)

                            time_encher_mesa = time_fazer_jogada = time.perf_counter()
                            print('esta tudo ok, sentado na mesa:', num_mesa)
                            if indice:
                                indice_atual = indice
                            else:
                                indice_atual = 0
                            indice_inicial = 0
                            reinicia_variaveis = False
                            pular_sala = False
                            if (upar and cont_slot < SLOT_UPAR) or slot:
                                gira_niquel(x_origem, y_origem)
                            break
                        else:
                            reinicia_variaveis = True

                    if indice_inicial == indice and indice_inicial != 0:
                        indice_inicial = 0
                        i = 0
                        break

                    indice_inicial = 0

                if i == 1:
                    pular_sala = False

                if sentou:
                    reinicia_variaveis = False
                    break
                else:
                    reinicia_variaveis = True

            if not sentou:
                indice_inicial = 0
                reinicia_variaveis = True
                print("rodou a lista de mesas 2x, da um F5 para recarregar as mesas")
                IP.tem_internet()
                print('f5')
                # pyautogui.press('f5')
                atualizar_navegador()
                time.sleep(25)

    if recolher:
        atualizar_estatos_mesa('retornará na mesa ' + num_mesa)
        indicar_pc_desativo()

    if indice_atual:
        indice_inicial = indice_atual
    else:
        indice_inicial = 0

        # # Ao final da função, atribui o valor da lista utilizada dentro da função à lista global
    dicionario_salas[blind_mesa][2] = lista_salas

    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
        return "sair da conta"

    Limpa.limpa_jogando(x_origem, y_origem)
    return


def mesa_upar_jogar_recolher_slote(x_origem, y_origem, funcoes='', apostar=False, blind_mesa='100200', ajusta_aposta=200, lugares=5,
                                   level_conta=4, numero_jogadas=40):
    print('mesa_upar_jogar_recolher_slote')

    """ a função pode executar 'upar', 'recolher', 'subir_level', 'jogar', 'slot', 'tarefa_mesa'"""

    global dicionario_salas, indice_inicial

    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
        return "sair da conta"
    Limpa.fecha_tarefa(x_origem, y_origem)
    Limpa.limpa_jogando(x_origem, y_origem)
    Limpa.limpa_promocao(x_origem, y_origem)

    valor_aposta1 = dicionario_salas[blind_mesa][0]
    valor_aposta2 = dicionario_salas[blind_mesa][1]
    lista_salas = dicionario_salas[blind_mesa][2]
    indice_atual = None
    pular_sala = False

    print(f'\nLista_salas: {lista_salas}, valores: {valor_aposta1}, {valor_aposta2}\n')

    continua_jogando = True
    cont_limpa_jogando = 0
    reinicia_variaveis = True
    tarefas_fazer = ()

    jogou_uma_vez = False
    humano = False
    teste_humano = False
    jogou_uma_vez_mesa_completa = False
    mesa_completa = False
    num_mesa = ''
    cont_jogou = 0
    cont_total_jogadas = 0

    LEVEL_SUBIR_LEVEL = 13.0511


    # 'upar', 'recolher', 'subir_level', 'jogar', 'slot', 'tarefa_mesa'
    match funcoes:
        case 'recolher':
            print('case recolher')
            senta_com_maximo = True

        case 'upar':
            print('case upar')
            senta_com_maximo = False

        case 'subir_level':
            print('case subir_level')
            senta_com_maximo = False
            xp2.pega_2xp(x_origem, y_origem)
            cont_total_jogadas = (level_conta - int(level_conta)) * 10000
            LEVEL_SUBIR_LEVEL = 13.0511

        case 'slot':
            print('case slot')
            senta_com_maximo = False
            if ajusta_aposta == 200:
                tarefas_fazer = (
                    'Jogar o caca-niquel da mesa 150 vezes',
                    'Jogar o caca-niquel da mesa 70 vezes',
                    'Jogar o caca-niquel da mesa 10 vezes')
            elif ajusta_aposta == 2000:
                tarefas_fazer = (
                    'Ganhar 100.000 fichas no caca niquel da mesa',
                    'Ganhar 30.000 fichas no caca niquel da mesa',
                    'Ganhar 10.000 fichas no caca niquel da mesa')

        case 'tarefa_mesa':
            print('case tarefa_mesa')
            senta_com_maximo = False
            tarefas_fazer = (
                'Jogar 5 maos em qualquer mesa',
                'Jogar 10 maos em qualquer mesa',
                'Jogar 20 maos em uma mesa com blinds acima de',
                'Jogar 20 maos em uma mesa com blinds acima de 25',
                'Jogar 20 maos em uma mesa com blinds acima de 50',
                'Jogar 20 maos em uma mesa com blinds acima de 100',
                'Jogar 40 maos em uma mesa com blinds acima de',
                'Jogar 40 maos em uma mesa com blinds acima de 50',
                'Jogar 40 maos em uma mesa com blinds acima de 100')

        case 'jogar':
            print('case jogar')
            senta_com_maximo = False

        case _:
            senta_com_maximo = False
            print(f' passou o primeiro match, função {funcoes} não tem ajustes')

    sentou, ficha_suficiente = sentar_mesa(x_origem, y_origem, senta_com_maximo, blind_mesa, True)

    print(f'Iniciando ações. Statos do sentar: {sentou}. Fichas suficiente para sentar: {ficha_suficiente}')
    if not ficha_suficiente:
        continua_jogando = False

    time_encher_mesa = time_comecou = time_fazer_jogada = time.perf_counter()  # zera os times que serao usados na funação

    while continua_jogando:  # permanece joghando

        if not ficha_suficiente:
            print('Não tem fichas suficientes')
            break

        if reinicia_variaveis:
            Limpa.limpa_total(x_origem, y_origem)
            Limpa.limpa_jogando(x_origem, y_origem)
            jogou_uma_vez = False
            humano = False
            teste_humano = False
            pular_sala = True
            mesa_completa = False
            sentou = False
            cont_limpa_jogando = 45
            time_encher_mesa = time_fazer_jogada = time.perf_counter()
            reinicia_variaveis = False

            if 'recolher' in funcoes:
                atualizar_estatos_mesa('Ainda não sentado ' + num_mesa)
                indicar_pc_desativo()

                confg_funcao, config_tempo_roleta, blind_recolher_auto, confg_secundaria = ler_configuracao()
                if blind_recolher_auto != blind_mesa:
                    blind_mesa = blind_recolher_auto
                    valor_aposta1 = dicionario_salas[blind_mesa][0]
                    valor_aposta2 = dicionario_salas[blind_mesa][1]
                    lista_salas = dicionario_salas[blind_mesa][2]
                    indice_atual = None
                    pular_sala = False
            else:
                IP.testa_trocar_IP()  # ve se tem que trocar ip

        cont_limpa_jogando += 1
        if cont_limpa_jogando > 10:
            cont_limpa_jogando = 0
            # testa as condiçoes para continuar jogando ou nao
            if (pyautogui.pixelMatchesColor((x_origem + 534), (y_origem + 357), (70, 126, 56), tolerance=10)
                    or pyautogui.pixelMatchesColor((x_origem + 534), (y_origem + 357), (23, 121, 166), tolerance=10)):
                print('Mesa esta limpa')
            else:
                print('Mesa não esta limpa')
                Limpa.fecha_tarefa(x_origem, y_origem, jogando=True)
                Limpa.limpa_jogando(x_origem, y_origem)
                Limpa.limpa_promocao(x_origem, y_origem)

            if pyautogui.pixelMatchesColor(495 + x_origem, 627 + y_origem, (15, 160, 220), tolerance=10):
                print('Não esta sentado')
                reinicia_variaveis = True
                continue

            sentou, ficha_suficiente = sentar_mesa(x_origem, y_origem, senta_com_maximo, blind_mesa, True)

            if not ficha_suficiente:
                print('Não tem fichas suficientes')
                break
            if pyautogui.pixelMatchesColor((x_origem + 38), (y_origem + 526), (187, 153, 111), tolerance=19):
                print("Presentinho de dentro da mesa")
                pyautogui.click(x_origem + 38, y_origem + 526)
            if funcoes not in ('tarefa_mesa', 'slot'):
                if not pyautogui.pixelMatchesColor((x_origem + 637), (y_origem + 68), (43, 14, 10), tolerance=19):
                    print("Presente de fazer tarefa")
                    pyautogui.click(x_origem + 637, y_origem + 68)

            tempo_decorrido, horas, minutos, segundos = cacular_tempo_decorrido(time_comecou)
            print(f"Tempo jogando: {horas:02d}:{minutos:02d}:{segundos:02d}")

            if funcoes in 'jogar':
                if tempo_decorrido >= 300:
                    print('\nLimite de tempo jogando mesa, abandona tentativa e pega uma nova conta.\n')
                    break
            if funcoes in 'recolher':
                if not sentou:
                    atualizar_estatos_mesa('Ainda não sentado ' + num_mesa)
                    indicar_pc_desativo()
                if ((time.perf_counter() - time_encher_mesa) > 150) and (not mesa_completa):
                    print('\nLimite de tempo esperando a mesa ficar completa durante o recolhimento, muda de mesa\n')
                    reinicia_variaveis = True
                    continue
            if funcoes in ('recolher', 'tarefa_mesa', 'upar', 'subir_level', 'jogar'):
                if time.perf_counter() - time_fazer_jogada > 120:
                    print('\nLimite de tempo sem jogar, 120 segundos\n')
                    reinicia_variaveis = True
                    continue
            if funcoes in ('upar', 'subir_level', 'jogar', 'slot', 'tarefa_mesa'):
                if HoraT.fim_tempo_tarefa():
                    Limpa.limpa_total(x_origem, y_origem)
                    print('Fim do horario destinado a tarefas')
                    break

            valor_fichas_ = OCR_tela.valor_fichas(x_origem, y_origem)
            if valor_fichas_ < 5000:
                valor_fichas_ = OCR_tela.valor_fichas(x_origem, y_origem)
                if valor_fichas_ < 5000:
                    print('Quantidade de fichas baixa')
                    break

        # parte dedicada as funçoes especificas
        if funcoes in 'slot':
            if slot_mesa_testa_parar(x_origem, y_origem, tarefas_fazer):
                break

        if funcoes in 'tarefa_mesa':
            if tarefa_mesa_testa_parar(x_origem, y_origem, tarefas_fazer):
                break

        # if funcoes in 'upar':
        #     if cont_slot < SLOT_UPAR:
        #         if gira_niquel(x_origem, y_origem):
        #             cont_slot += 10

        if jogou_uma_vez:
            if pyautogui.pixelMatchesColor((x_origem + 663), (y_origem + 538), (86, 169, 68), tolerance=20):
                # testa se apareceu as mensagens verdes na parte de baixo
                cont_jogou += 1
                print(f'Fim da partida. Jogou vezes igua a: {cont_jogou}. Limite de jogadas: {numero_jogadas}')

                if funcoes in 'recolher':
                    if jogou_uma_vez_mesa_completa:
                        print('Jogou uma partida com a mesa completa')
                        break

                if funcoes in ('upar', 'jogar'):
                    print(Fore.YELLOW + f"Esta {funcoes} a conta. Jogou vezes igua a: {cont_jogou}." + Fore.RESET)
                    if cont_jogou >= numero_jogadas:
                        break

                if funcoes in 'subir_level':
                    print(Fore.YELLOW + f"Esta {funcoes} a conta. Jogou vezes igua a: {cont_jogou}."
                                        f"\n Jogadas total: {cont_total_jogadas}" + Fore.RESET)
                    if cont_jogou % 5 == 0:  # testa se tem que trocar ip a casa 5 jogadas
                        level_conta, valor_fichas_perfil = OCR_tela.level_conta(x_origem, y_origem)
                        cont_total_jogadas = (level_conta - int(level_conta)) * 10000
                        xp2.pega_2xp(x_origem, y_origem)
                        IP.testa_trocar_IP()  # ve se tem que trocar ip
                        if level_conta >= LEVEL_SUBIR_LEVEL:
                            level_conta, valor_fichas_perfil = OCR_tela.level_conta(x_origem, y_origem)
                            if level_conta >= LEVEL_SUBIR_LEVEL:
                                break

                if funcoes in 'tarefa_mesa':
                    if tarefa_mesa_testa_parar(x_origem, y_origem, tarefas_fazer, abrir=True):
                        break

                jogou_uma_vez = False
                if not mesa_sem_humanos(x_origem, y_origem, lugares):
                    print('Sair da mesa fim da jogada com humanos na mesa')
                    humano = True
                    reinicia_variaveis = True
                    continue
                else:
                    humano = False

        else:
            # mensagem verde
            if pyautogui.pixelMatchesColor((x_origem + 663), (y_origem + 538), (86, 169, 68), tolerance=20):
                print('Mensagem verde fim da jogada')
                for i in range(10):
                    time.sleep(0.3)
                    if not mesa_sem_humanos(x_origem, y_origem, lugares):
                        print('Sair da mesa, fim da jogada, humanos na mesa')
                        humano = True
                        reinicia_variaveis = True
                        break
                    else:
                        humano = False

                if funcoes in 'recolher':
                    if not humano:
                        mesa_completa = testa_mesa_completa(x_origem, y_origem, lugares)
                        print('Reconhecimenteo de mesa completa: ', mesa_completa)
                        lugares_ocupados = contar_pessoas_mesa(num_mesa)
                        print('Firebase mesa com lugares ocupadas:', lugares_ocupados)

                        if mesa_completa and (lugares_ocupados < 5):
                            # testa se a mesa esta completa porem no firebase nao tem 5 pessoas
                            if teste_humano:  # para levantar so na segunada rodada
                                humano = True
                                print('\nJogador humano na mesa, troca de mesa\n')
                                reinicia_variaveis = True
                                continue
                            teste_humano = True
                        else:
                            teste_humano = False

                        if lugares_ocupados >= 5:
                            mesa_completa = True
                            time_encher_mesa = time_fazer_jogada = time.perf_counter()
                        elif lugares_ocupados == 4:
                            time_encher_mesa = time_fazer_jogada = time.perf_counter()
                            mesa_completa = False
                        else:
                            mesa_completa = False
                        print('Mesa esta com todas as caderas completas: ', mesa_completa)

            else:
                if not mesa_sem_humanos(x_origem, y_origem, lugares):
                    print('Sair da mesa, humanos na mesa')
                    humano = True
                    print('\nJogador humano na mesa, troca de mesa\n')
                    reinicia_variaveis = True
                    continue
                else:
                    humano = False

        if humano:
            print('\nJogador humano na mesa, troca de mesa\n')
            reinicia_variaveis = True
            continue

        if sentou:
            if not humano:
                if funcoes in 'recolher':
                    atualizar_estatos_mesa(num_mesa)
                    indicar_pc_ativo()
                    if mesa_completa:
                        jogou = apostar_pagar(x_origem, y_origem)
                        if jogou:
                            jogou_uma_vez_mesa_completa = True
                    else:
                        lugares_ocupados = contar_pessoas_mesa(num_mesa)
                        if lugares_ocupados < 5:
                            lento = True
                        else:
                            lento = False
                        (jogou, humano) = passa_corre_joga(x_origem, y_origem, valor_aposta1, valor_aposta2, lento)
                else:
                    if apostar:
                        jogou = apostar_pagar_jogar_mesa(x_origem, y_origem)
                    else:
                        (jogou, humano) = passa_corre_joga(x_origem, y_origem, valor_aposta1, valor_aposta2, lento=False)
                if jogou:
                    time_fazer_jogada = time.perf_counter()
                    jogou_uma_vez = True

        else:
            humano = False
            reinicia_variaveis = False
            print("ainda nao esta sentado")
            if funcoes in 'recolher':
                indicar_pc_desativo()
            for i in range(3):
                print('indice_inicial', indice_inicial)
                if not indice_inicial:
                    indice_inicial = 0
                if not indice_atual:
                    indice_atual = 0
                for indice, num_mesa in enumerate(lista_salas):
                    try:
                        if indice_inicial > indice:
                            print('Porcurando o indece / mesa: ', indice, num_mesa)
                            # faz o for interagir ate chegar na ultima sala que foi usada anteriormente
                            # troca o valor para que na proxima interação possamos iniciar do inicios da lista
                            continue

                        if (indice == indice_atual) and pular_sala:
                            print('Pula o indice / mesa: ', indice, num_mesa)
                            continue  # Pule a primeira iteração, começando pelo segundo item
                    except Exception as e:
                        print(e)

                    print('Continuar, indece / mesa para tentar sentar: ', indice, num_mesa)
                    IP.tem_internet()
                    Limpa.limpa_jogando(x_origem, y_origem)
                    Limpa.limpa_total(x_origem, y_origem)
                    blind_certo, sala_existe = escolher_sala_por_numero(x_origem, y_origem, num_mesa, blind_mesa, lugares=5)

                    if not sala_existe:
                        # Remova o item da posição específica
                        item_removido = lista_salas.pop(indice)
                        # Adicione o item ao final da lista
                        lista_salas.append(item_removido)

                    if blind_certo:
                        if funcoes in ('upar', 'joga', 'slot'):
                            aposta, auto10 = ajuste_valor_niquel(x_origem, y_origem, ajusta_aposta=200)
                        else:
                            aposta, auto10 = True, True
                        sentou, ficha_suficiente = sentar_mesa(x_origem, y_origem, senta_com_maximo, blind_mesa, True)
                        if sentou and aposta and auto10 and ficha_suficiente:
                            if funcoes in 'recolher':
                                atualizar_estatos_mesa(num_mesa)
                                indicar_pc_ativo()
                                mesa_completa = testa_mesa_completa(x_origem, y_origem, lugares)

                            time_encher_mesa = time_fazer_jogada = time.perf_counter()
                            print('esta tudo ok, sentado na mesa:', num_mesa)
                            if indice:
                                indice_atual = indice
                            else:
                                indice_atual = 0
                            indice_inicial = 0
                            reinicia_variaveis = False
                            pular_sala = False
                            if funcoes in 'slot':
                                gira_niquel(x_origem, y_origem)
                            break
                        else:
                            reinicia_variaveis = True

                    if indice_inicial == indice and indice_inicial != 0:
                        indice_inicial = 0
                        i = 0
                        break

                    indice_inicial = 0

                if i == 1:
                    pular_sala = False

                if sentou:
                    reinicia_variaveis = False
                    break
                else:
                    reinicia_variaveis = True

            if not sentou:
                indice_inicial = 0
                reinicia_variaveis = True
                print("rodou a lista de mesas 2x, da um F5 para recarregar as mesas")
                IP.tem_internet()
                print('f5')
                # pyautogui.press('f5')
                atualizar_navegador()
                time.sleep(25)

    print("FIM Mesa")

    if funcoes in 'recolher':
        atualizar_estatos_mesa('retornará na mesa ' + num_mesa)
        indicar_pc_desativo()

    if indice_atual:
        indice_inicial = indice_atual
    else:
        indice_inicial = 0

        # # Ao final da função, atribui o valor da lista utilizada dentro da função à lista global
    dicionario_salas[blind_mesa][2] = lista_salas

    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
        return "sair da conta"

    Limpa.limpa_jogando(x_origem, y_origem)
    return


def cacular_tempo_decorrido(time_comecou):
    # Cálculo do tempo decorrido desde que o jogador entrou no jogo
    tempo_decorrido = time.perf_counter() - time_comecou
    # Conversão de segundos para horas, minutos e segundos
    horas = int(tempo_decorrido // 3600)
    minutos = int((tempo_decorrido % 3600) // 60)
    segundos = int(tempo_decorrido % 60)

    # Impressão do tempo decorrido
    # print(f"Tempo jogando: {horas:02d}:{minutos:02d}:{segundos:02d}")
    return tempo_decorrido, horas, minutos, segundos


def tarefa_mesa_testa_parar(x_origem, y_origem, tarefas_fazer, abrir=False):
    """Função que giro o eslote caso precise ou retorna True quando terminou"""
    # print("tarefa_mesa_testa_parar")
    finalizar = False
    continua_jogando = True
    meta_atigida, pontos = Tarefas.tem_tarefa_para_recolher(x_origem, y_origem)

    if abrir:
        Limpa.limpa_abre_tarefa(x_origem, y_origem, com_pausa=False)
        print('manda recolher')
        Tarefas.recolher_tarefa(x_origem, y_origem)
        print('procura se ainda tem tarefa')

        continua_jogando, tarefa = Tarefas.comparar_listas_fazendo_tarefa(tarefas_fazer, x_origem, y_origem)
        meta_atigida, pontos = Tarefas.meta_tarefas(x_origem, y_origem)

        if Limpa.limpa_total_fazendo_tarefa(x_origem, y_origem) == "sair da conta":
            finalizar = True
            return finalizar
        IP.testa_trocar_IP()  # ve se tem que trocar ip

    if (not continua_jogando) or meta_atigida:
        Limpa.limpa_abre_tarefa(x_origem, y_origem, com_pausa=False)
        print('manda recolher')
        Tarefas.recolher_tarefa(x_origem, y_origem)
        print('procura se ainda tem tarefa')
        continua_jogando, tarefa = Tarefas.comparar_listas_fazendo_tarefa(tarefas_fazer, x_origem, y_origem)
        meta_atigida, pontos = Tarefas.meta_tarefas(x_origem, y_origem)
        if (not continua_jogando) or meta_atigida:
            Limpa.limpa_total(x_origem, y_origem)
            print('Atingiu a meta de pontos do dia ou terminou a missão')
            finalizar = True
            return finalizar

    if (pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 117), (72, 71, 76), tolerance=5) or
            pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 117), (22, 21, 23), tolerance=5)):
        pyautogui.click(821 + x_origem, 138 + y_origem)  # clica no fechar tarefa
        print('fecha lista tarefas jogando')

    return finalizar


def slot_mesa_testa_parar(x_origem, y_origem, tarefas_fazer):
    """Função que giro o eslote caso precise ou retorna True quando terminou"""
    finalizar = False
    continua_jogando = True
    meta_atigida, pontos = Tarefas.tem_tarefa_para_recolher(x_origem, y_origem)

    if gira_10auto(x_origem, y_origem):
        Limpa.limpa_abre_tarefa(x_origem, y_origem, com_pausa=False)
        print('manda recolher')
        Tarefas.recolher_tarefa(x_origem, y_origem)
        print('procura se ainda tem tarefa')

        continua_jogando, tarefa = Tarefas.comparar_listas_fazendo_tarefa(tarefas_fazer, x_origem, y_origem)
        meta_atigida, pontos = Tarefas.meta_tarefas(x_origem, y_origem)

        if Limpa.limpa_total_fazendo_tarefa(x_origem, y_origem) == "sair da conta":
            finalizar = True
            return finalizar
        IP.testa_trocar_IP()  # ve se tem que trocar ip

    if (not continua_jogando) or meta_atigida:
        Limpa.limpa_abre_tarefa(x_origem, y_origem, com_pausa=False)
        print('manda recolher')
        Tarefas.recolher_tarefa(x_origem, y_origem)
        print('procura se ainda tem tarefa')
        continua_jogando, tarefa = Tarefas.comparar_listas_fazendo_tarefa(tarefas_fazer, x_origem, y_origem)
        meta_atigida, pontos = Tarefas.meta_tarefas(x_origem, y_origem)
        if (not continua_jogando) or meta_atigida:
            Limpa.limpa_total(x_origem, y_origem)
            print('Atingiu a meta de pontos do dia ou terminou a missão')
            finalizar = True
            return finalizar

    if (pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 117), (72, 71, 76), tolerance=5) or
            pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 117), (22, 21, 23), tolerance=5)):
        pyautogui.click(821 + x_origem, 138 + y_origem)  # clica no fechar tarefa
        print('fecha lista tarefas jogando')

    gira_niquel(x_origem, y_origem)
    return finalizar


def blind_do_dia(dia_da_semana=10):
    """
    Retorna a mesa que sera usada em funçao do dia da semana.
    0 segunda, 1 terça, 2 quarta, 3 quinta, 4 sexta, 5 sábado, 6 domingo
    """
    if dia_da_semana == 10:
        # se dia da semana fora do falor esperado recupera o valor
        dia_da_semana = datetime.datetime.now().weekday()

    if dia_da_semana in [5]:
        print("O dia da semana é 100/200.")
        blind_mesa = '2550'
    elif dia_da_semana in [2]:
        print("O dia da semana é 50/100.")
        blind_mesa = '50100'
    elif dia_da_semana in [0]:
        print("O dia da semana é 25/50.")
        blind_mesa = '100200'
    else:
        print("Não joga mesa hoje")
        blind_mesa = 'Não joga'
    return blind_mesa


def dia_de_jogar_mesa(x_origem, y_origem, level_conta=1, valor_fichas_perfil=0, conta_upada=True, dia_da_semana=0, roleta='roleta_1'):
    cont_total_jogadas = (level_conta - int(level_conta))
    print(f"dia_de_jogar_mesa - level_conta: {level_conta},valor_fichas_perfil: {valor_fichas_perfil}, conta_upada: {conta_upada}, "
          f"dia_da_semana: {dia_da_semana}, cont_total_jogadas: {cont_total_jogadas}")
    # define o numero maximo e minimo que ira joga na mesa
    num_vezes_maximo = 4
    num_vezes_minimo = 2
    # limite de fichas minimo para jogar
    LIMITE_FICHAS = 1000
    LEVEL_UPAR = 7

    if datetime.datetime.now().time() < datetime.time(23, 50, 0):
        # nao joga se ja for mais tarde que o horario definido
        if level_conta == '' or level_conta == 1 or valor_fichas_perfil == 0 or valor_fichas_perfil == '':
            level_conta, valor_fichas_perfil = OCR_tela.level_conta(x_origem, y_origem)
    else:
        print('\n horario maior que o limite definido 23:00 \n')
        return level_conta, valor_fichas_perfil

    if valor_fichas_perfil < LIMITE_FICHAS:
        print('\n valor de fichar inferior ao definido \n')
        return level_conta, valor_fichas_perfil

    if HoraT.fim_tempo_tarefa():
        print('Fim do horario destinado a tarefas')
        return level_conta, valor_fichas_perfil

    if roleta == 'roleta_2':
        if (4 >= level_conta) or (not conta_upada):
            blind_mesa = '100200'
            # blind_mesa = '5001K'
            # Telegran.monta_mensagem(f'vai fazer as tarefas de upar, conta level {str(level_conta)}.  🆙', True)
            upar(x_origem, y_origem, blind_mesa=blind_mesa)
            level_conta, valor_fichas_perfil = OCR_tela.level_conta(x_origem, y_origem)
            # cont_total_jogadas = (level_conta - int(level_conta))
            conta_upada = Limpa.limpa_abre_tarefa(x_origem, y_origem)
            Telegran.monta_mensagem(f'terminou de fazer as tarefas de upar, conta level {str(level_conta)}.  🆙', True)
            # Limpa.limpa_total(x_origem, y_origem)
            print('level_conta: ', level_conta)
            print('valor_fichas_perfil: ', valor_fichas_perfil)

        if HoraT.fim_tempo_tarefa():
            print('Fim do horario destinado a tarefas')
            return level_conta, valor_fichas_perfil

        if (level_conta < LEVEL_UPAR) and (valor_fichas_perfil > (LIMITE_FICHAS * 5)) and conta_upada:
            blind_mesa = '100200'
            # blind_mesa = '5001K'
            Limpa.fecha_tarefa(x_origem, y_origem)
            Limpa.limpa_promocao(x_origem, y_origem)
            print('level_conta: ', level_conta)
            print('valor_fichas_perfil: ', valor_fichas_perfil)
            time.sleep(2)
            Limpa.limpa_total(x_origem, y_origem)

            Telegran.monta_mensagem(f'vai upar uma conta level  {str(level_conta)}.  🆙', True)
            mesa_upar_jogar(x_origem, y_origem, numero_jogadas=0, upar=True, blind_mesa=blind_mesa, apostar=False, recolher=False,
                            level_conta=level_conta, subir_level=False)
            level_conta, valor_fichas_perfil = OCR_tela.level_conta(x_origem, y_origem)
            Telegran.monta_mensagem(f'terminou de upar conta level {str(level_conta)}.  📈⬆️', True)

            print('level_conta: ', level_conta)
            print('valor_fichas_perfil: ', valor_fichas_perfil)
            conta_upada = Limpa.limpa_abre_tarefa(x_origem, y_origem)
            # return level_conta, valor_fichas_perfil

        # if HoraT.fim_tempo_tarefa():
        #     print('Fim do horario destinado a tarefas')
        #     return level_conta, valor_fichas_perfil
        #
        # if (level_conta < 8.0511) and (level_conta >= 7) and (valor_fichas_perfil > (LIMITE_FICHAS * 10)) and conta_upada:
        #     blind_mesa = '100200'
        #     # blind_mesa = '5001K'
        #     Limpa.fecha_tarefa(x_origem, y_origem)
        #     Limpa.limpa_promocao(x_origem, y_origem)
        #     print('level_conta: ', level_conta)
        #     print('valor_fichas_perfil: ', valor_fichas_perfil)
        #     time.sleep(2)
        #     Limpa.limpa_total(x_origem, y_origem)
        #
        #     print(f'vai upar uma conta level  {level_conta}. para o level 12.0511')
        #
        #     Telegran.monta_mensagem(f'vai upar uma conta level  {str(level_conta)}. para o level 7.0511  🆙', True)
        #     mesa_upar_jogar(x_origem, y_origem, numero_jogadas=0, upar=True, blind_mesa=blind_mesa, apostar=False, recolher=False,
        #                     level_conta=level_conta, subir_level=True)
        #     level_conta, valor_fichas_perfil = OCR_tela.level_conta(x_origem, y_origem)
        #     Telegran.monta_mensagem(f'terminou de upar conta level {str(level_conta)}.  📈⬆️', True)
        #
        #     print('level_conta: ', level_conta)
        #     print('valor_fichas_perfil: ', valor_fichas_perfil)
        # Limpa.limpa_total(x_origem, y_origem)
        print('\n level da conta nao adequado ou conta ja upada\n')
        return level_conta, valor_fichas_perfil

    elif roleta == 'roleta_1':
        blind_mesa = blind_do_dia(dia_da_semana)
        print('blinde do dia: ', blind_mesa)
        if blind_mesa == 'Não joga':
            return level_conta, valor_fichas_perfil

        Limpa.fecha_tarefa(x_origem, y_origem)
        Limpa.limpa_promocao(x_origem, y_origem)
        print('level_conta: ', level_conta)
        print('valor_fichas_perfil: ', valor_fichas_perfil)
        time.sleep(2)
        Limpa.limpa_total(x_origem, y_origem)

        numero_aleatorio = random.randint(num_vezes_minimo, num_vezes_maximo)
        mesa_upar_jogar(x_origem, y_origem, numero_jogadas=numero_aleatorio, upar=False, blind_mesa=blind_mesa, apostar=True, recolher=False)
        level_conta, valor_fichas_perfil = OCR_tela.level_conta(x_origem, y_origem)

        print('level_conta: ', level_conta)
        print('valor_fichas_perfil: ', valor_fichas_perfil)
        Limpa.limpa_total(x_origem, y_origem)
        return level_conta, valor_fichas_perfil
    else:
        print('\n nao é roleta 1 e nem roleta 2 \n')
        return level_conta, valor_fichas_perfil


def passa_corre_joga(x_origem, y_origem, valor_aposta1=40, valor_aposta2=80, lento=False):  # para se fazer tarefas
    time_lento = 7.5
    # print("passa_corre_joga")
    jogou_uma_vez = False, False
    # se esta com v azul dentro do quadrado branco
    if pyautogui.pixelMatchesColor((x_origem + 333), (y_origem + 610), (59, 171, 228), 3):
        return jogou_uma_vez

    # se esta com quadrado branco
    elif pyautogui.pixelMatchesColor((x_origem + 333), (y_origem + 610), (255, 255, 255), 3):
        if lento:
            # não usa o quadrado branco, para jogar amis lento
            return jogou_uma_vez
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
            if lento:
                time.sleep(time_lento)  # atrasa para passar
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


def apostar_pagar_jogar_mesa(x_origem, y_origem):
    jogou_uma_vez = False
    # quando se tem que apostar, testa se tem a barra de ajustar a aposta
    if pyautogui.pixelMatchesColor((x_origem + 513), (y_origem + 647), (180, 202, 224), 5):
        # se tem a barra de ajustar a aposta
        print('Barra de ajustar valor')

        correr = random.randint(1, 20)
        if correr == 1:
            pyautogui.click((x_origem + 592), (y_origem + 603))
            print('***Correu')
            jogou_uma_vez = True
            return jogou_uma_vez
        else:
            passa_paga_aposta = random.randint(1, 3)
            match passa_paga_aposta:
                case 1:
                    pyautogui.click((x_origem + 380), (y_origem + 603))
                    print('***Passou')
                    jogou_uma_vez = True
                    return jogou_uma_vez
                case 2:
                    pyautogui.click((x_origem + 380), (y_origem + 650))
                    print('***Apostou valor padrão')
                    jogou_uma_vez = True
                    return jogou_uma_vez
                case 3:
                    # cliaca no final da barra para ela ir ate o final
                    pyautogui.click((x_origem + 660), (y_origem + 647))
                    print('ajustou no final da barra')

                    numero_aleatorio = random.randint(540, 600)

                    for _ in range(100):
                        #  teste se a barra foi deslocada, nao esta mais na posição inicial
                        if not pyautogui.pixelMatchesColor((x_origem + 515), (y_origem + 647), (184, 212, 237), 5):
                            break
                        time.sleep(0.01)

                    # clicar em uma posição aleatoria da barra
                    pyautogui.click((x_origem + numero_aleatorio), (y_origem + 647))
                    print('Posição de valor aleatorio')
                    time.sleep(0.4)

                    pyautogui.click((x_origem + 380), (y_origem + 650))
                    print('***Apostou valor maior')
                    jogou_uma_vez = True
                    return jogou_uma_vez

    elif pyautogui.pixelMatchesColor((x_origem + 342), (y_origem + 601), (255, 255, 255), 5):
        # branco de interceção de pagar e passar sem o quadrado brando
        # se nao tem a barra de ajusta a posta e se tem o pagar
        pyautogui.click((x_origem + 380), (y_origem + 604))
        print('Clicou no Passar ou no Pagar')
        jogou_uma_vez = True
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

        if (pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 674), (27, 92, 155), tolerance=19) or pyautogui.pixelMatchesColor(
                (x_origem + 700), (y_origem + 674), (19, 64, 109), tolerance=19)):
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

# import Origem_pg
#





# # mesa_sem_humanos(x_origem, y_origem, tolerancia=8)
# # escolher_blind(x_origem, y_origem, blind='2K/4K', lugares=5)
# sentar_mesa(x_origem, y_origem, True, '200/400', True)
# mesa_recolher(x_origem, y_origem, 2, '20/40')
# x_origem, y_origem = Origem_pg.x_y()
# mesa_sem_humanos(x_origem, y_origem)
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
