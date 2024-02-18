# Importa a biblioteca necessária
import datetime  # Adicionado para manipulação de datas
import time
import json
import os
import pyrebase

# Configuração dos bancos de dados

# gayaluisaalmeida@gmail.com
config1 = {
    "apiKey": "AIzaSyDDzQMVxpKKqBZrDlhA9E4sInXB5toVRT8",
    "authDomain": "pokerdados-6884e.firebaseapp.com",
    "databaseURL": "https://pokerdados-6884e-default-rtdb.firebaseio.com",
    "projectId": "pokerdados-6884e",
    "storageBucket": "pokerdados-6884e.appspot.com",
    "messagingSenderId": "240019464920",
    "appId": "1:240019464920:web:a746cddaf41f43642aadad"
}
# luis.almeida@estudante.ufjf.br
config2 = {
    "apiKey": "AIzaSyBWJEh-hD6UIkpMz8J4V2Es4mP2AtuHx9k",
    "authDomain": "poker-dados.firebaseapp.com",
    "databaseURL": "https://poker-dados-default-rtdb.firebaseio.com",
    "projectId": "poker-dados",
    "storageBucket": "poker-dados.appspot.com",
    "messagingSenderId": "968238353891",
    "appId": "1:968238353891:web:b0026783a590efa99c24d6"
}

# lga.gustavo.a@gmail.com
config3 = {
    "apiKey": "AIzaSyBMhul_wFoi-7LFtS6PP22vCi8Op3RYIlE",
    "authDomain": "poker-dados-2.firebaseapp.com",
    "databaseURL": "https://poker-dados-2-default-rtdb.firebaseio.com",
    "projectId": "poker-dados-2",
    "storageBucket": "poker-dados-2.appspot.com",
    "messagingSenderId": "712512083103",
    "appId": "1:712512083103:web:6afab600554fdf1287beaa"
}

# luis.gustavo@engenharia.ufjf.br
config4 = firebaseConfig = {
    "apiKey": "AIzaSyD0OgT6l5HcMVM4HKPFRD7BGbKbCRgDeaM",
    "authDomain": "poker-dados-3-3e7cc.firebaseapp.com",
    "databaseURL": "https://poker-dados-3-3e7cc-default-rtdb.firebaseio.com",
    "projectId": "poker-dados-3-3e7cc",
    "storageBucket": "poker-dados-3-3e7cc.appspot.com",
    "messagingSenderId": "370013391029",
    "appId": "1:370013391029:web:acaa0cfbe3e53d269116fc"
}

# Variável para armazenar a última data de acesso
ultima_data_acesso = None

tempo_sem_uso_ip = 30


def escolher_configuracao_e_db():
    """
    Escolhe a configuração do banco com base na data atual.

    Retorna:
    tuple: Configuração do banco de dados e referência ao banco.
    """
    global db
    global configuracao_banco
    dia_atual = datetime.datetime.now().day

    if dia_atual < 8:
        configuracao = config1
        print('Sera usado o banco 1')

    elif 8 <= dia_atual < 16:
        configuracao = config2
        print('Sera usado o banco 2')

    elif 16 <= dia_atual < 24:
        configuracao = config3
        print('Sera usado o banco 3')

    else:
        configuracao = config4
        print('Sera usado o banco 4')

    # Inicializa o Firebase com a configuração escolhida
    firebase = pyrebase.initialize_app(configuracao)
    db = firebase.database()

    return configuracao, db


# Escolhe a configuração do banco com base na data atual
configuracao_banco, db = escolher_configuracao_e_db()


def unir_e_atualizar_dados():
    # Inicializa os bancos de dados
    firebase_4 = pyrebase.initialize_app(config4)
    firebase_3 = pyrebase.initialize_app(config3)
    firebase_2 = pyrebase.initialize_app(config2)
    firebase_1 = pyrebase.initialize_app(config1)

    # Obtém referências para os bancos de dados
    db_1 = firebase_1.database()
    db_2 = firebase_2.database()
    db_3 = firebase_3.database()
    db_4 = firebase_4.database()

    try:
        # Obtém os dados da referência 'ips' em ambos os bancos
        dados_1 = db_1.child('ips').get().val()
        dados_2 = db_2.child('ips').get().val()
        dados_3 = db_3.child('ips').get().val()
        dados_4 = db_4.child('ips').get().val()

        dados_1_banidos = db_1.child('ips_banidos').get().val()
        dados_2_banidos = db_2.child('ips_banidos').get().val()
        dados_3_banidos = db_3.child('ips_banidos').get().val()
        dados_4_banidos = db_4.child('ips_banidos').get().val()

        # Se as listas de IPs estão vazias ou não existem, inicializa listas vazias
        if dados_1 is None:
            dados_1 = []
        if dados_2 is None:
            dados_2 = []
        if dados_3 is None:
            dados_3 = []
        if dados_4 is None:
            dados_4 = []

        if dados_1_banidos is None:
            dados_1_banidos = []
        if dados_2_banidos is None:
            dados_2_banidos = []
        if dados_3_banidos is None:
            dados_3_banidos = []
        if dados_4_banidos is None:
            dados_4_banidos = []

        # Combina os dados de ambos os bancos
        dados_combinados = dados_1 + dados_2 + dados_3 + dados_4

        dados_combinados_banidos = dados_1_banidos + dados_2_banidos + dados_3_banidos + dados_4_banidos

        # Remove IPs duplicados
        dados_combinados = [dict(t) for t in {tuple(d.items()) for d in dados_combinados}]

        dados_combinados_banidos = [dict(t) for t in {tuple(d.items()) for d in dados_combinados_banidos}]

        # Ordena a lista com base no timestamp em ordem crescente
        dados_combinados_banidos = sorted(dados_combinados_banidos, key=lambda x: x['timestamp'])

        # Remove IPs que estão na lista por mais de 24 horas
        dados_combinados = [ip_info for ip_info in dados_combinados if time.time() - ip_info['timestamp'] <= tempo_sem_uso_ip * 3600]

        # Ordena a lista com base no timestamp
        dados_combinados.sort(key=lambda x: x['timestamp'])

        # Atualiza a referência 'ips' nos dois bancos
        db_1.child('ips').set(dados_combinados)
        db_2.child('ips').set(dados_combinados)
        db_3.child('ips').set(dados_combinados)
        db_4.child('ips').set(dados_combinados)

        db_1.child('ips_banidos').set(dados_combinados_banidos)
        db_2.child('ips_banidos').set(dados_combinados_banidos)
        db_3.child('ips_banidos').set(dados_combinados_banidos)
        db_4.child('ips_banidos').set(dados_combinados_banidos)

        print("Dados unidos, duplicatas removidas e IPs antigos removidos. Atualização concluída!")

    except Exception as e:
        print(f"Erro ao unir e atualizar dados: {e}")


def verifica_e_adiciona_ip(ip):
    global ultima_data_acesso
    global db
    global configuracao_banco

    while True:
        print('Testa se IP já foi usado')
        try:
            # Obtém a lista atual de IPs do Firebase
            lista_ips = db.child('ips').get().val()

            # Se a lista de IPs está vazia ou não existe, inicializa uma lista vazia
            if lista_ips is None:
                lista_ips = []

            # Verifica se o arquivo de backup existe e carrega a lista local de IPs a partir dele
            if os.path.exists('ips_backup.json'):
                with open('ips_backup.json', 'r') as file:
                    lista_ips_local = json.load(file)
            else:
                lista_ips_local = []

            # Verifica se a última data de acesso é nula ou se o dia mudou desde o último acesso
            if ultima_data_acesso is None or ultima_data_acesso.day != datetime.datetime.now().day:
                # Escolhe a configuração do banco com base na data atual
                nova_configuracao, novo_db = escolher_configuracao_e_db()

                # Atualiza a referência e o banco se a configuração mudou
                if nova_configuracao != configuracao_banco:
                    print("Configuração do banco alterada. Unindo e atualizando dados.")
                    unir_e_atualizar_dados()
                    configuracao_banco, db = nova_configuracao, novo_db

                # Atualiza a última data de acesso
                ultima_data_acesso = datetime.datetime.now()

            # Unir as duas listas
            lista_ips += lista_ips_local

            # Remove IPs que estão na lista por mais de 24 horas
            lista_ips = [ip_info for ip_info in lista_ips if time.time() - ip_info['timestamp'] <= tempo_sem_uso_ip * 3600]

            # Remove itens duplicados da lista_ips
            lista_ips = [dict(t) for t in {tuple(d.items()) for d in lista_ips}]

            # Ordena a lista com base no timestamp
            lista_ips.sort(key=lambda x: x['timestamp'])

            # Verifica se o IP já está na lista
            for ip_info in lista_ips:
                if ip_info['ip'] == ip:
                    quantidade_itens = len(lista_ips)
                    print(f"IP {ip} já está na lista. Quantidade de ips usados: {quantidade_itens}")
                    # Atualiza a lista local com os novos valores
                    with open('ips_backup.json', 'w') as file:
                        json.dump(lista_ips, file)
                    return False  # O IP já está na lista, retorna False

            # Adiciona o IP à lista com o timestamp atual
            lista_ips.append({
                'ip': ip,
                'timestamp': time.time()
            })

            # Atualiza a lista de IPs no Firebase
            db.child('ips').set(lista_ips)

            # Atualiza a lista local com os novos valores
            with open('ips_backup.json', 'w') as file:
                json.dump(lista_ips, file)

            # Calcula o tamanho da lista
            quantidade_itens = len(lista_ips)

            print(f"IP {ip} adicionado à lista de IPs. Quantidade de ips usados: {quantidade_itens}")
            return True  # O IP não estava na lista, retorna True e foi adicionado
        except Exception as e:
            print(f"Erro verifica_e_adiciona_ip: {e}")
            time.sleep(1)


# def escrever_IP_banido(ip):
#     global db
#
#     print('escrever_IP_banido')
#
#     print(ip)
#
#     data_hora_atual = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#
#     print(data_hora_atual)
#
#     # Crie uma estrutura de dados para o IP banido
#     ip_banido_info = {
#         'ip': ip,
#         'timestamp': time.time(),
#         'data_hora': data_hora_atual
#     }
#     while True:
#         try:
#             # Obtém os dados da referência 'ips_banidos' no Firebase
#             dados_banidos = db.child('ips_banidos').get().val()
#
#             # Se a lista de IPs banidos está vazia ou não existe, inicializa uma lista vazia
#             if dados_banidos is None:
#                 dados_banidos = []
#
#             # Verifica se o IP já está na lista
#             for ip_info in dados_banidos:
#                 if ip_info['ip'] == ip:
#                     print(f"IP {ip} já está na lista de IPs banidos.")
#                     return
#
#             # Adiciona o IP banido à lista
#             dados_banidos.append(ip_banido_info)
#
#             # Remove IPs duplicados
#             dados_banidos = [dict(t) for t in {tuple(d.items()) for d in dados_banidos}]
#
#             # Atualiza a referência 'ips_banidos' no Firebase
#             db.child('ips_banidos').set(dados_banidos)
#
#             print(f"IP {ip} adicionado à lista de IPs banidos.")
#         except Exception as e:
#             print(f"Erro ao adicionar IP banido do Firebase: {e}")
#             time.sleep(1)

def escrever_IP_banido(ip):
    global db

    print('escrever_IP_banido')

    print(ip)

    data_hora_atual = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(data_hora_atual)

    # Crie uma estrutura de dados para o IP banido
    ip_banido_info = {
        'ip': ip,
        'timestamp': time.time(),
        'data_hora': data_hora_atual
    }
    while True:
        try:
            # Obtém os dados da referência 'ips_banidos' no Firebase
            dados_banidos = db.child('ips_banidos').get().val()

            # Se a lista de IPs banidos está vazia ou não existe, inicializa uma lista vazia
            if dados_banidos is None:
                dados_banidos = []

            # Verifica se o IP já está na lista
            for ip_info in dados_banidos:
                if ip_info['ip'] == ip:
                    print(f"IP {ip} já está na lista de IPs banidos.")
                    return

            # Adiciona o IP banido à lista
            dados_banidos.append(ip_banido_info)

            # Ordena a lista com base no timestamp em ordem crescente
            dados_banidos = sorted(dados_banidos, key=lambda x: x['timestamp'])

            # Atualiza a referência 'ips_banidos' no Firebase
            db.child('ips_banidos').set(dados_banidos)

            print(f"IP {ip} adicionado à lista de IPs banidos.")
        except Exception as e:
            print(f"Erro ao adicionar IP banido do Firebase: {e}")
            time.sleep(1)


def lista_ip_banidos():
    global db
    while True:
        try:
            # Obtém os dados da referência 'ips_banidos' no Firebase
            dados_banidos = db.child('ips_banidos').get().val()

            # Se a lista de IPs banidos está vazia ou não existe, retorna uma lista vazia
            if dados_banidos is None:
                return []

            # Cria uma lista com os IPs banidos
            ips_banidos = [ip_info['ip'] for ip_info in dados_banidos]

            # Mostra quantos itens existem na lista sem duplicatas
            quantidade_ips_banidos = len(ips_banidos)
            print(f"Quantidade de IPs banidos: {quantidade_ips_banidos}")
            # print(ips_banidos)

            return ips_banidos
        except Exception as e:
            print(f"Erro ao obter lista de IPs banidos do Firebase: {e}")
            time.sleep(1)
            # return []

# # Chama a função para verificar e adicionar IP (substitua pelo IP desejado)
# verifica_e_adiciona_ip('1.1.1.3')

# unir_e_atualizar_dados()
#
# unir_e_atualizar_dados()

# lista_ip_banidos()
# escrever_IP_banido("0.0.1.1")
# verifica_e_adiciona_ip('2.1.1.3')
# unir_e_atualizar_dados()
