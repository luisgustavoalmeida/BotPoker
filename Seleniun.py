import datetime
import os
import socket
import time

import pyautogui
import pygetwindow as gw
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

import Google
import IP

# Desabilitar o fail-safe
pyautogui.FAILSAFE = False

# def criar_drive():
# servico = Service(ChromeDriverManager().install())  # criar um objeto Service com o caminho do webdriver

nome_computador = socket.gethostname()
nome_usuario = os.getlogin()
pasta_cookies = os.path.join(os.getcwd(), fr'C:\Cookie\{nome_usuario}')

options = Options()  # Criar um objeto 'Options' para definir as opções do Chrome
# options.add_argument("user-data-dir=C:\\Users\\lgagu\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1") # Você pode encontrar o caminho digitando "chrome://version/" na barra de endereço do Google Chrome e procurando o valo
options.add_argument('--disable-blink-features=AutomationControlled')  # desabilitam a detecção de automação no Chrome
options.add_argument("--disable-save-password-bubble")  # desabilitará a caixa de diálogo para salvar senhas do navegador
# options.add_argument("--disable-extensions")  # Desabilitar as extensões do Chrome
options.add_argument("--disable-infobars")  # Desabilitar a barra de informações do Chrome
options.add_argument("--disable-notifications")  # Desabilitar as notificações do Chrome
options.add_argument("--disable-save-password-bubble")  # Desabilitar a caixa de diálogo para salvar senhas
options.add_argument("--disable-password-generation")  # desabilita a geração automática de senhas pelo navegado
# options.add_argument('--disable-cookies') # desabilita o envio de cookies durante a navegação.
# options.add_argument('--disable-first-party-cookies') # Desativa o uso de cookies de primeira parte.
# options.add_argument('--disable-third-party-cookies') # Desativa o uso de cookies de terceiros.
# options.add_argument('--block-new-cookie-requests') # Bloqueia solicitações de criação de novos cookies.
# options.add_argument("--enable-cookies") # abilita o envio de cookies durante a navegação.
options.add_argument(f"--user-data-dir={pasta_cookies}")
# options.add_argument("--user-data-dir=/path/to/empty/folder") # Especifica um diretório vazio para a coleta de cookies. Isso permite que você utilize cookies pré-existentes ou salve os cookies gerados durante a execução do script.
options.add_argument("--disable-autofill")  # desabilitará o recurso de preenchimento automático de formulários do navegador.
options.add_argument("--disable-geolocation")  # desativar a funcionalidade de localização do navegador durante a execução do script Selenium
options.add_argument("--window-size=1380,1050")  # Definir o tamanho da janela # largura altura options.add_argument("--window-size=1440,1045")
options.add_argument("--window-position=-8,-5")  # Mover a janela para a posição (0,0) da tela
options.add_argument("--mute-audio")  # desativar o áudio
# options.add_argument("--disable-extensions")
# options.add_argument("--disable-gpu") # Desabilita o uso da GPU pelo navegador.
# options.add_argument("--disable-translate") # Desabilita a tradução automática de páginas pelo navegador

# options.add_argument("--disable-local-storage") # Desabilita o uso de armazenamento local pelo navegador. Isso inclui o armazenamento de dados em cache e outros recursos relacionados a cookies.
# options.add_argument("--disable-session-storage") # Desabilita o uso de armazenamento de sessão pelo navegador. Isso inclui o armazenamento temporário de dados relacionados a sessões de navegação.

options.add_experimental_option("detach", True)  # para manter o navegador aberto

# options.add_argument("--headless")# faz com que o browser não abra durante o processo
# options.add_argument("--disable-popup-blocking")                            #desabilitar o bloqueio de pop-ups no Chrome. Quando o Selenium abre o navegador, por padrão, o bloqueio de pop-ups é habilitado
# options.add_experimental_option("excludeSwitches", ["enable-automation"])   # Adicionar uma opção experimental para desabilitar a mensagem "O Chrome está sendo controlado por um software de teste automatizado."
# options.add_experimental_option('useAutomationExtension', False)            # Adicionar uma opção experimental para desabilitar a extensão do WebDriver

# navegador = webdriver.Chrome(service=servico, options=options)  # Inicializar o driver do navegador
# print(navegador)

navegador = None
url = None
id = ''
senha = ''


def cria_nevegador():
    global navegador  # Referenciar a variável global
    while True:
        try:
            print('Criando o navegador')
            servico = Service(ChromeDriverManager().install())  # criar um objeto Service com o caminho do webdriver
            navegador = webdriver.Chrome(service=servico, options=options)  # Inicializar o driver do navegador
            navegador.set_page_load_timeout(80)  # Redefina o tempo limite para XX segundos
            print('Navegador criado com sucesso')
            return navegador
        except Exception as e:
            print("Erro ao criar o navegador:", e)
            time.sleep(1)
            fechar_janelas_chrome()
            print('Iniciando nova tentativa para criar o navegador')
            time.sleep(3)


def fechar_janelas_chrome():
    # Lista todas as janelas abertas
    janelas = gw.getWindowsWithTitle('Google Chrome')

    # Itera sobre as janelas do Google Chrome e fecha cada uma delas
    for janela in janelas:
        # Fecha a janela
        janela.close()
        print('Navegador fechado', janelas)
        # Aguarda um curto período de tempo para a janela fechar
        time.sleep(1)


def abrir_navegador(urli):
    global navegador, url  # Referenciar a variável global
    url = urli
    while True:
        print("abrir navegador")
        IP.tem_internet()
        try:
            print('coloca o url no navegador')
            navegador.get(url)
            # print('manda sair do facebook')
            # sair_face(url, navegador)
            return
        except Exception as e:
            print(f"Erro ao abrir o navegador: {e}")
            # navegador.quit()
            time.sleep(2)
            continue


def se_esta_lagado():
    global navegador
    # Especifique o nome do cookie associado ao estado de login do Facebook
    nome_cookie = "c_user"
    while True:
        try:
            # Obtém todos os cookies
            cookies = navegador.get_cookies()

            # Verifica se o cookie está presente
            for cookie in cookies:
                if cookie["name"] == nome_cookie:
                    print("Está logado no Facebook.")
                    return True

            print("Não está logado no Facebook.")
            return False
        except Exception as e:
            print("Erro ao obter o URL do navegador, erro: ", e)
            IP.tem_internet()


def pega_url():
    global navegador
    while True:
        IP.tem_internet()
        try:
            url_atual = navegador.current_url
            return url_atual
        except Exception as e:
            print("Erro ao obter o URL do navegador, erro: ", e)
            IP.tem_internet()
            print(" clica no atualizar a pagina, atualizar")
            # pyautogui.press('f5')
            # navegador.get(url)
            pyautogui.click(85, 60)
            time.sleep(15)


def teste_logado():
    url_atual = pega_url()
    if ("/pokerbrasil?" in url_atual) or ("/rallyacespoker" in url_atual):
        print("teste_logado: Esta logado corretamente.")
        entrou = True
        status = 'Carregada'
        return entrou, status

    elif ("/pokerbrasil?" not in url_atual) or ("/rallyacespoker" in url_atual):  # se nao esta logado
        print("teste_logado: Não esta logado!!!")
        # IP.tem_internet()
        entrou, status = fazer_login()
        return entrou, status


def fazer_login(id_novo='', senha_novo='', url_novo='', loga_pk=True):
    global navegador, url, id, senha

    if url != url_novo and url_novo != '':
        url = url_novo

    if id_novo != '':
        id = id_novo
        senha = senha_novo

    while True:

        if se_esta_lagado():
            sair_face(url)

        print("faz login")
        IP.tem_internet()
        print('continua login')
        url_atual = pega_url()

        print(url_atual)

        if (("/login/" in url_atual) and loga_pk) or (not loga_pk and ("facebook.com" in url_atual)):
            print('Padrao de URL poker')
            try:
                email_field = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
                email_field.clear()
                email_field.send_keys(id)
                password_field = navegador.find_element(By.NAME, 'pass')
                password_field.clear()
                password_field.send_keys(senha)
                # fazer login clicando no botão de login
                login_button = navegador.find_element(By.NAME, 'login')
                login_button.click()
                print('fez o login. iniciando teste de logado')
                for i in range(20):

                    for _ in range(100):
                        url_atual = pega_url()
                        if "/login/" not in url_atual:
                            break
                        time.sleep(0.02)

                    if "/login/" not in url_atual:

                        if ("/pokerbrasil?" in url_atual) or ("/rallyacespoker" in url_atual):
                            print('URL padrao correta')
                            # https://apps.facebook.com/pokerbrasil?vtype&amfmethod=appLinkFanPageAward&SignedParams=JrLALkSch1wuQxrULK6SWLAcpjTOb9Pmi5QvavvikU0.eyJhY3QiOiJmcCIsImZwX2FpZCI6IjU5ODUifQ&fbclid=IwAR252AFFL560939epg6Ki4tzNtLvgQJiZISVIZXFPjjBpBp5TNLBNX6TFXk
                            time.sleep(1)
                            lista_face = ['temporariamente', 'não está disponível no momento']
                            for item in lista_face:  # percorre os textos que tem quando tem conta caida para o face
                                try:
                                    elemento = navegador.find_element(By.XPATH, f"//span[contains(text(), '{item}')]")
                                    print(item)
                                    status = 'Bloqueado temporariamente'
                                    entrou = False
                                    return entrou, status
                                except NoSuchElementException:
                                    continue

                            print("A conta está certa.")
                            entrou = True
                            status = 'Carregada'
                            return entrou, status

                        elif "pokerbrasil/?ref=bookmarks" in url_atual:
                            # https://apps.facebook.com/pokerbrasil/?ref=bookmarks&count=0
                            print("A conta está certa.")
                            entrou = False
                            status = 'Bloqueado temporariamente'
                            return entrou, status

                        elif ("/settings?" in url_atual) and (not loga_pk):
                            # https://www.facebook.com/settings?tab=applications&ref=settings

                            print("A conta está com a pagina carregada diponivel para remover o poker")
                            entrou = True
                            treminou_de_remover = False
                            status = 'Remover Poker não ok'

                            # Aguarda até que o texto seja visível na página
                            texto_a_procurar = ["Você não tem nenhum app ou site para analisar", 'Não tens apps ou sites para rever']

                            for i in range(7):
                                pyautogui.click(914, 368)  # clique bobo, agora na central de contas
                                print("Tentativa: ", i)
                                for texto in texto_a_procurar:
                                    try:
                                        WebDriverWait(navegador, 5).until(
                                            EC.text_to_be_present_in_element((By.XPATH, '//*[contains(text(), "{}")]'.format(texto)), texto)
                                        )
                                        print(f'O texto "{texto_a_procurar}" está visível na página.')
                                        status = 'Remover Poker ok'
                                        print('Terminou de remover')
                                        treminou_de_remover = True
                                        break
                                        # return entrou, status
                                    except TimeoutException:
                                        print(f'O texto "{texto_a_procurar}" não está visível na página.')
                                if treminou_de_remover:
                                    break

                                clicou_no_segundo = False

                                for _ in range(15):
                                    print('procurando 1')
                                    if (pyautogui.pixelMatchesColor(1207, 574, (235, 245, 255), tolerance=15)
                                            or pyautogui.pixelMatchesColor(1207, 574, (223, 233, 242), tolerance=15)):
                                        # testa se esta visivel o segundo botao azul de remover
                                        pyautogui.click(1207, 574)  # clique no segundo remover
                                        print('Clicou no primeiro remover')

                                        for _ in range(15):
                                            print('procurando 2')
                                            if (pyautogui.pixelMatchesColor(805, 730, (8, 102, 255), tolerance=15)
                                                    or pyautogui.pixelMatchesColor(805, 730, (8, 94, 242), tolerance=15)
                                                    or pyautogui.pixelMatchesColor(805, 730, (27, 116, 228), tolerance=15)):
                                                # testa se esta visivel o segundo botao azul de remover
                                                pyautogui.click(853, 730)  # clique no segundo remover
                                                print('Clicou no segundo remover')
                                                clicou_no_segundo = True
                                                break
                                            elif (pyautogui.pixelMatchesColor(805, 741, (8, 102, 255), tolerance=15)
                                                  or pyautogui.pixelMatchesColor(805, 741, (8, 94, 242), tolerance=15)
                                                  or pyautogui.pixelMatchesColor(805, 741, (27, 116, 228), tolerance=15)):
                                                # testa se esta visivel o segundo botao azul de remover
                                                pyautogui.click(853, 741)  # clique no segundo remover
                                                print('Clicou no segundo remover')
                                                clicou_no_segundo = True
                                                break
                                            time.sleep(1)
                                    if clicou_no_segundo:
                                        break
                                    time.sleep(1)

                            if status == 'Remover Poker não ok':
                                while True:
                                    print('\n\nOlhar manualmente o poker pode nao ter sido removido\n\n')
                                    time.sleep(20)

                            print('Terminou de remover')
                            url_atual = pega_url()
                            print(url_atual)

                            time.sleep(1)
                            urlpkrl = "https://apps.facebook.com/rallyacespoker/?fb_source=appcenter&fb_appcenter=1"
                            url = "https://apps.facebook.com/rallyacespoker/?fb_source=appcenter&fb_appcenter=1"
                            navegador.get(urlpkrl)
                            print('Loga no RL e espera 5 segundos')
                            time.sleep(2)
                            url_atual = pega_url()
                            print(url_atual)
                            time.sleep(3)
                            print('Continua os testes')
                            # return entrou, status

                        elif "/checkpoint/" in url_atual:
                            # https://www.facebook.com/checkpoint/1501092823525282/?next=https%3A%2F%2Fwww.facebook.com%2F%3Fsk%3Dwelcome

                            entrou = False
                            status = "Anomalia Fecebook"
                            print("A conta está suspensa.")
                            time.sleep(6)
                            lista_face_caidas = [
                                'você recorreu da decisão', 'confirmar que é você', 'confirmar que és tu', 'Insira o número de celular',
                                'Insere o número de telemóvel', 'Carregue uma foto sua', 'Carrega uma foto tua', 'Carregar uma selfie',
                                'Sua conta foi desativada', 'Sua conta foi suspensa', 'sua conta foi bloqueada', 'Suspendemos a tua conta',
                                'Desabilitamos sua conta', 'você apresentou um recurso', 'Confirme seu número de celular',
                                'precisamos confirmar que esta conta pertence a você', 'Verifique'
                            ]
                            # 'Suspeitamos que o comportamento da sua conta seja automatizado'

                            for item in lista_face_caidas:
                                # percorre os textos que tem quando tem conta caida para o face
                                try:
                                    elemento = navegador.find_element(By.XPATH, f"//span[contains(text(), '{item}')]")
                                    print(item)
                                    status = item
                                    return entrou, status
                                except NoSuchElementException:
                                    continue
                            # se nao for algum item da lista retorna uma mensagem generica

                            elementos_para_clicar = ['Começar', 'Avançar', 'Avançar', 'Avançar', 'Voltar para o Facebook', 'Ignorar']
                            encontrou = False
                            for _ in range(2):
                                for elemento in elementos_para_clicar:
                                    elemento_seletor = f'div[aria-label="{elemento}"]'
                                    print("procura: ", elemento)
                                    try:
                                        elemento_clicavel = WebDriverWait(navegador, 3).until(
                                            EC.element_to_be_clickable((By.CSS_SELECTOR, elemento_seletor)))
                                        elemento_clicavel.click()
                                        print("Clicou em: ", elemento)
                                        time.sleep(5)
                                        encontrou = True
                                    except Exception as e:  # Corrigido o erro aqui, "as e" ao invés de "e Exception:"
                                        print("Elememto para clicar não encontrado: ", elemento, e)
                                        continue
                            if encontrou:
                                time.sleep(3)
                                navegador.get(url)
                                time.sleep(5)
                            else:
                                return entrou, status

                        elif "/user_cookie_choice/" in url_atual:
                            # https://www.facebook.com/privacy/consent/user_cookie_choice/?source=pft_user_cookie_choice
                            print('responder cookies')

                            elemento_recusar = navegador.find_element(By.XPATH, f"//span[contains(text(), 'Recusar cookies opcionais')]")
                            if elemento_recusar:
                                elemento_recusar.click()
                                print('clicou')
                                time.sleep(5)
                                navegador.get(url)
                                time.sleep(5)
                            else:
                                status = "cookie"
                                entrou = False
                                return entrou, status

                        elif "/privacy/consent/pipa/" in url_atual:
                            # https://www.facebook.com/privacy/consent/pipa/?params%5Bpft_surface%5D=facebook_comet&params%5Bis_new_user_blocking_flow%5D=true&params%5Bpft_session_key%5D=afa5f865-6574-4376-9cb2-3349c7a3aed0&source=pipa_blocking_flow
                            print("Concorde com os itens")
                            entrou = False
                            status = "Concorde com os itens"
                            return entrou, status

                        elif "/privacy/" in url_atual:

                            elemento_clicavel_encontrado = False
                            #  https://www.facebook.com/privacy/consent/lgpd_migrated/?source=lgpd_blocking_flow
                            print("A conta termos de privacidade")
                            time.sleep(5)
                            lista_face = ['bloqueado temporariamente', 'concorde', 'temporariamente']
                            for item in lista_face:  # percorre os textos que tem quando tem conta caida para o face
                                try:
                                    elemento = navegador.find_element(By.XPATH, f"//span[contains(text(), '{item}')]")

                                    elemento_clicavel_encontrado = True
                                    print(item)
                                    status = item
                                    entrou = False
                                    return entrou, status
                                except NoSuchElementException:
                                    continue

                            # lista de elemento clicaveis
                            elementos_para_clicar = [
                                'Começar', 'Gerenciar configurações', 'Salvar', 'Continuar', 'Voltar para o Facebook', 'Usar essa atividade',
                                'Usar esta atividade', 'Usar gratuitamente', 'Concordo', 'Concordo', 'Fechar', 'Manter jogos sociais',
                                'Confirmar', 'Concluir'
                            ]
                            time.sleep(3)
                            for _ in range(2):
                                for elemento in elementos_para_clicar:
                                    print("procura: ", elemento)
                                    elemento_seletor = f'div[aria-label="{elemento}"]'
                                    try:
                                        elemento_clicavel = WebDriverWait(navegador, 0.5).until(
                                            EC.element_to_be_clickable((By.CSS_SELECTOR, elemento_seletor)))
                                        elemento_clicavel.click()
                                        print('cicou no elemento :', elemento)
                                        elemento_clicavel_encontrado = True
                                        time.sleep(4)
                                    except Exception as e:  # Corrigido o erro aqui, "as e" ao invés de "e Exception:"
                                        print("Elememto para clicar não encontrado: ", elemento)
                                        # print(e)
                                        continue

                                    # Construir a expressão XPath para o elemento atual na lista
                                    xpath_expression = f"//span[text()='{elemento}']"
                                    try:
                                        # Esperar até que o elemento seja clicável (nesse caso, esperaremos até 10 segundos)
                                        elemento = WebDriverWait(navegador, 0.5).until(EC.element_to_be_clickable((By.XPATH, xpath_expression)))

                                        # Clicar no elemento
                                        elemento.click()
                                        print('cicou no elemento :', elemento)
                                        elemento_clicavel_encontrado = True
                                        time.sleep(4)
                                    except Exception as e:
                                        print(f"Elemento para clicar não encontrado: {elemento}")
                                        # print(e)
                                        continue

                            if not elemento_clicavel_encontrado:
                                print("Nenhum elemento para clicar foi encontrado.")
                                status = 'Nova interação'
                                entrou = False
                                return entrou, status

                            time.sleep(3)
                            navegador.get(url)
                            time.sleep(5)

                    elif ("/login/?privacy" in url_atual) or ("/device-based/regular/login/?" in url_atual):
                        print("senha incorreta")
                        print('manda sair')
                        sair_face(url)

                        entrou = False
                        status = "Senha incorreta"
                        return entrou, status
                    else:
                        lista_face = [
                            'Você não pode usar este recurso no momento', 'Limitamos a frequência', 'senha inserida está incorreta',
                            'Esqueceu a senha', 'Esqueceu a conta?', 'Tentar outra forma', 'Enviaremos um código para o seu email',
                            'Insira o código de segurança'
                        ]
                        for item in lista_face:  # percorre os textos que tem quando tem conta caida para o face
                            try:
                                elemento = navegador.find_element(By.XPATH, f"//span[contains(text(), '{item}')]")
                                print(item)
                                status = item
                                entrou = False
                                return entrou, status
                            except NoSuchElementException:
                                continue

                print("Não carregou o poker")
                entrou = False
                status = "Não ok, outro"
                return entrou, status

            except Exception as e:

                print("Tempo limite excedido ao procurar o elemento faz_login.")
                print(e)
                sair_face(url)
                continue
        else:
            print('Padrao de URL não esperado')
            time.sleep(5)
            sair_face(url)


def abrir_fechar_guia(max_tentativas=5):
    global navegador, url
    print("abrir_fechar_guia")
    tentativas = 0

    while tentativas < max_tentativas:
        try:
            pyautogui.hotkey('ctrl', 't')

            # Aguarde até que haja pelo menos duas guias abertas
            WebDriverWait(navegador, 5).until(lambda x: len(x.window_handles) >= 2)

            # Mude para a primeira guia
            navegador.switch_to.window(navegador.window_handles[0])

            # Feche a primeira guia
            navegador.close()

            # Mude para a segunda guia
            navegador.switch_to.window(navegador.window_handles[0])

            # Aguarde até que a segunda guia esteja ativa
            WebDriverWait(navegador, 5).until(EC.number_of_windows_to_be(1))

            # Verifique se o foco está na primeira guia
            if navegador.current_window_handle != navegador.window_handles[0]:
                print("O foco não está na primeira guia.")
            else:
                print("O foco está na primeira guia.")
                # Recarregue a página
                navegador.get(url)
                return

        except TimeoutException as e:
            print(f"Tentativa {tentativas + 1} falhou. {e}")
            tentativas += 1

    print(f"Atenção: Todas as {max_tentativas} tentativas falharam. Encerrando.")
    return


def sair_face(url_novo=''):
    global navegador, url
    if url != url_novo and url_novo != '':
        url = url_novo

    for _ in range(30):
        IP.tem_internet()

        print("\n   Sair do facebook    \n")

        url_sair = ''

        script = """javascript:void(function(){ function deleteAllCookiesFromCurrentDomain() { var cookies = document.cookie.split("; "); for (var c = 0; c < cookies.length; c++) { var d = window.location.hostname.split("."); while (d.length > 0) { var cookieBase = encodeURIComponent(cookies[c].split(";")[0].split("=")[0]) + '=; expires=Thu, 01-Jan-1970 00:00:01 GMT; domain=' + d.join('.') + ' ;path='; var p = location.pathname.split('/'); document.cookie = cookieBase + '/'; while (p.length > 0) { document.cookie = cookieBase + p.join('/'); p.pop(); }; d.shift(); } } } deleteAllCookiesFromCurrentDomain(); location.href = '""" + url_sair + """'; })();"""

        try:
            print('inicia a execução do script sair')
            navegador.switch_to.window(navegador.window_handles[0])
            navegador.execute_script(script)
            print('script sair executado sem erros')

            # Exclui todos os cookies
            # navegador.delete_all_cookies()

            abrir_fechar_guia()
            print("nova guia ok")
            # recarregar_pagina(navegador, url)

            # print('abre novaguia')
            # # Abrir uma nova guia
            # pyautogui.hotkey('ctrl', 't')
            #
            # for _ in range(100):
            #     # Obtenha a lista de identificadores de janelas abertas
            #     window_handles = navegador.window_handles
            #     time.sleep(0.1)
            #     # Verifique se há duas guias abertas
            #     if len(window_handles) >= 2:
            #         # muda o foco par aa primeira guia
            #         navegador.switch_to.window(navegador.window_handles[0])
            #         # Obtém o identificador da janela atual
            #         janela_atual = navegador.current_window_handle
            #         # Obtém o identificador da primeira guia
            #         primeira_guia = navegador.window_handles[0]
            #
            #         # Verifica se o foco está na primeira guia
            #         if janela_atual == primeira_guia:
            #             print("O foco está na primeira guia.")
            #             # Pressione as teclas "Ctrl+W" para fechar a primeira guia
            #             pyautogui.hotkey('ctrl', 'w')
            #             break
            #         else:
            #             print("O foco não está na primeira guia.")
            #
            # try:
            #     for _ in range(100):
            #         # Obtenha a lista de identificadores de janelas abertas
            #         window_handles = navegador.window_handles
            #
            #         # Verifique se há uma guia aberta
            #         if len(window_handles) == 1:
            #             navegador.switch_to.window(navegador.window_handles[0])
            #             # Obtém o identificador da janela atual
            #             janela_atual = navegador.current_window_handle
            #             # Obtém o identificador da primeira guia
            #             primeira_guia = navegador.window_handles[0]
            #
            #             # Verifica se o foco está na primeira guia
            #             if janela_atual == primeira_guia:
            #                 print("So tem uma guia aberta")
            #                 navegador.get(url)
            #                 break
            #             else:
            #                 print("O foco não está na primeira guia.")
            #             break
            #         time.sleep(0.1)
            # except Exception as e:
            #     print(f"Erro ao fechar a guia: {e}")

            WebDriverWait(navegador, 5).until(EC.presence_of_element_located((By.NAME, 'email')))
            print('Pagina pronta, conta NÃO logada')
            return

        except Exception as e:
            try:
                print("ERRO ao executar o script sair ")
                print(e)
                # Exclui todos os cookies
                # navegador.delete_all_cookies()
                navegador.delete_cookie("xs")
                navegador.delete_cookie("c_user")
                IP.tem_internet()
                navegador.get(url)
                print("testa se tem nao é vc")

            except Exception as e:
                print("Erro ao sair.", e)

            try:
                # Esperar até que o elemento "Não é você?" seja clicável
                elemento_nao_e_voce = WebDriverWait(navegador, 7).until(EC.element_to_be_clickable((By.ID, 'not_me_link')))

                # Clicar no elemento
                print('Clicar no elemento nao_e_voce')
                elemento_nao_e_voce.click()
                print('espera 2s')
                time.sleep(2)

            except Exception as e:
                print("Elemento não encontrado na página.", e)


def atualizar_pagina():
    global navegador, url
    while True:
        IP.tem_internet()  # testa se tem internete enste de atualizar a pagina
        try:
            navegador.get(url)
            return
        except Exception as e:
            print("Erro de conexão com a internet. Tentando novamente em 5 segundos...")
            print(e)
            time.sleep(2)
            continue


def busca_link():
    global navegador
    print('busca_link')

    if nome_usuario == "PokerIP":  # and (nome_computador == "PC-I5-8600K"):
        id = "Luis.gustavo.almeida88"
        senha = "020996Pa"
        endereco_falha = 'F3'

    elif nome_usuario == "lgagu":  # and (nome_computador == "PC-I7-9700KF"):
        id = "stefaniaalmeida.jf"
        senha = "$TE20091992te"
        endereco_falha = 'F4'

    else:  # nome_usuario == "PokerIP": #and (nome_computador == "PC-i3-8145U"):
        id = "Luis.gustavo.almeida88"
        senha = "020996Pa"
        endereco_falha = 'F5'

    url = "https://pt-br.facebook.com/"

    navegador.get(url)

    time.sleep(3)

    if se_esta_lagado() is True:
        sair_face(url)

    print('faz login')
    email_field = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
    email_field.clear()
    email_field.send_keys(id)
    password_field = navegador.find_element(By.NAME, 'pass')
    password_field.clear()
    password_field.send_keys(senha)
    # fazer login clicando no botão de login
    login_button = navegador.find_element(By.NAME, 'login')
    login_button.click()

    print('fez login agurda 7 segundo para a paguna carregar')
    time.sleep(7)
    print('digita o endereço da fanpage')
    # Abrir a página do Facebook da qual você deseja obter a última postagem
    pagina_do_facebook = "https://www.facebook.com/people/Poker-Brasil/100064546038812/"
    navegador.get(pagina_do_facebook)
    print('agurade 7 segundas para a pagina carregar')
    time.sleep(7)

    print('rola')
    # Esperar um pouco para a rolagem ser concluída
    navegador.implicitly_wait(5)  # Aguarde por 5 segundos (ou o tempo que for necessário)

    try:
        # Encontrar todos os elementos de imagem na página
        elementos_imagem = navegador.find_elements(By.TAG_NAME, 'img')

    except TimeoutException:
        # Se ocorrer um TimeoutException, informe que a imagem não foi encontrada e escreva o erro no arquivo de dados
        print("Imagem não encontrada na página")
        Google.escrever_celula("Imagem não encontrada na página", 'Dados', endereco_falha)
        return

    # Procurar o primeiro link que começa com o padrão especificado
    teste_url = False
    try:
        # Iterar sobre os elementos de imagem e verificar se a URL começa com o padrão desejado
        for elemento in elementos_imagem:
            url_imagem = elemento.get_attribute('src')
            # print(url_imagem)
            # Verificar se a URL começa com o padrão especificado
            if url_imagem.startswith("https://external.fjdf2-2.fna.fbcdn.net/emg1"):
                print("\n\n URL válida: \n\n", url_imagem)
                # Se encontrar a URL válida, clicar no elemento e sair do loop
                elemento.click()
                print("\n\n Clicou na imagem correspondente \n\n ")
                teste_url = True
                break

    except Exception as e:
        # Se ocorrer uma exceção ao encontrar a URL, informar o erro e escrever no arquivo de dados
        print('Erro ao encontrar a URL:', str(e))
        Google.escrever_celula("Erro ao encontrar a URL", 'Dados', endereco_falha)
        return

    if not teste_url:
        print('url fora do padrao ou nao encontrada')
        # Google.escrever_celula('url fora do padrao ou nao encontrada', 'Dados', endereco_falha)
        pyautogui.click(670, 730)
        print('clique burro para tentar achar a imagem')
        # return

    time.sleep(5)

    # Obtém todos os identificadores de guias abertas
    guias_abertas = navegador.window_handles

    # Verifica o número de guias abertas
    if len(guias_abertas) == 2:

        print("Existem duas guias abertas, continua.")
        # Faça algo com as duas guias, se necessário
    else:
        print("Não existem duas guias abertas.")
        Google.escrever_celula('url fora do padrao ou nao encontrada a imagem com clique burro ', 'Dados', endereco_falha)

        guias_abertas = navegador.window_handles

        # Verifica se há mais de uma guia aberta
        if len(guias_abertas) > 1:
            # Fecha todas as guias adicionais, exceto a primeira
            for guia_id in guias_abertas[1:]:
                navegador.switch_to.window(guia_id)  # Alterna para a guia que será fechada
                navegador.close()  # Fecha a guia ativa

            # Após fechar as guias adicionais, volta para a primeira guia
            navegador.switch_to.window(guias_abertas[0])

            print("Apenas uma guia foi mantida aberta.")
        else:
            print("Apenas uma guia já está aberta.")
        return

    # Alterne o foco para a nova guia (segunda guia)
    navegador.switch_to.window(navegador.window_handles[1])
    time.sleep(5)
    # Pegar o link da barra de endereço do navegador
    link_da_barra_de_endereco = navegador.current_url
    # Feche a segunda guia
    navegador.close()
    # Volte para a primeira guia, se necessário
    navegador.switch_to.window(navegador.window_handles[0])
    # Verificar se a URL começa com o padrão desejado
    padrao_desejado = "https://apps.facebook.com/pokerbrasil?vtype=&amfmethod=appLinkFanPageAward&SignedParams="
    if link_da_barra_de_endereco.startswith(padrao_desejado):
        print("A URL começa com o padrão desejado.")
        print(link_da_barra_de_endereco)
        print('escreve o link')
        Google.escrever_celula(link_da_barra_de_endereco, 'Dados', 'F2')

        # Obtenha a data e hora atual
        data_hora_atual = str(datetime.datetime.now())
        print('escreve a data da atialização: ', data_hora_atual)
        if (nome_usuario == "PokerIP") and (nome_computador == "PC-I5-8600K"):
            Google.escrever_celula(data_hora_atual, 'Dados', endereco_falha)
        elif (nome_usuario == "lgagu") and (nome_computador == "PC-I7-9700KF"):
            Google.escrever_celula(data_hora_atual, 'Dados', endereco_falha)

        print('Link copiado com sucesso')
        time.sleep(5)
        return
    else:
        Google.escrever_celula("link fanpag fora do padrão", 'Dados', endereco_falha)
        print("link fanpag fora do padrão")

######################################################################################################################
# # para abrir o navegador e deixar abero. Descomentar as duas linhas abaixo
# navegador = cria_nevegador()
#
# navegador.get("https://apps.facebook.com/pokerbrasil?vtype=&amfmethod=appLinkFanPageAward&SignedParams=hIygZ7vSvP9r7RwePVy1W5XheNQYiuWT8U9EdgPVaB4.eyJhY3QiOiJmcCIsImZwX2FpZCI6IjYyMDAifQ&fbclid=IwAR1folpzzbjVGnnI-cxCtwm8rZky5Is52TGgzh_CNVvnCRVryopwAYAzbdQ")
#
# time.sleep(30)
# # Obter todos os cookies
# cookies = navegador.get_cookies()
#
# # Exibir nomes dos cookies
# for cookie in cookies:
#     print("Nome do Cookie:", cookie['name'])
#
# print('\npresence')
# navegador.delete_cookie("presence")
# navegador.get("https://apps.facebook.com/pokerbrasil?vtype=&amfmethod=appLinkFanPageAward&SignedParams=hIygZ7vSvP9r7RwePVy1W5XheNQYiuWT8U9EdgPVaB4.eyJhY3QiOiJmcCIsImZwX2FpZCI6IjYyMDAifQ&fbclid=IwAR1folpzzbjVGnnI-cxCtwm8rZky5Is52TGgzh_CNVvnCRVryopwAYAzbdQ")
#
# time.sleep(30)
# print("\nfr")
# navegador.delete_cookie("fr")
# navegador.get("https://apps.facebook.com/pokerbrasil?vtype=&amfmethod=appLinkFanPageAward&SignedParams=hIygZ7vSvP9r7RwePVy1W5XheNQYiuWT8U9EdgPVaB4.eyJhY3QiOiJmcCIsImZwX2FpZCI6IjYyMDAifQ&fbclid=IwAR1folpzzbjVGnnI-cxCtwm8rZky5Is52TGgzh_CNVvnCRVryopwAYAzbdQ")
#
# time.sleep(30)
# print("\nxs")
# navegador.delete_cookie("xs")
# navegador.get("https://apps.facebook.com/pokerbrasil?vtype=&amfmethod=appLinkFanPageAward&SignedParams=hIygZ7vSvP9r7RwePVy1W5XheNQYiuWT8U9EdgPVaB4.eyJhY3QiOiJmcCIsImZwX2FpZCI6IjYyMDAifQ&fbclid=IwAR1folpzzbjVGnnI-cxCtwm8rZky5Is52TGgzh_CNVvnCRVryopwAYAzbdQ")
#
# time.sleep(30)
# print("\nc_user")
# navegador.delete_cookie("c_user")
# navegador.get("https://apps.facebook.com/pokerbrasil?vtype=&amfmethod=appLinkFanPageAward&SignedParams=hIygZ7vSvP9r7RwePVy1W5XheNQYiuWT8U9EdgPVaB4.eyJhY3QiOiJmcCIsImZwX2FpZCI6IjYyMDAifQ&fbclid=IwAR1folpzzbjVGnnI-cxCtwm8rZky5Is52TGgzh_CNVvnCRVryopwAYAzbdQ")
#
# time.sleep(30)
# print("\nwd")
# navegador.delete_cookie("wd")
# navegador.get("https://apps.facebook.com/pokerbrasil?vtype=&amfmethod=appLinkFanPageAward&SignedParams=hIygZ7vSvP9r7RwePVy1W5XheNQYiuWT8U9EdgPVaB4.eyJhY3QiOiJmcCIsImZwX2FpZCI6IjYyMDAifQ&fbclid=IwAR1folpzzbjVGnnI-cxCtwm8rZky5Is52TGgzh_CNVvnCRVryopwAYAzbdQ")
#
# time.sleep(30)
# print("\noo")
# navegador.delete_cookie("oo")
# navegador.get("https://apps.facebook.com/pokerbrasil?vtype=&amfmethod=appLinkFanPageAward&SignedParams=hIygZ7vSvP9r7RwePVy1W5XheNQYiuWT8U9EdgPVaB4.eyJhY3QiOiJmcCIsImZwX2FpZCI6IjYyMDAifQ&fbclid=IwAR1folpzzbjVGnnI-cxCtwm8rZky5Is52TGgzh_CNVvnCRVryopwAYAzbdQ")
#
# time.sleep(30)
# print("\nsb")
# navegador.delete_cookie("sb")
# navegador.get("https://apps.facebook.com/pokerbrasil?vtype=&amfmethod=appLinkFanPageAward&SignedParams=hIygZ7vSvP9r7RwePVy1W5XheNQYiuWT8U9EdgPVaB4.eyJhY3QiOiJmcCIsImZwX2FpZCI6IjYyMDAifQ&fbclid=IwAR1folpzzbjVGnnI-cxCtwm8rZky5Is52TGgzh_CNVvnCRVryopwAYAzbdQ")
#
# time.sleep(30)
# print("\ndatr")
# navegador.delete_cookie("datr")
# navegador.get("https://apps.facebook.com/pokerbrasil?vtype=&amfmethod=appLinkFanPageAward&SignedParams=hIygZ7vSvP9r7RwePVy1W5XheNQYiuWT8U9EdgPVaB4.eyJhY3QiOiJmcCIsImZwX2FpZCI6IjYyMDAifQ&fbclid=IwAR1folpzzbjVGnnI-cxCtwm8rZky5Is52TGgzh_CNVvnCRVryopwAYAzbdQ")


# # busca_link(navegador)
# time.sleep(10000)
