aviso_sistema_global = False


def alterar_global_aviso_sistema(novo_valor):
    global aviso_sistema_global
    aviso_sistema_global = novo_valor
    print('aviso do sistema, Variavel global atualizada:', aviso_sistema_global)
