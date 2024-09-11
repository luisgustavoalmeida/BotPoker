from Firebase import atualizar_configuracao_pc
from IP import iniciando_testando_conexao_internet

iniciando_testando_conexao_internet()

novos_dados = {'confg_funcao': 'roleta_auto'}
atualizar_configuracao_pc(novos_dados)

print(f'\nBanco atualizado com sucesso!, {novos_dados}\n')

