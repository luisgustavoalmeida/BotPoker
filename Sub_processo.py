import os


def inicializa_cmd_novo():
    shortcut_path = r'Fechar_CMD.lnk'

    try:
        os.startfile(shortcut_path)
    except Exception as e:
        print(f"Erro ao executar o arquivo .bat: {e}")
    else:
        print("Arquivo .bat executado com sucesso!")
