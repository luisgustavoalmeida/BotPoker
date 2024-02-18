# deve se instlar a biblioteca
# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

from __future__ import print_function

import os
import os.path
import socket
import time

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

import IP

# from googleapiclient.errors import HttpError


# Define o escopo, desta forma tem permição total a plania e ao google drive
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']  # permite que a aplicação tenha acesso de leitura e escrita a planilhas do Google Sheets.

# ID da planilha
planilha_id = '1cEeMrBRVLnw7qtjiA63dK5q_HNvmJaCC5kNudzDjLgM'

# Obter o nome do computador
nome_computador = socket.gethostname()
# Obter o nome de usuário
# nome_usuario = os.getlogin()
# nome do computador e do usuario
nome_completo = socket.gethostname() + "_" + os.getlogin()

dicionari_token_credencial_n = {'PC-I5-8600K_PokerIP': ("token1.json", "credentials0.json", 1, 'gayaluisaalmeida@gmail.com', 'lglg32379089'),
                                'PC-I5-8600K_lgagu': ("token2.json", "credentials0.json", 2, 'lga.gustavo.a@gmail.com', 'LGlg32379089@'),
                                'PC-I5-8600K_Poker': ("token3.json", "credentials0.json", 3, 'luis.gustavo@engenharia.ufjf.br', 'LGlg32379089@#'),

                                'PC-I5-9400A_PokerIP': ("token4.json", "credentials1.json", 4, 'gayaluisaalmeida@gmail.com', 'lglg32379089'),
                                'PC-I5-9400A_lgagu': ("token5.json", "credentials1.json", 5, 'lga.gustavo.a@gmail.com', 'LGlg32379089@'),
                                'PC-I5-9400A_Poker': ("token6.json", "credentials1.json", 6, 'luis.gustavo@engenharia.ufjf.br', 'LGlg32379089@#'),

                                'PC-I5-9400B_PokerIP': ("token7.json", "credentials2.json", 7, 'gayaluisaalmeida@gmail.com', 'lglg32379089'),
                                'PC-I5-9400B_lgagu': ("token8.json", "credentials2.json", 8, 'lga.gustavo.a@gmail.com', 'LGlg32379089@'),
                                'PC-I5-9400B_Poker': ("token9.json", "credentials2.json", 9, 'luis.gustavo@engenharia.ufjf.br', 'LGlg32379089@#'),

                                'PC-I5-9400C_PokerIP': ("token10.json", "credentials3.json", 10, 'gayaluisaalmeida@gmail.com', 'lglg32379089'),
                                'PC-I5-9400C_lgagu': ("token11.json", "credentials3.json", 11, 'lga.gustavo.a@gmail.com', 'LGlg32379089@'),
                                'PC-I5-9400C_Poker': ("token12.json", "credentials3.json", 12, 'luis.gustavo@engenharia.ufjf.br', 'LGlg32379089@#'),

                                'PC-R5-7600A_PokerIP': ("token13.json", "credentials4.json", 13, 'gayaluisaalmeida@gmail.com', 'lglg32379089'),
                                'PC-R5-7600A_lgagu': ("token14.json", "credentials4.json", 14, 'lga.gustavo.a@gmail.com', 'LGlg32379089@'),
                                'PC-R5-7600A_Poker': ("token15.json", "credentials4.json", 15, 'luis.gustavo@engenharia.ufjf.br', 'LGlg32379089@#'),

                                'PC-I5-13400A_PokerIP': ("token16.json", "credentials5.json", 16, 'gayaluisaalmeida@gmail.com', 'lglg32379089'),
                                'PC-I5-13400A_lgagu': ("token17.json", "credentials5.json", 17, 'lga.gustavo.a@gmail.com', 'LGlg32379089@'),
                                'PC-I5-13400A_Poker': ("token18.json", "credentials5.json", 18, 'luis.gustavo@engenharia.ufjf.br', 'LGlg32379089@#'),

                                'PC-I5-13400B_PokerIP': ("token19.json", "credentials0.json", 19, 'gayaluisaalmeida@gmail.com', 'lglg32379089'),
                                'PC-I5-13400B_lgagu': ("token20.json", "credentials0.json", 20, 'lga.gustavo.a@gmail.com', 'LGlg32379089@'),
                                'PC-I5-13400B_Poker': ("token21.json", "credentials0.json", 21, 'luis.gustavo@engenharia.ufjf.br', 'LGlg32379089@#'),

                                'PC-I5-13400C_PokerIP': ("token22.json", "credentials1.json", 22, 'gayaluisaalmeida@gmail.com', 'lglg32379089'),
                                'PC-I5-13400C_lgagu': ("token23.json", "credentials1.json", 23, 'lga.gustavo.a@gmail.com', 'LGlg32379089@'),
                                'PC-I5-13400C_Poker': ("token24.json", "credentials1.json", 24, 'luis.gustavo@engenharia.ufjf.br', 'LGlg32379089@#'),

                                'PC-I5-13400D_PokerIP': ("token25.json", "credentials2.json", 25, 'gayaluisaalmeida@gmail.com', 'lglg32379089'),
                                'PC-I5-13400D_lgagu': ("token26.json", "credentials2.json", 26, 'lga.gustavo.a@gmail.com', 'LGlg32379089@'),
                                'PC-I5-13400D_Poker': ("token27.json", "credentials2.json", 27, 'luis.gustavo@engenharia.ufjf.br', 'LGlg32379089@#'),

                                'PC-R5-5600G_PokerIP': ("token28.json", "credentials3.json", 28, 'gayaluisaalmeida@gmail.com', 'lglg32379089'),
                                'PC-R5-5600G_lgagu': ("token29.json", "credentials3.json", 29, 'lga.gustavo.a@gmail.com', 'LGlg32379089@'),
                                'PC-R5-5600G_Poker': ("token30.json", "credentials3.json", 30, 'luis.gustavo@engenharia.ufjf.br', 'LGlg32379089@#'),

                                'PC-I5-13400E_PokerIP': ("token31.json", "credentials4.json", 31, 'gayaluisaalmeida@gmail.com', 'lglg32379089'),
                                'PC-I5-13400E_lgagu': ("token32.json", "credentials4.json", 32, 'lga.gustavo.a@gmail.com', 'LGlg32379089@'),
                                'PC-I5-13400E_Poker': ("token33.json", "credentials4.json", 33, 'luis.gustavo@engenharia.ufjf.br', 'LGlg32379089@#'),

                                'PC-I7-9700KF_PokerIP': ("token34.json", "credentials5.json", 34, 'gayaluisaalmeida@gmail.com', 'lglg32379089'),
                                'PC-I7-9700KF_lgagu': ("token35.json", "credentials5.json", 35, 'lga.gustavo.a@gmail.com', 'LGlg32379089@'),
                                'PC-I7-9700KF_Poker': ("token36.json", "credentials5.json", 36, 'luis.gustavo@engenharia.ufjf.br', 'LGlg32379089@#'),

                                'PC-i3-8145U_PokerIP': ("token37.json", "credentials5.json", 37, 'gayaluisaalmeida@gmail.com', 'lglg32379089')
                                }

dicionari_PC_IP = {'PC-I5-8600K': "IP!F3",
                   'PC-I5-9400A': "IP!F6",
                   'PC-I5-9400B': "IP!F9",
                   'PC-I5-9400C': "IP!F12",
                   'PC-R5-7600A': "IP!F15",
                   'PC-I5-13400A': "IP!F18",
                   'PC-I5-13400B': "IP!F21",
                   'PC-I5-13400C': "IP!F24",
                   'PC-I5-13400D': "IP!F27",
                   'PC-R5-5600G': "IP!F30",
                   'PC-I5-13400E': "IP!F33",
                   'PC-I7-9700KF': "IP!F36",
                   'PC-i3-8145U': "IP!F39"}

valor_dicionario = dicionari_token_credencial_n[nome_completo]
valor_pc = valor_dicionario[2]  # numero do computador
token = valor_dicionario[0]  # pega o primeiro item da tupla
credentials = valor_dicionario[1]  # pega o segundo item da tuplas
token_path = os.path.join('Tokens', token)
credencial_path = os.path.join('Tokens', credentials)


def credencial():
    # IP.tem_internet()
    """Mostra o uso básico da Sheets API.
    Imprime valores de uma planilha de amostra.
    """
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


cred = credencial()
service = build('sheets', 'v4', credentials=cred)

# def primeira_celula_vazia3(guia):
#     print('primeira celula vazia')
#     global cred
#     global service
#     regiao = f"{guia}!D:D"  # 'R1!D:D'
#     # Chame a API Sheets
#     sheet = service.spreadsheets()
#     while True:
#         try:
#             result = sheet.values().get(
#                 spreadsheetId=planilha_id,
#                 range=regiao,
#                 majorDimension="COLUMNS",
#                 valueRenderOption="UNFORMATTED_VALUE"
#             ).execute()
#             values = result.get('values', [[]])[0]
#
#             try:
#                 i = values.index("")
#                 return f"D{i + 1}"
#             except ValueError:
#                 i = len(values)
#                 return f"D{i + 1}"
#         except Exception as error:
#             print(f"Ocorreu um erro ao obter o valor da célula:")
#             print(f"Erro: {str(error)}")
#             time.sleep(5)
#             IP.tem_internet()
#             cred = credencial()
#             service = build('sheets', 'v4', credentials=cred)


linha_vazia_anterior = 2  # Inicializa a variável global
intervalo_de_busca = 500
guia_antiga = None


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
        print('linha vazia: ', linha_vazia_anterior)
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

            # Tenta encontrar a célula vazia no intervalo
            try:
                i = values.index("")
                # print(i)
                linha_vazia_anterior += i  # Atualiza a variável global com a próxima linha vazia
                print('linha encontrada: ', linha_vazia_anterior)
                endereco = f"D{linha_vazia_anterior}"
                print(endereco)
                return f"D{linha_vazia_anterior}"

            except ValueError:
                i = len(values)
                # print(i)
                if i < intervalo_de_busca + 1:
                    linha_vazia_anterior += i  # Atualiza a variável global com a próxima linha vazia
                    print('linha encontrada: ', linha_vazia_anterior)
                    endereco = f"D{linha_vazia_anterior}"
                    print(endereco)
                    return f"D{linha_vazia_anterior}"

                else:
                    linha_vazia_anterior += intervalo_de_busca

        except Exception as e:
            print(f"primeira_celula_vazia Ocorreu um erro ao obter o valor da célula:", e)
            print("Erro primeira_celula_vazia. Tentando novamente em 5 segundos...")
            # time.sleep(5)
            IP.tem_internet()
            cred = credencial()
            service = build('sheets', 'v4', credentials=cred)


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
        except Exception as error:
            print(f"escrever_celula Ocorreu um erro ao obter o valor da célula:")
            print(f"Erro: {str(error)}")
            # time.sleep(5)
            IP.tem_internet()
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
        except Exception as error:
            print(f"escrever_valores Ocorreu um erro ao obter o valor da célula:")
            print(f"Erro: {str(error)}")
            # time.sleep(5)
            IP.tem_internet()
            cred = credencial()
            service = build('sheets', 'v4', credentials=cred)


def escrever_valores_lote(valores, guia, linha):
    global cred
    global service
    range_start = f"{guia}!E{linha}:I{linha}"

    # Verifica se o quinto valor é vazio
    if valores[4] == "":
        # Se for vazio, exclui o quinto valor da lista
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

        except Exception as error:
            print(f" escrever_valores_lote Ocorreu um erro ao obter o valor da célula:")
            print(f"Erro: {str(error)}")
            # time.sleep(5)
            IP.tem_internet()
            cred = credencial()
            service = build('sheets', 'v4', credentials=cred)


def reservar_linha(guia, endereco, salta_linhas=True):
    print("reservar_linha")
    global linha_vazia_anterior

    values = None
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
            time.sleep(10.5)  # tempo entre pegar o id e testa se nao teve concorrencia
        else:
            time.sleep(5.5)  # tempo entre pegar o id e testa se nao teve concorrencia
        values, id, senha, fichas, contagem_ip = lote_valor(guia, linha)
        try:
            values = int(values)
            if valor_pc == values:
                print("Não teve concorrencia pela celula")
                return True, id, senha, fichas, linha, contagem_ip  # Retorna o valor testado, id, senha e linha
            else:
                print("Pego por outro computador")
                if salta_linhas:
                    linha_vazia_anterior += 40
                else:
                    linha_vazia_anterior += 10
                return False, id, senha, fichas, linha, contagem_ip
            # print("values :",values)
        except:
            if salta_linhas:
                linha_vazia_anterior += 40
            else:
                linha_vazia_anterior += 1
            return False, id, senha, fichas, linha, contagem_ip

    else:
        print('A chave não existe no dicionário')


def lote_valor(guia, linha):
    global cred
    global service
    regiao1 = f"{guia}!B{linha}:E{linha}"  # regiao com a informação id senha e numero computador
    # print(regiao1)
    regiao2 = f"{dicionari_PC_IP[nome_computador]}"  # pega a contagem de ip
    # print(regiao2)
    regiao = [regiao1, regiao2]

    # print(regiao)

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

            print("Os valores são:", values)

            if len(values) >= 4:
                id = values[0]
                senha = values[1]
                valor = values[2]
                fichas = values[3]
                cont_IP = values[4]
                # print(cont_IP)
                return valor, id, senha, fichas, cont_IP

        except Exception as error:
            print(f"lote_valor Ocorreu um erro ao obter o valor da célula:")
            print(f"Erro: {str(error)}")
            time.sleep(5)
            IP.tem_internet()
            cred = credencial()
            service = build('sheets', 'v4', credentials=cred)


def pega_valor(guia, endereco):
    print('pega_valor')
    global cred
    global service
    regiao = f"{guia}!{endereco}"  # 'R1!B150'
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
        except Exception as error:
            print(f"pega_valor Ocorreu um erro ao obter o valor da célula:")
            print(f"Erro: {str(error)}")
            IP.tem_internet()
            # return None
            cred = credencial()
            service = build('sheets', 'v4', credentials=cred)


# def pega_valores_em_lote(guia, enderecos):
#     '''
#     # Para um único endereço
#     valor = pega_valores_em_lote("Planilha1", "A1")
#     print("Valor obtido:", valor)
#
#     # Para uma lista de endereços
#     enderecos = ["A1", "B1", "C1"]
#     valores = pega_valores_em_lote("Planilha1", enderecos)
#     print("Valores obtidos:", valores)'''
#
#     print('pega_valores_em_lote')
#     global cred
#     global service
#
#     if isinstance(enderecos, str):
#         enderecos = [enderecos]  # Se for um único endereço, coloca em uma lista
#
#     regioes = [f"{guia}!{endereco}" for endereco in enderecos]
#
#     while True:
#         try:
#             # Faz a requisição para obter os valores das células em lote
#             result = service.spreadsheets().values().batchGet(
#                 spreadsheetId=planilha_id,
#                 ranges=regioes).execute()
#
#             # Extrai os valores das células e retorna como uma lista de valores
#             valores_retornados = []
#             for value_range in result.get('valueRanges', []):
#                 valores_range = value_range.get('values', [])
#                 if valores_range:
#                     valores_retornados.append(valores_range[0][0])
#                 else:
#                     valores_retornados.append(None)
#
#             print("Valores obtidos em lote:", valores_retornados)
#
#             if len(valores_retornados) == 1:
#                 return valores_retornados[0]  # Retorna o único valor quando a lista tem um item
#             else:
#                 return valores_retornados  # Retorna a lista completa quando tem mais de um item
#
#         except Exception as error:
#             print(f"pega_valores_em_lote Ocorreu um erro ao obter os valores das células:")
#             print(f"Erro: {str(error)}")
#             IP.tem_internet()
#             cred = credencial()
#             service = build('sheets', 'v4', credentials=cred)


# def celula_esta_vazia(guia, endereco):
#     print('celula_esta_vazia')
#     global cred
#     global service
#     celula = f"{guia}!{endereco}"
#     print(celula)
#
#     try:
#         result = service.spreadsheets().values().get(
#             spreadsheetId=planilha_id,
#             range=celula,
#             valueRenderOption="UNFORMATTED_VALUE"
#         ).execute()
#
#         # Verifica se a lista de valores não está vazia antes de acessar o primeiro elemento
#         values = result.get('values', [])
#         print(values)
#         if len(values) == 0:
#             return True
#         else:
#             return False
#
#     except Exception as e:
#         print(f"celula_esta_vazia Ocorreu um erro celula esta vasia:", e)
#         return False


def zera_cont_IP(endereco):
    global cred
    global service

    cred = credencial()
    service = build('sheets', 'v4', credentials=cred)

    letra = endereco[0]  # obtém a primeira letra do endereço
    numero = int(endereco[1:])  # obtém o número do endereço
    endereco2 = letra + str(numero - 1)  # cria a variável com o endereço imediatamente inferior
    endereco1 = letra + str(numero - 2)  # cria a variável com o endereço duas posições abaixo
    regiao1 = f"IP!{endereco1}"  # 'R1!F1'
    regiao2 = f"IP!{endereco2}"  # 'R1!F2'
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
        except Exception as error:
            print(f"zera_cont_IP Ocorreu um erro ao obter o valor da célula:")
            print(f"Erro: {str(error)}")
            # time.sleep(5)
            IP.tem_internet()
            cred = credencial()
            service = build('sheets', 'v4', credentials=cred)


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
#             IP.tem_internet()
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
#             IP.tem_internet()
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
#             IP.tem_internet()
#             cred = credencial()
#             service = build('sheets', 'v4', credentials=cred)


def credenciais(guia, salta_linhas=True):
    print("credenciais")
    reservado = False

    while True:  # pega a peimira celula vazia e pega as credenciais para entrar

        endereco = primeira_celula_vazia(guia)

        reservado, id, senha, fichas, linha, cont_IP = reservar_linha(guia, endereco, salta_linhas)

        if reservado:
            try:
                cont_IP = int(cont_IP)
                return id, senha, fichas, linha, cont_IP
            except Exception as error:
                print(error)
        print('tentar credenciaias')


# def marca_horario(guia, linha):
#     endereco = f"G{linha}"
#     hora_atual = datetime.datetime.now().strftime('%H:%M:%S')
#     escrever_celula(hora_atual, guia, endereco)


# def marca_banida(status, guia, linha):
#     endereco = f"G{linha}"
#     escrever_celula(status, guia, endereco)
#     endereco = f"L{linha}"
#     escrever_celula(status, guia, endereco)


def marca_caida(status, guia, linha):
    if status != 'Banida':
        endereco = f"D{linha}"
        escrever_celula('x', guia, endereco)
    endereco = f"G{linha}"
    escrever_celula(status, guia, endereco)
    # endereco = f"L{linha}"
    # escrever_celula(status, guia, endereco)


# def marca_ip(guia, linha):
#     endereco = f"H{linha}"
#     ip, com_internete = IP.tem_internet()
#     escrever_celula(ip, guia, endereco)


# def marca_ficha(guia, linha, valor_fichas):
#     endereco = f"E{linha}"
#     escrever_celula(valor_fichas, guia, endereco)


# def marca_pontuacao(guia, linha, pontuacao_tarefas):
#     endereco = f"F{linha}"
#     escrever_celula(pontuacao_tarefas, guia, endereco)


# def marca_informacoes(valores, guia, linha):
#     endereco = f"E{linha}"
#     escrever_valores(valores, guia, endereco)


def apagar_numerodo_pc(valores, guia, linha):
    endereco = f"D{linha}"
    escrever_valores(valores, guia, endereco)

# credencial()


# guia = "R1"
#
# credenciais(guia)
# linha = 3
# marca_horario(guia,linha)

#

# creds = credencial()
# escrever_celula("14", "R1", "G8") # conteudo, guia , endereço B150

# zera_cont_IP("F15")

# credenciais('R4')
# testa_valor("R4", 'D2')

# guia = "IP"
# endereco = "F1"
# pega_valores_em_lote(guia, endereco)
# pega_valor(guia, endereco)
