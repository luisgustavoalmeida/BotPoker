import os
import time

import pyautogui
import pygetwindow as gw
import undetected_chromedriver as uc
from fake_useragent import UserAgent
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import IP
from F5_navegador import atualizar_navegador
from Requerimentos import nome_usuario

# Desabilitar o fail-safe
pyautogui.FAILSAFE = False

pasta_cookies = os.path.join(os.getcwd(), fr'C:\Cookie\{nome_usuario}')
navegador = None
url = None
id = ''
senha = ''

def get_random_user_agent():
    return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.84 Safari/537.36"
    # user_agents = [
    #     # Google Chrome
    #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.84 Safari/537.36",
    #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    #
    #     # Mozilla Firefox
    #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0",
    #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
    #
    #     # Safari
    #     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Version/15.1 Safari/537.36",
    #     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:14.1) Gecko/20100101 Firefox/14.1",  # Firefox for Mac
    #
    #     # Microsoft Edge
    #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0",
    #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; AS; Microsoft Outlook 16.0; MSIE 11.0; Windows NT 10.0; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/18.17763",
    #
    #     # Opera
    #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Opera/75.0.3969.149) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    #
    #     # Dispositivos Móveis
    #     "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/537.36",
    #     "Mozilla/5.0 (Android 12; Mobile; rv:108.0) Gecko/108.0 Firefox/108.0",
    #
    #     # Tablets
    #     "Mozilla/5.0 (iPad; CPU OS 16_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/16.0 Safari/537.36",
    #     "Mozilla/5.0 (Android 12; Tablet; rv:106.0) Gecko/106.0 Firefox/106.0",
    # ]
    # return random.choice(user_agents)
    # ua = UserAgent()
    # while True:
    #     user_agent = ua.random
    #     # Verifica se o User-Agent contém palavras que indicam dispositivos móveis
    #     if any(keyword in user_agent for keyword in ["Mobile", "iPhone", "Android", "iPad", "Tablet"]):
    #         continue  # Ignora User-Agent de dispositivos móveis e tenta novamente
    #     print(user_agent)
    #     return user_agent


def cria_nevegador():
    global navegador  # Referenciar a variável global
    while True:
        try:
            print('Carregando opções do navegador')
            # Criar um objeto 'Options' para definir as opções do Chrome
            options = uc.ChromeOptions()
            options.add_argument(f"--user-agent={get_random_user_agent()}")
            options.add_argument("--accept-language=pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7")
            options.add_argument("--accept-encoding=gzip, deflate, br")
            options.add_argument("--referer=https://www.facebook.com/people/Poker-Italia/100068008035507/")
            options.add_argument("--connection=keep-alive")
            options.add_argument("--disable-blink-features=AutomationControlled")  # Desativa a detecção de automação
            options.add_argument("--disable-notifications")  # Desativa as notificações
            options.add_argument("--disable-extensions")  # Desativa extensões
            options.add_argument("--disable-cache")  # Desativa o cache
            # options.add_argument("--incognito")  # Usa o modo de navegação anônima
            options.add_argument("--no-sandbox")  # Desativa o sandboxing
            options.add_argument("--disable-dev-shm-usage")  # Desativa o uso do compartilhamento de memória
            options.add_argument("--disable-save-password-bubble")  # desabilitará a caixa de diálogo para salvar senhas do navegador
            options.add_argument("--disable-password-generation")  # desabilita a geração automática de senhas pelo navegado
            options.add_argument("--disable-autofill")  # desabilitará o recurso de preenchimento automático de formulários do navegador.
            options.add_argument("--disable-geolocation")  # desativar localização.
            options.add_argument("--mute-audio")  # desativar o áudio
            options.add_argument("--disable-save-password-bubble")  # desabilitará a caixa de diálogo para salvar senhas do navegador
            # options.add_argument("--disable-infobars")  # Desabilitar a barra de informações do Chrome
            options.add_argument("--disable-autofill")  # desabilitará o recurso de preenchimento automático de formulários do navegador.
            options.add_argument(f"--user-data-dir={pasta_cookies}")


            # Configuração adicional para bloquear pop-ups
            prefs = {
                "profile.default_content_setting_values.notifications": 2,  # Bloqueia notificações
                "profile.default_content_setting_values.popups": 2,  # Bloqueia pop-ups
            }
            options.add_experimental_option("prefs", prefs)

            print('Criando o navegador')

            # undetected-chromedriver
            # Inicializa o driver do navegador com undetected-chromedriver
            navegador = uc.Chrome(options=options)
            # Redefina o tempo limite para XX segundos
            navegador.set_page_load_timeout(80)
            # Definir o tamanho da janela # largura altura options.add_argument
            navegador.set_window_size(1380, 1060)
            # Mover a janela para a posição (0,0) da tela
            navegador.set_window_position(-8, -5)

            print('Navegador criado com sucesso')

            return navegador
        except Exception as e:
            print("Erro ao criar o navegador:", e)
            time.sleep(1)
            # fechar_janelas_chrome()
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
            navegador.get(url)
            # colocar_url(url)
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
    intervalo = 2
    while True:
        try:
            navegador.get(url_colocar)
            # Sucesso na conexão, sair do loop
            return True
        except Exception as e:
            print('\n erro: \n', e, '\n')

            print(f"Tentativa {tentativa + 1} falhou. Sem conexão. Tentando novamente em {intervalo} segundos...\n")
            time.sleep(intervalo)
        IP.tem_internet()


def fazer_login(id_novo='', senha_novo='', url_novo='', loga_pk=True, loga_face=False):
    global navegador, url, id, senha

    if url != url_novo and url_novo != '':
        url = url_novo

    if id_novo != '':
        id = id_novo
        senha = senha_novo

    if loga_pk is False:
        # navegador.get(url)
        colocar_url(url)
        time.sleep(2)

    while True:

        if se_esta_lagado():
            sair_face(url)

        print("faz login")
        IP.tem_internet()
        # print('continua login')
        url_atual = pega_url()

        if ("pt-br.facebook.com" in url_atual) or (("facebook.com" in url_atual) and loga_pk) or (not loga_pk and ("facebook.com" in url_atual)):
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
                # time.sleep(2)
                for _ in range(100):
                    url_atual = pega_url()
                    # print(url_atual)
                    if ('https://www.facebook.com/' in url_atual) or ('https://web.facebook.com/' in url_atual):
                        # navegador.get(url)
                        colocar_url(url)
                        print('coloca url do jogo')
                        # time.sleep(2)
                        break
                    time.sleep(0.05)
                    if "/login/?privacy" in url_atual or "/device-based/regular/login/?" in url_atual:
                        print("senha incorreta")
                        print('manda sair')
                        sair_face(url)

                        entrou = False
                        status = "Senha incorreta"
                        return entrou, status

                print('url testa logado ', url_atual)
                for i in range(20):

                    for _ in range(100):
                        url_atual = pega_url()
                        if "/login/" not in url_atual:
                            print('url com /login/')
                            break
                        time.sleep(0.02)

                        if "/login/?privacy" in url_atual or "/device-based/regular/login/?" in url_atual:
                            print("senha incorreta")
                            print('manda sair')
                            sair_face(url)

                            entrou = False
                            status = "Senha incorreta"
                            return entrou, status

                    if "/login/" not in url_atual:

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
                            elemento_clicavel_encontrado = False
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
                            # navegador.get(url)
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
                                # navegador.get(url)
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
                            # navegador.get(url)
                            colocar_url(url)
                            time.sleep(5)

                    elif "/login/?privacy" in url_atual or "/device-based/regular/login/?" in url_atual:
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
                            except Exception as e:
                                print(f'Elemento "{item}" não encontrado')

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
            # time.sleep(5)
            sair_face(url)


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


def abrir_fechar_guia(max_tentativas=5):
    global navegador, url
    print("abrir_fechar_guia")
    tentativas = 0

    while tentativas < max_tentativas:
        try:
            # Verifique se há mais de uma guia aberta
            if len(navegador.window_handles) > 1:
                # Mude para a segunda guia
                navegador.switch_to.window(navegador.window_handles[1])

                # Feche a segunda guia
                navegador.close()

                # Mude para a primeira guia
                navegador.switch_to.window(navegador.window_handles[0])

                # Aguarde até que a primeira guia esteja ativa
                WebDriverWait(navegador, 5).until(EC.number_of_windows_to_be(1))

            else:
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
                    # navegador.get(url)
                    # colocar_url(url)
                    url_sair = 'https://pt-br.facebook.com/'
                    navegador.get(url_sair)
                    return

        except Exception as e:
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

        url_sair = 'https://pt-br.facebook.com/'

        script = """javascript:void(function(){ function deleteAllCookiesFromCurrentDomain() { var cookies = document.cookie.split("; "); for (var c = 0; c < cookies.length; c++) { var d = window.location.hostname.split("."); while (d.length > 0) { var cookieBase = encodeURIComponent(cookies[c].split(";")[0].split("=")[0]) + '=; expires=Thu, 01-Jan-1970 00:00:01 GMT; domain=' + d.join('.') + ' ;path='; var p = location.pathname.split('/'); document.cookie = cookieBase + '/'; while (p.length > 0) { document.cookie = cookieBase + p.join('/'); p.pop(); }; d.shift(); } } } deleteAllCookiesFromCurrentDomain(); location.href = '""" + url_sair + """'; })();"""

        try:
            print('inicia a execução do script sair')
            navegador.switch_to.window(navegador.window_handles[0])
            navegador.execute_script(script)
            print('script sair executado sem erros')

            # Exclui todos os cookies
            # navegador.delete_all_cookies()
            # print('deletar cookes')

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
                url_sair = 'https://pt-br.facebook.com/'
                navegador.get(url_sair)
                print("testa se tem nao é vc")

            except Exception as e:
                print("Erro ao sair.", e)
                atualizar_navegador()

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
                atualizar_navegador()


def atualizar_pagina():
    global navegador, url
    while True:
        IP.tem_internet()  # testa se tem internete enste de atualizar a pagina
        try:
            navegador.get(url)
            # colocar_url(url)
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
    print('Endereço da fanpage')
    pagina_do_facebook = "https://www.facebook.com/people/Poker-Brasil/100064546038812/"
    navegador.get(pagina_do_facebook)
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
# # para abrir o navegador e deixar abero. Descomentar as duas linhas abaixo
# cria_nevegador()
# busca_link()
# time.sleep(10000)
