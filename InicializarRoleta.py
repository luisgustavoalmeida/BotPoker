from Firebase import atualizar_configuracao_pc

novos_dados = {'confg_funcao': 'roleta_auto', 'config_tempo_roleta': '5:00:5'}
atualizar_configuracao_pc(novos_dados)

print(f'\nBanco atualizado com sucesso!, {novos_dados}\n')
