import datetime
import pytz

# Hora atual no fuso horário local
hora_atual_local = datetime.datetime.now()

# Defina o fuso horário desejado (por exemplo, 'America/Sao_Paulo')
# fuso_horario = pytz.timezone('America/Sao_Paulo')

# Defina o fuso horário da Itália
fuso_horario = pytz.timezone('Europe/Rome')

# Converta a hora atual para o fuso horário desejado
hora = hora_atual_local.astimezone(fuso_horario)

# Formate a hora sem incluir o fuso horário
hora_formatada = hora.strftime('%Y-%m-%d %H:%M:%S.%f')

print("Hora atual no fuso horário local:", hora_atual_local)
print("Hora atual no fuso horário desejado:", hora_formatada)


def horario():
    hora_atual = hora_atual_local.astimezone(fuso_horario)
    hora_atual = hora_atual.strftime('%Y-%m-%d %H:%M:%S.%f')
    return hora_atual
