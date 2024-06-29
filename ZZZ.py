def encontrar_indices_vazios(lista, indece):
    """
    Encontra os valores dos três primeiros índices vazios ('') em uma lista.

    Parameters:
    - lista (list): A lista a ser verificada.

    Returns:
    - list: Uma lista contendo os valores dos três primeiros índices vazios.
    """
    indices_vazios = []
    for i, value in enumerate(lista):
        if value == '':
            indices_vazios.append(i)
            if len(indices_vazios) == indece:
                print('ok')

                return True, indices_vazios[indece - 1]
    return False, 0


# Exemplo de uso
values2 = ['', 6, 1, 25, 33, '', 39, 38, 13, 17, '', 34, 35, 29, 5, 33, 11, 30, 22, 15, 15, 16, 43, 7, 8, 7, 4, 20, 14, 24, 37,
         36, 25, 31, 34, 28, 17, 22, 46, 31, 15, 43, 12, 19, 28, 13, 13, 18, 26, 46, 15, 9, 22, 11, 23, 37, 17, 33, 30, 7, 32, 16, 33,
         7, 37, 34, 8, 8, 14, 25, 5, 10, 14, 23, 31, 27, 46, 13, 34, 18, 12, 31, 38, 9, 11, 16, 36, 14, 33, 2, 1, 43, 43, 1, 29, 25, 21, 15, 26, 20,
         37, 32, 4, 10, 43, 28, 19, 28, 16, 29, 18, 11, 32, 43, 18, 35, 35, 17, 4, 34, 23, 2, 30, 15, 20, 2, 26, 38, 25, 19, 39, 22, 36, 10,
         27, 16, 11, 7, 46, 7, 1, 21, 13, 24, 43, 4, 19, 23, 2, 31, 17, 33, 22, 7, 28, 8, 12, 34, 12, 27, 8, 36, 17, 9, 25, 35, 26, 10, 32, 14, 15,
         36, 33, 2, 20, 34, 20, 25, 1, 4, 1, 22, 31, 16, 31, 33, 38, 15, 21, 13, 37, 21, 28, 9, 18, 29, 19, 11, 46, 26, 46, 14, 10, 6, 10, 36, 19, 43,
         16, 24, 38, 10, 37, 2, 20, 13, 35, 30, 25, 34, 30, 7, 5, 1, 23, 29, 8, 34, 9, 26, 8, 24, 43, 28, 19, 16, 6, 21, 2, 32, 36, 4, 32, 17, 22, 23,
         25, 34, 1, 7, 21, 30, 11, 5, 27, 27, 23, 43, 35, 16, 17, 28, 15, 13, 31, 20, 10, 31, 33, 36, 43, 14, 14, 1, 39, 46, 18, 15, 28, 9, 43, 46,
         26, 11, 35, 4, 32, 13, 22, 13, 33, 27, 20, 7, 29, 29, 10, 19, 11, 25, 34, 25, 12, 2, 2, 18, 31, 26, 43, 32, 7, 15, 4, 17, 16, 14, 30, 28, 46,
         38, 38, 39, 32, 19, 14, 34, 24, 34, 24, 23, 43, 12, 5, 36, 36, 10, 33, 25, 37, 22, 25, 1, 35, 37, 46, 32, 8, 11, 16, 31, 16, 43, 13, 2, 33,
         29, 17, 17, 39, 18, 7, 32, 30, 20, 20, 10, 18, 26, 46, 15, 29, 22, 25, 1, 19, 28, 35, 28, 31, 11, 19, 5, 31, 14, 9, 26, 23, 16, 36, 25, 21,
         27, 10, 34, 12, 37, 8, 20, 46, 24, 34, 7, 4, 38, 14, 23, 30, 2, 2, 43, 1, 43, 1, 30, 16, 9, 25, 34, 36, 35, 13, 29, 31, 39, 21, 28, 22, 4,
         26, 27, 17, 17, 15, 29, 35, 5, 30, 25, 6, 38, 43, 8, 9, 18, 43, 31, 28, 19, 25, 31, 8, 9, 24, 7, 7, 13, 14, 37, 1, 36, 1, 13, 46, 34, 12, 19,
         24, 14, 33, 16, 2, 2, 39, 35, 23, 2, 8, 7, 10, 22, 36, 16, 15, 15, 46, 29, 28, 28, 9, '', '', '', '']
values = []

print(values)
intervalo_de_busca = 500
linha_vazia_anterior = 10
indece_usuario = 1
teste_indece, indices_vazio = encontrar_indices_vazios(values, indece_usuario)
print('indices_vazio', indices_vazio)
# i = values.index("")
# print(i)
if teste_indece:
    print('linha encontrada: ', linha_vazia_anterior)
    linha_vazia_anterior += indices_vazio
    print('linha nova: ', linha_vazia_anterior)
    endereco = f"D{linha_vazia_anterior}"
    print("endereco", endereco)

else:
    tamanho_lista = len(values)
    print('tamanho_lista', tamanho_lista)

    if tamanho_lista <= intervalo_de_busca:
        print('2linha encontrada: ', linha_vazia_anterior)
        linha_vazia_anterior += (tamanho_lista + indece_usuario - 1)
        print('2linha nova: ', linha_vazia_anterior)
        endereco = f"D{linha_vazia_anterior}"
        print(endereco)


    linha_vazia_anterior += intervalo_de_busca

