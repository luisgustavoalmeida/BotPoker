# pip install pyrebase5
import time
import pyrebase
import requests
from requests.exceptions import ConnectionError

from Requerimentos import numero_pc, nome_computador, nome_usuario, nome_completo

config = {
    "apiKey": "AIzaSyCZ7PjgHEe16o9KFAsZ4eZ3PjiAJ06qWlE",
    "authDomain": "pokerdados-faf1f.firebaseapp.com",
    "databaseURL": "https://pokerdados-faf1f-default-rtdb.firebaseio.com",
    "projectId": "pokerdados-faf1f",
    "storageBucket": "pokerdados-faf1f.appspot.com",
    "messagingSenderId": "368579247698",
    "appId": "1:368579247698:web:3429ba54dcb18127f5a98b"
}

# Dicionário global para armazenar as variáveis com seus respectivos valores
global_variables = {
    'group1': {'PC10': None, 'PC13': None, 'PC16': None, 'PC19': None, 'PC22': None, 'PC25': None, 'PC28': None, 'PC31': None, 'PC34': None},
    'group2': {'PC11': None, 'PC14': None, 'PC17': None, 'PC20': None, 'PC23': None, 'PC26': None, 'PC29': None, 'PC32': None, 'PC35': None},
    'group3': {'PC12': None, 'PC15': None, 'PC18': None, 'PC21': None, 'PC24': None, 'PC27': None, 'PC30': None, 'PC33': None, 'PC36': None}
}

# Define listas de arranjos de computadores cada arranjo será uma mesa diferente
# Criando as tuplas diretamente a partir do dicionário
arranjo1_pc = tuple(f"Comandos1/{pc}" for pc in global_variables['group1'])
arranjo2_pc = tuple(f"Comandos2/{pc}" for pc in global_variables['group2'])
arranjo3_pc = tuple(f"Comandos3/{pc}" for pc in global_variables['group3'])

#  lista com os computadores que vao dar comando nos escravos, colocar nesta lista para funcionar como metre
lista_PC_meste = ('xPC-I7-9700KF', 'xPC-i3-8145U', 'xPC-R5-7600')
# roleta_auto Substituir_codigo Atualizar_codigo
# Dados padrões de configuração a serem escritos
dados_config = {
    'PC01': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC02': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC03': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC04': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC05': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC06': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC07': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC08': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC09': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC10': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC11': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC12': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC13': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC14': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC15': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC16': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC17': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC18': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC19': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC20': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC21': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC22': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC23': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC24': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC25': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC26': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC27': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC28': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC29': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC30': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC31': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC32': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC33': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC34': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC35': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC36': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC37': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC38': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC39': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC40': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC41': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC42': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC43': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC44': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC45': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC46': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC47': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC48': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC49': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC50': {'confg_funcao': 'roleta_auto', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
    'PC51': {'confg_funcao': 'Atualizar_codigo', 'config_tempo_roleta': '0:00:5', 'blind_recolher_auto': '5001K', 'confg_secundaria': 'auto'},
}

teve_atualizacao = False
comando_escravo = None
resposta_anterior = None
status_anterior = None


def cria_caminho_resposta_fb():
    """Função destinada a manipular o dicionário com os nomes dos computadores
    e criar um caminho para apontar na função callback """

    if numero_pc in global_variables['group1']:
        caminho_resposta = f'Comandos1/{numero_pc}'
    elif numero_pc in global_variables['group2']:
        caminho_resposta = f'Comandos2/{numero_pc}'
    elif numero_pc in global_variables['group3']:
        caminho_resposta = f'Comandos3/{numero_pc}'
    else:
        print(f"{numero_pc} não está em nenhum dos arranjos")
        caminho_resposta = f'Comandos_despadronizado/{numero_pc}'

    caminho_resposta1 = f'Resposta1/{numero_pc}'

    print("caminho_resposta :", caminho_resposta)
    print("caminho_resposta1 :", caminho_resposta1)
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
        if response.status_code == 200:
            try:
                firebase = pyrebase.initialize_app(config)
                return firebase
            except ConnectionError as e:
                print(f"Erro de conexão com o Firebase: {e}")
                print("Tentando reconectar em 5 segundos...")
                time.sleep(1)
        else:
            print('firebase sem internete')
            time.sleep(1)


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

        # print("Atualização detectada:", event)  # Aqui você pode acessar diretamente os dados atualizados
        # Acessar o valor associado à chave 'data' no dicionário 'event'
        dado_atualizado = event['data']
        caminho_atualizado = event['path']
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
    # # Registrar o observador usando o método "stream"
    # # A função "on" irá chamar a função "on_update" sempre que ocorrer uma edição no nó referenciado
    ref.stream(on_update)
else:
    print(f"{nome_completo} não está na lista de PCs mestres.")


def comando_escravo():
    try:
        dado = db.child(caminho_resposta).get().val()
        if dado:
            # print(f"O dado em {caminho_resposta} é: {dado}")
            return dado
        else:
            print("Nenhum dado encontrado no caminho:", caminho_resposta)
    except Exception as e:
        print("Erro ao obter dados:", str(e))


def alterar_dado_global(nome_variavel, valor):
    global global_variables
    global teve_atualizacao
    global comando_escravo
    grupo = None
    nome_variavel = nome_variavel.replace('/', '')

    # print('nome_variavel:', nome_variavel)

    if "PC" in nome_variavel:
        # Verifique em qual grupo colocar a variável com base no nome_variavel
        if nome_variavel in global_variables['group1']:
            grupo = global_variables['group1']
        elif nome_variavel in global_variables['group2']:
            grupo = global_variables['group2']
        elif nome_variavel in global_variables['group3']:
            grupo = global_variables['group3']

        if grupo is not None:
            grupo[nome_variavel] = valor
            teve_atualizacao = True
            # print(global_variables)
        # else:
        #     print(f"A variável '{nome_variavel}' não corresponde a nenhum grupo existente.")
    else:
        # print("é um comando para uma escravo")
        comando_escravo = valor
        # print("comando: ", comando_escravo)


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
    """ da a resposta do estado do computador """
    global firebase, db
    try:
        # Escreva a informação aleatória no banco de dados Firebase
        db.child(caminho_resposta1).set(resposta_escravo)
        # print(f"Informação {resposta_escravo} escrita com sucesso em {caminho_resposta1}")
    except Exception as e:
        print(f"Ocorreu um erro ao escrever a informação: {str(e)}")


def escreve_configuracao(dados_config):
    """ da a resposta do estado do computador """
    global firebase, db
    try:
        # Escreva a informação aleatória no banco de dados Firebase
        db.child('Ajustes').set(dados_config)
        # print(f"Informação {resposta_escravo} escrita com sucesso em {caminho_resposta1}")
    except Exception as e:
        print(f"Ocorreu um erro ao escrever a informação: {str(e)}")


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
        if resposta_escravo == "Sair":
            confirmacao_escravo('Saindo')

        escreve_resposta_escravo(resposta_escravo)
        resposta_anterior = resposta_escravo
    else:
        return


def comando_coleetivo_escravo_escravo(comando):
    """'quando um escravo precisa comandar os outro escravos de forma automatica"""
    if nome_usuario == "PokerIP":
        # print(nome_usuario)
        enviar_comando_coletivo(arranjo1_pc, comando)
    elif nome_usuario == "lgagu":
        # print(nome_usuario)
        enviar_comando_coletivo(arranjo2_pc, comando)
    elif nome_usuario == "Poker":
        # print(nome_usuario)
        enviar_comando_coletivo(arranjo3_pc, comando)
    else:
        print("nome de usuario não configurado")


def escreve_configuracao(dados_config):
    """ Escreve os dados de configuração no banco de dados Firebase """
    global firebase, db
    try:
        # Escreve os dados de configuração no nó 'Ajustes' do banco de dados Firebase
        db.child('Ajustes').set(dados_config)
        print(dados_config)
        print("\nDados de configuração escritos com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao escrever os dados de configuração: {str(e)}")


def ler_configuracao():
    """ Lê os dados de configuração do banco de dados Firebase """
    global firebase, db

    try:
        # Lê os dados de configuração do nó 'Ajustes' do banco de dados Firebase
        dados_config = db.child('Ajustes').child(numero_pc).get().val()
        if dados_config:
            # print("Dados de configuração lidos com sucesso:")
            print(dados_config)

            # Separa os dados em variáveis individuais
            confg_funcao = dados_config.get('confg_funcao', "roleta_auto")
            config_tempo_roleta = dados_config.get('config_tempo_roleta', '0:00:5')
            blind_recolher_auto = dados_config.get('blind_recolher_auto', '0000')
            confg_secundaria = dados_config.get('confg_secundaria', 'auto')

            return confg_funcao, config_tempo_roleta, blind_recolher_auto, confg_secundaria
        else:
            print("Nenhum dado de configuração encontrado.")
            return None, None, None, None
    except Exception as e:
        print(f"Ocorreu um erro ao ler os dados de configuração: {str(e)}")
        return None, None, None, None


def atualizar_configuracao_pc(novos_dados):
    """ Atualiza os dados de configuração para um PC específico """
    # while True:
    global firebase, db
    try:
        if not firebase or not db:
            raise ValueError("Firebase ou banco de dados não inicializado corretamente.")

        # Atualiza os dados de configuração específicos para o PC fornecido
        db.child('Ajustes').child(numero_pc).update(novos_dados)
        print(f"Dados de configuração para {numero_pc} atualizados com sucesso.")
        return
    except Exception as e:
        print(f"Ocorreu um erro ao atualizar os dados de configuração para {numero_pc}: {str(e)}")
        # time.sleep(5)


def atualizar_estatos_mesa(statos):
    """
    Atualiza os dados de configuração para um PC específico
    modelo de parametro a ser passado pc_statos = {'5001K': 'sentado'}
    """

    global firebase, db, status_anterior
    if status_anterior == statos:
        return
    try:
        if not firebase or not db:
            raise ValueError("Firebase ou banco de dados não inicializado corretamente.")

        pc_statos = {numero_pc: statos}
        # # Atualiza os dados de configuração específicos para o PC fornecido
        db.child('Mesa').update(pc_statos)

        print(f"Dados de configuração para {numero_pc} atualizados com sucesso.")
        status_anterior = statos
    except Exception as e:
        print(f"Ocorreu um erro ao atualizar os dados de configuração para {numero_pc}: {str(e)}")


def ler_statos_mesa():
    """ Lê os dados de configuração do banco de dados Firebase """
    global firebase, db, dados_mesa

    try:
        # Lê os dados de configuração do nó 'Ajustes' do banco de dados Firebase
        dados_mesa = db.child('Mesa').get().val()
        if dados_config:
            # print("Dados de configuração lidos com sucesso:")
            # print(dados_mesa)

            return dados_mesa
        else:
            print("Nenhum dado de configuração encontrado.")
            return None
    except Exception as e:
        print(f"Ocorreu um erro ao ler os dados de configuração: {str(e)}")
        return None


def contar_ocupacao_mesas(sala=''):
    """
    Conta cada uma das salas e retorna um dicionário com a quantidade de pessoas em cada sala.

    Args:
        sala: A sala que você deseja contar.

    Returns:
        O número de pessoas na sala especificada e o dicionario com a quantidade de pessoas por sala
    """
    dicionario = ler_statos_mesa()

    # Verifica se dados_mesa é um dicionário
    if isinstance(dicionario, dict):
        contagem_numeros = {}
        for pc, dados in dicionario.items():
            if isinstance(dados, str):
                if dados in contagem_numeros:
                    contagem_numeros[dados] += 1
                else:
                    contagem_numeros[dados] = 1

        # Verifica se a sala existe
        if sala in contagem_numeros:
            return contagem_numeros[sala], contagem_numeros
        else:
            return 0, contagem_numeros
    else:
        return None, None


def contar_pessoas_mesa(sala):
    print('conta quantas pessosa tem na mesa: ', sala)
    """
    Conta quantas vezes uma sala se repete nos dados.

    Args:
      sala: A sala que você deseja contar.

    Returns:
      O número de vezes que a sala se repete.
    """
    try:
        dicionario = ler_statos_mesa()
        contagem_repeticoes = 0
        for pc, dados in dicionario.items():
            if isinstance(dados, str):
                if dados == sala:
                    contagem_repeticoes += 1

        print('sala ', sala, ' com ', contagem_repeticoes)
    except Exception as e:
        contagem_repeticoes = 0
        print(e)
    return int(contagem_repeticoes)


# escreve_configuracao(dados_config)

