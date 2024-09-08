"""Verificar se o ADB está instalado corretamente
Certifique-se de que o ADB está instalado e funcionando. Para verificar, abra o Prompt de Comando e digite:

bash
Copiar código
adb version
Se o ADB estiver instalado corretamente, ele mostrará a versão. Caso contrário, você precisará instalar o ADB seguindo os passos que mencionei anteriormente.

2. Adicionar o ADB ao PATH
Se o ADB estiver instalado, mas o erro continuar, é provável que o caminho do ADB não tenha sido adicionado ao PATH. Aqui está como corrigir isso:

Passo 1: Adicionar o ADB ao PATH
Localize a pasta onde o ADB foi instalado/extrado. Por exemplo: C:\platform-tools.
Clique com o botão direito em Este PC (ou Meu Computador) e selecione Propriedades.
Vá em Configurações Avançadas do Sistema e clique em Variáveis de Ambiente.
Encontre a variável Path em Variáveis do Sistema e clique em Editar.
Clique em Novo e adicione o caminho da pasta onde o ADB está (exemplo: C:\platform-tools).
Clique em OK para fechar todas as janelas.
Passo 2: Verificar o ADB novamente
Abra um novo Prompt de Comando e verifique se o ADB funciona corretamente:
adb version

"""

import subprocess

caminho_adb = r"C:\platform-tools\adb.exe"  # Caminho para o adb


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
        return False


def set_usb_tethering(ativar):
    """
    Ativa ou desativa o USB Tethering com root.
    :param ativar: '1' para ativar, '0' para desativar.
    """
    if not dispositivo_conectado():
        print("Falha: Dispositivo não está conectado via ADB.")
        return

    if ativar not in ["1", "0"]:
        raise ValueError("O estado deve ser '1' para ativar ou '0' para desativar.")

    try:
        # Comando para ativar ou desativar o USB tethering
        subprocess.run([caminho_adb, "shell", "su", "-c", f"service call connectivity 34 i32 {ativar}"], check=True)
        print(f"Tethering USB {'ativado' if ativar == '1' else 'desativado'}.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao alterar o estado do tethering USB: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


def is_usb_tethering_active():
    """
    Verifica se o USB Tethering está ativo.
    :return: True se o tethering USB estiver ativo, False caso contrário.
    """
    if not dispositivo_conectado():
        print("Falha: Dispositivo não está conectado via ADB.")
        return False

    try:
        # Executa o comando para obter o status do tethering
        result = subprocess.run([caminho_adb, "shell", "dumpsys", "connectivity"], capture_output=True, text=True)

        # Verifica se há a string que indica que o tethering USB está ativo
        if "Tethering services" in result.stdout and "usbTethering: true" in result.stdout:
            print("Tethering USB está ativo.")
            return True
        else:
            print("Tethering USB não está ativo.")
            return False
    except Exception as e:
        print(f"Erro ao verificar o estado do tethering USB: {e}")
        return False


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
    except Exception as erro:
        print(f"Erro inesperado: {erro}")


# Exemplo de uso
set_usb_tethering(1)  # ativar o compartilhamento usb de internet
alterar_modo_aviao(True)  # Ativar modo avião
alterar_modo_aviao(False)  # Desativar modo avião
