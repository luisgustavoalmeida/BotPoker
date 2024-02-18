# # # # # lista =['rico tab bien odio ia Lana nina iodo iii ua ind ias de 50', 'ua a nn ao Cidia ias ini fundir insira E en,',
# # # # #         'unas boina ia iara ia caia so uniiitn tias', 'iu da age dai ain adiantado iria daria',
# # # # #         'ia a nao tis io dial us iria vãs,', 'TA AAm e mA a Eg NE eRr aaA', 'ESET EN) TN RI E e RR E',
# # # # #         '& 1000 PN ke. São', 'S +500 BP +11)', "em es = ou CO'", '1000 A)1000 A', '6 +2000 P+30', 'C200  BPD0 |',
# # # # #         '* +500 B 10', 'l; *1000 [A', '6 2000 B 30', 'B 500 B 10', 'C200  BPD0', '& 500 B 10', '3 +500 A/)',
# # # # #         'E 27 a/) =', '6 500 B 10', 'B 500 A/)', '& 1000 A)', 'Sum CEPE.', 'pc ai fa', '6 500 R/', 'º +500 /',
# # # # #         'E 27 a =', 'pacos ra', '4 500 Po', 'pç ai fa', 'paços ra', '& 500 [A', '& 1000 P', '1000 UA)', 'B +s00 A',
# # # # #         '& 1000 A', '1000 [A', 'pião SO', 'poça fo', '2000 B0', '1000 A)', '200 BP0', 'poça fa', 'B 500 /',
# # # # #         '2000 BP', '500 Bi)', '2000 PD', 'POA fo', '100 Pn', '200 PD', '500 Bi', '200 BP', '0 BA /', ') [A;/',
# # # # #         'poo P0', 'SM Pt', 'os“ 3', '500 A', '|||.', ') R/', ') ”', '/ -', '/ ”', 'P0', '[A', 'B0', ')', '/']
# # # # #
# # # # # print(len(lista))
# # # # #
# # # # # lista_sem_duplicados = list(set(lista))
# # # # #
# # # # # print(len(lista_sem_duplicados))
# # # # #
# # # # # lista_ordenada = sorted(lista_sem_duplicados, key=len, reverse=True)
# # # # #
# # # # # print(lista_ordenada)
# # # # #
# # # # #
# # # #
# # # #
# # # # # troca_tarefa = ['Ganhar 10 maos em uma mesa com blinds acima de 25',
# # # # #                 'Ganhar um premio em um torneio de eliminacao',
# # # # #                 'Jogar 20 mão em uma mesa com blinds acima de 25',
# # # # #                 'Participe de um campeonato de eliminação 1 vezes',
# # # # #                 'Participe de um campeonato de eliminação 2 vezes',
# # # # #                 'Participe de um campeonato de eliminação 3 vezes',
# # # # #                 'Tirar Sequencia 1 vezes em mesas com blinds maiores que 25',
# # # # #                 'Tirar trinca 1 vez em mesa com blinds maiores que 25',
# # # # #                 'Tirar um flush ou quaquer mãos superior 1 vez em mesas com blinds laiores que 25',
# # # # #                 'Ganhar 10 mãos em uma mesa com blinds acima de 50',
# # # # #                 'Ganhar 20 mãos em uma mesa com blinds acima de 50',
# # # # #                 'Ganhar 30.000 fichas em mesas com blinds acima da 50',
# # # # #                 'Jogar 20 mão em uma mesa com blinds acima de 50',
# # # # #                 'Jogar 40 mão em uma mesa com blinds acima de 50',
# # # # #                 'Tirar Flush ou qualquer mão superior 1 vez em mesas com blindes maiores que 25',
# # # # #                 'Tirar Sequencia 2 vezes em mesas com blinds maiores que 50',
# # # # #                 'Tirar trinca 1 vez em mesas com blinds maiores que 50',
# # # # #                 'Ganhar 20 mãos em uma mesa com blinds acima de 100',
# # # # #                 'Ganhar 100.000 fichas em mesas com blinds acima de 50',
# # # # #                 'Ganhar 200.000 fichas em mesas com blindes acima da 100',
# # # # #                 'Jogar 20 mão em uma mesa com blinds acima de 100',
# # # # #                 'Jogar 40 mão em uma mesa com blinds acima de 100',
# # # # #                 'Tirar Flush ou qualquer mão superior 1 vez em mesas com blindes maiores que 50',
# # # # #                 'Tirar Flush ou qualquer mão superior 2 vez em mesas com blindes maiores que 100',
# # # # #                 'Tirar Sequencia 2 vezes em mesas com blinds maiores que 100',
# # # # #                 'Tirar trinca 2 vez em mesas com blinds maiores que 100']
# # # # #
# # # # # for i in range(len(troca_tarefa)):
# # # # #     troca_tarefa[i] = troca_tarefa[i].replace('ç', 'c').replace('í', 'i').replace('ê', 'e').replace('-', ' ').replace('ã', 'a')
# # # # #     troca_tarefa[i] = troca_tarefa[i].replace('\n', ' ').rstrip('.')
# # # # #     troca_tarefa[i] = ' '.join(troca_tarefa[i].split())
# # # # #
# # # # # print(troca_tarefa)
# # # #
# # # #
# # # #
# # # # # import time
# # # # # inicio = time.time()
# # # # # #inicio = time.perf_counter()
# # # # # time.sleep(2)
# # # # # fim = time.time()
# # # # # #fim = time.perf_counter()
# # # # #
# # # # # # Calcula a diferença de tempo
# # # # # tempo_total = fim - inicio
# # # # #
# # # # # # Imprime o tempo total em segundos
# # # # # print("Tempo total: ", tempo_total, "segundos")
# # # #
# # # #
# # # #
# # # # # import pyautogui
# # # # #
# # # # # try:
# # # # #     # Localize a janela do ExpressVPN com base na classe 'ahk_class'
# # # # #     expressvpn_window = pyautogui.getWindowsWithTitle('ExpressVPN')[0]
# # # # #     print(expressvpn_window)
# # # # #
# # # # #
# # # # #     # Traz a janela para o primeiro plano (caso esteja minimizada ou oculta)
# # # # #     expressvpn_window.activate()
# # # # #
# # # # #     # Aguarde um pequeno intervalo para garantir que a janela esteja completamente ativada
# # # # #     pyautogui.sleep(1)
# # # # #
# # # # #     # Use 'Alt + Esc' para alternar entre as janelas e, assim, exibir a interface do ExpressVPN
# # # # #     #pyautogui.hotkey('alt', 'esc')
# # # # #
# # # # # except Exception as e:
# # # # #     print("Erro ao abrir a interface do ExpressVPN:", e)
# # # #
# # # #
# # # #
# # import subprocess
# # import pyautogui
# # import time
# # import pygetwindow as gw
# # import time
# #
# # #Caminho para o executável da VPN
# #
# # caminho_executavel_vpn = "C:/Program Files (x86)/ExpressVPN/expressvpn-ui/ExpressVPN.exe"
# # conexao_vpn_x = 1100
# # conexao_vpn_y = 440
# #
# #
# #     # Caminho para o executável da VPN
# #
# #
# # while True:
# #
# #     print('abre a vpn')
# #     try:
# #         vpn_window = gw.getWindowsWithTitle('ExpressVPN')[0]
# #         print(vpn_window)
# #         # vpn_window.activate()
# #         # Verificar se a janela está visível antes de movê-la
# #         if vpn_window.left == 1100 and vpn_window.top == 440:
# #             conexao_vpn_vpn_x = vpn_window.left
# #             conexao_vpn_vpn_y = vpn_window.top
# #             print("A posição da janela é (930, 440).")
# #             break
# #         if vpn_window.left < 0 and vpn_window.top < 0:
# #             print('esta minizada')
# #             subprocess.Popen(caminho_executavel_vpn)
# #         else:
# #             vpn_window.activate()
# #             # Mover a janela da VPN para a posição desejada (x, y) da tela
# #             conexao_vpn_vpn_x = 1100
# #             conexao_vpn_vpn_y = 440
# #
# #             vpn_window.moveTo(conexao_vpn_vpn_x, conexao_vpn_vpn_y)
# #     except Exception as e:
# #         print("Erro ao abrir a VPN:", e)
# #         subprocess.Popen(caminho_executavel_vpn)
# #         time.sleep(5)
# #         continue
# #     time.sleep(0.5)
# #
# # while True:
# #     print('refazendo conexao')
# #     # testa se esta verde e ligado
# #     if pyautogui.pixelMatchesColor((conexao_vpn_vpn_x + 189), (conexao_vpn_vpn_y + 186), (15, 134, 108), tolerance=10) \
# #             or pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (77, 182, 172), tolerance=10):
# #         pyautogui.click(conexao_vpn_x + 189, conexao_vpn_y + 186)
# #         print('desligou')
# #         for i in range(100):
# #             # testa se esta vermelho e desligado
# #             if pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (126, 15, 83), tolerance=10) \
# #                     or pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (164, 17, 94), tolerance=10):
# #                 time.sleep(0.5)
# #                 print('VPN Desconectado')
# #                 break
# #             time.sleep(0.5)
# #
# #     # testa se esta vermelho e desligado
# #     elif pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (126, 15, 83), tolerance=10) \
# #             or pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (164, 17, 94), tolerance=10):
# #         pyautogui.click(conexao_vpn_x + 189, conexao_vpn_y + 186)
# #         print('ligou')
# #         for i in range(100):
# #             # testa se esta vermelho e desligado
# #             if pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (15, 134, 108), tolerance=10) \
# #                     or pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (77, 182, 172), tolerance=10):
# #                 print('VPN Conectado')
# #                 break
# #             time.sleep(0.5)
# #         if pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (15, 134, 108), tolerance=10) \
# #                 or pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (77, 182, 172), tolerance=10):
# #             print('VPN Conectado')
# #             # Minimizar a janela
# #             vpn_window.minimize()
# #             break
# # #
# # #
# # #
# # # import requests
# # # import pyautogui
# # # import time
# # # def f5_quando_internete_ocila():
# # #
# # #     conectado = True
# # #     while True:
# # #         print('f5_quando_internete_ocila')
# # #         try:
# # #             response = requests.get('http://www.google.com', timeout=5)
# # #             print(response)
# # #
# # #             if response.status_code == 200 or response.status_code == 429:
# # #                 print("Conexão com a internet ativa.")
# # #                 if not conectado:
# # #                     try:
# # #                         pyautogui.press('f5')
# # #                         time.sleep(15)
# # #                     except Exception as e:
# # #                         print('erro autogui: ', e)
# # #
# # #                 #entrou_corretamente, stataus = Seleniun.teste_logado(id, senha, url, navegador)
# # #                 return True
# # #         except Exception as e:
# # #             print("Sem conexão com a internet...")
# # #             print(e)
# # #             time.sleep(5)
# # #             conectado = False
# # #
# # # #f5_quando_internete_ocila()
# # #
# # # import random
# # # def tem_internet():
# # #     cont_erro2 = 0
# # #     cont_erro = 0
# # #     #print('tem_internet')
# # #
# # #     sites = [
# # #         'http://www.google.com',
# # #         'http://www.facebook.com',
# # #         'http://www.twitter.com',
# # #         'http://www.youtube.com',
# # #         'http://www.instagram.com',
# # #         'http://www.linkedin.com',
# # #         'http://www.github.com',
# # #         'http://www.reddit.com',
# # #         'http://www.amazon.com',
# # #         'http://www.netflix.com'
# # #     ]
# # #
# # #
# # #     com_internete = True
# # #     while com_internete:
# # #         print('testa a internete')
# # #         cont_erro2 += 1
# # #         site_aleatorio = random.choice(sites)
# # #         print(site_aleatorio)
# # #         try:
# # #             response = requests.get(site_aleatorio, timeout=10)
# # #             print(response)
# # #             if response.status_code == 200:
# # #                 print("Conexão com a internet ativa.")
# # #                 #com_internete = False
# # #                 #return True
# # #         except Exception as e:
# # #             print("Sem conexão com a internet. Encerrando os testes...")
# # #             print(e)
# # #             time.sleep(3)
# # #             cont_erro += 1
# # #             continue
# # #
# # #
#
# #
# # import threading
# #
# # # Variáveis globais para as variáveis e controle da tarefa independente
# # variavel1 = 0
# # variavel2 = 0
# # continuar_tarefa = False
# #
# # # Semaphore para iniciar a tarefa independente
# # iniciar_tarefa = threading.Semaphore(0)
# #
# # # Semaphore para a tarefa independente indicar que terminou e aguardar novo comando
# # tarefa_concluida = threading.Semaphore(0)
# #
# # # Função que será executada na tarefa independente
# # def tarefa_independente():
# #     global continuar_tarefa
# #     global variavel1
# #     global variavel2
# #
# #     while True:
# #         # Aguardar o comando para iniciar a execução
# #         iniciar_tarefa.acquire()
# #
# #         # Verificar se a tarefa deve continuar executando ou parar
# #         if continuar_tarefa:
# #             # Atualizar as variáveis
# #             variavel1 += 1
# #             variavel2 -= 1
# #
# #             # Simular a execução da tarefa
# #             print("Executando tarefa independente...")
# #
# #             # Indicar que a tarefa terminou e está pronta para aguardar novo comando
# #             tarefa_concluida.release()
# #         else:
# #             print("Tarefa independente parada.")
# #
# # # Resto do código...
# #
# # # Iniciar a execução da tarefa
# # tarefa = threading.Thread(target=tarefa_independente)
# # tarefa.start()
# #
# # # O código principal pode continuar a partir daqui
# # # Ele pode acessar as variáveis atualizadas pela tarefa independente
# #
# # # Exemplo de comando para iniciar a tarefa independente
# # continuar_tarefa = True
# # iniciar_tarefa.release()
# #
# # # Aguardar a tarefa terminar
# # tarefa_concluida.acquire()
# #
# # # Exemplo de comando para pausar a tarefa independente
# # continuar_tarefa = False
# # iniciar_tarefa.release()
# #
# # # Aguardar a tarefa terminar
# # tarefa_concluida.acquire()
# #
# # # Agora a tarefa independente está pausada e pronta para aguardar um novo comando do código principal
# # # Você pode repetir esse processo quantas vezes for necessário para controlar a execução da tarefa independente.
#
#
# lista_ips = [
#     "186.235.103.220",
#     "177.104.68.243",
#     "177.104.93.127",
#     "177.104.93.130",
#     "177.104.93.163",
#     "177.104.93.90",
#     "177.104.95.224",
#     "186.235.99.36",
#     "187.16.187.56",
#     "187.68.10.158",
#     "187.68.10.84",
#     "187.68.11.9",
#     "187.68.14.197",
#     "187.68.16.121",
#     "187.68.17.209",
#     "187.68.24.239",
#     "187.68.25.124",
#     "187.68.25.18",
#     "187.68.25.252",
#     "187.68.25.28",
#     "187.68.25.50",
#     "187.68.27.62",
#     "187.68.28.101",
#     "187.68.28.214",
#     "187.68.28.59",
#     "187.68.28.86",
#     "187.68.28.98",
#     "187.68.29.52",
#     "187.68.30.134",
#     "187.68.30.183",
#     "187.68.31.21",
#     "187.68.4.92",
#     "187.68.5.32",
#     "187.68.7.14",
#     "187.68.9.113",
#     "187.68.9.158",
#     "187.69.64.217",
#     "187.69.64.90",
#     "187.69.64.94",
#     "187.69.65.12",
#     "187.69.65.16",
#     "187.69.65.194",
#     "187.69.65.21",
#     "187.69.65.38",
#     "187.69.65.53",
#     "187.69.65.62",
#     "187.69.66.133",
#     "187.69.67.242",
#     "187.69.68.186",
#     "187.69.68.242",
#     "187.69.68.251",
#     "187.69.69.193",
#     "187.69.69.45",
#     "187.69.69.58",
#     "187.69.70.111",
#     "187.69.70.94",
#     "187.69.71.224",
#     "187.69.71.30",
#     "187.69.71.40",
#     "187.69.71.41",
#     "187.69.72.94",
#     "187.69.73.1",
#     "187.69.73.21",
#     "187.69.75.180",
#     "187.69.75.25",
#     "187.69.76.108",
#     "187.69.79.222",
#     "187.69.79.28",
#     "187.69.80.192",
#     "187.69.80.57",
#     "187.69.81.146",
#     "187.69.81.227",
#     "187.69.82.20",
#     "187.69.83.104",
#     "187.69.84.168",
#     "187.69.85.128",
#     "187.69.85.148",
#     "187.69.85.31",
#     "187.69.85.73",
#     "187.69.86.150",
#     "187.69.86.20",
#     "187.69.87.1",
#     "187.69.87.108",
#     "187.69.87.131",
#     "187.69.87.185",
#     "187.69.88.133",
#     "187.69.88.16",
#     "187.69.89.220",
#     "187.69.90.38",
#     "187.69.90.59",
#     "187.69.92.127",
#     "187.69.92.178",
#     "187.69.92.245",
#     "187.69.92.43",
#     "187.69.93.114",
#     "187.69.93.47",
#     "187.69.95.112",
#     "187.69.95.167",
#     "187.69.95.25",
#     "189.93.226.105",
#     "189.93.226.142",
#     "189.93.226.21",
#     "189.93.226.239",
#     "189.93.226.27",
#     "189.93.227.162",
#     "189.93.227.224",
#     "189.93.227.56",
#     "189.93.227.97",
#     "189.93.228.184",
#     "189.93.228.244",
#     "189.93.229.170",
#     "189.93.230.10",
#     "189.93.230.53",
#     "189.93.230.56",
#     "189.93.231.142",
#     "189.93.232.212",
#     "189.93.233.232",
#     "189.93.233.6",
#     "189.93.233.95",
#     "189.93.234.178",
#     "189.93.234.232",
#     "189.93.235.128",
#     "189.93.235.51",
#     "189.93.235.70",
#     "189.93.236.248",
#     "189.93.237.192",
#     "189.93.237.48",
#     "189.93.237.84",
#     "189.93.239.139",
#     "189.93.239.37",
#     "189.93.239.94",
#     "189.93.240.220",
#     "189.93.241.229",
#     "189.93.242.164",
#     "189.93.242.203",
#     "189.93.242.229",
#     "189.93.242.239",
#     "189.93.243.209",
#     "189.93.244.40",
#     "189.93.246.106",
#     "189.93.246.155",
#     "189.93.246.232",
#     "189.93.246.37",
#     "189.93.247.205",
#     "189.93.248.163",
#     "189.93.248.33",
#     "189.93.248.75",
#     "189.93.250.137",
#     "189.93.250.174",
#     "189.93.250.239",
#     "189.93.250.70",
#     "189.93.251.20",
#     "189.93.252.102",
#     "189.93.252.147",
#     "189.93.252.25",
#     "189.93.253.218",
#     "189.93.254.71",
#     "189.93.255.212"
# ]
#
# # Transforme a lista de strings em uma lista de Python
#
# print(len(lista_ips))
# print(lista_ips)
#
#
#
# import Origem_pg
# import Slot
# testa_slot_lipo(x_origem, y_origem)
#
# x_origem, y_origem = Origem_pg.x_y()
# slot_aberto = Slot.abre_slot(x_origem, y_origem, True)
# Slot.testa_slot_lipo(x_origem, y_origem)
# # status_tarefa = Tarefas.recolher_tarefa_upando(x_origem, y_origem)
# # Slot.ajustar_valor(x_origem, y_origem, True)
# Slot.solot_joga_vezes_upando(x_origem, y_origem)

#
# # Lista de salas para jogar
# lista_salas_jogar = [{'1027': ('2040', 80, 40)}, {'1028': ('2040', 80, 40)}, {'1236': ('2040', 80, 40)},
#                      {'1537': ('2040', 80, 40)}, {'1538': ('2040', 80, 40)}, {'1546': ('2040', 80, 40)},
#                      {'1542': ('2040', 80, 40)}, {'1545': ('2040', 80, 40)}, {'1543': ('2040', 80, 40)},
#                      {'1541': ('2040', 80, 40)}, {'1540': ('2040', 80, 40)},
#                      {'1538': ('2040', 80, 40)}, {'1537': ('2040', 80, 40)}, {'1536': ('2040', 80, 40)},
#                      {'1535': ('2040', 80, 40)},
#                      {'1648': ('2040', 80, 40)}, {'1649': ('2040', 80, 40)}, {'1650': ('2040', 80, 40)},
#                      {'1651': ('2040', 80, 40)}, {'1652': ('2040', 80, 40)},
#                      {'1769': ('2040', 80, 40)}, {'1768': ('2040', 80, 40)}, {'1767': ('2040', 80, 40)},
#                      {'1766': ('2040', 80, 40)}, {'1765': ('2040', 80, 40)}, {'435': ('2040', 80, 40)},
#                      ]
#
# # Ordenar a lista de dicionários com base nas chaves
# lista_salas_ordenada = sorted(lista_salas_jogar, key=lambda x: int(list(x.keys())[0]))
#
# # Exibir a lista ordenada
# print(lista_salas_ordenada)
#
#
# lista_salas_jogar = [{'134': ('2550', 100, 50)}, {'135': ('2550', 100, 50)}, {'999': ('2550', 100, 50)},
#                      {'1003': ('2550', 100, 50)}, {'1004': ('2550', 100, 50)}, {'1243': ('2550', 100, 50)},
#                      {'1245': ('2550', 100, 50)}, {'1246': ('2550', 100, 50)}, {'1247': ('2550', 100, 50)},
#                      {'1673': ('2550', 100, 50)}, {'1674': ('2550', 100, 50)}, {'1675': ('2550', 100, 50)},
#                      {'1676': ('2550', 100, 50)}, {'1677': ('2550', 100, 50)}, {'1678': ('2550', 100, 50)}]
#
# # Especifica o índice de início como 2 para começar do segundo item
# indice_inicial = 0
#
# print(lista_salas_jogar)
#
# for indice, dicionario in enumerate(lista_salas_jogar, start=indice_inicial):
#     print(indice, dicionario)
#
#     if indice == 1:
#         # # Remover o primeiro item da lista usando pop(0)
#         # primeiro_item = lista_salas_jogar.pop(0)
#         # # Adicionar o primeiro item de volta à lista usando append(), colocando-o no final
#         # lista_salas_jogar.append(primeiro_item)
#
#         # Remova o item da posição específica
#         item_removido = lista_salas_jogar.pop(indice)
#         # Adicione o item ao final da lista
#         lista_salas_jogar.append(item_removido)
#
# print(lista_salas_jogar)

#
# #
# import pygetwindow as gw
# import pywinauto
# import time
# import os
#
# # Execute o comando para abrir a janela de configurações
# # os.system("start ms-settings:network-airplanemode")
# time.sleep(2)  # Aguarde um pouco para a janela abrir
#
# # Obtenha a janela ativa usando pygetwindow
# target_window = gw.getActiveWindow()
# if target_window.title == "Configurações":
#     print("A janela é 'Configurações'")
# else:
#     print("A janela não é 'Configurações'")

# # Use pywinauto para obter informações detalhadas da janela
# try:
#     app = pywinauto.Application().connect(handle=target_window._hWnd)
#     target_window = app.top_window()
#     print(f"Título: {target_window.window_text()}")
#     print(f"Classe: {target_window.class_name()}")
#     print(f"Estilo: {hex(target_window.style())}")
#     print(f"ExStyle: {hex(target_window.exstyle())}")
#     # Obter informações sobre sub-janelas, se houver
#     for child_window in target_window.children():
#         print("\n--- Sub-janela ---")
#         print(f"Título: {child_window.window_text()}")
#         print(f"Classe: {child_window.class_name()}")
#         print(f"Estilo: {hex(child_window.style())}")
#         print(f"ExStyle: {hex(child_window.exstyle())}")
# except Exception as e:
#     print(f"Erro ao obter informações da janela: {e}")
#
#
# import ListaIpFirebase
# import IP
# import Google
#
# # ip, com_internet = IP.meu_ip()
#
#
# # lista_negra_ip = Google.lista_ip_banidos()
# #
# # print(lista_negra_ip)
# #
# # # Iterando sobre a lista e chamando a função para cada IP
# # for ip in lista_negra_ip:
# #     ListaIpFirebase.escrever_IP_banido(ip)
#
# ips_banidos_firebase = ListaIpFirebase.lista_ip_banidos()
# print("Lista de IPs banidos do Firebase:", ips_banidos_firebase)


# # Cria uma lista com os IPs banidos
# ips_banidos = [{'ip': '192.168.1.1', 'timestamp': 123456789, 'data_hora': '2024-01-15 12:34:56'},
#                {'ip': '192.168.1.2', 'timestamp': 123456790, 'data_hora': '2024-01-15 12:35:00'},
#                {'ip': '192.168.1.1', 'timestamp': 123456791, 'data_hora': '2024-01-15 12:35:05'},
#                {'ip': '192.168.1.3', 'timestamp': 123456792, 'data_hora': '2024-01-15 12:35:10'}]
#
# # Dicionário temporário para verificar duplicatas
# temp_dict = {}
#
# # Lista resultante sem IPs duplicados
# ips_banidos_sem_duplicatas = []
#
# for ip_info in ips_banidos:
#     ip = ip_info['ip']
#     # Verifica se o IP já foi adicionado
#     if ip not in temp_dict:
#         # Adiciona o IP ao dicionário temporário
#         temp_dict[ip] = True
#         # Adiciona o registro completo à lista resultante
#         ips_banidos_sem_duplicatas.append(ip_info)
#
# # Exibe a lista resultante
# print(ips_banidos_sem_duplicatas)

