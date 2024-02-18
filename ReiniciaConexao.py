import os
import time

import psutil
import pyautogui
import pygetwindow as gw
import pywinauto
import requests

conexao_x = 930
conexao_y = 710

# Título e nome da classe da janela que você deseja verificar
window_title = 'Configurações'
window_class = 'ApplicationFrameWindow'

precisao = 0.9

nome_usuario = os.getlogin()
print('nome de ususario: ', nome_usuario)

# Vero
telefone = fr"C:\Users\{nome_usuario}\PycharmProjects\CodigoPoker\Imagens\Conexao\telefone.png"
regiao_telefone = (conexao_x + 22, conexao_y + 109, 59, 56)
desconectar = fr"C:\Users\{nome_usuario}\PycharmProjects\CodigoPoker\Imagens\Conexao\desconectar.png"
regiao_desconectar = (conexao_x + 361, conexao_y + 185, 109, 36)
conectar = fr"C:\Users\{nome_usuario}\PycharmProjects\CodigoPoker\Imagens\Conexao\conectar.png"
regiao_conectar = (conexao_x + 124, conexao_y + 185, 92, 34)
conectado = fr"C:\Users\{nome_usuario}\PycharmProjects\CodigoPoker\Imagens\Conexao\conectado.png"
regiao_conectado = (conexao_x + 70, conexao_y + 133, 92, 34)
fechar = fr"C:\Users\{nome_usuario}\PycharmProjects\CodigoPoker\Imagens\Conexao\fechar.png"
regiao_fechar = (conexao_x + 380, conexao_y + 236, 91, 80)
cancelar = fr"C:\Users\{nome_usuario}\PycharmProjects\CodigoPoker\Imagens\Conexao\cancelar.png"
regiao_cancelar = (conexao_x + 358, conexao_y + 204, 111, 36)

# Modem
celular = fr"C:\Users\{nome_usuario}\PycharmProjects\CodigoPoker\Imagens\Conexao\celular.png"
regiao_celular = (conexao_x + 19, conexao_y + 261, 55, 22)
ativado = fr"C:\Users\{nome_usuario}\PycharmProjects\CodigoPoker\Imagens\Conexao\ativado.png"
desativado = fr"C:\Users\{nome_usuario}\PycharmProjects\CodigoPoker\Imagens\Conexao\desativado.png"
regiao_ativado_desativado = (conexao_x + 75, conexao_y + 292, 73, 22)

tipo_conexao = "modem"


print("Espera 5 minutos para testar a conexão")

time.sleep(300)

# Obtém a hora atual em segundos desde a época
hora_atual_em_segundos = time.time()

# Converte a hora atual em uma estrutura de tempo local
hora_local = time.localtime(hora_atual_em_segundos)

# Formata a hora local em uma string legível
hora_formatada = time.strftime("%H:%M:%S", hora_local)

# Imprime a hora formatada
print("Hora atual inicio:", hora_formatada)


def tem_internet():
    cont_erro2 = 0
    cont_erro = 0
    # print('tem_internet')

    com_internete = True
    while com_internete:
        print('testa a internete')
        cont_erro2 += 1
        # site_aleatorio = random.choice(sites)
        # print(site_aleatorio)
        try:
            # response = requests.get(site_aleatorio, timeout=10)
            response = requests.get('http://www.google.com', timeout=5)
            if response.status_code == 200 or response.status_code == 429:
                print("Conexão com a internet ativa!")
                cont_erro = 0
                cont_erro2 = 0
                com_internete = False
                return True

        except Exception as e:
            print("Sem conexão com a internet. Encerrando os testes...")
            print(e)
            time.sleep(3)
            cont_erro += 1
            print('contagem de erro 1: ', cont_erro)
            if cont_erro >= 5:
                cont_erro = 0
                cont_erro2 = 0
                conexao()  # chama a função que troca ip

        if cont_erro2 >= 20:
            cont_erro = 0
            cont_erro2 = 0
            conexao()  # chama a função que troca ip

        print('contagem de erro 1: ', cont_erro)
        print('contagem de erro 2: ', cont_erro2)
    return True


def conexao():
    print("Reinicia a conexão")

    while True:
        while True:
            # Tempo máximo para esperar (em segundos)
            tempo_passado = 0

            # Loop até que a janela esteja ativa ou o tempo máximo seja atingido
            while tempo_passado < 3:
                # Encontre a janela pelo título
                target_window = gw.getWindowsWithTitle("Configurações")

                # Verifique se a janela foi encontrada e está ativa
                if target_window and target_window[0].isActive:
                    print("Janela encontrada e ativa.")
                    break
                else:
                    print("Manda a jenela de conexao abrir")
                    if tipo_conexao == "vero":
                        os.system("start ms-settings:network-dialup")  # abre a conexão discada
                    elif tipo_conexao == "modem":
                        os.system("start ms-settings:network-airplanemode")  # modo aviao
                    else:
                        os.system("start ms-settings:network-airplanemode")  # modo aviao

                # Aguarde um curto período antes de verificar novamente
                time.sleep(0.2)
                tempo_passado += 0.2

            try:
                app = pywinauto.Application().connect(title=window_title, class_name=window_class)
                # A janela já está aberta, ative-a
                app_top_window = app.top_window()
                app_top_window.restore()
                app_top_window.move_window(x=conexao_x, y=conexao_y, width=500, height=330)
                # conexao_x = app_top_window.rectangle().left
                # conexao_y = app_top_window.rectangle().top
                app_top_window.set_focus()
                # Verifique se a janela está respondendo
                if app_top_window.is_active():
                    print("A janela está ativa.")
                    break
                time.sleep(0.5)
            except:
                # A janela não está aberta, abra-a
                target_window = gw.getWindowsWithTitle("Configurações")

                # Verifique se a janela foi encontrada
                if target_window:
                    # Feche a janela
                    target_window[0].close()
                    print("Janela configuraçoes ativa.")
                    time.sleep(1)
                else:
                    print("Janela não encontrada.")
                time.sleep(0.5)
                continue
        # time.sleep(0.5)
        if tipo_conexao == "vero":
            app_top_window.set_focus()
            print("conexão vero")
            cont_erro = 0
            clicou_conecar = False

            for _ in range(200):
                app_top_window.set_focus()
                posicao_telefone = localizar_imagem(telefone, regiao_telefone, precisao)
                if posicao_telefone is not None:
                    centro_discada = pyautogui.center(posicao_telefone)  # Obtém o centro da posição da imagem encontrada
                    pyautogui.click(centro_discada)  # Clica no centro da posição encontrada
                    print("clica no telefoen")

                    posicao_desconectar = localizar_imagem(desconectar, regiao_desconectar, precisao)
                    if posicao_desconectar is not None:
                        centro_desconectar = pyautogui.center(posicao_desconectar)  # Obtém o centro da posição da imagem encontrada
                        pyautogui.click(centro_desconectar)  # Clica no centro da posição encontrada
                        print("clica no desconectar")
                        time.sleep(2)

                    posicao_fechar = localizar_imagem(fechar, regiao_fechar, precisao)
                    if posicao_fechar is not None:
                        centro_fechar = pyautogui.center(posicao_fechar)  # Obtém o centro da posição da imagem encontrada
                        pyautogui.click(centro_fechar)  # Clica no centro da posição encontrada
                        print("clica no fechar 1")
                        time.sleep(2)

                    posicao_conectar = localizar_imagem(conectar, regiao_conectar, precisao)
                    if posicao_conectar is not None:
                        centro_conectar = pyautogui.center(posicao_conectar)  # Obtém o centro da posição da imagem encontrada
                        pyautogui.click(centro_conectar)  # Clica no centro da posição encontrada

                        print("clica no conectar")
                        time.sleep(2)
                        clicou_conecar = True
                        break
                time.sleep(0.3)

            if clicou_conecar:
                app_top_window.set_focus()
                for _ in range(200):
                    cont_erro += 1
                    posicao_conectado = localizar_imagem(conectado, regiao_conectado, precisao)
                    if posicao_conectado is not None:
                        print("Esta conectado")
                        # app_top_window.minimize()  # minimiza a janela
                        app_top_window.close()  # fecha a janela
                        return None

                    posicao_conectar = localizar_imagem(conectar, regiao_conectar, precisao)
                    if posicao_conectar is not None:
                        centro_conectar = pyautogui.center(posicao_conectar)  # Obtém o centro da posição da imagem encontrada
                        pyautogui.click(centro_conectar)  # Clica no centro da posição encontrada
                        print("clica no conectar 2")
                        time.sleep(2)

                    # se deu algum erro e nao conectou aparece um mensagem de erro e opção de fechar
                    posicao_fechar = localizar_imagem(fechar, regiao_fechar, precisao)
                    if posicao_fechar is not None:
                        cont_erro = 0
                        centro_fechar = pyautogui.center(posicao_fechar)  # Obtém o centro da posição da imagem encontrada
                        pyautogui.click(centro_fechar)  # Clica no centro da posição encontrada
                        print("clica no fechar 2")
                        time.sleep(2)

                    # se esta demorando muito para conectar clia em cancelar e tenta novamente
                    if cont_erro >= 60:
                        posicao_cancelar = localizar_imagem(cancelar, regiao_cancelar, precisao)
                        if posicao_cancelar is not None:
                            cont_erro = 0
                            centro_cancelar = pyautogui.center(posicao_cancelar)  # Obtém o centro da posição da imagem encontrada
                            pyautogui.click(centro_cancelar)  # Clica no centro da posição encontrada
                            time.sleep(2)
                    time.sleep(0.5)

        elif tipo_conexao == "modem":
            print('modem')

            for _ in range(400):
                app_top_window.set_focus()
                posicao_celular = localizar_imagem(celular, regiao_celular, precisao)
                if posicao_celular is not None:
                    centro_celular = pyautogui.center(posicao_celular)  # Obtém o centro da posição da imagem encontrada
                    posicao_botao = pyautogui.Point(centro_celular.x, centro_celular.y + 30)
                    posicao_ativado = localizar_imagem(ativado, regiao_ativado_desativado, precisao)
                    if posicao_ativado is not None:
                        time.sleep(0.3)
                        pyautogui.click(posicao_botao)  # Clica para desativar a coneção
                        print("foi desativado")
                        time.sleep(0.3)
                        for _ in range(50):
                            status = obter_status_conexao("Celular")
                            print('esperando desconectar')
                            if status == "Desconectado":
                                print(status)
                                time.sleep(0.5)
                                break
                            time.sleep(0.5)
                        app_top_window.set_focus()

                    posicao_desativado = localizar_imagem(desativado, regiao_ativado_desativado, precisao)
                    if posicao_desativado is not None:
                        pyautogui.click(posicao_botao)  # Clica para ativar a coneção
                        print("foi ativado")
                        for _ in range(100):
                            status = obter_status_conexao("Celular")
                            print('esperando conectar')
                            if status == "Conectado":
                                print(status)
                                # app_top_window.minimize()  # minimiza a janela
                                app_top_window.close()  # fecha a janela
                                return None
                            time.sleep(0.5)
                        app_top_window.set_focus()
                time.sleep(0.3)

        app_top_window.set_focus()
        app_top_window.close()  # fecha a janela
        print('Não consegiu realizar a abertura da janela de conexão para a troca de ip')
        time.sleep(1)


def localizar_imagem(imagem, regiao, precisao):
    try:
        posicao = pyautogui.locateOnScreen(imagem, region=regiao, confidence=precisao, grayscale=True)
        return posicao
    except Exception as e:
        print(e)
        print("Ocorreu um erro ao localizar a imagem")
        time.sleep(2)
        return None


def obter_status_conexao(nome_conexao):
    conexoes = psutil.net_if_stats()
    if nome_conexao in conexoes:
        status = conexoes[nome_conexao].isup
        if status:
            return "Conectado"
        else:
            return "Desconectado"
    else:
        time.sleep(1)
        return "Conexão não encontrada"


tem_internet()

# Obtém a hora atual em segundos desde a época
hora_atual_em_segundos = time.time()

# Converte a hora atual em uma estrutura de tempo local
hora_local = time.localtime(hora_atual_em_segundos)

# Formata a hora local em uma string legível
hora_formatada = time.strftime("%H:%M:%S", hora_local)

# Imprime a hora formatada
print("Hora atual fim:", hora_formatada)

# testar se o python esta intalado:
# python --version
# instalar via CMD:
# python.exe -m pip install --upgrade pip
# pip install psutil
# pip install pyautogui
# pip install pywinauto
# pip install PyScreeze==0.1.29
# pip install opencv-python
# pip install Pillow
# pip install requests
