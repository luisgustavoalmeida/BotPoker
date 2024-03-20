from Firebase import atualizar_configuracao_pc

novos_dados = {'confg_funcao': 'Face'}
atualizar_configuracao_pc(novos_dados)

print(f'\nBanco atualizado com sucesso!, {novos_dados}\n')