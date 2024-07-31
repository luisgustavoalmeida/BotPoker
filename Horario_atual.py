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

print("Hora atual no fuso horário local:", hora_atual_local)
print("Hora atual no fuso horário desejado:", hora)


def horario():
    hora_atual = hora_atual_local.astimezone(fuso_horario)
    return hora_atual
