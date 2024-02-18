# pip install pyrebase5
import os
import re
import socket
import time

import pyrebase
import requests
from requests.exceptions import ConnectionError

from Google import dicionari_token_credencial_n

# importa o dicionário com os nomes dos computadores e o námero referete a cada um
# from Parametros import dicionari_token_credencial_n

config = {
    "apiKey": "AIzaSyDDzQMVxpKKqBZrDlhA9E4sInXB5toVRT8",
    "authDomain": "pokerdados-6884e.firebaseapp.com",
    "databaseURL": "https://pokerdados-6884e-default-rtdb.firebaseio.com",
    "projectId": "pokerdados-6884e",
    "storageBucket": "pokerdados-6884e.appspot.com",
    "messagingSenderId": "240019464920",
    "appId": "1:240019464920:web:a746cddaf41f43642aadad"
}

# Dicionário global para armazenar as variáveis com seus respectivos valores
global_variables = {
    'group1': {'PC07': None, 'PC10': None, 'PC13': None, 'PC16': None, 'PC19': None, 'PC22': None, 'PC25': None, 'PC28': None, 'PC31': None},
    'group2': {'PC08': None, 'PC11': None, 'PC14': None, 'PC17': None, 'PC20': None, 'PC23': None, 'PC26': None, 'PC29': None, 'PC32': None},
    'group3': {'PC09': None, 'PC12': None, 'PC15': None, 'PC18': None, 'PC21': None, 'PC24': None, 'PC27': None, 'PC30': None, 'PC33': None}
}
orderem_chave = {
    'group1': ['PC07', 'PC10', 'PC13', 'PC16', 'PC19', 'PC22', 'PC25', 'PC28', 'PC31'],
    'group2': ['PC08', 'PC11', 'PC14', 'PC17', 'PC20', 'PC23', 'PC26', 'PC29', 'PC32'],
    'group3': ['PC09', 'PC12', 'PC15', 'PC18', 'PC21', 'PC24', 'PC27', 'PC30', 'PC33']
}

# Define listas de arranjos de computadores cada arranjo será uma mesa diferente
arranjo1_pc = (
    'Comandos1/PC07', 'Comandos1/PC10', 'Comandos1/PC13', 'Comandos1/PC16', 'Comandos1/PC19', 'Comandos1/PC22',
    'Comandos1/PC25', 'Comandos1/PC28', 'Comandos1/PC31'
)

arranjo2_pc = (
    'Comandos2/PC08', 'Comandos2/PC11', 'Comandos2/PC14', 'Comandos2/PC17', 'Comandos2/PC20', 'Comandos2/PC23',
    'Comandos2/PC26', 'Comandos2/PC29', 'Comandos2/PC32'
)

arranjo3_pc = (
    'Comandos3/PC09', 'Comandos3/PC12', 'Comandos3/PC15', 'Comandos3/PC18', 'Comandos3/PC21', 'Comandos3/PC24',
    'Comandos3/PC27', 'Comandos3/PC30', 'Comandos3/PC33'
)

#  lista com os computadores que vao dar comando nos escravos, colocar nesta lista para funcionar como metre
lista_PC_meste = ('PC-I7-9700KF', 'PC-i3-8145U', 'Thiago-PC')

teve_atualizacao = False
comando_escravo = None

nome_computador = socket.gethostname()
print('nome_computador', nome_computador)
nome_usuario = os.getlogin()

nome_completo = nome_computador + "_" + nome_usuario


def cria_caminho_resposta_fb():
    """Função destinada a manipular o dicionário com os nomes dos computadores
    e criar um caminho para apontar na função callback """

    caminho_resposta = f'Comandos/PCXX'
    caminho_resposta1 = f'Resposta1/PCXX'

    # Crie um dicionário com os valores formatados
    dicionari_pc = {}
    for chave, (_, _, terceiro_item, *_resto) in dicionari_token_credencial_n.items():
        # Formate o valor para ter dois dígitos e adicione "PC" antes
        valor_formatado = f"PC{terceiro_item:02d}"
        dicionari_pc[chave] = valor_formatado

    # Verifique se o nome completo existe no dicionário
    if nome_completo in dicionari_pc:
        conteudo = dicionari_pc[nome_completo]
        print(f"Conteúdo para {nome_completo}: {conteudo}")

        # Verifique em qual grupo o conteúdo está
        for grupo, membros in global_variables.items():
            print(grupo)
            print(membros)
            if conteudo in membros:
                # Use uma expressão regular para extrair o número após 'group'
                numero_grupo = re.search(r'group(\d+)', grupo).group(1)
                # Use re.sub para substituir "group" por "Comandos"
                grupo_modificado = re.sub(r'group', r'Comandos', grupo)
                print(f"{conteudo} está no grupo {grupo_modificado} ({numero_grupo})")
                caminho_resposta = f'{grupo_modificado}/{conteudo}'
                print("caminho_resposta :", caminho_resposta)  # Comandos2/PC23
                caminho_resposta1 = f'Resposta1/{conteudo}'
                print("caminho_resposta1 :", caminho_resposta1)  # Comandos2/PC23
                return caminho_resposta, caminho_resposta1
        else:
            print(f"{conteudo} não está em nenhum dos grupos")
            return caminho_resposta, caminho_resposta1

    else:
        print(f"{nome_completo} não encontrado no dicionário")
        return caminho_resposta, caminho_resposta1


if nome_computador in lista_PC_meste:
    print(f"O nome do computador ({nome_computador}) está na lista de PCs mestres.")
    caminho_resposta = f"Resposta1"
else:
    print(f"O nome do computador ({nome_computador}) não está na lista de PCs mestres.")
    caminho_resposta, caminho_resposta1 = cria_caminho_resposta_fb()


def inicializar_firebase():
    while True:
        response = requests.get('http://www.google.com', timeout=5)
        if response.status_code == 200 or response.status_code == 429:
            try:
                firebase = pyrebase.initialize_app(config)
                return firebase
            except ConnectionError as e:
                print(f"Erro de conexão com o Firebase: {e}")
                print("Tentando reconectar em 5 segundos...")
                time.sleep(5)
        else:
            print('firebase sem internete')
            time.sleep(5)


def enviar_comando_coletivo(arranjo, comando):
    """Envie nesta fonção dois parametros que pode ser a tiplae dos arranjos dos conputadores "arranjo3_pc" ou
    uma lista do com um unico itêm "['Comandos3/PC03']" que contenha o caminho e nome do computado a ser atualizado.
    O segundo paremetro a ser recebido deve ser o comando que deve ser executado pelo arranjo de computadores ou pelo
    computador individual ex: "senta", "passa" ..."""
    global firebase, db
    atualizacoes = {}
    for caminho in arranjo:
        # Define a chave do dicionário como o caminho e o valor como o comando
        atualizacoes[caminho] = comando
    try:
        db.update(atualizacoes)  # responsável por atualizar os dados no banco de dados Firebase
        print("Comando coletivo executado")
    except Exception as e:
        print("Erro ao processar atualização:", e)


# Função de callback para manipular os dados quando houver uma atualização
def on_update(event):
    try:
        print("Atualização detectada:")
        print(event)  # Aqui você pode acessar diretamente os dados atualizados
        # Acessar o valor associado à chave 'data' no dicionário 'event'
        dado_atualizado = event['data']
        caminho_atualizado = event['path']
        print(caminho_atualizado)
        print(dado_atualizado)
        alterar_dado_global(caminho_atualizado, dado_atualizado)

    except Exception as e:
        print("Erro ao processar atualização:", e)
        # Se ocorrer um erro durante a atualização, aguarde e tente novamente
        time.sleep(5)  # Ajuste o tempo de espera conforme necessário
        print("Tentando reconectar...")
        # reconectar_firebase()


# Inicializa o Firebase
firebase = pyrebase.initialize_app(config)

# Obtém uma referência para o banco de dados
db = firebase.database()

if nome_computador in lista_PC_meste:
    print(f"{nome_completo} está na lista de PCs mestres.")
    # # Referência para o nó do Firebase que você deseja observar
    ref = firebase.database().child(caminho_resposta)  # colocar o caminho de onde vem os comandos
    #
    # # Registrar o observador usando o método "stream"
    # # A função "on" irá chamar a função "on_update" sempre que ocorrer uma edição no nó referenciado
    ref.stream(on_update)
else:

    print(f"{nome_completo} não está na lista de PCs mestres.")


def comando_escravo():
    # global comando_escravo
    try:
        dado = db.child(caminho_resposta).get().val()
        if dado:
            # Faça algo com os dados
            # print(f"O dado em {caminho_resposta} é: {dado}")
            return dado
        else:
            print("Nenhum dado encontrado no caminho:", caminho_resposta)
    except Exception as e:
        print("Erro ao obter dados:", str(e))


# Função para reconectar ao Firebase
# def reconectar_firebase():
#     global firebase, db, ref, caminho_resposta
#     print("Tentando reconectar ao Firebase...")
#     firebase = inicializar_firebase()
#     db = firebase.database()
#     ref = firebase.database().child(caminho_resposta)  # colocar o caminho de onde vem os comandos
#     ref.stream(on_update)
# reconectar_firebase()


def alterar_dado_global(nome_variavel, valor):
    global global_variables
    global teve_atualizacao
    global comando_escravo
    grupo = None
    nome_variavel = nome_variavel.replace('/', '')

    print('nome_variavel:', nome_variavel)

    if "PC" in nome_variavel:
        # Verifique em qual grupo colocar a variável com base no nome_variavel
        if nome_variavel in orderem_chave['group1']:
            grupo = global_variables['group1']
        elif nome_variavel in orderem_chave['group2']:
            grupo = global_variables['group2']
        elif nome_variavel in orderem_chave['group3']:
            grupo = global_variables['group3']

        if grupo is not None:
            grupo[nome_variavel] = valor
            teve_atualizacao = True
            # print(global_variables)
        else:
            print(f"A variável '{nome_variavel}' não corresponde a nenhum grupo existente.")
    else:
        print("é um comando para uma escravo")

        comando_escravo = valor

        print("comando: ", comando_escravo)


def atualizar_dados_globais():
    # Função para atualizar as informações do dicionário global com os dados do Firebase
    global firebase, db
    try:
        # Use db.child() para acessar o nó desejado no Firebase
        dados_firebase = db.child(caminho_resposta).get()

        if dados_firebase.each() is not None:
            for dado in dados_firebase.each():
                chave = dado.key()  # Obtém a chave (nome da variável)
                valor = dado.val()  # Obtém o valor associado à chave
                alterar_dado_global(chave, valor)

    except Exception as e:
        print("Erro ao buscar dados do Firebase:", e)

    # print(f"Atualizado: {chave} -> {valor}")


# Chame a função para atualizar os dados globais com os dados do Firebase
atualizar_dados_globais()


def escreve_resposta_escravo(resposta_escravo):
    ''' da a resposta do estado do computador '''
    global firebase, db
    try:
        # Escreva a informação aleatória no banco de dados Firebase
        db.child(caminho_resposta1).set(resposta_escravo)
        # print(f"Informação {resposta_escravo} escrita com sucesso em {caminho_resposta1}")
    except Exception as e:
        print(f"Ocorreu um erro ao escrever a informação: {str(e)}")


resposta_anterior = None


def confirmacao_escravo(resposta_escravo):
    global resposta_anterior
    '''Esta função escreve no banco onde é destinado a receber comando, com o intuito de deixar um comando nao aplicavel'''
    global firebase, db
    if resposta_anterior != resposta_escravo:
        resposta_anterior = resposta_escravo
        # LEMBRETE, criar um teste para mandar comando apenas se o valor for diferete do anterior
        try:
            # Escreva a informação aleatória no banco de dados Firebase
            db.child(caminho_resposta).set(resposta_escravo)
            print(f"Informação: {resposta_escravo}, escrita com sucesso em: {caminho_resposta}")
        except Exception as e:
            print(f"Ocorreu um erro ao escrever a informação: {str(e)}")
    else:
        return


def confirmacao_comando_resposta(resposta_escravo):
    global resposta_anterior
    '''Esta função escreve no banco onde é destinado a receber comando, com o intuito de deixar um comando não aplicável'''

    if resposta_anterior != resposta_escravo:
        # # Crie um dicionário com os caminhos de resposta e seus valores correspondentes
        # dados_para_atualizar = {
        #     caminho_resposta1: resposta_escravo,
        #     caminho_resposta: resposta_escravo
        # }
        # try:
        #     # Use a função update() para atualizar ambos os caminhos com os respectivos valores
        #     db.update(dados_para_atualizar)
        #
        #     resposta_anterior = resposta_escravo
        #
        #     print(f"Informação: {resposta_escravo}, escrita com sucesso em: {caminho_resposta} e {caminho_resposta1}")
        #     time.sleep(2)
        # except Exception as e:
        #     resposta_anterior = None
        #     print(f"Ocorreu um erro ao escrever a informação: {str(e)}")
        if resposta_escravo == "Sair":
            confirmacao_escravo('Saindo')

        escreve_resposta_escravo(resposta_escravo)
        resposta_anterior = resposta_escravo
    else:
        return


def comando_coleetivo_escravo_escravo(comando):
    ''''quando um escravo precisa comandar os outro escravos de forma automatica'''
    if nome_usuario == "PokerIP":
        print(nome_usuario)
        enviar_comando_coletivo(arranjo1_pc, comando)
    elif nome_usuario == "lgagu":
        print(nome_usuario)
        enviar_comando_coletivo(arranjo2_pc, comando)
    elif nome_usuario == "Poker":
        print(nome_usuario)
        enviar_comando_coletivo(arranjo3_pc, comando)
    else:
        print("nome de usuario não configurado")

# caminho = "Resposta1/PC01"
#
# def escrever_informacoes_aleatorias():
#
#     # Gere uma informação aleatória (por exemplo, um número aleatório)
#     informacao_aleatoria = random.randint(1, 100)
#     try:
#         # Escreva a informação aleatória no banco de dados Firebase
#         db.child(caminho).set(informacao_aleatoria)
#         print(f"Informação aleatória {informacao_aleatoria} escrita com sucesso em {caminho}")
#     except Exception as e:
#         print(f"Ocorreu um erro ao escrever a informação: {str(e)}")

# def loop_infinito():
#     global global_variables
#     while True:
#         print(global_variables)
#         escrever_informacoes_aleatorias()


# loop_infinito()


# Mantenha o programa em execução para continuar recebendo as atualizações
# while True:
#     time.sleep(10)
#     variavel = obter_dado()
#     print('ta rodando')
#     print(variavel)
#     pass


# escrever_dado("Comandos/PC01/Teste", "Firebase!")
#
# ler_dado("Comandos/PC01/Teste")

# confirmacao_escravo("funciona")
# escreve_resposta_escravo("funciona")


# comando_escravo()
