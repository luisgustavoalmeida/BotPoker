lista_tarefas_fazer = ['Gioca la Carta Genio del Casino per 50 volte', 'Gioca 20 mani su un tavolo con bui maggiori di 50']
missao_encontrada = False
for item_tarefa in lista_tarefas_fazer:
    print(item_tarefa)
    if 'Jogar o caca-niquel da mesa' in item_tarefa:
        missao_encontrada = True
    elif 'Gioca alla Slot machine al tavolo' in item_tarefa:
        missao_encontrada = True

print(missao_encontrada)