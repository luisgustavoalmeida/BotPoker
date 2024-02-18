# Importe as bibliotecas necessárias
import tkinter as tk
from tkinter import scrolledtext

import Firebase
from Firebase import global_variables

dicionario_comandos = \
    {0: 'Senta', 1: 'Levanta', 2: 'Senta2', 3: 'Aposta', 4: 'Sair', 5: '1K/2K',
     6: '2K/4K', 7: '5K/10K', 8: '10K/20K', 9: '20K/40K', 10: 'Limpa',
     11: 'Senta3', 12: 'Posi_0', 13: 'Posi_1', 14: 'Posi_2', 15: 'Cofre'}


# Função que será chamada quando um botão for pressionado
def button_name(text):
    print(text)

    # Divide a string em três partes com base no hífen
    partes = text.split("-")

    # Verifica se há três partes após a divisão
    if len(partes) == 3:
        # Atribui cada parte a uma variável
        item1, item2, item3 = partes
        # Verifica se item3 é um número válido
        if item3.isdigit():
            item3 = int(item3)
            # Verifique se o item3 existe no dicionário de comandos
            if item3 in dicionario_comandos:
                comando = dicionario_comandos[item3]
                # Verifica o valor de item1 (primeira parte da string)
                if item1 == "A":
                    if item2 == "0":
                        # Se item1 é "A" e item2 é "0", é um comando coletivo no arranjo 1
                        print("comando coletivo no arranjo 1")
                        Firebase.enviar_comando_coletivo(Firebase.arranjo1_pc, comando)
                    else:
                        # Se item1 é "A" e item2 não é "0", é um comando individual no arranjo 1
                        print("comando individual no arranjo 1")
                        item2_str = str(item2).zfill(2)
                        comando_individual = [f'Comandos1/PC{item2_str}']
                        Firebase.enviar_comando_coletivo(comando_individual, comando)

                elif item1 == "B":
                    if item2 == "0":
                        # Se item1 é "B" e item2 é "0", é um comando coletivo no arranjo 2
                        print("comando coletivo no arranjo 2")
                        Firebase.enviar_comando_coletivo(Firebase.arranjo2_pc, comando)
                    else:
                        # Se item1 é "B" e item2 não é "0", é um comando individual no arranjo 2
                        print("comando individual no arranjo 2")
                        item2_str = str(item2).zfill(2)
                        comando_individual = [f'Comandos2/PC{item2_str}']
                        Firebase.enviar_comando_coletivo(comando_individual, comando)

                elif item1 == "C":
                    if item2 == "0":
                        # Se item1 é "C" e item2 é "0", é um comando coletivo no arranjo 3
                        print("comando coletivo no arranjo 3")
                        Firebase.enviar_comando_coletivo(Firebase.arranjo3_pc, comando)
                    else:
                        # Se item1 é "C" e item2 não é "0", é um comando individual no arranjo 3
                        print("comando individual no arranjo 3")
                        item2_str = str(item2).zfill(2)
                        comando_individual = [f'Comandos3/PC{item2_str}']
                        Firebase.enviar_comando_coletivo(comando_individual, comando)

                else:
                    # Se item1 não for "A", "B" ou "C", o arranjo de computadores não está definido
                    print("Arranjo de computadores não definido")
        else:
            print("item3 não é um número válido.")
    else:
        # Se não houver três partes após a divisão, o texto de entrada não possui o formato esperado
        print("Texto de entrada não possui o formato esperado.")


# Função para criar um botão
def create_button(parent, text):
    # Crie um botão com o texto especificado
    custom_font = ("Helvetica", 8, "bold")  # tipo de fonte, tamnho e negrito
    botao = tk.Button(parent, text=text, font=custom_font, width=1, height=1)
    # Associe a função button_name ao botão, passando o texto como argumento
    botao.config(command=lambda t=text: button_name(t))
    # Empacote o botão no widget pai (parent)
    botao.pack(fill="both", expand=True)
    return botao


# Função para criar uma área de texto com barra de rolagem
def create_info_area(parent):
    # Crie uma barra de rolagem vertical
    scrollbar = tk.Scrollbar(parent, orient="vertical")
    # Crie uma fonte personalizada com o tamanho desejado
    custom_font = ("Helvetica", 11, "bold")  # tipo de fonte, tamnho e negrito
    # Crie uma área de texto com rolagem, configurando a barra de rolagem
    info_text = scrolledtext.ScrolledText(parent, wrap=tk.WORD, yscrollcommand=scrollbar.set, font=custom_font)
    scrollbar.config(command=info_text.yview)
    # Configure a largura máxima (por exemplo, 400 pixels)
    info_text.config(width=65)
    # Empacote a área de texto e a barra de rolagem
    info_text.pack(side="top", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    return info_text


# Função para adicionar uma nova informação ao histórico de um arranjo específico
def add_info_to_history(info_text, text_widget):
    # Obtenha o texto atual na área de texto
    current_text = text_widget.get("1.0", "end-1c")
    # Limpe a área de texto
    text_widget.delete("1.0", tk.END)
    # Insira a nova informação no topo da área de texto
    text_widget.insert("1.0", info_text + "\n" + current_text)


# Crie uma janela do Tkinter
janela = tk.Tk()

# Maximize a janela (Windows)
janela.state('zoomed')

# Defina o número de colunas e linhas
numero_colunas = 12
numero_linhas = 16

# Crie as áreas de informações
info_labels = []
info_text_widgets = []

# Letras para identificar cada arranjo
arranjo_letters = ["A", "B", "C"]

# Loop para criar os arranjos
for i in range(3):
    arranjo = tk.Frame(janela)  # Cria um novo arranjo (frame)
    info_text_widget = create_info_area(arranjo)  # Cria uma área de informações dentro do arranjo
    info_text_widgets.append(info_text_widget)  # Adiciona a área de informações à lista

    # Loop para criar as colunas e botões dentro de cada arranjo
    for j in range(numero_colunas):
        # ajustar as colunas conforne a faixa de computadores 1 ao 9
        if j == 1 or j == 2:
            continue  # Pula o primeiro item
        if 1 <= j <= numero_colunas:
            # Aplica a regra de mapeamento para os valores de j
            j = (j - 1) * 3 + 1 + i

        coluna = tk.Frame(arranjo)  # Cria uma nova coluna dentro do arranjo
        for k in range(numero_linhas):
            button_text = f"{arranjo_letters[i]}-{j}-{k}"  # Cria o texto do botão
            create_button(coluna, button_text)  # Cria um botão dentro da coluna
        coluna.pack(side="left", fill="both", expand=True)  # Empacota a coluna

    arranjo.pack(side="left", fill="both", expand=True)  # Empacota o arranjo

# Exiba a janela

# Use a função add_info_to_history para adicionar informações ao histórico de uma área de informações específica
add_info_to_history("Informação 1 do Arranjo 1", info_text_widgets[0])
add_info_to_history("Informação 1 do Arranjo 2", info_text_widgets[1])
add_info_to_history("Informação 1 do Arranjo 3", info_text_widgets[2])

# # Função para atualizar as áreas de texto com base no dicionário global
# def update_text_widgets_inicio():
#
#     # if Firebase.teve_atualizacao:
#     for i, (group, pc_data) in enumerate(global_variables.items()):
#         # Crie uma string para exibir os valores do grupo
#         text = f'{group}:\n'
#         for pc, value in pc_data.items():
#             text += f'{pc}: {value}\n'
#
#         # Atualize o texto na área de texto correspondente em info_text_widgets
#         #info_text_widgets[i].delete('1.0', tk.END)  # Limpe o texto existente
#         info_text_widgets[i].insert(tk.END, text)  # Insira o novo texto
#         info_text_widgets[i].yview_moveto(1.0)# Role a barra de rolagem vertical para a posição "end"
# #             Firebase.teve_atualizacao = False
# #     # Agende a próxima chamada desta função após 5 segundos (ou ajuste o intervalo desejado)
# #     janela.after(3000, update_text_widgets)
# #
# #
# # # Agende a primeira chamada da função após 5 segundos
# # janela.after(500, update_text_widgets)
# update_text_widgets_inicio()


# Crie um dicionário para armazenar os valores anteriores dos grupos
valores_anteriores = {group: dict(pc_data) for group, pc_data in global_variables.items()}


def update_text_widgets():
    # global valores_anteriores

    if Firebase.teve_atualizacao:
        print('tem atualizações')
        for i, (group, pc_data) in enumerate(global_variables.items()):

            # Verifique se os valores atuais são diferentes dos valores anteriores
            if pc_data != valores_anteriores[group]:
                # Se houver diferença, crie uma string para exibir os valores do grupo
                text = f'{group}:\n'
                for pc, value in pc_data.items():
                    text += f'{pc}: {value}\n'

                # Atualize o texto na área de texto correspondente em info_text_widgets
                # info_text_widgets[i].delete('1.0', tk.END)  # Limpe o texto existente
                info_text_widgets[i].insert(tk.END, text)  # Insira o novo texto
                info_text_widgets[i].yview_moveto(1.0)  # Role a barra de rolagem vertical para a posição "end"

                # Atualize os valores anteriores para refletir os valores atuais
                valores_anteriores[group] = dict(pc_data)
        Firebase.teve_atualizacao = False

    # Agende a próxima chamada desta função após 5 segundos (ou ajuste o intervalo desejado)
    janela.after(300, update_text_widgets)


janela.after(500, update_text_widgets)

# Inicie o loop principal da interface gráfica
janela.mainloop()
