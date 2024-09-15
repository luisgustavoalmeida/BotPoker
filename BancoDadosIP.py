import datetime
import json
import sqlite3
import time

from Requerimentos import nome_usuario

pc_ativado = True

ARQUIVO_BD = 'tabele_ip.db'
CRIAR_TABELA = '''CREATE TABLE IF NOT EXISTS contagem_ip (
                            id INTEGER PRIMARY KEY,
                            dado_PC_1 NOT NULL DEFAULT 1,
                            dado_PC_2 NOT NULL DEFAULT 1,
                            dado_PC_3 NOT NULL DEFAULT 1,
                            soma_IP NOT NULL DEFAULT 1,
                            zera_IP NOT NULL DEFAULT 1,
                            ativo_PC_1 BOOLEAN DEFAULT 0,
                            ativo_PC_2 BOOLEAN DEFAULT 0,
                            ativo_PC_3 BOOLEAN DEFAULT 0
                        )'''
DELETAR_TABELA = "DROP TABLE contagem_ip;"
VERIFICAR_TABELA = "SELECT name FROM sqlite_master WHERE type='table' AND name='contagem_ip'"
INSERIR_INFO_INICIAL = ("INSERT INTO contagem_ip (dado_PC_1, dado_PC_2, dado_PC_3, soma_IP, zera_IP, ativo_PC_1, ativo_PC_2, ativo_PC_3) "
                        "VALUES (?, ?, ?, ?, ?, ?, ?, ?)")
ATUALIZAR_INFO_INICIAL = ("UPDATE contagem_ip SET dado_PC_1 = ?, dado_PC_2 = ?, dado_PC_3 = ?, soma_IP = ?, zera_IP = ?, "
                          "ativo_PC_1 = ?, ativo_PC_2 = ?, ativo_PC_3 = ? WHERE id = 1")
SELECIONAR_INFO_LINHA_1 = "SELECT * FROM contagem_ip WHERE id = 1;"
ATUALIZAR_DADO_PC_1 = "UPDATE contagem_ip SET dado_PC_1 = ? WHERE id = 1;"
ATUALIZAR_DADO_PC_2 = "UPDATE contagem_ip SET dado_PC_2 = ? WHERE id = 1;"
ATUALIZAR_DADO_PC_3 = "UPDATE contagem_ip SET dado_PC_3 = ? WHERE id = 1;"
INCREMENTA_PC_1 = "UPDATE contagem_ip SET dado_PC_1 = dado_PC_1 + 1 WHERE id = 1;"
INCREMENTA_PC_2 = "UPDATE contagem_ip SET dado_PC_2 = dado_PC_2 + 1 WHERE id = 1;"
INCREMENTA_PC_3 = "UPDATE contagem_ip SET dado_PC_3 = dado_PC_2 + 1 WHERE id = 1;"
DECREMENTA_PC_1 = "UPDATE contagem_ip SET dado_PC_1 = dado_PC_1 - 1 WHERE id = 1;"
DECREMENTA_PC_2 = "UPDATE contagem_ip SET dado_PC_2 = dado_PC_2 - 1 WHERE id = 1;"
DECREMENTA_PC_3 = "UPDATE contagem_ip SET dado_PC_3 = dado_PC_2 - 1 WHERE id = 1;"
ATUALIZAR_SOMA = "UPDATE contagem_ip SET soma_IP = dado_PC_1 + dado_PC_2 + dado_PC_3 WHERE id = 1;"
ZERA_CONTAGEM_IP = "UPDATE contagem_ip SET zera_IP = soma_IP;"
ATIVADO_PC_1 = "UPDATE contagem_ip SET ativo_PC_1 = 1 WHERE id = 1;"
ATIVADO_PC_2 = "UPDATE contagem_ip SET ativo_PC_2 = 1 WHERE id = 1;"
ATIVADO_PC_3 = "UPDATE contagem_ip SET ativo_PC_3 = 1 WHERE id = 1;"
DESATIVADO_PC_1 = "UPDATE contagem_ip SET ativo_PC_1 = 0 WHERE id = 1;"
DESATIVADO_PC_2 = "UPDATE contagem_ip SET ativo_PC_2 = 0 WHERE id = 1;"
DESATIVADO_PC_3 = "UPDATE contagem_ip SET ativo_PC_3 = 0 WHERE id = 1;"
TESTA_PC_ATIVO = "SELECT CASE WHEN EXISTS(SELECT 1 FROM contagem_ip WHERE ativo_PC_1 = 1 OR ativo_PC_2 = 1 OR ativo_PC_3 = 1) THEN 1 ELSE 0 END;"

tentativas_maximas = 9999999
intervalo_entre_tentativas = 2
antes_incremetar = 0
conn = None


def carregar_data_anterior():
    try:
        with open('data_anterior.json', 'r') as arquivo:
            data_anterior = json.load(arquivo)
    except FileNotFoundError:
        data_anterior = datetime.datetime.now().date().day
    return data_anterior


def salvar_data_anterior(data_anterior):
    with open('data_anterior.json', 'w') as arquivo:
        json.dump(data_anterior, arquivo)


data_anterior = carregar_data_anterior()


def teste_novo_dia():
    global data_anterior
    data_atual = datetime.datetime.now().date().day
    if data_atual != data_anterior:
        atualizar_info()
        salvar_data_anterior(data_atual)
        data_anterior = data_atual


import sqlite3

# Declara a variável global
conn = None


def criar_conexao():
    """
    Função para criar uma conexão com o banco de dados SQLite.

    Retorna:
        conn: Objeto de conexão com o banco de dados ou None se a conexão falhar.
    """
    global conn

    if conn is None:
        try:
            conn = sqlite3.connect(ARQUIVO_BD)
            print("Conexão com o banco de dados estabelecida.")
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            conn = None
    else:
        print("Conexão com o banco de dados já estava estabelecida.")

    return conn


def fechar_conexao():
    global conn
    if conn:
        conn.close()
        conn = None
        print("Conexão com o banco de dados encerrada.")


def criar_tabela():
    """
    Função para criar a tabela 'contagem_ip' no banco de dados, se ela não existir.

    Parâmetros:
        conn: Objeto de conexão com o banco de dados.
    """
    global conn
    try:
        criar_conexao()
        if conn:
            cursor = conn.cursor()
            # Verificando se a tabela já existe
            cursor.execute(VERIFICAR_TABELA)
            tabela_existe = cursor.fetchone() is not None

            if tabela_existe:
                # deleta a tabela
                cursor.execute(DELETAR_TABELA)

            cursor.execute(CRIAR_TABELA)
            print("Tabela 'contagem_ip' criada com sucesso!")
            inserir_info_inicial(dado_1=2, dado_2=2, dado_3=2, soma_ip=6, zera_ip=0, ativo_PC_1=0, ativo_PC_2=0, ativo_PC_3=0)
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela: {e}")


def atualizar_info(dado_1=0, dado_2=0, dado_3=0, soma_ip=0, zera_ip=0, ativo_PC_1=0, ativo_PC_2=0, ativo_PC_3=0):
    """
    Função para atualizar informações nas colunas da tabela 'contagem_ip'.
    """
    global conn
    for tentativa in range(tentativas_maximas):
        try:
            # Abre a conexão se ela não estiver aberta
            if not conn:
                conn = criar_conexao()

            if conn:
                with conn:
                    conn.execute(ATUALIZAR_INFO_INICIAL, (dado_1, dado_2, dado_3, soma_ip, zera_ip, ativo_PC_1, ativo_PC_2, ativo_PC_3))
                    conn.commit()  # Confirma as alterações
                print(f"Informações atualizadas com sucesso na tentativa {tentativa + 1}!")
                conn.close()
                conn = None  # Limpa a referência à conexão
                return  # Saia da função após a operação bem-sucedida

        except sqlite3.Error as e:
            # Fecha a conexão se ocorrer um erro
            if conn:
                conn.close()
                conn = None  # Limpa a referência à conexão
            print(f"Erro atualizar_info na tentativa {tentativa + 1}: {e}")
            if tentativa < tentativas_maximas - 1:
                time.sleep(intervalo_entre_tentativas)  # Aguarda antes de tentar novamente
            else:
                raise  # Propaga o erro na última tentativa

    print(f"Falha na atualização das informações após {tentativas_maximas} tentativas.")



def inserir_info_inicial(dado_1=0, dado_2=0, dado_3=0, soma_ip=0, zera_ip=0, ativo_PC_1=0, ativo_PC_2=0, ativo_PC_3=0):
    """
    Função para inserir informações nas três primeiras colunas da tabela 'contagem_ip'.
    """
    global conn
    for tentativa in range(tentativas_maximas):
        try:
            # Verifica se a conexão já existe ou cria uma nova
            if not conn:
                conn = criar_conexao()

            if conn:
                with conn:
                    conn.execute(INSERIR_INFO_INICIAL, (dado_1, dado_2, dado_3, soma_ip, zera_ip, ativo_PC_1, ativo_PC_2, ativo_PC_3))
                    conn.commit()  # Confirma as alterações
                print(f"Todas as colunas atualizadas com sucesso na tentativa {tentativa + 1}!")
                return  # Retorna se a operação foi bem-sucedida

        except sqlite3.Error as e:
            print(f"Erro na tentativa {tentativa + 1}: {e}")
            if conn:
                conn.close()
                conn = None  # Redefine a conexão após o erro
            if tentativa < tentativas_maximas - 1:
                time.sleep(intervalo_entre_tentativas)  # Aguarda antes da próxima tentativa
            else:
                raise  # Propaga o erro na última tentativa

    print(f"Falha na inserir_info_inicial após {tentativas_maximas} tentativas.")


def atualizar_contagem_ip(data):
    """
    Função para atualizar a informação do Script 2 na segunda coluna da tabela 'contagem_ip'.
    """
    global conn
    for tentativa in range(tentativas_maximas):
        try:
            # Tentativa de atualização
            criar_conexao()
            if conn:
                # criar_tabela(conn)  # Chamada para criar a tabela
                with conn:
                    match nome_usuario:
                        case 'PokerIP':
                            conn.execute(ATUALIZAR_DADO_PC_1, (data,))
                        case 'lgagu':
                            conn.execute(ATUALIZAR_DADO_PC_2, (data,))
                        case 'Poker':
                            conn.execute(ATUALIZAR_DADO_PC_3, (data,))
                        case _:
                            print(f'A T E N Ç Ã O Computador fora da faixa {nome_usuario}')

                    conn.commit()  # Confirma as alterações
                print(f"Dados atualizados com sucesso na tentativa {tentativa + 1}!")
                conn.close()
                return  # Retorna caso a atualização seja bem-sucedida
            else:
                print("Falha ao conectar ao banco de dados")
                conn.close()
        except sqlite3.Error as e:
            print(f"Erro na tentativa {tentativa + 1}: {e}")
            if tentativa < tentativas_maximas - 1:
                time.sleep(intervalo_entre_tentativas)  # Aguarda antes da próxima tentativa
            else:
                raise  # Propaga o erro na última tentativa

    print(f"Falha na atualizar_dado após {tentativas_maximas} tentativas.")


def incrementa_contagem_ip():
    """
    Função para incrementar a informação da tabela 'contagem_ip' referente a contagem de cada computador.
    """
    global antes_incremetar, conn
    while True:
        for tentativa in range(tentativas_maximas):
            try:
                # Tentar abrir uma conexão, se ainda não estiver aberta
                if not conn:
                    conn = criar_conexao()

                if conn:
                    with conn:
                        # Verifica o nome do usuário e aplica o incremento correto
                        match nome_usuario:
                            case 'PokerIP':
                                conn.execute(INCREMENTA_PC_1)
                                pc = 1
                            case 'lgagu':
                                conn.execute(INCREMENTA_PC_2)
                                pc = 2
                            case 'Poker':
                                conn.execute(INCREMENTA_PC_3)
                                pc = 3
                            case _:
                                print(f'A T E N Ç Ã O Computador com nome de usuario errado')
                                pc = 4

                        conn.commit()  # Confirma as alterações no banco

                    # Visualiza os dados atualizados após o incremento
                    dados = visualizar_tabela_banco()
                    if dados:
                        depois_incremetar = int(dados[pc])
                        if depois_incremetar != antes_incremetar:
                            antes_incremetar = depois_incremetar
                            print(f"Dados atualizados com sucesso na tentativa {tentativa + 1}!")
                            conn.close()  # Fecha a conexão após o sucesso
                            conn = None  # Limpa a referência da conexão
                            return  # Retorna ao final do loop se o sucesso for atingido
                        else:
                            print('\n\n A T E N Ç Ã O , FALHA PARA INCREMENTAR CONTAGEM DE IP \n\n')
                            conn.close()
                            conn = None
                            # time.sleep(1)
                else:
                    print("Falha ao conectar ao banco de dados")
                    time.sleep(intervalo_entre_tentativas)

            except sqlite3.Error as e:
                print(f"Erro na tentativa {tentativa + 1}: {e}")
                if conn:
                    conn.close()
                    conn = None  # Certifique-se de limpar a referência para evitar operar em uma conexão fechada
                if tentativa < tentativas_maximas - 1:
                    time.sleep(intervalo_entre_tentativas)  # Aguarda antes de tentar novamente
                else:
                    raise  # Propaga o erro na última tentativa

        print(f"Falha na incrementa_contagem_ip após {tentativas_maximas} tentativas.")
        conn.close()
        conn = None
        time.sleep(5)


def decrementa_contagem_ip():
    """
    Função para decrementar a informação da tabela 'contagem_ip' referente a contagem de cada computador.
    """
    global conn
    for tentativa in range(tentativas_maximas):
        try:
            # Verifica se a conexão já existe ou cria uma nova
            if not conn:
                conn = criar_conexao()

            if conn:
                with conn:
                    match nome_usuario:
                        case 'PokerIP':
                            conn.execute(DECREMENTA_PC_1)
                        case 'lgagu':
                            conn.execute(DECREMENTA_PC_2)
                        case 'Poker':
                            conn.execute(DECREMENTA_PC_3)
                        case _:
                            print("A T E N Ç Ã O: Computador com nome de usuário incorreto")
                            return

                    conn.commit()  # Confirma as alterações após o `match`
                print(f"Dados atualizados com sucesso na tentativa {tentativa + 1}!")
                return  # Saímos da função se a operação foi bem-sucedida

        except sqlite3.Error as e:
            print(f"Erro na tentativa {tentativa + 1}: {e}")
            if conn:
                conn.close()
                conn = None  # Redefine a conexão após o erro
            if tentativa < tentativas_maximas - 1:
                time.sleep(intervalo_entre_tentativas)  # Aguarda antes da próxima tentativa
            else:
                raise  # Propaga o erro na última tentativa

    print(f"Falha na decrementa_contagem_ip após {tentativas_maximas} tentativas.")


def indicar_pc_ativo():
    """
    Função para indicar que o computador está dentro da mesa.
    """
    global pc_ativado, conn

    if pc_ativado:
        return  # Se o PC já está ativado, não há necessidade de continuar

    for tentativa in range(tentativas_maximas):
        try:
            # Verifica se a conexão já existe ou cria uma nova
            if not conn:
                conn = criar_conexao()

            if conn:
                with conn:
                    match nome_usuario:
                        case 'PokerIP':
                            conn.execute(ATIVADO_PC_1)
                        case 'lgagu':
                            conn.execute(ATIVADO_PC_2)
                        case 'Poker':
                            conn.execute(ATIVADO_PC_3)
                        case _:
                            print("\n\nA T E N Ç Ã O: Computador com nome de usuário incorreto\n\n")
                            return

                    conn.commit()  # Confirma as alterações após o `match`
                    pc_ativado = True  # Atualiza o estado para indicar que o PC está ativado

                print(f"Dados atualizados com sucesso na tentativa {tentativa + 1}!")
                return  # Saímos da função se a operação foi bem-sucedida

        except sqlite3.Error as e:
            print(f"Erro na tentativa {tentativa + 1}: {e}")
            if conn:
                conn.close()
                conn = None  # Redefine a conexão após o erro
            if tentativa < tentativas_maximas - 1:
                time.sleep(intervalo_entre_tentativas)  # Aguarda antes da próxima tentativa
            else:
                raise  # Propaga o erro na última tentativa

    print(f"Falha ao ativar o PC após {tentativas_maximas} tentativas.")


def indicar_pc_desativo():
    """
    Função para indicar que o computador não está na mesa.
    """
    global pc_ativado, conn

    if not pc_ativado:
        return  # Se o PC já está desativado, não faz nada

    for tentativa in range(tentativas_maximas):
        try:
            # Verifica se a conexão já existe ou cria uma nova
            if not conn:
                conn = criar_conexao()

            if conn:
                # Executa o comando correspondente ao nome do usuário
                match nome_usuario:
                    case 'PokerIP':
                        conn.execute(DESATIVADO_PC_1)
                    case 'lgagu':
                        conn.execute(DESATIVADO_PC_2)
                    case 'Poker':
                        conn.execute(DESATIVADO_PC_3)
                    case _:
                        print(f"\n\nA T E N Ç Ã O: Computador com nome de usuário incorreto\n\n")
                        return  # Se o nome do usuário está errado, não há necessidade de continuar

                conn.commit()  # Confirma as alterações uma vez ao final
                pc_ativado = False  # Marca o PC como desativado

                print(f"Computador desativado com sucesso na tentativa {tentativa + 1}!")
                return  # Saímos da função em caso de sucesso

            else:
                print("Falha ao conectar ao banco de dados")
        except sqlite3.Error as e:
            print(f"Erro na tentativa {tentativa + 1}: {e}")
            if conn:
                conn.close()
                conn = None  # Redefine a conexão para evitar reutilizar uma conexão com falha
            if tentativa < tentativas_maximas - 1:
                time.sleep(intervalo_entre_tentativas)  # Aguarda antes de tentar novamente
            else:
                raise  # Propaga o erro na última tentativa

    print(f"Falha na desativação do computador após {tentativas_maximas} tentativas.")


def verificar_pc_ativo():
    """
    Verifica se há pelo menos um PC ativo no banco de dados.

    Retorna True se houver PC ativo, False caso contrário.
    """
    global conn
    try:
        if not conn:
            conn = criar_conexao()

        if conn:
            with conn:
                cursor = conn.cursor()
                cursor.execute(TESTA_PC_ATIVO)  # Executa a consulta SQL
                resultado = cursor.fetchone()  # Obtém o primeiro resultado da consulta

            # Verifica o resultado e retorna o valor correspondente
            return resultado[0] == 1 if resultado else False
        else:
            print("Falha ao conectar ao banco de dados")

    except sqlite3.Error as e:
        print(f"Erro ao verificar PC ativo: {e}")

    # Retorna False em caso de erro ou falha de conexão
    return False


def atualizar_soma_ip():
    """
    Função para atualizar a quarta coluna da tabela 'contagem_ip', que é a soma das três primeiras colunas.
    """
    global conn
    for tentativa in range(tentativas_maximas):  # Utilize as variáveis definidas na função `atualizar_dado`
        try:
            # Tentativa de atualização
            criar_conexao()
            if conn:
                # criar_tabela(conn)  # Chamada para criar a tabela
                with conn:
                    conn.execute(ATUALIZAR_SOMA)
                    conn.commit()  # Confirma as alterações
                print(f"Coluna de soma atualizada com sucesso na tentativa {tentativa + 1}!")
                return
            else:
                print("Falha ao conectar ao banco de dados")
                conn.close()
        except sqlite3.Error as e:
            print(f"Erro na tentativa {tentativa + 1}: {e}")
            if tentativa < tentativas_maximas - 1:
                time.sleep(intervalo_entre_tentativas)  # Aguarda antes da próxima tentativa
            else:
                raise  # Propaga o erro na última tentativa

    print(f"Falha na atualizar_soma_ip após {tentativas_maximas} tentativas.")


def zera_contagem_ip_banco():
    """
    Função para atualizar a quinta coluna da tabela 'contagem_ip', que é responsável por zerar a contagem de IP.
    """
    global conn
    teste_novo_dia()  # Chama a função para verificar se é um novo dia

    for tentativa in range(tentativas_maximas):
        try:
            # Verifica se a conexão já existe ou cria uma nova
            if not conn:
                conn = criar_conexao()

            if conn:
                # Atualiza a soma de IPs
                conn.execute(ATUALIZAR_SOMA)
                conn.commit()

                # Atualiza a coluna 'zera_IP' com a soma de IPs
                conn.execute(ZERA_CONTAGEM_IP)
                conn.commit()

                print(f"Coluna de soma atualizada com sucesso na tentativa {tentativa + 1}!")
                return  # Saímos da função se a operação foi bem-sucedida

        except sqlite3.Error as e:
            print(f"Erro na tentativa {tentativa + 1}: {e}")
            if conn:
                conn.close()
                conn = None  # Limpa a variável para evitar reuso de uma conexão falha
            if tentativa < tentativas_maximas - 1:
                time.sleep(intervalo_entre_tentativas)  # Aguardar antes da próxima tentativa
            else:
                raise  # Propaga o erro na última tentativa

    print(f"Falha ao zerar a contagem de IP após {tentativas_maximas} tentativas.")


def visualizar_tabela_banco():
    """
    Função para visualizar toda a tabela 'contagem_ip'.
    """
    global conn
    for tentativa in range(tentativas_maximas):
        try:
            # Tentativa de conexão
            if not conn:
                conn = criar_conexao()

            if conn:
                with conn:
                    conn.execute(ATUALIZAR_SOMA)  # Atualiza a soma antes de exibir
                    conn.commit()  # Confirma as alterações
                    cursor = conn.execute(SELECIONAR_INFO_LINHA_1)
                    primeira_linha = cursor.fetchall()[0]  # Obtem a primeira linha dos dados

                print(f"\nValores da contagem de IP: {primeira_linha}\n")
                return primeira_linha  # Retorna os dados obtidos

        except sqlite3.Error as e:
            print(f"Erro na tentativa {tentativa + 1}: {e}")
            if conn:
                conn.close()
                conn = None  # Redefine a conexão após o erro


    print(f"Falha ao visualizar a tabela após {tentativas_maximas} tentativas.")
    return None


def limpar_tabela():
    """
    Função para limpar toda a tabela 'contagem_ip'.
    """
    global conn
    try:
        criar_conexao()
        if conn:
            with conn:
                conn.execute("DELETE FROM contagem_ip")
            print("Tabela 'contagem_ip' limpa com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao limpar tabela: {e}")


def contagem_ip_banco():
    # global conn
    dados = visualizar_tabela_banco()
    # conn.close()
    # print(int(dados[4] - dados[5]))
    return int(dados[4] - dados[5])


# incrementa_contagem_ip()
# # verificar_pc_ativo()
#
# # atualizar_info()
# visualizar_tabela_banco()
# incrementa_contagem_ip()
# incrementa_contagem_ip()
# # atualizar_info()
#
# # atualizar_info()
# # indicar_pc_desativo()
# # indicar_pc_ativo()
#
#
# # criar_tabela()
# # contagem_ip_banco()
# # atualizar_info()
# # indicar_pc_ativo()
# # indicar_pc_desativo()
# contagem_ip_banco()
# visualizar_tabela_banco()
# print(verificar_pc_ativo()
# incrementa_contagem_ip()
