# deve se instlar a biblioteca
# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from OCR_tela import *
from Requerimentos import dicionari_token_credencial_n, nome_completo
from colorama import Fore
from IP import *
from Requerimentos import nome_usuario, nome_computador

if nome_computador == 'PC-I7-9700KF':
    indece_usuario = 1
else:
    match nome_usuario:
        case 'PokerIP':
            indece_usuario = 1
        case 'lgagu':
            indece_usuario = 2
        case 'Poker':
            indece_usuario = 3
        case _:
            indece_usuario = 1

# Define o escopo, desta forma tem permição total a plania e ao google drive
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']  # permite que a aplicação tenha acesso de leitura e escrita a planilhas do Google Sheets.

# ID da planilha
planilha_id = '1cEeMrBRVLnw7qtjiA63dK5q_HNvmJaCC5kNudzDjLgM'

valor_dicionario = dicionari_token_credencial_n[nome_completo]
token = valor_dicionario[0]  # pega o primeiro item da tupla
credentials = valor_dicionario[1]  # pega o segundo item da tupla
valor_pc = valor_dicionario[2]  # numero do computador
end_contagem_ip = valor_dicionario[5]  # pega o sexxto item da tupla
token_path = os.path.join('Tokens', token)
credencial_path = os.path.join('Tokens', credentials)

linha_vazia_anterior = 2  # Inicializa a variável global
intervalo_de_busca = 500
guia_antiga = None

cred = None
service = None


def credencial():
    # tem_internet()
    """Mostra o uso básico da Sheets API.
    Imprime valores de uma planilha de amostra.
    """
    while True:
        try:
            creds = None
            # Verifique se o arquivo de token existe
            if os.path.exists(token_path):
                creds = Credentials.from_authorized_user_file(token_path, SCOPES)

            # Se não houver credenciais válidas, solicite ao usuário que faça login
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(credencial_path, SCOPES)
                    creds = flow.run_local_server(port=0)
                # Salve as credenciais para a próxima execução
                with open(token_path, 'w') as token_nome:
                    token_nome.write(creds.to_json())

            return creds
        except Exception as e:
            print(Fore.RED + f"{e}" + Fore.RESET)
            time.sleep(3)
            tem_internet()


def gerar_tokens():
    """
    Função para iterar sobre um dicionário de tokens e exibir informações relevantes.

    Esta função utiliza variáveis globais 'token' e 'credentials', e chama a função 'credencial()'.

    Dicionário esperado: dicionari_token_credencial_n, onde cada valor é uma tupla
    contendo informações como token, credentials, conta e senha.

    Exemplo de chamada:
    gerar_tokens()
    """
    global token, credentials, token_path, credencial_path
    # Itera sobre o dicionário
    for chave, valor_dicionario in dicionari_token_credencial_n.items():
        # Extração de valores do dicionário
        token = valor_dicionario[0]
        credentials = valor_dicionario[1]
        conta = valor_dicionario[3]
        senha = valor_dicionario[4]
        token_path = os.path.join('Tokens', token)
        credencial_path = os.path.join('Tokens', credentials)
        # Exibe informações
        print(f"\n\n Para a chave: {chave} \n Token: {token} \n Credentials: {credentials} \n Conta: {conta} \n Senha: {senha} \n\n ")
        # Chama a função 'credencial()'
        credencial()


# cred = credencial()
# service = build('sheets', 'v4', credentials=cred)


def retona_para_inicio_planilha():
    global linha_vazia_anterior
    linha_vazia_anterior = 2
    print('Cursor da planiilha retonardo para a primeira linha')
    return


def primeira_celula_vazia(guia):
    """
    Encontra a primeira célula vazia em uma coluna específica da planilha.

    Parameters:
    - guia (str): O nome da guia na planilha.

    Returns:
    - str: O endereço da primeira célula vazia no formato 'D{n}', onde n é o número da linha.
    """
    global linha_vazia_anterior
    global intervalo_de_busca
    global guia_antiga
    print('primeira celula vazia')
    global cred
    global service

    # Verifica se a guia foi alterada
    if guia_antiga != guia:
        guia_antiga = guia
        linha_vazia_anterior = 2

    # Chama a API Sheets
    sheet = service.spreadsheets()

    while True:
        print('linha_vazia_anterior: ', linha_vazia_anterior)
        try:
            # Obtém os valores do intervalo
            result = sheet.values().get(
                spreadsheetId=planilha_id,
                range=f"{guia}!D{linha_vazia_anterior}:D{linha_vazia_anterior + intervalo_de_busca}",
                majorDimension="COLUMNS",
                valueRenderOption="UNFORMATTED_VALUE"
            ).execute()
            values = result.get('values', [[]])[0]

            # print(values)

            teste_indece, indices_vazio = encontrar_indices_vazios(values, indece_usuario)
            # print('indices_vazio', indices_vazio)

            if teste_indece:
                # print('linha encontrada: ', linha_vazia_anterior)
                linha_vazia_anterior += indices_vazio
                # print('linha nova: ', linha_vazia_anterior)
                endereco = f"D{linha_vazia_anterior}"
                linha_vazia_anterior += 1
                # print("endereco", endereco)
                return endereco

            tamanho_lista = len(values)
            # print('tamanho_lista', tamanho_lista)

            if tamanho_lista <= intervalo_de_busca:
                # print('2linha encontrada: ', linha_vazia_anterior)
                linha_vazia_anterior += (tamanho_lista + indece_usuario - 1)
                # print('2linha nova: ', linha_vazia_anterior)
                endereco = f"D{linha_vazia_anterior}"
                linha_vazia_anterior += 1
                # print(endereco)
                return endereco

            linha_vazia_anterior += intervalo_de_busca

        except Exception as e:
            print(Fore.RED + f"primeira_celula_vazia Ocorreu um erro ao obter o valor da célula. Erro: {e}" + Fore.RESET)
            tem_internet()
            cred = credencial()
            service = build('sheets', 'v4', credentials=cred)


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
                return True, indices_vazios[indece - 1]
    return False, 0


def escrever_celula(valor, guia, endereco):
    print("escrever_celula")
    global cred
    global service
    regiao = f"{guia}!{endereco}"  # 'R1!B150'
    while True:
        try:
            # Define o corpo da solicitação de atualização
            value_input_option = 'USER_ENTERED'
            values = [[valor]]
            data = {'values': values}
            result = service.spreadsheets().values().update(
                spreadsheetId=planilha_id,
                range=regiao,
                valueInputOption=value_input_option,
                body=data).execute()
            break
            # print('{0} células atualizadas.'.format(result.get('updatedCells')))
        # except (socket.gaierror, TransportError, ServerNotFoundError) as error:
        except Exception as e:
            print(Fore.RED + f"escrever_celula. Erro: {e}" + Fore.RESET)
            # time.sleep(5)
            tem_internet()
            cred = credencial()
            service = build('sheets', 'v4', credentials=cred)


def escrever_valores(valores, guia, endereco):
    # recebe uma lista de valores como argumento valores. Essa lista será usada para preencher três células adjacentes.
    # Os valores serão escritos nas células adjacentes começando pela célula especificada em endereco.

    global cred
    global service
    regiao = f"{guia}!{endereco}"  # 'R1!B150'
    while True:
        try:
            # Define o corpo da solicitação de atualização
            value_input_option = 'USER_ENTERED'
            values = [valores]  # Lista de valores a serem escritos nas células
            data = {'values': values}
            result = service.spreadsheets().values().update(
                spreadsheetId=planilha_id,
                range=regiao,
                valueInputOption=value_input_option,
                body=data).execute()
            break
            # print('{0} células atualizadas.'.format(result.get('updatedCells')))
        # except (socket.gaierror, TransportError, ServerNotFoundError) as error:
        except Exception as e:
            print(Fore.RED + f"escrever_valores. Erro: {e}" + Fore.RESET)
            # time.sleep(5)
            tem_internet()
            cred = credencial()
            service = build('sheets', 'v4', credentials=cred)


def escrever_valores_lote(valores, guia, linha):
    global cred
    global service
    range_start = f"{guia}!E{linha}:I{linha}"

    if len(valores) >= 5:
        # Verifica se o quinto valor está vazio
        if valores[4] == "":
            # Remove o quinto valor se estiver vazio
            valores = valores[:4]

    data = {
        'range': range_start,
        'majorDimension': 'ROWS',
        'values': [valores]
    }

    while True:
        try:
            result = service.spreadsheets().values().batchUpdate(
                spreadsheetId=planilha_id,
                body={
                    'valueInputOption': 'USER_ENTERED',
                    'data': [data]
                }
            ).execute()
            break

        except Exception as e:
            print(Fore.RED + f"escrever_valores_lote. Erro: {e}" + Fore.RESET)
            tem_internet()
            cred = credencial()
            service = build('sheets', 'v4', credentials=cred)


def reservar_linha(guia, endereco, salta_linhas=True):
    print("reservar_linha")
    global linha_vazia_anterior

    n_pc = None
    id = ""
    senha = ""
    linha = ""
    fichas = ""
    contagem_ip = ""
    # print(valor)
    if valor_pc is not None:

        escrever_celula(valor_pc, guia, endereco)
        linha = endereco[1:]
        if salta_linhas:
            time.sleep(10)  # tempo entre pegar o id e testa se nao teve concorrencia
        else:
            time.sleep(5.5)  # tempo entre pegar o id e testa se nao teve concorrencia
        n_pc, id, senha, fichas, level = lote_valor(guia, linha)
        try:
            n_pc = int(n_pc)
            if valor_pc == n_pc:
                print("Não teve concorrencia pela celula")
                return True, id, senha, fichas, linha, level  # Retorna o valor testado, id, senha e linha
            else:
                print("Pego por outro computador")
                if salta_linhas:
                    linha_vazia_anterior += random.randint(5, 30)
                else:
                    linha_vazia_anterior += random.randint(5, 20)
                return False, id, senha, fichas, linha, level
            # print("values :",values)
        except:
            if salta_linhas:
                linha_vazia_anterior += random.randint(5, 30)
            else:
                linha_vazia_anterior += random.randint(5, 20)
            return False, id, senha, fichas, linha, level

    else:
        print('A chave não existe no dicionário')


def lote_valor(guia, linha):
    global cred, service

    regiao2 = f"{guia}!B{linha}:I{linha}"  # regiao com a informação id senha e numero computador
    # regiao1 = f"{end_contagem_ip}"  # pega a contagem de ip

    regiao = [regiao2]

    while True:

        try:
            result = service.spreadsheets().values().batchGet(
                spreadsheetId=planilha_id,
                ranges=regiao
            ).execute()

            value_ranges = result.get('valueRanges', [])
            values = []

            for range_data in value_ranges:
                range_values = range_data.get('values', [])
                if range_values:
                    values.extend(range_values[0])

            # print("Os valores são:", values)

            if len(values) > 3:
                # cont_IP = values[0]
                id = values[0]
                senha = values[1]
                n_pc = values[2]
                fichas = values[3]
                level = values[-1]

            else:
                # cont_IP = values[0]
                id = values[0]
                senha = values[1]
                n_pc = values[2]
                fichas = 0
                level = 1
            return n_pc, id, senha, fichas, level

        except Exception as e:
            print(Fore.RED + f"lote_valor. Erro: {e}" + Fore.RESET)
            tem_internet()
            cred = credencial()
            service = build('sheets', 'v4', credentials=cred)


def pega_valor_endereco(endereco):
    print('pega_valor')
    global cred
    global service
    regiao = f"{endereco}"  # 'R1!B150'

    if cred is None or service is None:
        cred = credencial()
        service = build('sheets', 'v4', credentials=cred)

    while True:
        try:
            # Faz a requisição para obter os valores da célula
            result = service.spreadsheets().values().get(
                spreadsheetId=planilha_id,
                range=regiao).execute()
            # Extrai o valor da célula e retorna
            values = result.get('values', [])
            print("o valor escrito na celula é :", values[0][0])
            return values[0][0]

        # except (socket.gaierror, TransportError, ServerNotFoundError) as error:
        except Exception as e:
            print(Fore.RED + f"pega_valor_endereco. Erro: {e}" + Fore.RESET)
            tem_internet()
            # return None
            cred = credencial()
            service = build('sheets', 'v4', credentials=cred)


def zera_cont_IP(endereco):
    global cred
    global service

    cred = credencial()
    service = build('sheets', 'v4', credentials=cred)

    letra = endereco[:4]  # obtém a primeira letra do endereço
    numero = int(endereco[4:])  # obtém o número do endereço
    endereco2 = letra + str(numero - 1)  # cria a variável com o endereço imediatamente inferior
    endereco1 = letra + str(numero - 2)  # cria a variável com o endereço duas posições abaixo
    regiao1 = f"{endereco1}"  # 'R1!F1'
    regiao2 = f"{endereco2}"  # 'R1!F2'
    while True:
        try:
            result = service.spreadsheets().values().get(
                spreadsheetId=planilha_id,
                range=regiao1).execute()
            values = result.get('values', [])
            if len(values) > 0:
                value = values[0][0]
                data = {'values': [[value]]}
                result = service.spreadsheets().values().update(
                    spreadsheetId=planilha_id,
                    range=regiao2,
                    valueInputOption='USER_ENTERED',
                    body=data).execute()
                print('{0} células atualizadas.'.format(result.get('updatedCells')))
                return
        # except (socket.gaierror, TransportError, ServerNotFoundError) as error:
        except Exception as e:
            print(Fore.RED + f"zera_cont_IP. Erro: {e}" + Fore.RESET)
            # time.sleep(5)
            tem_internet()
            cred = credencial()
            service = build('sheets', 'v4', credentials=cred)


def credenciais(guia, salta_linhas=True):
    print("credenciais")
    reservado = False

    while True:  # pega a peimira celula vazia e pega as credenciais para entrar

        endereco = primeira_celula_vazia(guia)

        reservado, id, senha, fichas, linha, level = reservar_linha(guia, endereco, salta_linhas)

        if reservado:
            try:
                level = float(level.replace(",", "."))
            except Exception as error:
                print(error)
                level = 1
            try:
                fichas = tratar_valor_numerico(fichas)
            except Exception as error:
                print(error)
                fichas = 1
            return id, senha, fichas, linha, level

        print('tentar credenciaias')


def marca_caida(status, guia, linha, ip):
    if (status != 'Banida') and (status != "Senha incorreta"):
        endereco = f"D{linha}"
        escrever_celula('x', guia, endereco)
    if status == "Senha incorreta":
        endereco = f"D{linha}"
        # escrever_celula("", guia, endereco)
        escrever_valores([""], guia, endereco)
    if status == "Banida":
        endereco = f"H{linha}"
        escrever_celula(ip, guia, endereco)
    endereco = f"G{linha}"
    escrever_celula(status, guia, endereco)
    # endereco = f"L{linha}"
    # escrever_celula(status, guia, endereco)


def apagar_numerodo_pc(valores, guia, linha):
    endereco = f"D{linha}"
    escrever_valores(valores, guia, endereco)




def obter_id_proxy():
    """
    Função para ler a guia 'dados' e montar um dicionário 'dic_id_prox' com base nos valores
    das colunas B (IDs) e D (Proxies). A função usa o tamanho da coluna B como referência.

    A função é robusta para tratar erros de conexão ou de execução, e continuará tentando
    até que o dicionário seja montado corretamente.

    Retorna:
    - dict: Um dicionário no formato {ID: Proxy}.
    """
    global cred, service
    guia = 'Dados'
    dic_id_proxy = {}

    while True:  # Loop até que o dicionário seja montado corretamente
        try:
            # Verifica se as credenciais e o serviço foram inicializados
            if cred is None or service is None:
                cred = credencial()  # Obtém as credenciais
                service = build('sheets', 'v4', credentials=cred)  # Inicializa o serviço

            # Buscar as colunas B (IDs) e D (Proxies) em uma única requisição
            try:
                result = service.spreadsheets().values().batchGet(
                    spreadsheetId=planilha_id,
                    ranges=[f"{guia}!B:B", f"{guia}!D:D"],  # Pegando as colunas B e D
                    majorDimension="COLUMNS",  # Major dimension em colunas para retornar os valores em listas
                    valueRenderOption="UNFORMATTED_VALUE"
                ).execute()

                ids = result.get('valueRanges', [])[0].get('values', [[]])[0]  # Coluna B (IDs)
                proxies = result.get('valueRanges', [])[1].get('values', [[]])[0]  # Coluna D (Proxies)
                ultima_linha_preenchida = len(ids)  # Número de IDs encontrados
            except Exception as e:
                print(Fore.RED + f"Erro ao obter IDs e Proxies: {e}. Tentando novamente..." + Fore.RESET)
                time.sleep(5)  # Espera antes de tentar novamente
                continue  # Tenta novamente

            # Se não houver IDs, retorna um dicionário vazio
            if ultima_linha_preenchida == 0:
                print("Nenhum ID encontrado.")
                return {}

            # Ajustar o tamanho da lista de proxies para o tamanho da coluna B
            while len(proxies) < ultima_linha_preenchida - 1:
                proxies.append('')  # Preenche com strings vazias caso a lista de proxies seja menor que a de IDs

            # Montar o dicionário de IDs e Proxies
            for i in range(1, ultima_linha_preenchida):  # Começa da linha 2, pois a 1ª linha é o cabeçalho
                id_conta = str(ids[i])  # Converte o ID para string
                proxy = proxies[i] if i < len(proxies) else ''  # Previne erro se proxies tiverem menos linhas
                dic_id_proxy[id_conta] = proxy

            tamanho = len(dic_id_proxy)

            print(f"Dicionário de IDs e Proxies montado com {tamanho} id/proxy.")
            return dic_id_proxy  # Retorna o dicionário montado

        except Exception as e:
            # Qualquer erro inesperado será tratado aqui
            print(Fore.RED + f"Erro inesperado: {e}. Tentando novamente..." + Fore.RESET)
            time.sleep(5)  # Espera antes de tentar novamente
            continue  # Tenta novamente








# dic_id_prox = obter_id_proxy()






# gerar_tokens()


# def pega_ID_senha(guia, endereco):
#     global cred
#     global service
#     linha = re.sub("[^0-9]", "", endereco)  # pega a linha
#     regiao = f"{guia}!B{linha}:C{linha}"  # 'R1!B2:C2'
#     while True:
#         try:
#             # Faz a requisição para obter os valores das células
#             result = service.spreadsheets().values().get(
#                 spreadsheetId=planilha_id,
#                 range=regiao).execute()
#             # Extrai os valores das células B2 e C2
#             values = result.get('values', [])
#             print("O ID e senhas são :", values)
#             if len(values) == 1:
#                 id = values[0][0]
#                 senha = values[0][1]
#                 return id, senha, linha
#         # except (socket.gaierror, TransportError, ServerNotFoundError) as error:
#         except Exception as error:
#             print(f"pega_ID_senha Ocorreu um erro ao obter o valor da célula:")
#             print(f"Erro: {str(error)}")
#             print("Erro pega_ID_senha. Tentando novamente em 5 segundos...")
#             time.sleep(5)
#             tem_internet()
#             cred = credencial()
#             service = build('sheets', 'v4', credentials=cred)


# def escrever_IP_banido(ip):
#
#     # nome_computador = socket.gethostname()
#     # nome_usuario = os.getlogin()
#     print('\n\n ip banido \n')
#     print(ip)
#     print('\n\n')
#
#     print("espera 30 para nao ter concorrencia por recurso do googles")
#     time.sleep(30)
#     print('continua')
#
#     if (nome_usuario == "PokerIP") or ((nome_usuario == "lgagu") and (
#             nome_computador == "PC-I7-9700KF")):  # teste se o usuario do computador é o que troca IP se nao for fica esperando esta livre
#         print('computador principarl vai marcar o IP banido')
#     else:
#         print('Não é um computador prncipal, apenas espera liberar um novo ip')
#         return
#
#     global cred
#     global service
#
#     # cred = credencial()
#     # service = build('sheets', 'v4', credentials=cred)
#
#     data_hora_atual = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#
#     while True:
#         try:
#             # Define o corpo da solicitação de pesquisa da célula vazia
#             range_ = 'Ban!A:A'
#             result = service.spreadsheets().values().get(
#                 spreadsheetId=planilha_id,
#                 range=range_).execute()
#             values = result.get('values', [])
#
#             # Encontra a primeira célula vazia na coluna A
#             primeira_celula_vazia = len(values) + 1
#
#             # Define o intervalo da célula a ser atualizada
#             range_atualizar = f'Ban!A{primeira_celula_vazia}:D{primeira_celula_vazia}'
#
#             # Define o corpo da solicitação de atualização
#             value_input_option = 'USER_ENTERED'
#             values = [[ip, data_hora_atual, nome_usuario, nome_computador]]  # valores que deseja adicionar
#             data = {'values': values}
#             result = service.spreadsheets().values().update(
#                 spreadsheetId=planilha_id,
#                 range=range_atualizar,
#                 valueInputOption=value_input_option,
#                 body=data).execute()
#
#             # Exibe a quantidade de células atualizadas
#             print('{0} células atualizadas.'.format(result.get('updatedCells')))
#             return
#         except Exception as error:
#             print("escrever_IP_banido Ocorreu um erro ao escrever na célula:")
#             print(f"Erro: {str(error)}")
#             print("Tentando novamente em 5 segundos...")
#             # time.sleep(5)
#             tem_internet()
#             cred = credencial()
#             service = build('sheets', 'v4', credentials=cred)


# def lista_ip_banidos():
#     global cred
#     global service
#     guia = 'Ban'
#     coluna = 'A'
#     # Construa o intervalo da coluna desejada (por exemplo, "Ban!A:A" para a coluna A da guia "Ban")
#     intervalo = f"{guia}!{coluna}2:{coluna}"
#     while True:
#         try:
#             # Faz a requisição para obter os valores da coluna
#             result = service.spreadsheets().values().get(
#                 spreadsheetId=planilha_id,
#                 range=intervalo).execute()
#
#             # Extrai os valores da coluna
#             valores_coluna = result.get('values', [])
#
#             if not valores_coluna:
#                 return []  # Retorna uma lista vazia se a coluna estiver vazia
#
#             # Converte a lista de tuplas em uma lista simples de endereços IP
#             enderecos_ip = [item[0] for item in valores_coluna]
#
#             # Remove valores duplicados usando um conjunto (set) e, em seguida, converte de volta para uma lista
#             valores_unicos = list(set(enderecos_ip))
#             print(valores_unicos)
#             print('a lista de IP banido tem: ', len(valores_unicos))
#             return valores_unicos
#
#         except Exception as error:
#             print(f"lista_ip_banidos: Ocorreu um erro ao obter os valores da coluna:")
#             print(f"Erro: {str(error)}")
#             tem_internet()
#             cred = credencial()
#             service = build('sheets', 'v4', credentials=cred)


# def tem_internet():
#     com_internete = True
#     while com_internete:
#         print('Google testa a internete')
#         try:
#             response = requests.get('http://www.google.com', timeout=5)
#             if response.status_code == 200:
#                 print("Conexão com a internet ativa...")
#                 com_internete = False
#                 return True
#
#         except Exception as e:
#             print(Fore.RED + f"tem_internet. Erro: {e}" + Fore.RESET)
#             time.sleep(3)
#
#     return True
