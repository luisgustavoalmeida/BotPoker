import sqlite3

ARQUIVO_BD = 'tabele_ip.db'
CRIAR_TABELA_QUERY = '''CREATE TABLE IF NOT EXISTS contagem_ip (
                            id INTEGER PRIMARY KEY,
                            dado_PC_1 INTEGER,
                            dado_PC_2 INTEGER,
                            dado_PC_3 INTEGER,
                            soma_IP INTEGER,
                            dado_coluna_cinco TEXT
                        )'''
INSERIR_INFO_QUERY = "UPDATE contagem_ip SET (dado_PC_1, dado_PC_2, dado_PC_3) VALUES (?, ?, ?)"
SELECIONAR_TODAS_INFO_QUERY = "SELECT * FROM contagem_ip"
ATUALIZAR_DADO_PC_1 = "UPDATE contagem_ip SET dado_PC_1 = ?"
ATUALIZAR_DADO_PC_2 = "UPDATE contagem_ip SET dado_PC_2 = ?"
ATUALIZAR_DADO_PC_3 = "UPDATE contagem_ip SET dado_PC_3 = ?"
ATUALIZAR_SOMA_QUERY = "UPDATE contagem_ip SET soma_dos_tres_primeiros = dado_PC_1 + dado_PC_2 + dado_PC_3"
ATUALIZAR_DADO_COLUNA_CINCO_QUERY = "UPDATE contagem_ip SET dado_coluna_cinco = ?"


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
        cursor.execute(CRIAR_TABELA_QUERY)
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela: {e}")


def inserir_info_dos_3_computadores(dado_1, dado_2, dado_3):
    """
    Função para inserir informações nas três primeiras colunas da tabela 'contagem_ip'.

    Parâmetros:
        dado_script_um: Informação numérica do script 1.
        dado_script_dois: Informação do script 2.
        dado_script_tres: Informação do script 3.
    """
    try:
        conn = criar_conexao()
        if conn:
            criar_tabela(conn)  # Chamada para criar a tabela
            with conn:
                conn.execute(INSERIR_INFO_QUERY, (dado_1, dado_2, dado_3))
    except sqlite3.Error as e:
        print(f"Erro ao inserir informação: {e}")
    finally:
        if conn:
            conn.close()
            
    with sqlite3.connect(ARQUIVO_BD) as conexao:  # Conexão aberta automaticamente
        cursor = conexao.cursor()
        cursor.execute(ATUALIZAR_DADO_PC_1, (dado_1, dado_2, dado_3))
        conexao.commit()  # Transação confirmada antes do fechamento
        print(f"Dado do Script 1 atualizado para: {novo_dado}")


def atualizar_dado_script_um(novo_dado):
    """
    Função para atualizar o valor do Script 1 na tabela 'contagem_ip'.

    Parâmetros:
        novo_dado: Novo valor do Script 1.
    """
    with sqlite3.connect(ARQUIVO_BD) as conexao:  # Conexão aberta automaticamente
        cursor = conexao.cursor()
        cursor.execute(ATUALIZAR_DADO_PC_1, (novo_dado,))
        conexao.commit()  # Transação confirmada antes do fechamento
        print(f"Dado do Script 1 atualizado para: {novo_dado}")


def atualizar_dado_script_dois(data):
    """
    Função para atualizar a informação do Script 2 na segunda coluna da tabela 'contagem_ip'.

    Parâmetros:
        data: Nova informação do Script 2.
    """
    try:
        conn = criar_conexao()
        if conn:
            criar_tabela(conn)  # Chamada para criar a tabela
            with conn:
                conn.execute(ATUALIZAR_DADO_PC_2, (data,))
    except sqlite3.Error as e:
        print(f"Erro ao atualizar dado do Script 2: {e}")
    finally:
        if conn:
            conn.close()


def atualizar_dado_script_tres(data):
    """
    Função para atualizar a informação do Script 3 na terceira coluna da tabela 'contagem_ip'.

    Parâmetros:
        data: Nova informação do Script 3.
    """
    try:
        conn = criar_conexao()
        if conn:
            criar_tabela(conn)  # Chamada para criar a tabela
            with conn:
                conn.execute(ATUALIZAR_DADO_PC_3, (data,))
    except sqlite3.Error as e:
        print(f"Erro ao atualizar dado do Script 3: {e}")
    finally:
        if conn:
            conn.close()


def atualizar_soma_coluna():
    """
    Função para atualizar a quarta coluna da tabela 'contagem_ip', que é a soma das três primeiras colunas.
    """
    try:
        conn = criar_conexao()
        if conn:
            criar_tabela(conn)  # Chamada para criar a tabela
            with conn:
                conn.execute(ATUALIZAR_SOMA_QUERY)
    except sqlite3.Error as e:
        print(f"Erro ao atualizar coluna de soma: {e}")
    finally:
        if conn:
            conn.close()


def atualizar_dado_coluna_cinco(data):
    """
    Função para atualizar a quinta coluna da tabela 'contagem_ip'.

    Parâmetros:
        data: Nova informação da quinta coluna.
    """
    try:
        conn = criar_conexao()
        if conn:
            criar_tabela(conn)  # Chamada para criar a tabela
            with conn:
                conn.execute(ATUALIZAR_DADO_COLUNA_CINCO_QUERY, (data,))
    except sqlite3.Error as e:
        print(f"Erro ao atualizar dado da coluna cinco: {e}")
    finally:
        if conn:
            conn.close()


def visualizar_tabela():
    """
    Função para visualizar toda a tabela 'contagem_ip'.
    """
    try:
        conn = criar_conexao()
        if conn:
            criar_tabela(conn)  # Chamada para criar a tabela
            with conn:
                cursor = conn.execute(SELECIONAR_TODAS_INFO_QUERY)
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
    except sqlite3.Error as e:
        print(f"Erro ao visualizar tabela: {e}")
    finally:
        if conn:
            conn.close()


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
    finally:
        if conn:
            conn.close()


# Exemplo de como usar as funções definidas acima
if __name__ == "__main__":
    # Script 1
    inserir_info_dos_3_computadores(1, 2, 3)
    # atualizar_dado_script_um(2)
    # atualizar_soma_coluna()
    # atualizar_dado_coluna_cinco('Dado da coluna cinco do Script 1')
    #
    # # Script 2
    # atualizar_dado_script_dois('Dado atualizado do Script 2')
    #
    # # Script 3
    # atualizar_dado_script_tres('Dado atualizado do Script 3')
    #
    # # Visualizar tabela
    # visualizar_tabela()

    # Limpar tabela
    # limpar_tabela()
