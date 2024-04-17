import os


def inicializa_cmd_novo():
    arquivo_bat = r'Fechar_CMD.bat'  # Substitua pelo caminho do seu arquivo

    try:
        os.system(arquivo_bat)  # Utilize o os.system para executar o arquivo .bat diretamente
    except Exception as e:
        print(f"Erro ao executar o arquivo .bat: {e}")
    else:
        print("Arquivo .bat executado com sucesso!")


inicializa_cmd_novo()  # Chame a função para executar o arquivo .bat
