"""Verificar se o ADB está instalado corretamente
Certifique-se de que o ADB está instalado e funcionando. Para verificar, abra o Prompt de Comando e digite:

bash
Copiar código
adb version
Se o ADB estiver instalado corretamente, ele mostrará a versão. Caso contrário, você precisará instalar o ADB seguindo os passos que mencionei anteriormente.

2. Adicionar o ADB ao PATH
Se o ADB estiver instalado, mas o erro continuar, é provável que o caminho do ADB não tenha sido adicionado ao PATH. Aqui está como corrigir isso:

Passo 1: Adicionar o ADB ao PATH
Localize a pasta onde o ADB foi instalado/extrado. Por exemplo: C:\GitHub\BotPoker\platform-tools.
Clique com o botão direito em Este PC (ou Meu Computador) e selecione Propriedades.
Vá em Configurações Avançadas do Sistema e clique em Variáveis de Ambiente.
Encontre a variável Path em Variáveis do Sistema e clique em Editar.
Clique em Novo e adicione o caminho da pasta onde o ADB está (exemplo: C:\GitHub\BotPoker\platform-tools).
Clique em OK para fechar todas as janelas.
Passo 2: Verificar o ADB novamente
Abra um novo Prompt de Comando e verifique se o ADB funciona corretamente:
adb version
adb shell dumpsys activity activities # descobrir o nome da tela ativa

"""

import subprocess
import time

caminho_adb = r"platform-tools\adb.exe"  # Caminho para o adb


def dispositivo_conectado():
    """Verifica se um dispositivo está conectado via ADB."""
    try:
        resultado = subprocess.run([caminho_adb, "devices"], capture_output=True, text=True)
        if "device" in resultado.stdout.splitlines()[1]:  # Verifica se o dispositivo está na lista
            print("Dispositivo conectado.")
            return True
        else:
            print("Nenhum dispositivo conectado.")
            return False
    except Exception as erro:
        print(f"Erro ao verificar conexão com o dispositivo: {erro}")
        time.sleep(5)
        return False


def abrir_tela_tethering():
    """
    Abre a tela de configurações de compartilhamento de internet via USB no dispositivo Android.
    """
    try:
        # Comando para abrir a tela de configurações de compartilhamento de internet via USB
        comando = [caminho_adb, "shell", "am", "start", "-n", "com.android.settings/.TetherSettings"]

        # Executa o comando
        resultado = subprocess.run(comando, capture_output=True, text=True)

        if resultado.returncode == 0:
            print("Tela de configurações de compartilhamento de internet via USB aberta com sucesso.")
        else:
            print(f"Erro ao abrir a tela de configurações de compartilhamento de internet via USB: {resultado.stderr}")

    except Exception as e:
        print(f"Erro inesperado: {e}")
        time.sleep(5)


def ligar_ou_desligar_tela(acionar=True):
    """
    Liga ou desliga a tela do dispositivo Android.
    :param acionar: True para ligar a tela, False para desligar a tela.
    """
    try:
        if acionar:
            subprocess.run([caminho_adb, "shell", "input", "keyevent", "KEYCODE_WAKEUP"], check=True)
            print("Tela ligada.")
        else:
            subprocess.run([caminho_adb, "shell", "input", "keyevent", "KEYCODE_SLEEP"], check=True)
            print("Tela desligada.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao {'ligar' if acionar else 'desligar'} a tela: {e}")
        time.sleep(5)
    except Exception as e:
        print(f"Erro inesperado: {e}")
        time.sleep(5)


def clicar_em_coordenada(x, y):
    """
    Simula um clique na coordenada (x, y) da tela do celular.
    :param x: Coordenada X onde o clique deve ser simulado.
    :param y: Coordenada Y onde o clique deve ser simulado.
    """
    try:
        # Comando adb para simular um toque na coordenada (x, y)
        subprocess.run([caminho_adb, "shell", "input", "tap", str(x), str(y)], check=True)
        print(f"Clique simulado nas coordenadas ({x}, {y}).")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao simular clique: {e}")
        time.sleep(5)
    except Exception as e:
        print(f"Erro inesperado: {e}")
        time.sleep(5)


def alterar_modo_aviao(ativado):
    """Ativa ou desativa o modo avião com root."""
    if not dispositivo_conectado():
        print("Falha: Dispositivo não está conectado via ADB.")
        return

    try:
        if ativado:
            print("Ativando modo avião...")
            subprocess.run([caminho_adb, "shell", "su", "-c", "settings put global airplane_mode_on 1"], check=True)
            subprocess.run([caminho_adb, "shell", "su", "-c", "am broadcast -a android.intent.action.AIRPLANE_MODE --ez state true"], check=True)
        else:
            print("Desativando modo avião...")
            subprocess.run([caminho_adb, "shell", "su", "-c", "settings put global airplane_mode_on 0"], check=True)
            subprocess.run([caminho_adb, "shell", "su", "-c", "am broadcast -a android.intent.action.AIRPLANE_MODE --ez state false"], check=True)

        print(f"Modo avião {'ativado' if ativado else 'desativado'} com sucesso.")
    except subprocess.CalledProcessError as erro:
        print(f"Erro ao executar comando: {erro}")
        time.sleep(5)
    except Exception as erro:
        print(f"Erro inesperado: {erro}")
        time.sleep(5)


def is_modo_aviao_ativo():
    """Verifica se o modo avião está ativo."""
    try:
        # Comando para verificar o estado do modo avião
        resultado = subprocess.run([caminho_adb, "shell", "settings", "get", "global", "airplane_mode_on"], capture_output=True, text=True)

        # Verifica se o valor retornado é '1' (ativo) ou '0' (desativado)
        if resultado.stdout.strip() == "1":
            print("Modo avião está ativo.")
            return True
        else:
            print("Modo avião está desativado.")
            return False
    except Exception as e:
        print(f"Erro ao verificar o estado do modo avião: {e}")
        time.sleep(5)
        return False


def abrir_barra_botoes_rapidos():
    """
    Abre a barra de botões rápidos (configurações rápidas) no dispositivo Android.
    """
    try:
        subprocess.run([caminho_adb, "shell", "cmd", "statusbar", "expand-settings"], check=True)
        print("Barra de botões rápidos aberta com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao abrir a barra de botões rápidos: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Exemplo de uso
# ligar_ou_desligar_tela(True)  # Liga a tel
# time.sleep(2)  # Aguarda 5 segundos
# alterar_modo_aviao(False)  # Desativar modo avião
# time.sleep(2)  # Aguarda 5 segundos
# abrir_tela_tethering()
# time.sleep(2)  # Aguarda 5 segundos
# clicar_em_coordenada(500, 400)  # Ajuste as coordenadas conforme necessário

# is_modo_aviao_ativo()
# alterar_modo_aviao(True)  # Ativar modo avião
# alterar_modo_aviao(False)  # Desativar modo avião
# is_modo_aviao_ativo()


# # Exemplo de uso
# is_usb_tethering_active()
# set_usb_tethering(1)  # ativar o compartilhamento usb de internet
# is_modo_aviao_ativo()
# alterar_modo_aviao(True)  # Ativar modo avião
# alterar_modo_aviao(False)  # Desativar modo avião
# is_modo_aviao_ativo()
