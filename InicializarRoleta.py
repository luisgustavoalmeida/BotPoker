from Firebase import atualizar_configuracao_pc

novos_dados = {'confg_funcao': 'roleta_auto', 'config_tempo_roleta': '4:40:5'}
atualizar_configuracao_pc(novos_dados)

print('\nBanco atualizado com sucesso!\n')
