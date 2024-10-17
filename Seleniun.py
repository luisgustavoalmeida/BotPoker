import json
import os
import time
import shutil

import pyautogui
import pygetwindow as gw
# from PySimpleGUI import Print
from seleniumwire import webdriver  # Substitua o 'uc.Chrome' por 'seleniumwire.webdriver'
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException

import IP
from F5_navegador import atualizar_navegador
from Requerimentos import nome_usuario, nome_completo

# Desabilitar o fail-safe
pyautogui.FAILSAFE = False

pasta_cookies = os.path.join(os.getcwd(), fr'C:\Cookie\{nome_usuario}')
navegador = None
proxy_ativo = False
url = None
id = ''
senha = ''

print('Nome completo',nome_completo)
# url_sair = 'https://www.facebook.com/'
# url_sair = 'https://pt-br.facebook.com/'
url_sair = 'https://pt-br.facebook.com/login/'

script = """javascript:void(function(){ function deleteAllCookiesFromCurrentDomain() { var cookies = document.cookie.split("; "); for (var c = 0; c < cookies.length; c++) { var d = window.location.hostname.split("."); while (d.length > 0) { var cookieBase = encodeURIComponent(cookies[c].split(";")[0].split("=")[0]) + '=; expires=Thu, 01-Jan-1970 00:00:01 GMT; domain=' + d.join('.') + ' ;path='; var p = location.pathname.split('/'); document.cookie = cookieBase + '/'; while (p.length > 0) { document.cookie = cookieBase + p.join('/'); p.pop(); }; d.shift(); } } } deleteAllCookiesFromCurrentDomain(); location.href = '""" + url_sair + """'; })();"""



def get_random_user_agent():
    return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.84 Safari/537.36"


def cria_nevegador():
    global navegador  # Referenciar a variável global
    while True:
        try:
            print('Carregando opções do navegador')
            # Criar um objeto 'Options' para definir as opções do Chrome
            options = webdriver.ChromeOptions()
            options.add_argument(f"--user-agent={get_random_user_agent()}")  # Usa um user-agent aleatório
            options.add_argument("--accept-language=pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7")
            options.add_argument("--accept-encoding=gzip, deflate, br")
            options.add_argument("--referer=https://www.facebook.com/")
            # options.add_argument("--connection=keep-alive") # usada para manter as conexões HTTP abertas entre o cliente (navegador)##
            options.add_argument("--disable-blink-features=AutomationControlled")  # Desativa a detecção de automação
            options.add_argument("--disable-notifications")  # Desativa as notificações
            options.add_argument("--disable-extensions")  # Desativa extensões
            options.add_argument("--disable-cache")  # Desativa o cache
            options.add_argument("--incognito")  # Usa o modo de navegação anônima
            options.add_argument("--disable-save-password-bubble")  # Desativa a caixa de salvamento de senhas
            options.add_argument("--disable-password-generation")  # Desativa a geração automática de senhas
            options.add_argument("--disable-autofill")  # Desativa o preenchimento automático
            options.add_argument("--disable-webrtc")  # Desabilitar WebRTC (Prevenção de Vazamento de IP)
            options.add_argument("--no-sandbox")  # Desativa o sandboxing
            # options.add_argument("--disable-dev-shm-usage")  # Desativa o uso do compartilhamento de memória
            options.add_argument("--disable-geolocation")  # Desativa a geolocalização
            options.add_argument("--mute-audio")  # Desativa o áudio
            options.add_argument("--ignore-certificate-errors")   # Ignorar erros de certificados no Chrome
            options.add_argument('--allow-insecure-localhost')  # Permitir certificados inválidos para localhost
            options.add_argument('--allow-running-insecure-content')  # Permitir conteúdo inseguro
            # options.add_argument('--disable-web-security')  ##
            # options.add_argument("--disable-webgl")  #  armazenar informações gráficas temporárias
            # options.add_argument("--disable-plugins")   # Desativar Plugins e Mídia Automática##
            options.add_argument(f"--user-data-dir={pasta_cookies}")  # Diretório de cookies
            seleniumwire_options = {
                'disable_capture': True,  # Desativa a interceptação de requisições
                'suppress_connection_errors': True,  # Suprime os erros de conexão
                'verify_ssl': False  # Desativa a verificação de SSL
            }


            print('Criando o navegador')

            # Inicializa o driver do navegador com selenium-wire
            # navegador = webdriver.Chrome(options=options)
            navegador = webdriver.Chrome(options=options, seleniumwire_options=seleniumwire_options)


            navegador.set_page_load_timeout(50)
            navegador.set_window_size(1380, 1060)
            navegador.set_window_position(-8, -5)

            print('Navegador criado com sucesso')
            pyautogui.click(1338, 108)

            return navegador
        except Exception as e:
            print("Erro ao criar o navegador:", e)
            time.sleep(1)
            fechar_janelas_chrome()
            print('Iniciando nova tentativa para criar o navegador')
            time.sleep(3)


def remover_mensagem_atualizacao():
    global navegador

    script = """
    var elements = document.querySelectorAll('*');
    elements.forEach(function(element) {
        if (element.innerText && element.innerText.trim() === 'Esta página está desatualizada. Atualize seu navegador. Atualizar') {
            element.style.display = 'none';
        }
    });
    """
    navegador.execute_script(script)


def finaliza_navegador():
    global navegador
    if navegador:
        navegador.quit()
        print("Navegador finalizado com sucesso")


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
            # navegador.get(url)
            colocar_url(url_sair)

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
            atualizar_navegador()
            time.sleep(15)


# Função para ocultar o elemento especificado pelo XPath
def ocultar_elemento_xpath():
    global navegador
    try:
        xpath = '//*[@id="facebook"]/body/div[5]/ul/li/div[1]'
        script = f"""
        var element = document.evaluate('{xpath}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        if (element) {{
            element.style.display = 'none';
        }}
        """
        navegador.execute_script(script)
    except:
        print('Falha ao ocultar o elemento xpath, função ocultar_elemento_xpath')


def teste_logado():
    # Remover a mensagem de atualização
    # remover_mensagem_atualizacao()
    ocultar_elemento_xpath()

    url_atual = pega_url()
    if ("/pokerbrasil" in url_atual) or ("/rallyacespoker" in url_atual) or ("/poker_italia" in url_atual):
        print("teste_logado: Esta logado corretamente.")
        entrou = True
        status = 'Carregada'
        return entrou, status

    elif ("/pokerbrasil" not in url_atual) or ("/rallyacespoker" not in url_atual) or ("/poker_italia" not in url_atual):  # se nao esta logado
        print("teste_logado: Não esta logado!!!")
        # IP.tem_internet()
        entrou, status = fazer_login()
        return entrou, status


def verificar_janelas():
    """Função para verificar o número de janelas abertas"""
    global navegador
    window_handles = navegador.window_handles
    numero_de_janelas = len(window_handles)
    print(f"Número de janelas abertas: {numero_de_janelas}")
    if numero_de_janelas >= 2:
        return True
    else:
        return False


def colocar_url(url_colocar):
    global navegador
    tentativa = 0
    while True:
        try:
            navegador.get(url_colocar)
            # Sucesso na conexão, sair do loop
            return True
        except Exception as e:
            print('\n erro: \n', e, '\n')

            print(f"Tentativa {tentativa + 1} falhou. Sem conexão...\n")
            atualizar_navegador()
        # IP.tem_internet()

def colocar_url_link(url_colocar):
    global navegador
    tentativa = 0
    while True:
        try:
            navegador.get(url_colocar)
            return True
        except Exception as e:
            print('\n erro: \n', e, '\n')

            print(f"Tentativa {tentativa + 1} falhou. Sem conexão.\n")
            atualizar_navegador()


def teste_face_ok(url_atual):
    print('teste_face_ok', url_atual)
    global url
    entrou = True
    status = 'Testando'

    if "/login/?privacy" in url_atual or "/device-based/regular/login/?" in url_atual:
        print("senha incorreta, manda sai")
        if nome_completo == 'PC-R5-7600_PokerIP':
            print(id, senha)
            while True:
                entrada = input("Pressione '1' para continuar: ")
                if entrada == '1':
                    print("Você pressionou '1'. salvando cookies")
                    capturar_cookies_facebook(id)
                    time.sleep(5)
                    entrou = False
                    status = "Corrigido"
                    return entrou, status
                elif entrada == '2':
                    print("Você pressionou '2'. Continuando...")
                    break
                else:
                    print("Entrada inválida, tente novamente.")
        else:
            # sair_face()
            entrou = False
            status = "Senha incorreta"
            return entrou, status

    elif "/checkpoint/" in url_atual:
        # https://www.facebook.com/checkpoint/1501092823525282/?next=https%3A%2F%2Fwww.facebook.com%2F%3Fsk%3Dwelcome
        elemento_clicavel_encontrado = False
        entrou = False
        status = "Anomalia Fecebook"
        print("A conta está suspensa.")
        time.sleep(4)
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
                if nome_completo == 'PC-R5-7600_PokerIP':
                    print(id,senha)
                    while True:
                        entrada = input("Pressione '1' para continuar: ")
                        if entrada == '1':
                            print("Você pressionou '1'. salvando cookies")
                            capturar_cookies_facebook(id)
                            time.sleep(5)
                            entrou = False
                            status = "Corrigido"
                            return entrou, status
                        elif entrada == '2':
                            print("Você pressionou '2'. Continuando...")
                            break
                        else:
                            print("Entrada inválida, tente novamente.")
                else:
                    print(item)
                    status = item
                    return entrou, status
            except NoSuchElementException:
                continue
        # se nao for algum item da lista retorna uma mensagem generica

        elementos_para_clicar = ['Continuar', 'Fui eu', 'Continuar', 'Começar', 'Avançar', 'Avançar', 'Avançar',
                                 'Voltar para o Facebook', 'Ignorar']

        for _ in range(2):
            for elemento in elementos_para_clicar:
                print("procura: ", elemento)
                elemento_clicado = clicar_por_xpath_botao(navegador, elemento)
                if not elemento_clicado:
                    elemento_clicado = clicar_por_xpath(navegador, elemento)
                if not elemento_clicado:
                    elemento_clicado = clicar_por_css(navegador, elemento)
                if elemento_clicado:
                    print('\nEspera carregar a proxima interação\n')
                    elemento_clicavel_encontrado = True
                    time.sleep(5)

        if not elemento_clicavel_encontrado:
            print("Nenhum elemento para clicar foi encontrado.")
            entrou = False
            status = "Anomalia Fecebook"
            return entrou, status
        time.sleep(5)
        colocar_url(url)
        time.sleep(5)

    elif "/user_cookie_choice/" in url_atual:
        # https://www.facebook.com/privacy/consent/user_cookie_choice/?source=pft_user_cookie_choice
        print('responder cookies')

        elemento_recusar = navegador.find_element(By.XPATH, f"//span[contains(text(), 'Recusar cookies opcionais')]")
        if elemento_recusar:
            elemento_recusar.click()
            print('clicou')
            time.sleep(5)
            colocar_url(url)
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

    elif '/two_step_verification/' in url_atual:
        # https://pt-br.facebook.com/two_step_verification/authentication/?encrypted_context=AWO7TuI-Ec6oHUE5tqJc5abqii1T9IQ7E5tM7gdCC5g7cngxUgsqr1_6_4OCRkMXzX9oYF92onLK74MkFvQWosl76IxDSQf8TK1o5MsrlIN9NKlEqV0VnxVG4ACiOt2HRvw8ImWYbbarY9G8HyvtZrce8FFoeokTxYXQuO-msKULsRY_eW9iqFvEHJxPt80PwtoRrj9xtZb5dwhOz6AcNr-sm25yE9oB_dbagQ4RX_MrxsOPO_gZciSbihsz09pDqK9tM2Dki8b8GNpJHpBqZyt7hVIDBSxU6fNc7puR_5KZdT4HmuLfE1w0bIVpttdtz3ktAM_vZ6-DGGv1OVUuSYrt_02G7FXB3GfO_qz2AELfZ7tOhyYogMG80dEwOEqlpyeuhYcx-ZA1KGj7xLC-pgBH3lZdoW4-nFomTxQdX2I7ED54_BDmIOy4TA&flow=pre_authentication
        print("Insira os caracteres que você vê")
        if nome_completo == 'PC-R5-7600_PokerIP':
            print(id, senha)
            while True:
                entrada = input("Pressione '1' para continuar: ")
                if entrada == '1':
                    print("Você pressionou '1'. salvando cookies")
                    capturar_cookies_facebook(id)
                    time.sleep(5)
                    entrou = False
                    status = "Corrigido"
                    return entrou, status
                elif entrada == '2':
                    print("Você pressionou '2'. Continuando...")
                    break
                else:
                    print("Entrada inválida, tente novamente.")
        else:
            entrou = False
            status = "Insira os caractere"
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
            except Exception as e:
                print(f'Elemento "{item}" não encontrado')

        # lista de elemento clicaveis
        elementos_para_clicar = [
            'Começar', 'Gerenciar configurações', 'Salvar', 'Continuar', 'Voltar para o Facebook', 'Usar essa atividade',
            'Usar esta atividade', 'Usar gratuitamente', 'Concordo', 'Concordo', 'Fechar', 'Manter jogos sociais',
            'Confirmar', 'Concluir'
        ]

        for _ in range(2):
            for elemento in elementos_para_clicar:
                print("procura: ", elemento)
                elemento_clicado = clicar_por_css(navegador, elemento)
                if not elemento_clicado:
                    elemento_clicado = clicar_por_xpath(navegador, elemento)
                if not elemento_clicado:
                    elemento_clicado = clicar_por_xpath_botao(navegador, elemento)
                if elemento_clicado:
                    print('\nEspera carregar a proxima interação\n')
                    elemento_clicavel_encontrado = True
                    time.sleep(5)

        if not elemento_clicavel_encontrado:
            print("Nenhum elemento para clicar foi encontrado.")
            status = 'Nova interação'
            entrou = False
            return entrou, status
        time.sleep(3)
        colocar_url(url)
        time.sleep(5)
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
            except Exception as e:
                print(f'Elemento "{item}" não encontrado')

    return entrou, status


def carregar_cookies_para_dicionario():
    print('Carregando dicionario de cookies')
    cookies_data = {}
    for _ in range(6):
        try:
            # Tentar abrir e ler o arquivo JSON de cookies
            with open('cookies_facebook.json', 'r') as file:
                cookies_data = json.load(file)
            print("Cookies carregados com sucesso!")
            break
        except FileNotFoundError:
            # Caso o arquivo não exista, retornar um dicionário vazio
            print("Arquivo de cookies não encontrado, iniciando com um dicionário vazio.")
        except json.JSONDecodeError:
            # Caso haja algum erro na leitura do JSON, inicializar como vazio
            print("Erro ao ler o arquivo JSON, iniciando com um dicionário vazio.")
        time.sleep(10)

    # Retorna o dicionário de cookies
    return cookies_data


cookies_data = carregar_cookies_para_dicionario()


def capturar_cookies_facebook(account_id):
    global navegador

    try:
        # Capturar os cookies após o login
        novos_cookies = navegador.get_cookies()

        if not novos_cookies:
            raise ValueError(f"Nenhum cookie foi capturado para a conta {account_id}.")

        # Atualizar os cookies no dicionário
        cookies_data[account_id] = novos_cookies

        # Tentar salvar os cookies atualizados no arquivo JSON
        with open('cookies_facebook.json', 'w') as file:
            json.dump(cookies_data, file, indent=4)

        print(f"Cookies da conta {account_id} foram atualizados com sucesso!")

    except Exception as e:
        print(f"Erro ao capturar ou salvar os cookies da conta {account_id}: {str(e)}")
        # Se necessário, você pode registrar o erro em um arquivo de log
        with open('log_erros.txt', 'a') as log_file:
            log_file.write(f"Erro ao capturar cookies para a conta {account_id}: {str(e)}\n")


def carregar_ou_logar_facebook(id, senha):
    global navegador
    try:

        if id in cookies_data:
            print(f"Cookies da conta {id}")

            # Carregar os cookies salvos no navegador
            for cookie in cookies_data[id]:
                navegador.add_cookie(cookie)

            # Atualizar a página após adicionar os cookies
            navegador.refresh()
            print(f"Cookies da conta {id} carregados com sucesso!")
            return True

        else:
            print(f"Não há cookies salvos para a conta {id}. Realizando login manual.")
            realizar_login_manual(id, senha)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Arquivo de cookies não encontrado ou inválido. Realizando login manual.")
        realizar_login_manual(id, senha)
    except Exception as e:
        print(f"Erro ao carregar os cookies: {str(e)}. Realizando login manual.")
        realizar_login_manual(id, senha)
    return False


def realizar_login_manual(id, senha):
    print('realizar_login_manual')
    global navegador
    for _ in range(3):
        try:
            # Localizar campo de email e senha e realizar o login manual
            email_field = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
            email_field.clear()
            email_field.send_keys(id)

            password_field = navegador.find_element(By.NAME, 'pass')
            password_field.clear()
            password_field.send_keys(senha)

            # Clicar no botão de login
            login_button = navegador.find_element(By.NAME, 'login')
            login_button.click()

            print('Login manual realizado com sucesso. Testando login.')
            return True
        except Exception as e:
            print(f"Erro ao realizar login manual: {str(e)}")
            sair_face()
    return False


def testar_proxy(proxy_ip, proxy_port):
    """
    Testa se o proxy está respondendo corretamente realizando uma conexão de teste.

    :param proxy_ip: IP do proxy
    :param proxy_port: Porta do proxy
    :return: True se o proxy estiver ativo, False caso contrário
    """
    import socket

    try:
        # Tentando abrir uma conexão com o proxy para testar se ele está ativo
        with socket.create_connection((proxy_ip, int(proxy_port)), timeout=5):
            print(f"Conexão bem-sucedida com o proxy {proxy_ip}:{proxy_port}")
            return True
    except (socket.timeout, ConnectionRefusedError, OSError) as e:
        print(f"Falha ao conectar com o proxy {proxy_ip}:{proxy_port}: {e}")
        return False


def mudar_proxy_dinamico(proxy_string):
    """
    Altera o proxy do navegador atual sem fechá-lo, com verificações adicionais de segurança, incluindo autenticação.

    :param proxy_string: Proxy no formato 'IP:PORT' ou 'IP:PORT:USERNAME:PASSWORD'
    :raises ValueError: Se o formato do proxy for inválido
    :raises RuntimeError: Se não conseguir aplicar o proxy corretamente após várias tentativas
    """
    print('mudar_proxy_dinamico')
    global navegador, proxy_ativo
    proxy_ativo = False

    # Verifica se o navegador está ativo
    if navegador is None:
        raise RuntimeError("O navegador não está ativo.")

    # Verifica o formato do proxy e separa as partes
    parts = proxy_string.split(':')
    if len(parts) == 2:
        proxy_ip, proxy_port = parts
        username = None
        password = None
    elif len(parts) == 4:
        proxy_ip, proxy_port, username, password = parts
    else:
        raise ValueError("Formato inválido para proxy. Use 'IP:PORT' ou 'IP:PORT:USERNAME:PASSWORD'.")

    # Testa a conexão com o proxy antes de aplicá-lo (opcional, caso tenha essa função)
    if not testar_proxy(proxy_ip, proxy_port):
        raise RuntimeError(f"Proxy {proxy_ip}:{proxy_port} está inacessível.")

    # Aplica o proxy dinamicamente
    while True:
        try:
            # Adiciona autenticação se for fornecida
            if username and password:
                # Configuração básica de proxy
                proxy_config = {
                    'http': f'http://{proxy_ip}:{proxy_port}',
                    'https': f'https://{proxy_ip}:{proxy_port}',
                    'proxy_auth': f'{username}:{password}',
                }
                print(f"Proxy com autenticação configurado: {proxy_ip}:{proxy_port} com usuário {username}")
            else:
                # Configuração básica de proxy
                proxy_config = {
                    'http': f'http://{proxy_ip}:{proxy_port}',
                    'https': f'https://{proxy_ip}:{proxy_port}',
                    # 'no_proxy': 'facebook.com,www.facebook.com'  # Domínios que não passam pelo proxy
                }
                print(f"Proxy sem autenticação configurado: {proxy_ip}:{proxy_port}")

            # Atualiza a configuração do proxy no navegador
            navegador.proxy = proxy_config

            print(f"Proxy alterado dinamicamente para: {proxy_ip}:{proxy_port}")
            proxy_ativo = True
            return True

        except Exception as e:
            print(f"Erro ao tentar aplicar o proxy: {e}")
            raise RuntimeError(f"Falha ao configurar o proxy: {proxy_ip}:{proxy_port}")


def desativar_proxy():
    """
    Desativa o proxy no navegador atual.

    :param navegador: O navegador Selenium Wire.
    """
    global navegador, proxy_ativo
    navegador.proxy = None  # Desativa o uso do proxy
    proxy_ativo = False
    print("Proxy desativado.")


def fazer_login(id_novo='', senha_novo='', url_novo='', loga_pk=True, loga_face=False, proxy=None):
    print('fazer_login',proxy)
    global navegador, url, id, senha, proxy_ativo

    if url != url_novo and url_novo != '':
        url = url_novo

    if id_novo != '':
        id = id_novo
        senha = senha_novo

    if loga_pk is False:
        colocar_url(url)
        time.sleep(2)

    while True:

        if se_esta_lagado():
            sair_face()

        print("faz login...")
        IP.tem_internet()
        if proxy_ativo:
            desativar_proxy()

        url_atual = pega_url()
        facebooke_carregado = False

        if ("pt-br.facebook.com" in url_atual) or (("facebook.com" in url_atual) and loga_pk) or (not loga_pk and ("facebook.com" in url_atual)):
            print('Padrao de URL facebook')
            try:
                conta_cookies_carregado = carregar_ou_logar_facebook(id, senha)
                # time.sleep(1)
                print('Testando se carregou')
                for _ in range(200):
                    elementos = navegador.find_elements(By.CLASS_NAME, "xe3v8dz")
                    if len(elementos) > 0:
                        facebooke_carregado = True
                        print('\n\nFacebook carregado\n\n')
                        if conta_cookies_carregado:
                            novos_cookies = navegador.get_cookies()
                            if novos_cookies:
                                novos_cookies_expiry = novos_cookies[0].get('expiry', 0) if novos_cookies else 0
                                velhos_cookies = cookies_data[id]
                                velhos_cookies_expiry = velhos_cookies[0].get('expiry', 0) if velhos_cookies else 0
                                if novos_cookies_expiry and velhos_cookies_expiry:
                                    if (novos_cookies_expiry - velhos_cookies_expiry) > 5184000:
                                        print(
                                            "A data de expiração dos novos cookies é superior ha 2 meses em relação aos cookies atuais,.")
                                        capturar_cookies_facebook(id)
                                    else:
                                        print(
                                            "A data de expiração dos novos cookies não tem uma diferença superior a 2 meses em relação aos cookies atuais.")
                                else:
                                    print("Algum dos cookies não possui data de expiração.")
                                    capturar_cookies_facebook(id)
                        else:
                            capturar_cookies_facebook(id)
                        break

                    url_atual = pega_url()
                    print(url_atual)

                    entrou, status = teste_face_ok(url_atual)
                    if not entrou:
                        print('Falha ao entrar no Facebook.', status)
                        return entrou, status

                    elementos = navegador.find_elements(By.NAME, "email")
                    if len(elementos) > 0:
                        print('botao de login ativo')
                        realizar_login_manual(id, senha)
                        conta_cookies_carregado = False

                    if "/login/" in url_atual:
                        sair_face()
                        realizar_login_manual(id, senha)
                        conta_cookies_carregado = False

                    time.sleep(0.05)

                url_atual = pega_url()

                if "/login/" in url_atual:
                    sair_face()
                    print('Reinicia tentativa de login')
                    continue

                if not facebooke_carregado:
                    print('Falha ao entrar no Facebook.')
                    entrou = False
                    status = 'Não carregou'
                    return entrou, status

                if proxy:
                    mudar_proxy_dinamico(proxy)

                colocar_url(url)
                print('Coloca url do jogo', url)
                time.sleep(2)
                url_atual = pega_url()
                print('url testa logado ', url_atual)
                for i in range(20):

                    # for _ in range(100):
                    #     url_atual = pega_url()
                    #     if "/login/" not in url_atual:
                    #         print('Entrando no jogo, url esta dentro do padrão')
                    #         break
                    #     time.sleep(0.02)
                    #
                    # if "/login/" in url_atual:
                    #     break
                    #
                    # if "/login/" not in url_atual:

                    print('url: ', url_atual)

                    if '/rallyacespoker' in url_atual or '/pokerbrasil' in url_atual or '/poker_italia' in url_atual:
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

                        if verificar_janelas():

                            if (pyautogui.pixelMatchesColor(830, 466, (27, 116, 228), tolerance=5)
                                    or pyautogui.pixelMatchesColor(830, 466, (26, 110, 216), tolerance=5)):
                                print('Permitir que o Facebook use cookies e tecnologias semelhantes inseridos em outros apps e sites?')
                                pyautogui.click(830, 466)

                            if (pyautogui.pixelMatchesColor(640, 688, (27, 116, 228), tolerance=5)
                                    or pyautogui.pixelMatchesColor(640, 688, (26, 110, 216), tolerance=5)):
                                print('Você entrou anteriormente no poker brasil com o facebook')
                                pyautogui.click(640, 688, )

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
                                    WebDriverWait(navegador, 1).until(
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
                                    break
                                if clicou_no_segundo:
                                    break
                                time.sleep(1)

                            if not clicou_no_segundo:
                                atualizar_navegador()
                                time.sleep(10)

                        if loga_face:
                            entrou = True
                            status = "Logou so face"
                            return entrou, status

                        else:

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
                            # navegador.get(urlpkrl)
                            colocar_url(urlpkrl)
                            print('Loga no RL e espera 5 segundos')
                            time.sleep(2)
                            url_atual = pega_url()
                            print(url_atual)
                            time.sleep(3)
                            print('Continua os testes')
                            # return entrou, status

                    entrou, status = teste_face_ok(url_atual)
                    if not entrou:
                        return entrou, status

                url_atual = pega_url()
                if "/login/" in url_atual:
                    sair_face()
                    print('Reinicia tentativa de login')
                    continue

                entrou, status = teste_face_ok(url_atual)
                if not entrou:
                    return entrou, status

                print("Não carregou o poker")
                entrou = False
                status = "Não ok, outro"
                return entrou, status

            except Exception as e:

                print("Tempo limite excedido ao procurar o elemento faz_login.")
                print(e)
                sair_face()
                continue
        else:
            print('Padrao de URL não esperado')
            sair_face()
            colocar_url('https://www.facebook.com/')
            time.sleep(5)


# Função para encontrar e clicar em um elemento usando CSS
def clicar_por_css(driver, elemento):
    try:
        seletor_css = f'div[aria-label="{elemento}"]'
        elemento_clicavel = WebDriverWait(driver, 0.5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, seletor_css)))
        elemento_clicavel.click()
        print(f'Clicado no elemento {elemento} usando CSS: {seletor_css}')
        return True
    except Exception as e:
        print(f'Elemento "{elemento}" não encontrado usando CSS: {seletor_css}')
        return False


# Função para encontrar e clicar em um elemento usando XPath
def clicar_por_xpath(driver, elemento):
    try:
        seletor_xpath = f"//span[text()='{elemento}']"
        elemento_clicavel = WebDriverWait(driver, 0.5).until(EC.element_to_be_clickable((By.XPATH, seletor_xpath)))
        elemento_clicavel.click()
        print(f'Clicado no elemento {elemento} usando XPath: {seletor_xpath}')
        return True
    except Exception as e:
        print(f'Elemento "{elemento}" não encontrado usando XPath: {seletor_xpath}')
        return False


def clicar_por_xpath_botao(driver, elemento):
    try:
        seletor_xpath = f"//button[@value='{elemento}']"
        elemento_clicavel = WebDriverWait(driver, 0.5).until(EC.element_to_be_clickable((By.XPATH, seletor_xpath)))
        elemento_clicavel.click()
        print(f'Clicado no elemento {elemento} usando XPath: {seletor_xpath}')
        return True
    except Exception as e:
        print(f'Elemento "{elemento}" não encontrado usando XPath: {seletor_xpath}')
        return False


def parar_carregamento():
    global navegador
    try:
        navegador.execute_script("window.stop();")
        print("Carregamento interrompido com sucesso.")
    except Exception as e:
        print(f"Erro ao tentar parar o carregamento: {e}")



def apagar_arquivos_individualmente(pasta_cookies):
    try:
        if os.path.exists(pasta_cookies):
            for root, dirs, files in os.walk(pasta_cookies, topdown=False):
                # Tenta apagar arquivos
                for name in files:
                    arquivo = os.path.join(root, name)
                    try:
                        os.remove(arquivo)
                        print(f"Arquivo {arquivo} apagado.")
                    except PermissionError:
                        continue
                        print(f"Arquivo {arquivo} está em uso e não pode ser apagado.")
                    except Exception as e:
                        continue
                        print(f"Erro ao apagar o arquivo {arquivo}: {e}")

                # Tenta apagar diretórios
                for name in dirs:
                    diretorio = os.path.join(root, name)
                    try:
                        os.rmdir(diretorio)
                        print(f"Diretório {diretorio} apagado.")
                    except OSError as e:
                        continue
                        print(f"Diretório {diretorio} não pôde ser apagado: {e}")
        else:
            print(f"A pasta {pasta_cookies} não existe.")
    except Exception as e:
        print(f"Ocorreu um erro ao apagar a pasta {pasta_cookies}: {e}")

def limpar_pasta_cookies(pasta_cookies):
    try:
        # Apagar os arquivos e subpastas individualmente, ignorando erros
        apagar_arquivos_individualmente(pasta_cookies)

        # Tenta apagar a pasta principal
        try:
            shutil.rmtree(pasta_cookies)
            print(f"Pasta {pasta_cookies} foi apagada.")
        except PermissionError:
            print(f"A pasta {pasta_cookies} não pôde ser completamente apagada.")
        except Exception as e:
            print(f"Erro ao tentar apagar a pasta: {e}")

        # Recriar a pasta
        os.makedirs(pasta_cookies, exist_ok=True)
        print(f"Pasta {pasta_cookies} recriada.")
    except Exception as e:
        print(f"Ocorreu um erro ao limpar a pasta {pasta_cookies}: {e}")

def abrir_fechar_guia():
    global navegador
    print("abrir_fechar_guia")
    tentativas = 0

    while True:
        try:
            # Verifique se há mais de uma guia aberta
            if len(navegador.window_handles) > 1:
                # Mude para a segunda guia
                navegador.switch_to.window(navegador.window_handles[-1])

                # Feche a segunda guia
                navegador.close()

                # Mude para a primeira guia, se ainda existir
                if len(navegador.window_handles) > 0:
                    navegador.switch_to.window(navegador.window_handles[0])

                    # Aguarde até que a primeira guia esteja ativa
                    WebDriverWait(navegador, 5).until(EC.number_of_windows_to_be(1))

            else:
                if len(navegador.window_handles) == 1:
                    print('mandando abrir uma nova guia')
                    # Abrir uma nova guia com o atalho 'Ctrl + T'
                    pyautogui.hotkey('ctrl', 't')

                    # Aguarde até que haja pelo menos duas guias abertas
                    WebDriverWait(navegador, 10).until(lambda x: len(x.window_handles) >= 2)

                    if len(navegador.window_handles) == 2:
                        print('Duas guias abertas')
                        time.sleep(1)
                        navegador.switch_to.window(navegador.window_handles[0])
                        # Feche a primeira guia
                        navegador.close()

                        # Aguarde até que haja apenas uma guia aberta
                        WebDriverWait(navegador, 5).until(lambda x: len(x.window_handles) == 1)

                        if len(navegador.window_handles) == 1:
                            print('Uma guia aberta')
                            time.sleep(1)
                            # Mude para a guia restante
                            navegador.switch_to.window(navegador.window_handles[0])

                            # Aguarde até que a guia esteja ativa
                            WebDriverWait(navegador, 5).until(EC.number_of_windows_to_be(1))

                            # Verifique se o foco está na guia correta
                            if navegador.current_window_handle != navegador.window_handles[0]:
                                print("O foco não está na primeira guia.")
                            else:
                                print("O foco está na primeira guia.")
                                # Aqui você pode carregar a URL desejada
                                # colocar_url(url_sair)
                                navegador.execute_script("window.location.href = '{}';".format(url_sair))
                                # navegador.execute_script("window.location.replace('{}');".format(url_sair))
                                print('URL colocada com sucesso')
                                return
        except Exception as e:
            print(f"Tentativa {tentativas + 1} falhou. Erro: {e}")
            tentativas += 1

    print(f"Atenção: Todas as {max_tentativas} tentativas falharam. Encerrando.")
    return

def limpar_navegador():
    try:
        # Limpar cookies, cache, autenticação e histórico via DevTools
        print("Limpando dados via DevTools...")
        navegador.execute_cdp_cmd('Network.clearBrowserCookies', {})
        navegador.execute_cdp_cmd('Network.clearBrowserCache', {})
        navegador.execute_cdp_cmd('Performance.disable', {})
        navegador.execute_cdp_cmd('Page.resetNavigationHistory', {})
        print("Dados de cache, cookies e histórico limpos via DevTools.")
    except Exception as e:
        print(f"Erro ao limpar dados via DevTools: {e}")

    try:
        # Deletar todos os cookies
        print("Deletando cookies...")
        navegador.delete_all_cookies()
    except Exception as e:
        print(f"Erro ao deletar cookies: {e}")

    try:
        # Limpar o localStorage
        print("Limpando localStorage...")
        navegador.execute_script("window.localStorage.clear();")
    except Exception as e:
        print(f"Erro ao limpar localStorage: {e}")

    try:
        # Limpar o sessionStorage
        print("Limpando sessionStorage...")
        navegador.execute_script("window.sessionStorage.clear();")
    except Exception as e:
        print(f"Erro ao limpar sessionStorage: {e}")

    try:
        # Deletar cookies manualmente com JavaScript
        print("Deletando cookies manualmente com JavaScript...")
        navegador.execute_script("""
            var cookies = document.cookie.split(";");
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i];
                var eqPos = cookie.indexOf("=");
                var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
                document.cookie = name + '=;expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
            }
        """)
    except Exception as e:
        print(f"Erro ao deletar cookies manualmente: {e}")

    try:
        # Limpar IndexedDB
        print("Limpando IndexedDB...")
        navegador.execute_script("indexedDB.databases().then(dbs => dbs.forEach(db => indexedDB.deleteDatabase(db.name)));")
    except Exception as e:
        print(f"Erro ao limpar IndexedDB: {e}")

    try:
        # Limpar Service Workers
        print("Limpando Service Workers...")
        navegador.execute_script("""
            if ('serviceWorker' in navigator) {
                navigator.serviceWorker.getRegistrations().then(function(registrations) {
                    for (let registration of registrations) {
                        registration.unregister();
                    }
                });
            }
        """)
    except Exception as e:
        print(f"Erro ao limpar Service Workers: {e}")

    # try:
    #     navegador.execute_script(script)
    # except Exception as e:
    #     print(f"Erro ao limpar script: {e}")



    print("Limpeza do navegador concluída.\n\n")


def sair_face():
    global navegador, proxy_ativo
    navegador.set_page_load_timeout(5)

    while True:
        print("\n   Sair do facebook    \n")
        cookies = navegador.get_cookies()
        print(f"Cookies presentes\n\n: {cookies}\n\n")

        try:
            while True:
                navegador.switch_to.window(navegador.window_handles[0])

                try:

                    navegador.execute_script(script)

                    limpar_navegador()

                    url_atual = pega_url()
                    print('\n\nUrl SAIR , CORRETO', url_atual, '\n\n')
                    if url_sair in url_atual:
                        cookies = navegador.get_cookies()
                        if len(cookies) == 0:
                            print("Todos os cookies foram deletados com sucesso.")
                            limpar_navegador()
                            limpar_pasta_cookies(pasta_cookies)
                            break
                        else:
                            print(f"Alguns cookies ainda permanecem: {cookies}")

                except Exception as e:
                    print(f"Erro ao limpar script: {e}")

                limpar_navegador()


            abrir_fechar_guia()
            limpar_navegador()
            print("nova guia ok")

            url_atual = pega_url()
            print('urla apos sair do facebook', url_atual)
            if url_sair in url_atual:
                cookies = navegador.get_cookies()
                if len(cookies) == 0:
                    print("Todos os cookies foram deletados com sucesso.")
                    WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
                    print('Pagina pronta, conta NÃO logada')
                    if proxy_ativo:
                        desativar_proxy()
                    navegador.set_page_load_timeout(50)
                    return
                else:
                    print(f"Alguns cookies ainda permanecem: {cookies}")

        except Exception as e:
            print("Erro ao sair...", e)

            try:
                # Esperar até que o elemento "Não é você?" seja clicável
                elemento_nao_e_voce = WebDriverWait(navegador, 3).until(EC.element_to_be_clickable((By.ID, 'not_me_link')))

                # Clicar no elemento
                print('Clicar no elemento nao_e_voce')
                elemento_nao_e_voce.click()
                print('espera 2s')
                time.sleep(2)

            except Exception as e:
                print("Elemento não encontrado na página.", e)
                atualizar_navegador()





def busca_link():
    global navegador
    print('busca_link')

    if nome_usuario == "PokerIP":  # and (nome_computador == "PC-I5-8600K"):
        id = "Luis.gustavo.almeida88"
        senha = "020996Pa"

    elif nome_usuario == "lgagu":  # and (nome_computador == "PC-I7-9700KF"):
        id = "Luis.gustavo.almeida88"
        senha = "020996Pa"
        # id = "stefaniaalmeida.jf"
        # senha = "$TE20091992te"

    else:  # nome_usuario == "PokerIP": #and (nome_computador == "PC-i3-8145U"):
        id = "Luis.gustavo.almeida88"
        senha = "020996Pa"

    url = "https://pt-br.facebook.com/"

    # navegador.get(url)
    colocar_url(url)

    time.sleep(3)

    if se_esta_lagado() is True:
        sair_face()

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
    print('Endereço da fanpage')
    pagina_do_facebook = "https://www.facebook.com/people/Poker-Brasil/100064546038812/"
    # navegador.get(pagina_do_facebook)
    colocar_url(pagina_do_facebook)
    print(' agurade 7 segundas para a pagina carregar')
    time.sleep(7)
    # Procurar o primeiro link que começa com o padrão especificado postado na descrição da imagem
    try:
        links = navegador.find_elements(By.CSS_SELECTOR, "a[href]")
        for link in links:
            # print(link.get_attribute("href"))
            href = link.get_attribute("href")
            # Verificar se a URL começa com o padrão especificado
            if href.startswith("https://l.facebook.com/l.php?u=https%3A%2F%2Fbr-texas.rallyacespoker.com%2Fapplink%"):
                print(f"\nURL valida:\n {href}")
                link.click()
                print('Espera a pagina ficar carregada...')
                time.sleep(7)
                break
            # else:
            #     print(f"\nURL invalida:\n {href}")
    except Exception as e:
        print(e)

    # Obtém todos os identificadores de guias abertas
    guias_abertas = navegador.window_handles

    # Verifica o número de guias abertas
    if len(guias_abertas) == 2:

        print("Existem duas guias abertas, continua.")
        encontrado, descricao = link_segunda_guia()
        if encontrado:
            print('Link encontrado')
            return encontrado, descricao
    else:
        print("\n\n Não existem duas guias abertas, tentativa se achar uma imagem com o link.")
        # Procurar uma imagem que tenha o link guardado dentro
        try:
            # Encontrar todos os elementos de imagem na página
            elementos_imagem = navegador.find_elements(By.TAG_NAME, 'img')
            # Iterar sobre os elementos de imagem e verificar se a URL começa com o padrão desejado
            for elemento in elementos_imagem:
                url_imagem = elemento.get_attribute('src')
                # print(url_imagem)
                # Verificar se a URL começa com o padrão especificado
                if url_imagem.startswith("https://external."):
                    print(f"\nURL valida:\n {url_imagem}")
                    # Se encontrar a URL válida, clicar no elemento e sair do loop
                    elemento.click()
                    print('Espera a pagina ficar carregada...')
                    time.sleep(7)
                    break
                # else:
                #     print(f"\nURL invalida:\n {url_imagem}")

            guias_abertas = navegador.window_handles
            if len(guias_abertas) == 2:
                print("Existem duas guias abertas, continua.")
                encontrado, descricao = link_segunda_guia()
                if encontrado:
                    print('Link encontrado')
                    return encontrado, descricao
        except Exception as e:
            print(e)

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

        return False, "link nao encontrado"


def link_segunda_guia():
    print('Procurando link na segunda guia ')
    # Alterne o foco para a nova guia (segunda guia)
    navegador.switch_to.window(navegador.window_handles[1])
    time.sleep(5)
    # Pegar o link da barra de endereço do navegador
    link_da_barra_de_endereco = navegador.current_url
    print('link da barra de endereços: ', link_da_barra_de_endereco)
    # Feche a segunda guia
    navegador.close()
    # Volte para a primeira guia, se necessário
    navegador.switch_to.window(navegador.window_handles[0])
    # Verificar se a URL começa com o padrão desejado
    padrao_desejado_1 = "https://apps.facebook.com/pokerbrasil?"
    padrao_desejado_2 = "https://webgame.rallyacespoker.com/index.html?"
    if link_da_barra_de_endereco.startswith(padrao_desejado_1):
        print("A URL começa com o padrão desejado 1.")
        print(link_da_barra_de_endereco)
        return True, link_da_barra_de_endereco
    elif link_da_barra_de_endereco.startswith(padrao_desejado_2):
        print("A URL começa com o padrão desejado 2.")
        print(link_da_barra_de_endereco)
        # Capturando a parte após o último "="
        parte_final = link_da_barra_de_endereco.split('Params=')[-1]
        # removendo parte nao exsencial removendo o fim depois do igual
        if "=" in parte_final:
            parte_central = parte_final.split('=')[0]

        inicio = "https://apps.facebook.com/pokerbrasil?ref=fb_page&vtype&amfmethod=appLinkFanPageAward&SignedParams="
        reconstruido = inicio + parte_central
        print('Link reconstruido: ', reconstruido)
        return True, reconstruido
    else:
        print("link fanpag fora do padrão")
    return False, "link fanpag fora do padrão"


######################################################################################################################
# # # # para abrir o navegador e deixar abero. Descomentar as duas linhas abaixo
# cria_nevegador()
# time.sleep(10000)
# # sair_face('https://apps.facebook.com/poker_italia')
# mudar_proxy_dinamico('91.123.10.63:6605:sybzonhv:t096lck1sung')
# time.sleep(6000)
# desativar_proxy()
# time.sleep(120)
