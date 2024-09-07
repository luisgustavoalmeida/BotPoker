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
import time
adb_path = r"C:\platform-tools\adb.exe"  # Substitua pelo caminho correto onde o adb está instalado
def set_airplane_mode(enabled):

    if enabled:
        # Ativar modo avião
        subprocess.run([adb_path, "shell", "settings", "put", "global", "airplane_mode_on", "1"])
        subprocess.run([adb_path, "shell", "am", "broadcast", "-a", "android.intent.action.AIRPLANE_MODE", "--ez", "state", "true"])
    else:
        # Desativar modo avião
        subprocess.run([adb_path, "shell", "settings", "put", "global", "airplane_mode_on", "0"])
        subprocess.run([adb_path, "shell", "am", "broadcast", "-a", "android.intent.action.AIRPLANE_MODE", "--ez", "state", "false"])

# Exemplo de uso
# set_airplane_mode(True)  # Coloca em modo avião
# set_airplane_mode(False)  # Remove do modo avião


def toggle_airplane_mode():
    # Desliza a barra de notificações para baixo (ajuste as coordenadas conforme necessário)
    subprocess.run([adb_path, "shell", "input", "swipe", "500", "0", "500", "1000"])

    # Aguarda um breve momento para a animação da barra de notificações ser concluída
    time.sleep(1)

    # Simula um toque no ícone de modo avião (substitua x e y pelas coordenadas corretas do botão de modo avião)
    # subprocess.run([adb_path, "shell", "input", "tap", "x", "y"])


# Exemplo de uso
toggle_airplane_mode()