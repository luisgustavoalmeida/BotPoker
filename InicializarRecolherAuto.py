from Firebase import atualizar_configuracao_pc

novos_dados = {'confg_funcao': 'Recolher_automatico', 'blind_recolher_auto': '1K2K', 'config_tempo_roleta': '4:40:5'}
atualizar_configuracao_pc(novos_dados)

print('\nBanco atualizado com sucesso!\n')
