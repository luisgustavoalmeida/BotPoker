import datetime
import time

from IP import ip_troca_agora

guias = ["R1", "R2", "R3", "R4", "R5"]

faixa_tempo = 1200  # janela de tempo para sair das contas no tarefas
tempo_total = 18000
tempo_tarefa = 1200
fim_dia = 85800
hora_roleta = 5
minutos_roleta = 0
tempo_total_ciclo = 5


def mudar_guia(id, guia, config_tempo_roleta='4:00:5'):
    global tempo_total, tempo_tarefa, tempo_total_ciclo, hora_roleta, minutos_roleta
    print('mudar_guia', config_tempo_roleta)

    # Atribuindo os valores da lista às variáveis
    if isinstance(config_tempo_roleta, str) and ':' in config_tempo_roleta:
        if config_tempo_roleta.count(":") == 2:
            try:
                tempo_separado = config_tempo_roleta.split(':')
                try:
                    hora_roleta = int(tempo_separado[0])
                except ValueError:
                    print("Erro: A hora não é um número válido")
                    hora_roleta = 4

                try:
                    minutos_roleta = int(tempo_separado[1])
                except ValueError:
                    print("Erro: Os minutos não são um número válido")
                    minutos_roleta = 00

                try:
                    tempo_total_ciclo = int(tempo_separado[2])
                except ValueError:
                    print("Erro: O tempo total do ciclo não é um número válido")
                    tempo_total_ciclo = 5
            except TypeError as e:
                print(e)

    tempo_roletas = (hora_roleta * 3600) + (minutos_roleta * 60)  # 4h

    tempo_total = 3600 * tempo_total_ciclo  # 5 horas em segudos

    tempo_tarefa = tempo_total - tempo_roletas  # tempo tarefa em segundos # tempo total menos tempo não usado nas roletas

    hora_atual = datetime.datetime.now().time()

    tempo_atual = (hora_atual.hour * 3600) + (hora_atual.minute * 60) + hora_atual.second

    while (17580 < tempo_atual < 18000) or (35580 < tempo_atual < 36000) or (53580 < tempo_atual < 54000) or (71580 < tempo_atual < 72000):
        print('espera 7 minutoa para organisar a planilha')
        time.sleep(45)
        hora_atual = datetime.datetime.now().time()
        tempo_atual = (hora_atual.hour * 3600) + (hora_atual.minute * 60) + hora_atual.second

    if tempo_atual > fim_dia:
        ip_troca_agora()

    while tempo_atual > fim_dia:  # se maior que 23:55:00
        print('Espera virar 0h')
        time.sleep(45)
        hora_atual = datetime.datetime.now().time()
        tempo_atual = (hora_atual.hour * 3600) + (hora_atual.minute * 60) + hora_atual.second

    if guia in ["R1", "R2", "R3", "R4", "R5"]:
        if id == "":  # se a cabou o R vai para tarefa
            if tempo_tarefa > 0:  # se tem algim tempo destinado as tarefas
                print('Fim do R, vai para as tarefas')
                # T1
                guia_atual = "T1"
                print('vai para a guia', guia_atual)
                return guia_atual
            elif tempo_tarefa <= 0:
                # print('hora teste 3')
                ip_troca_agora()
                while True:
                    hora_atual = datetime.datetime.now().time()
                    tempo_atual = (hora_atual.hour * 3600) + (hora_atual.minute * 60) + hora_atual.second
                    print('Fim da lista, espera horario para iniciar novo R\n Hora: ', hora_atual)
                    time.sleep(30)

                    for j in range(0, 5):
                        inicio_faixa = tempo_total * j
                        fim_faixa = inicio_faixa + faixa_tempo
                        if inicio_faixa <= tempo_atual <= fim_faixa:
                            print("tempo atigido, inicia novo R")
                            for i, guia_atual in enumerate(guias):
                                print("gia atual:", guia_atual)
                                if (i * tempo_total) <= tempo_atual <= ((i + 1) * tempo_total - tempo_tarefa):
                                    print('vai para a guia', guia_atual)
                                    return guia_atual

        else:
            for i, guia_atual in enumerate(guias):
                # print("gia atual:", guia_atual)
                if (i * tempo_total) <= tempo_atual <= ((i + 1) * tempo_total - tempo_tarefa):
                    print('vai para a guia', guia_atual)
                    return guia_atual
            # T1
            guia_atual = "T1"
            print('vai para a guia', guia_atual)
            return guia_atual

    elif guia == "T1":
        if id == "":
            print('Fim do tarefas, espera a hora para começar os Rs')
            ip_troca_agora()
            while True:
                hora_atual = datetime.datetime.now().time()
                tempo_atual = (hora_atual.hour * 3600) + (hora_atual.minute * 60) + hora_atual.second
                print('Fim da lista, espera pelo horario para iniciar novo R. \n Hora: ', hora_atual)
                time.sleep(30)

                for j in range(0, 5):
                    inicio_faixa = tempo_total * j
                    fim_faixa = inicio_faixa + faixa_tempo
                    if inicio_faixa <= tempo_atual <= fim_faixa:
                        print("tempo atigido, inicia novo R")
                        for i, guia_atual in enumerate(guias):
                            print("gia atual:", guia_atual)
                            if (i * tempo_total) <= tempo_atual <= ((i + 1) * tempo_total - tempo_tarefa):
                                print('vai para a guia', guia_atual)
                                return guia_atual
        else:
            print('não acabou o tarefa')
            for j in range(0, 5):
                inicio_faixa = tempo_total * j
                fim_faixa = inicio_faixa + faixa_tempo
                if inicio_faixa <= tempo_atual <= fim_faixa:
                    print("tempo atigido, inicia novo R")
                    for i, guia_atual in enumerate(guias):
                        if (i * tempo_total) <= tempo_atual <= ((i + 1) * tempo_total - tempo_tarefa):
                            print('vai para a guia', guia_atual)
                            return guia_atual
                # T1
            guia_atual = "T1"
            print('vai para a guia', guia_atual)
            return guia_atual

    else:
        for i, guia_atual in enumerate(guias):
            # print("gia atual:", guia_atual)
            if (i * tempo_total) <= tempo_atual <= ((i + 1) * tempo_total - tempo_tarefa):
                print('vai para a guia', guia_atual)
                return guia_atual
        # T1
        guia_atual = "T1"
        print('vai para a guia', guia_atual)
        return guia_atual


def fim_tempo_tarefa():
    hora_atual = datetime.datetime.now().time()

    tempo_atual = (hora_atual.hour * 3600) + (hora_atual.minute * 60) + hora_atual.second  # hora atual em segundos
    print("Testa se esta na hora de parar o tarefas, tempo_atual: ", tempo_atual)

    if tempo_atual > 85800:  # proximo das 24H - 10 minutos
        print('Interrompe a tarefa e vai pra o R1, proximo das 0h')
        return True
    elif 0 < tempo_atual < tempo_total:  # se menor que 5H
        print("Continua fazendo tarefas, tempo menor que 5H")
        return False

    for i in range(1, 5):
        if ((tempo_total * i) - tempo_tarefa) <= tempo_atual <= (((tempo_total * i) - tempo_tarefa) + tempo_tarefa):
            print("Continua fazendo tarefas")
            return False

    for i in range(0, 5):  # do 0 ate o 4
        if (tempo_total * i) < tempo_atual < ((tempo_total * i) + faixa_tempo):
            print('Interrompe a tarefa e vai para o R')
            return True

    print("outro, Continua fazendo tarefas")
    return False
