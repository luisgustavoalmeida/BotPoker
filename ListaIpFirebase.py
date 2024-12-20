# Importa a biblioteca necessária
import datetime  # Adicionado para manipulação de datas
import json
import os
import time

import pyrebase

# Configuração dos bancos de dados

# gayaluisaalmeida@gmail.com
config1 = {"apiKey": "AIzaSyAejgpCgHmBFyESI1cvOJ0nzUX3gQ3k4h8", "authDomain": "config1-f0277.firebaseapp.com",
           "databaseURL": "https://config1-f0277-default-rtdb.firebaseio.com", "projectId": "config1-f0277",
           "storageBucket": "config1-f0277.appspot.com", "messagingSenderId": "547584039775", "appId": "1:547584039775:web:1c675dda6cf5da01caf4ea"}

config2 = {"apiKey": "AIzaSyALRmZR-_VcHS0GPsm41Pk_zQn47a8uq44", "authDomain": "config2-7f437.firebaseapp.com",
           "databaseURL": "https://config2-7f437-default-rtdb.firebaseio.com", "projectId": "config2-7f437",
           "storageBucket": "config2-7f437.appspot.com", "messagingSenderId": "589089564888", "appId": "1:589089564888:web:e6816ec8a1b4ddb0764fad"}

config3 = {"apiKey": "AIzaSyBIJ-Z7Z6Mim2CEJB3vNDBMld8ZKqkt7HY", "authDomain": "config3-db30a.firebaseapp.com",
           "databaseURL": "https://config3-db30a-default-rtdb.firebaseio.com", "projectId": "config3-db30a",
           "storageBucket": "config3-db30a.appspot.com", "messagingSenderId": "428851296907", "appId": "1:428851296907:web:259d26ef77d050cf51f28e"}

config4 = {"apiKey": "AIzaSyBDjQDvYKWh8bEgKTTHCJnMc9O8lUDaSFU", "authDomain": "config4-eeca6.firebaseapp.com",
           "databaseURL": "https://config4-eeca6-default-rtdb.firebaseio.com", "projectId": "config4-eeca6",
           "storageBucket": "config4-eeca6.appspot.com", "messagingSenderId": "178010237452", "appId": "1:178010237452:web:9b30673b9dd802c4471c29"}

config5 = {"apiKey": "AIzaSyB8EN2_FrdORLdr7hRFqdJ5eNM_vW2T_jA", "authDomain": "config4-62427.firebaseapp.com",
           "databaseURL": "https://config4-62427-default-rtdb.firebaseio.com", "projectId": "config4-62427",
           "storageBucket": "config4-62427.appspot.com", "messagingSenderId": "706824343416", "appId": "1:706824343416:web:47ad80d993b89037bac28d"}

config6 = {"apiKey": "AIzaSyCVizFSlEEwAUpUrGZRjTVu7LKPgvlR-vs", "authDomain": "config6-5760a.firebaseapp.com",
           "databaseURL": "https://config6-5760a-default-rtdb.firebaseio.com", "projectId": "config6-5760a",
           "storageBucket": "config6-5760a.appspot.com", "messagingSenderId": "652300196188", "appId": "1:652300196188:web:089fabbd85d34136860999"}

config7 = {"apiKey": "AIzaSyA7ol3mz6E36vEvEnUbCzeASTLhZYgyrVQ", "authDomain": "config7-f487a.firebaseapp.com",
           "databaseURL": "https://config7-f487a-default-rtdb.firebaseio.com", "projectId": "config7-f487a",
           "storageBucket": "config7-f487a.appspot.com", "messagingSenderId": "702319895919", "appId": "1:702319895919:web:df25fdca2ecfe75fb3b49a"}

config8 = {"apiKey": "AIzaSyDQ0xDgtSBV5oVH4GN2qEO_Q3KH1P9j5y4", "authDomain": "config8-e0575.firebaseapp.com",
           "databaseURL": "https://config8-e0575-default-rtdb.firebaseio.com", "projectId": "config8-e0575",
           "storageBucket": "config8-e0575.appspot.com", "messagingSenderId": "232802811692", "appId": "1:232802811692:web:fd7179331ea1429563f689"}

config9 = {"apiKey": "AIzaSyCq6gTJoLYsa3TOnZthLTQRYZv38baICX0", "authDomain": "config9-e2073.firebaseapp.com",
           "databaseURL": "https://config9-e2073-default-rtdb.firebaseio.com", "projectId": "config9-e2073",
           "storageBucket": "config9-e2073.appspot.com", "messagingSenderId": "696118180138", "appId": "1:696118180138:web:bf826bad3b87d1aff28653"}

config10 = {"apiKey": "AIzaSyCyoPVlThZLAVWFuYgqCrUGIeCoFz6MRC0", "authDomain": "config10-332a7.firebaseapp.com",
            "databaseURL": "https://config10-332a7-default-rtdb.firebaseio.com", "projectId": "config10-332a7",
            "storageBucket": "config10-332a7.appspot.com", "messagingSenderId": "771719475801", "appId": "1:771719475801:web:962e452654babdb7ba3748"}

config11 = {"apiKey": "AIzaSyAZRtBB1qXwQ9GfPilEMUuIBKBJbgUbUAk", "authDomain": "config11-39c6f.firebaseapp.com",
            "databaseURL": "https://config11-39c6f-default-rtdb.firebaseio.com", "projectId": "config11-39c6f",
            "storageBucket": "config11-39c6f.appspot.com", "messagingSenderId": "254326604770", "appId": "1:254326604770:web:770f278e9842c230a82fbb"}

# Variável para armazenar a última data de acesso
ultima_data_acesso = None

tempo_sem_uso_ip = 20


def escolher_configuracao_e_db():
    """
    Escolhe a configuração do banco com base na data atual.

    Retorna:
    tuple: Configuração do banco de dados e referência ao banco.
    """
    global db, configuracao_banco

    dia_atual = datetime.datetime.now().day

    if dia_atual < 4:
        configuracao_banco = config1
        print('Sera usado o banco 1')

    elif 4 <= dia_atual < 7:
        configuracao_banco = config2
        print('Sera usado o banco 2')

    elif 7 <= dia_atual < 10:
        configuracao_banco = config3
        print('Sera usado o banco 3')

    elif 10 <= dia_atual < 13:
        configuracao_banco = config4
        print('Sera usado o banco 4')

    elif 13 <= dia_atual < 16:
        configuracao_banco = config6
        print('Sera usado o banco 6')

    elif 16 <= dia_atual < 19:
        configuracao_banco = config5
        print('Sera usado o banco 5')

    elif 19 <= dia_atual < 22:
        configuracao_banco = config7
        print('Sera usado o banco 7')

    elif 22 <= dia_atual < 25:
        configuracao_banco = config8
        print('Sera usado o banco 8')

    elif 25 <= dia_atual < 28:
        configuracao_banco = config9
        print('Sera usado o banco 9')

    elif 28 <= dia_atual < 31:
        configuracao_banco = config10
        print('Sera usado o banco 10')

    else:
        configuracao_banco = config11
        print('Sera usado o banco 11')

    # Inicializa o Firebase com a configuração escolhida
    firebase = pyrebase.initialize_app(configuracao_banco)
    db = firebase.database()

    return configuracao_banco, db


# Escolhe a configuração do banco com base na data atual
# configuracao_banco, db = escolher_configuracao_e_db()


def unir_e_atualizar_dados():
    # Inicializa os bancos de dados
    firebase_1 = pyrebase.initialize_app(config1)
    firebase_2 = pyrebase.initialize_app(config2)
    firebase_3 = pyrebase.initialize_app(config3)
    firebase_4 = pyrebase.initialize_app(config4)
    firebase_5 = pyrebase.initialize_app(config5)
    firebase_6 = pyrebase.initialize_app(config6)
    firebase_7 = pyrebase.initialize_app(config7)
    firebase_8 = pyrebase.initialize_app(config8)
    firebase_9 = pyrebase.initialize_app(config9)
    firebase_10 = pyrebase.initialize_app(config10)
    firebase_11 = pyrebase.initialize_app(config11)

    # Obtém referências para os bancos de dados
    db_1 = firebase_1.database()
    db_2 = firebase_2.database()
    db_3 = firebase_3.database()
    db_4 = firebase_4.database()
    db_5 = firebase_5.database()
    db_6 = firebase_6.database()
    db_7 = firebase_7.database()
    db_8 = firebase_8.database()
    db_9 = firebase_9.database()
    db_10 = firebase_10.database()
    db_11 = firebase_11.database()

    try:
        # Obtém os dados da referência 'ips' em ambos os bancos
        dados_1 = db_1.child('ips').get().val()
        dados_2 = db_2.child('ips').get().val()
        dados_3 = db_3.child('ips').get().val()
        dados_4 = db_4.child('ips').get().val()
        dados_5 = db_5.child('ips').get().val()
        dados_6 = db_6.child('ips').get().val()
        dados_7 = db_7.child('ips').get().val()
        dados_8 = db_8.child('ips').get().val()
        dados_9 = db_9.child('ips').get().val()
        dados_10 = db_10.child('ips').get().val()
        dados_11 = db_11.child('ips').get().val()

        # dados_1_banidos = db_1.child('ips_banidos').get().val()
        # dados_2_banidos = db_2.child('ips_banidos').get().val()
        # dados_3_banidos = db_3.child('ips_banidos').get().val()
        # dados_4_banidos = db_4.child('ips_banidos').get().val()
        # dados_5_banidos = db_5.child('ips_banidos').get().val()
        # dados_6_banidos = db_6.child('ips_banidos').get().val()
        # dados_7_banidos = db_7.child('ips_banidos').get().val()
        # dados_8_banidos = db_8.child('ips_banidos').get().val()
        # dados_9_banidos = db_9.child('ips_banidos').get().val()
        # dados_10_banidos = db_10.child('ips_banidos').get().val()
        # dados_11_banidos = db_11.child('ips_banidos').get().val()

        # Se as listas de IPs estão vazias ou não existem, inicializa listas vazias
        if dados_1 is None:
            dados_1 = []
        if dados_2 is None:
            dados_2 = []
        if dados_3 is None:
            dados_3 = []
        if dados_4 is None:
            dados_4 = []
        if dados_5 is None:
            dados_5 = []
        if dados_6 is None:
            dados_6 = []
        if dados_7 is None:
            dados_7 = []
        if dados_8 is None:
            dados_8 = []
        if dados_9 is None:
            dados_9 = []
        if dados_10 is None:
            dados_10 = []
        if dados_11 is None:
            dados_11 = []

        # if dados_1_banidos is None:
        #     dados_1_banidos = []
        # if dados_2_banidos is None:
        #     dados_2_banidos = []
        # if dados_3_banidos is None:
        #     dados_3_banidos = []
        # if dados_4_banidos is None:
        #     dados_4_banidos = []
        # if dados_5_banidos is None:
        #     dados_5_banidos = []
        # if dados_6_banidos is None:
        #     dados_6_banidos = []
        # if dados_7_banidos is None:
        #     dados_7_banidos = []
        # if dados_8_banidos is None:
        #     dados_8_banidos = []
        # if dados_9_banidos is None:
        #     dados_9_banidos = []
        # if dados_10_banidos is None:
        #     dados_10_banidos = []
        # if dados_11_banidos is None:
        #     dados_11_banidos = []

        # Combina os dados de ambos os bancos
        dados_combinados = dados_1 + dados_2 + dados_3 + dados_4 + dados_5 + dados_6 + dados_7 + dados_8 + dados_9 + dados_10 + dados_11

        # dados_combinados_banidos = (
        #         dados_1_banidos + dados_2_banidos + dados_3_banidos + dados_4_banidos + dados_5_banidos + dados_6_banidos + dados_7_banidos +
        #         dados_8_banidos + dados_9_banidos + dados_10_banidos + dados_11_banidos)

        # Remove IPs duplicados
        dados_combinados = [dict(t) for t in {tuple(d.items()) for d in dados_combinados}]

        # dados_combinados_banidos = [dict(t) for t in {tuple(d.items()) for d in dados_combinados_banidos}]
        #
        # # Ordena a lista com base no timestamp em ordem crescente
        # dados_combinados_banidos = sorted(dados_combinados_banidos, key=lambda x: x['timestamp'])

        # Remove IPs que estão na lista por mais de 24 horas
        dados_combinados = [ip_info for ip_info in dados_combinados if time.time() - ip_info['timestamp'] <= tempo_sem_uso_ip * 3600]

        # Ordena a lista com base no timestamp
        dados_combinados.sort(key=lambda x: x['timestamp'])

        # Atualiza a referência 'ips' nos dois bancos
        db_1.child('ips').set(dados_combinados)
        db_2.child('ips').set(dados_combinados)
        db_3.child('ips').set(dados_combinados)
        db_4.child('ips').set(dados_combinados)
        db_5.child('ips').set(dados_combinados)
        db_6.child('ips').set(dados_combinados)
        db_7.child('ips').set(dados_combinados)
        db_8.child('ips').set(dados_combinados)
        db_9.child('ips').set(dados_combinados)
        db_10.child('ips').set(dados_combinados)
        db_11.child('ips').set(dados_combinados)

        # db_1.child('ips_banidos').set(dados_combinados_banidos)
        # db_2.child('ips_banidos').set(dados_combinados_banidos)
        # db_3.child('ips_banidos').set(dados_combinados_banidos)
        # db_4.child('ips_banidos').set(dados_combinados_banidos)
        # db_5.child('ips_banidos').set(dados_combinados_banidos)
        # db_6.child('ips_banidos').set(dados_combinados_banidos)
        # db_7.child('ips_banidos').set(dados_combinados_banidos)
        # db_8.child('ips_banidos').set(dados_combinados_banidos)
        # db_9.child('ips_banidos').set(dados_combinados_banidos)
        # db_10.child('ips_banidos').set(dados_combinados_banidos)
        # db_11.child('ips_banidos').set(dados_combinados_banidos)

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
            try:
                # Verifica se o arquivo de backup existe e carrega a lista local de IPs a partir dele
                if os.path.exists('ips_backup.json'):
                    with open('ips_backup.json', 'r') as file:
                        lista_ips_local = json.load(file)
                else:
                    lista_ips_local = []
            except Exception as e:
                print(f"Erro ao obter o arquivo json local, será criado uma lista em branco. ERRO: {e}")
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
            lista_ips.append({'ip': ip, 'timestamp': time.time()})

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
#     ip_banido_info = {'ip': ip, 'timestamp': time.time(), 'data_hora': data_hora_atual}
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
#             # Ordena a lista com base no timestamp em ordem crescente
#             dados_banidos = sorted(dados_banidos, key=lambda x: x['timestamp'])
#
#             # Atualiza a referência 'ips_banidos' no Firebase
#             db.child('ips_banidos').set(dados_banidos)
#
#             print(f"IP {ip} adicionado à lista de IPs banidos.")
#         except Exception as e:
#             print(f"Erro ao adicionar IP banido do Firebase: {e}")
#             time.sleep(1)


# def lista_ip_banidos():
#     global db
#     while True:
#         try:
#             # Obtém os dados da referência 'ips_banidos' no Firebase
#             dados_banidos = db.child('ips_banidos').get().val()
#
#             # Se a lista de IPs banidos está vazia ou não existe, retorna uma lista vazia
#             if dados_banidos is None:
#                 return []
#
#             # Cria uma lista com os IPs banidos
#             ips_banidos = [ip_info['ip'] for ip_info in dados_banidos]
#
#             # Mostra quantos itens existem na lista sem duplicatas
#             quantidade_ips_banidos = len(ips_banidos)
#             print(f"Quantidade de IPs banidos: {quantidade_ips_banidos}")
#             # print(ips_banidos)
#             #
#             # # Escreve a lista de IPs banidos em um arquivo .txt
#             # with open('ips_banidos.txt', 'w') as file:
#             #     for ip in ips_banidos:
#             #         file.write(ip + '\n')
#
#             return ips_banidos
#         except Exception as e:
#             print(f"Erro ao obter lista de IPs banidos do Firebase: {e}")
#             time.sleep(1)  # return []

# # Chama a função para verificar e adicionar IP (substitua pelo IP desejado)
# verifica_e_adiciona_ip('1.1.1.3')

# unir_e_atualizar_dados()
# escrever_IP_banido("187.69.77.175")
# lista_ip_banidos()
# escrever_IP_banido("0.0.1.1")
# verifica_e_adiciona_ip('2.1.1.3')
# unir_e_atualizar_dados()
