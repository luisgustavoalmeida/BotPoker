# pip install pyrebase5
import time
import json
import pyrebase

from Requerimentos import nome_computador, nome_usuario


config_cookies = {
    'apiKey': "AIzaSyBat9wHSgN8WpVa6FUaLhd0fRx66wdIhvw",
    'authDomain': "cookiesfacebook-c04db.firebaseapp.com",
    'databaseURL': "https://cookiesfacebook-c04db-default-rtdb.firebaseio.com",
    'projectId': "cookiesfacebook-c04db",
    'storageBucket': "cookiesfacebook-c04db.appspot.com",
    'messagingSenderId': "209513125145",
    'appId': "1:209513125145:web:fa732060beb24a322e6188"
}

firebase_cookies = pyrebase.initialize_app(config_cookies)
db_cookies = firebase_cookies.database()

def sincronizar_cookies_com_firebase():
    if nome_computador == 'PC-I7-9700KF' or nome_usuario == 'PokerIP':
        print('PC liberado para sincronisar Cookies com Firebase')
    else:
        print('PC NÃO liberado')
        return

    print('\n\nIniciando a sincronização dos cookies com Firebase')
    global firebase_cookies, db_cookies
    # Referência ao local de cookies no Realtime Database
    ref = db_cookies.child('cookies_facebook')

    # Carregar os dados do Firebase
    cookies_firebase_data = ref.get().val()  # Converte para um dicionário utilizável
    if cookies_firebase_data is None:
        cookies_firebase_data = {}  # Se não houver dados no Firebase, inicia com um dicionário vazio

    print(f"Quantidade de contas no Firebase antes da sincronização: {len(cookies_firebase_data)}")

    for _ in range(10):
        try:
            with open('cookies_facebook.json', 'r') as file:
                cookies_local_data = json.load(file)
            print("Arquivo JSON de cookies carregado com sucesso.")
            break  # Saímos do loop se a leitura for bem-sucedida
        except FileNotFoundError:
            print("Arquivo JSON de cookies não encontrado. Iniciando com dicionário vazio.")
            cookies_local_data = {}
            break  # Se o arquivo não existe, não há necessidade de tentar novamente
        except json.JSONDecodeError as e:
            print(f"Erro ao tentar carregar os cookies do arquivo JSON: {e}.")
            cookies_local_data = {}
        except Exception as e:
            print(f"Erro ao tentar carregar os cookies do arquivo JSON: {e}.")
            cookies_local_data = {}
        time.sleep(5)

    print(f"Quantidade de contas no arquivo local antes da sincronização: {len(cookies_local_data)}")

    # Função para verificar e substituir cookies por uma lista mais recente
    def substituir_se_mais_novo(cookies_existentes, novos_cookies):
        # Pega o cookie de referência (primeiro cookie da lista, pode mudar para outro critério)
        cookie_existente_expiry = cookies_existentes[0].get('expiry', 0) if cookies_existentes else 0
        novo_cookie_expiry = novos_cookies[0].get('expiry', 0) if novos_cookies else 0

        # Se a nova lista tem cookies com expiração mais recente, substituir
        if novo_cookie_expiry > cookie_existente_expiry:
            # print(f"Substituindo cookies por uma versão mais nova (expiração: {novo_cookie_expiry})")
            # print(novos_cookies)
            return novos_cookies  # Substitui toda a lista
        else:
            # print(f"Cookies mantidos, pois são mais recentes ou iguais (expiração: {cookie_existente_expiry})")
            return cookies_existentes  # Mantém a lista existente

    # Mesclar os dados do Firebase com o JSON local
    for account_id, cookies in cookies_firebase_data.items():
        if account_id in cookies_local_data:
            # Verificar se os cookies locais são mais recentes
            cookies_local_data[account_id] = substituir_se_mais_novo(cookies_local_data[account_id], cookies)
        else:
            # Se a conta não existe no arquivo local, adicionar do Firebase
            cookies_local_data[account_id] = cookies

    # Mesclar os dados do JSON local com o Firebase
    for account_id, cookies in cookies_local_data.items():
        if account_id in cookies_firebase_data:
            # Verificar se os cookies Firebase são mais recentes
            cookies_firebase_data[account_id] = substituir_se_mais_novo(cookies_firebase_data[account_id], cookies)
        else:
            # Se a conta não existe no Firebase, adicionar do arquivo local
            cookies_firebase_data[account_id] = cookies

    # Atualizar os dados no Firebase
    db_cookies.child('cookies_facebook').set(cookies_firebase_data)

    # Atualizar o arquivo JSON local com tratamento de exceções
    for _ in range(6):
        try:
            with open('cookies_facebook.json', 'w') as file:
                json.dump(cookies_local_data, file, indent=4)
            print("Arquivo JSON de cookies atualizado com sucesso.")
            break
        except Exception as e:
            print(f"Ocorreu um erro inesperado ao tentar salvar os cookies no arquivo JSON: {e}. \nNova tentativa em 10 segundos")
            time.sleep(10)

    # Print da quantidade de IDs sincronizados
    print(f"Quantidade de contas sincronizadas: {len(cookies_firebase_data)}")

    print("Sincronização de cookies com o Firebase e o arquivo local concluída!\n\n")


def apagar_cookies_firebase():
    if nome_computador == 'PC-I7-9700KF' or nome_usuario == 'PokerIP':
        print('PC liberado para apagar Cookies do Firebase')
    else:
        print('PC NÃO liberado')
        return

    print("\n\nIniciando a exclusão dos cookies no Firebase...")

    global firebase_cookies, db_cookies
    # Referência ao local de cookies no Realtime Database
    ref = db_cookies.child('cookies_facebook')

    try:
        # Remover todos os cookies
        ref.remove()
        print("Todos os cookies foram apagados com sucesso do Firebase.")
    except Exception as e:
        print(f"Erro ao tentar apagar os cookies do Firebase: {e}")

# sincronizar_cookies_com_firebase()