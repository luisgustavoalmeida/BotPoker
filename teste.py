import sqlite3

ARQUIVO_BD = 'shared_data.db'
CRIAR_TABELA_QUERY = '''CREATE TABLE IF NOT EXISTS contagem_ip (
                            id INTEGER PRIMARY KEY,
                            dado_script_um INTEGER,
                            dado_script_dois TEXT,
                            dado_script_tres TEXT,
                            soma_dos_tres_primeiros INTEGER,
                            dado_coluna_cinco TEXT
                        )'''
INSERIR_INFO_QUERY = "INSERT INTO contagem_ip (dado_script_um, dado_script_dois, dado_script_tres) VALUES (?, ?, ?)"
SELECIONAR_TODAS_INFO_QUERY = "SELECT * FROM contagem_ip"
ATUALIZAR_DADO_SCRIPT_UM_QUERY = "UPDATE contagem_ip SET dado_script_um = ?"
ATUALIZAR_DADO_SCRIPT_DOIS_QUERY = "UPDATE contagem_ip SET dado_script_dois = ?"
ATUALIZAR_DADO_SCRIPT_TRES_QUERY = "UPDATE contagem_ip SET dado_script_tres = ?"
ATUALIZAR_SOMA_QUERY = "UPDATE contagem_ip SET soma_dos_tres_primeiros = dado_script_um + dado_script_dois + dado_script_tres"
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


def inserir_info(dado_script_um, dado_script_dois, dado_script_tres):
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
                conn.execute(INSERIR_INFO_QUERY, (dado_script_um, dado_script_dois, dado_script_tres))
    except sqlite3.Error as e:
        print(f"Erro ao inserir informação: {e}")
    finally:
        if conn:
            conn.close()


def atualizar_dado_script_um(data):
    """
    Função para atualizar a informação do Script 1 na primeira coluna da tabela 'contagem_ip'.

    Parâmetros:
        data: Nova informação do Script 1.
    """
    try:
        conn = criar_conexao()
        if conn:
            criar_tabela(conn)  # Chamada para criar a tabela
            with conn:
                conn.execute(ATUALIZAR_DADO_SCRIPT_UM_QUERY, (data,))
    except sqlite3.Error as e:
        print(f"Erro ao atualizar dado do Script 1: {e}")
    finally:
        if conn:
            conn.close()


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
                conn.execute(ATUALIZAR_DADO_SCRIPT_DOIS_QUERY, (data,))
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
                conn.execute(ATUALIZAR_DADO_SCRIPT_TRES_QUERY, (data,))
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
    inserir_info(10, 'Dado do Script 2', 'Dado do Script 3')
    atualizar_dado_script_um(10)
    atualizar_soma_coluna()
    atualizar_dado_coluna_cinco('Dado da coluna cinco do Script 1')

    # Script 2
    atualizar_dado_script_dois('Dado atualizado do Script 2')

    # Script 3
    atualizar_dado_script_tres('Dado atualizado do Script 3')

    # Visualizar tabela
    visualizar_tabela()

    # Limpar tabela
    limpar_tabela()
