import datetime
import time

guias = ["R1", "R2", "R3", "R4", "R5"]

faixa_tempo = 1200  # janela de tempo para sair das contas no tarefas
tempo_total = 18000
tempo_tarefa = 1200
fim_dia = 85800
hora_roleta = 5
minutos_roleta = 0
tempo_total_ciclo = 5
atrasos_roleta = 3600  # valor fixo de tempo que vai atrazar o inicio do Rs secundarios
atrasos_roleta_incremento = 600  # pequeno temo que vai ser agregado ao iniciar as roletas ex 10, 20, 30, 40 minutos


def converter_tempo(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    print(f"horario - {horas}:{minutos}:{segundos_restantes}")


hora_atual = datetime.datetime.now().time()
tempo_atual = (hora_atual.hour * 3600) + (hora_atual.minute * 60) + hora_atual.second
print('Fim da lista, espera horario para iniciar novo R\n Hora: ', hora_atual, tempo_atual)

tempo_atual = 78000
# for j in range(0, 5):
for j, guia_atual in enumerate(guias):
    print("j", j)
    if j == 0:
        inicio_faixa = tempo_total * j
    else:
        inicio_faixa = (tempo_total * j) + atrasos_roleta + (atrasos_roleta_incremento * j)
    print("inicio_faixa", inicio_faixa)
    converter_tempo(inicio_faixa)
    fim_faixa = inicio_faixa + faixa_tempo
    print("fim_faixa", fim_faixa)
    converter_tempo(fim_faixa)

    if inicio_faixa <= tempo_atual <= fim_faixa:
        guia_atual = guias[j]
        print("Tempo atingido, inicia novo R, gia atual:", guia_atual)




for j, guia_atual in enumerate(guias):
    print("j", j)
    if j == 0:
        inicio_faixa = tempo_total * j
    else:
        inicio_faixa = (tempo_total * j) + atrasos_roleta + (atrasos_roleta_incremento * j)
    if inicio_faixa <= tempo_atual <= ((j + 1) * tempo_total - tempo_tarefa):
        print('vai para a guia', guia_atual)







