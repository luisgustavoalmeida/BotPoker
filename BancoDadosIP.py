import sqlite3
import time

ARQUIVO_BD = 'tabele_ip.db'
CRIAR_TABELA = '''CREATE TABLE IF NOT EXISTS contagem_ip (
                            id INTEGER PRIMARY KEY,
                            dado_PC_1 NOT NULL DEFAULT 1,
                            dado_PC_2 NOT NULL DEFAULT 1,
                            dado_PC_3 NOT NULL DEFAULT 1,
                            soma_IP NOT NULL DEFAULT 1,
                            zera_IP NOT NULL DEFAULT 1
                        )'''
VERIFICAR_TABELA = "SELECT name FROM sqlite_master WHERE type='table' AND name='contagem_ip'"

INSERIR_INFO_INICIAL = "INSERT INTO contagem_ip (dado_PC_1, dado_PC_2, dado_PC_3, soma_IP, zera_IP) VALUES (?, ?, ?, ?, ?)"
ATUALIZAR_INFO_INICIAL = "UPDATE contagem_ip SET dado_PC_1 = ?, dado_PC_2 = ?, dado_PC_3 = ?, soma_IP = ?, zera_IP = ? WHERE id = 1"

SELECIONAR_INFO_LINHA_1 = "SELECT * FROM contagem_ip WHERE id = 1;"
ATUALIZAR_DADO_PC_1 = "UPDATE contagem_ip SET dado_PC_1 = ? WHERE id = 1;"
ATUALIZAR_DADO_PC_2 = "UPDATE contagem_ip SET dado_PC_2 = ? WHERE id = 1;"
ATUALIZAR_DADO_PC_3 = "UPDATE contagem_ip SET dado_PC_3 = ? WHERE id = 1;"
INCREMENTA_PC_1 = "UPDATE contagem_ip SET dado_PC_1 = dado_PC_1 + 1 WHERE id = 1;"
INCREMENTA_PC_2 = "UPDATE contagem_ip SET dado_PC_2 = dado_PC_2 + 1 WHERE id = 1;"
INCREMENTA_PC_3 = "UPDATE contagem_ip SET dado_PC_3 = dado_PC_2 + 1 WHERE id = 1;"
ATUALIZAR_SOMA = "UPDATE contagem_ip SET soma_IP = dado_PC_1 + dado_PC_2 + dado_PC_3 WHERE id = 1;"
ZERA_CONTAGEM_IP = "UPDATE contagem_ip SET zera_IP = soma_IP;"


tentativas_maximas=5
intervalo_entre_tentativas=1

def criar_conexao():
    """
    Função para criar uma conexão com o banco de dados SQLite.

    Retorna:
        conn: Objeto de conexão com o banco de dados.
    """
    try:
        conn = sqlite3.connect(ARQUIVO_BD)
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao criar conexão com o banco de dados: {e}")
        return None


def criar_tabela(conn):
    """
    Função para criar a tabela 'contagem_ip' no banco de dados, se ela não existir.

    Parâmetros:
        conn: Objeto de conexão com o banco de dados.
    """
    try:
        cursor = conn.cursor()

        # Verificando se a tabela já existe
        cursor.execute(VERIFICAR_TABELA)
        tabela_existe = cursor.fetchone() is not None

        if not tabela_existe:
            # Criando a tabela se ela não existir
            cursor.execute(CRIAR_TABELA)
            print("Tabela 'contagem_ip' criada com sucesso!")
        else:
            print("Tabela 'contagem_ip' já existe.")
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela: {e}")


def atualizar_info(dado_1, dado_2, dado_3, soma_ip, zera_ip):
    """
    Função para inserir informações nas três primeiras colunas da tabela 'contagem_ip'.
    """
    try:
        conn = criar_conexao()
        if conn:
            # criar_tabela(conn)  # Chamada para criar a tabela
            with conn:
                conn.execute(ATUALIZAR_INFO_INICIAL, (dado_1, dado_2, dado_3, soma_ip, zera_ip))
    except sqlite3.Error as e:
        print(f"Erro atualizar_info: {e}")



def inserir_info_inicial(dado_1, dado_2, dado_3, soma_ip, zera_ip):
    """
    Função para inserir informações nas três primeiras colunas da tabela 'contagem_ip'.
    """

    for tentativa in range(tentativas_maximas):  # Utilize as variáveis definidas na função `atualizar_dado`
        try:
            # Tentativa de atualização
            conn = criar_conexao()
            if conn:
                # criar_tabela(conn)  # Chamada para criar a tabela
                with conn:
                    conn.execute(INSERIR_INFO_INICIAL, (dado_1, dado_2, dado_3, soma_ip, zera_ip))
                    conn.commit()  # Confirma as alterações
                    print(f"Todas as colunas atualizadas com sucesso na tentativa {tentativa + 1}!")
                return
            else:
                print("Falha ao conectar ao banco de dados")
        except sqlite3.Error as e:
            print(f"Erro na tentativa {tentativa + 1}: {e}")
            if tentativa < tentativas_maximas - 1:
                time.sleep(intervalo_entre_tentativas)  # Aguarda antes da próxima tentativa
            else:
                raise  # Propaga o erro na última tentativa

    print(f"Falha na inserir_info_inicial após {tentativas_maximas} tentativas.")


def atualizar_dado(data, pc):
    """
    Função para atualizar a informação do Script 2 na segunda coluna da tabela 'contagem_ip'.
    """
    for tentativa in range(tentativas_maximas):
        try:
            # Tentativa de atualização
            conn = criar_conexao()
            if conn:
                # criar_tabela(conn)  # Chamada para criar a tabela
                with conn:
                    match pc:
                        case 1:
                            conn.execute(ATUALIZAR_DADO_PC_1, (data,))
                        case 2:
                            conn.execute(ATUALIZAR_DADO_PC_2, (data,))
                        case 3:
                            conn.execute(ATUALIZAR_DADO_PC_3, (data,))
                        case _:
                            print(f'A T E N Ç Ã O Computador fora da faixa: {pc}')

                    conn.commit()  # Confirma as alterações
                print(f"Dados atualizados com sucesso na tentativa {tentativa + 1}!")
                return  # Retorna caso a atualização seja bem-sucedida
            else:
                print("Falha ao conectar ao banco de dados")
        except sqlite3.Error as e:
            print(f"Erro na tentativa {tentativa + 1}: {e}")
            if tentativa < tentativas_maximas - 1:
                time.sleep(intervalo_entre_tentativas)  # Aguarda antes da próxima tentativa
            else:
                raise  # Propaga o erro na última tentativa

    print(f"Falha na atualizar_dado após {tentativas_maximas} tentativas.")


def incrementa_dado(pc):
    """
    Função para incrementar a informação da tabela'contagem_ip' referente a contagem de cada computador.
    """
    for tentativa in range(tentativas_maximas):
        try:
            # Tentativa de atualização
            conn = criar_conexao()
            if conn:
                # criar_tabela(conn)  # Chamada para criar a tabela
                with conn:
                    match pc:
                        case 1:
                            conn.execute(INCREMENTA_PC_1)
                            conn.commit()  # Confirma as alterações
                        case 2:
                            conn.execute(INCREMENTA_PC_2)
                            conn.commit()  # Confirma as alterações
                        case 3:
                            conn.execute(INCREMENTA_PC_3)
                            conn.commit()  # Confirma as alterações
                        case _:
                            print(f'A T E N Ç Ã O Computador fora da faixa: {pc}')

                    conn.commit()  # Confirma as alterações
                print(f"Dados atualizados com sucesso na tentativa {tentativa + 1}!")
                return  # Retorna caso a atualização seja bem-sucedida
            else:
                print("Falha ao conectar ao banco de dados")
        except sqlite3.Error as e:
            print(f"Erro na tentativa {tentativa + 1}: {e}")
            if tentativa < tentativas_maximas - 1:
                time.sleep(intervalo_entre_tentativas)  # Aguarda antes da próxima tentativa
            else:
                raise  # Propaga o erro na última tentativa

    print(f"Falha na incrementa_dado após {tentativas_maximas} tentativas.")


def atualizar_soma_ip():
    """
    Função para atualizar a quarta coluna da tabela 'contagem_ip', que é a soma das três primeiras colunas.
    """
    for tentativa in range(tentativas_maximas):  # Utilize as variáveis definidas na função `atualizar_dado`
        try:
            # Tentativa de atualização
            conn = criar_conexao()
            if conn:
                # criar_tabela(conn)  # Chamada para criar a tabela
                with conn:
                    conn.execute(ATUALIZAR_SOMA)
                    conn.commit()  # Confirma as alterações
                print(f"Coluna de soma atualizada com sucesso na tentativa {tentativa + 1}!")
                return
            else:
                print("Falha ao conectar ao banco de dados")
        except sqlite3.Error as e:
            print(f"Erro na tentativa {tentativa + 1}: {e}")
            if tentativa < tentativas_maximas - 1:
                time.sleep(intervalo_entre_tentativas)  # Aguarda antes da próxima tentativa
            else:
                raise  # Propaga o erro na última tentativa

    print(f"Falha na atualizar_soma_ip após {tentativas_maximas} tentativas.")


def zera_contagem_ip():
    """
    Função para atualizar a quinta coluna da tabela 'contagem_ip', que é responsavel por zera a contagem de ip.
    """
    for tentativa in range(tentativas_maximas):  # Utilize as variáveis definidas na função `atualizar_dado`
        try:
            # Tentativa de atualização
            conn = criar_conexao()
            if conn:
                # criar_tabela(conn)  # Chamada para criar a tabela
                with conn:
                    conn.execute(ATUALIZAR_SOMA)
                    conn.commit()
                    conn.execute(ZERA_CONTAGEM_IP)
                    conn.commit()  # Confirma as alterações
                print(f"Coluna de soma atualizada com sucesso na tentativa {tentativa + 1}!")
                return
            else:
                print("Falha ao conectar ao banco de dados")
        except sqlite3.Error as e:
            print(f"Erro na tentativa {tentativa + 1}: {e}")
            if tentativa < tentativas_maximas - 1:
                time.sleep(intervalo_entre_tentativas)  # Aguarda antes da próxima tentativa
            else:
                raise  # Propaga o erro na última tentativa

    print(f"Falha na zera_contagem_ip após {tentativas_maximas} tentativas.")


def visualizar_tabela():
    """
    Função para visualizar toda a tabela 'contagem_ip'.
    """
    for tentativa in range(tentativas_maximas):  # Utilize as variáveis definidas na função `atualizar_dado`
        try:
            # Tentativa de visualização
            conn = criar_conexao()
            if conn:
                # criar_tabela(conn)  # Chamada para criar a tabela
                with conn:
                    conn.execute(ATUALIZAR_SOMA)
                    conn.commit()  # Confirma as alterações
                    cursor = conn.execute(SELECIONAR_INFO_LINHA_1)
                    primeira_linha = cursor.fetchall()[0]  # obtem a tupla da primeira linha na lista de linhas
                print(primeira_linha)
                return primeira_linha  # Retorna a lista de linhas
            else:
                print("Falha ao conectar ao banco de dados")

        except sqlite3.Error as e:
            print(f"Erro na tentativa {tentativa + 1}: {e}")
            if tentativa < tentativas_maximas - 1:
                time.sleep(intervalo_entre_tentativas)  # Aguarda antes da próxima tentativa
            else:
                raise  # Propaga o erro na última tentativa

    print(f"Falha na visualizar_tabela após {tentativas_maximas} tentativas.")
    return None  # Retorna `None` em caso de falha após todas as tentativas


def limpar_tabela():
    """
    Função para limpar toda a tabela 'contagem_ip'.
    """
    try:
        conn = criar_conexao()
        if conn:
            with conn:
                conn.execute("DELETE FROM contagem_ip")
            print("Tabela 'contagem_ip' limpa com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao limpar tabela: {e}")


# Exemplo de como usar as funções definidas acima
if __name__ == "__main__":
    # conn = criar_conexao()
    # criar_tabela(conn)
    # Script 1
    # inserir_info_inicial(0, 0, 0, 0, 0)
    # atualizar_info(0, 0, 0, 0, 0)
    # atualizar_dado(40, 3)
    # atualizar_dado(40, 2)
    # atualizar_dado(40, 1)
    # zera_contagem_ip()
    # atualizar_soma_ip()

    incrementa_dado(1)
    incrementa_dado(2)
    incrementa_dado(3)
    # zera_contagem_ip()

    #

    # Limpar tabela
    # limpar_tabela()
    dados = visualizar_tabela()
