import datetime
import time

import pytz

# Hora atual no fuso horário local
hora_atual_local = datetime.datetime.now()

# Defina o fuso horário desejado (por exemplo, 'America/Sao_Paulo')
# fuso_horario = pytz.timezone('America/Sao_Paulo')

# Defina o fuso horário da Itália
fuso_horario = pytz.timezone('Europe/Rome')

# Converta a hora atual para o fuso horário desejado
hora = hora_atual_local.astimezone(fuso_horario)

# Remover o fuso horário para exibir apenas a data e hora
hora_sem_fuso = hora.replace(tzinfo=None)

print("Hora atual no fuso horário local:", hora_atual_local)
print("Hora atual no fuso horário desejado:", hora_sem_fuso)

print("Dia da semana na Itália:", int(hora.weekday()))


def horario():
    # Obtém a hora atual no fuso horário especificado
    hora_local = datetime.datetime.now(pytz.timezone('Europe/Rome'))
    # Remove o fuso horário para exibir apenas a data e hora
    horario_fuso = hora_local.replace(tzinfo=None)
    return horario_fuso


def dia_semana():
    # 0 segunda, 1 terça, 2 quarta, 3 quinta, 4 sexta, 5 sábado, 6 domingo
    # Obtenha a hora atual no fuso horário da Itália
    hora_local = datetime.datetime.now(pytz.timezone('Europe/Rome'))

    # Pegue o dia da semana (0 = segunda-feira, 6 = domingo)
    dia_da_semana = int(hora_local.weekday())

    print("Dia da semana na Itália:", dia_da_semana)

    return dia_da_semana
