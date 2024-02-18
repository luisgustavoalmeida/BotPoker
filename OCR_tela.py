import difflib
import os
import re
import time
from difflib import SequenceMatcher

import cv2
import numpy
import pyautogui
import pytesseract
# import Origem_pg
from fuzzywuzzy import fuzz

import IP
import Variaveis_Globais

# Desabilitar o fail-safe
pyautogui.FAILSAFE = False

'''
--psm 0: Modo de segmentação automática com detecção de bloco.
--psm 1: Modo de segmentação automática com detecção de linha.
--psm 2: Modo de segmentação automática com detecção de palavra.
--psm 3: Modo totalmente automático com detecção de bloco.
--psm 4: Modo de segmentação de caractere único.
--psm 5: Modo de segmentação de palavra única.
--psm 6: Modo de segmentação de bloco de texto com detecção automática de linhas.
--psm 7: Modo tratamento de imagem - Linha única, sem OCR.
--psm 8: Modo tratamento de imagem - Palavra única, sem OCR.
--psm 9: Modo tratamento de imagem - Caractere único, sem OCR.
--psm 10: Modo tratamento de imagem - Tratamento de imagem por OSD.
--oem 0: Usar o Tesseract OCR Engine padrão.
--oem 1: Usar o Tesseract OCR Engine LSTM.
--oem 2: Usar o Tesseract OCR Engine com LSTM apenas para treinamento.
--oem 3: Usar o Tesseract OCR Engine com LSTM apenas para inferência.
-c tessedit_char_whitelist=0123456789: Restringir o OCR apenas aos caracteres
-c tessedit_char_blacklist=abcde: Excluir caracteres específicos do OCR. Nesse exemplo, os caracteres 'a', 'b', 'c', 'd' e 'e' serão excluídos da análise.
-l eng: Definir o idioma do OCR. Nesse exemplo, o idioma é definido como inglês. Você pode substituir "eng" pelo código de idioma adequado, como "por" para português.
-psm 11: Modo tratamento de imagem - Sparse text. Usado para texto com layout irregular ou não estruturado.
-psm 12: Modo tratamento de imagem - Sparse text com OSD. Similar ao modo 11, mas com detecção de orientação e script
-e textonly_pdf=1: Gera um arquivo PDF contendo apenas o texto extraído, sem imagens ou formatação.
-c preserve_interword_spaces=1: Preserva os espaços entre as palavras durante a extração do texto.
-c textord_tabfind_show_vlines=1: Exibe linhas verticais encontradas durante o processo de detecção de tabelas.
-c textord_tabfind_find_tables=1: Ativa a detecção automática de tabelas.
-c textord_tabfind_find_tables_recursive=1: Ativa a detecção recursiva de tabelas, útil para tabelas aninhadas.
-c tessedit_create_hocr=1: Gera um arquivo HOCR (HTML OCR) contendo o texto extraído com informações de layout e formatação.
-c hocr_font_info=1: Inclui informações sobre a fonte no arquivo HOCR gerado.
-c hocr_char_boxes=1: Inclui informações sobre os limites de cada caractere no arquivo HOCR gerado.

0 (Orientação e Detecção de Blocos de Texto (OSD) somente):

Descrição: Tesseract tenta determinar a orientação e a detecção de blocos de texto sem executar a OCR.
Observações: Pode ser útil quando você deseja apenas obter informações sobre a orientação e a localização dos blocos de texto.
python
Copy code
custom_config = r'--psm 0'
1 (Auto-segmentação de Página com OSD):

Descrição: Tesseract tenta automaticamente segmentar a página, incluindo a detecção de orientação e detecção de blocos de texto.
Observações: É a opção padrão para segmentação de páginas.
python
Copy code
custom_config = r'--psm 1'
2 (Auto-segmentação de Página, mas sem OSD ou OCR):

Descrição: Tesseract tenta automaticamente segmentar a página sem realizar a detecção de orientação ou OCR.
Observações: Pode ser útil quando você deseja apenas a segmentação da página, sem processamento adicional.
python
Copy code
custom_config = r'--psm 2'
3 (Totalmente Automático, mas sem OSD ou OCR):

Descrição: Tesseract tenta realizar a segmentação de página totalmente automaticamente sem executar a detecção de orientação ou OCR.
Observações: Adequado para casos em que a segmentação automática é a principal prioridade.
python
Copy code
custom_config = r'--psm 3'
4 (Assumir uma única coluna de texto de uma imagem):

Descrição: Tesseract assume que há uma única coluna de texto na imagem.
Observações: Pode ser útil quando você está lidando com uma imagem que contém apenas uma coluna de texto.
python
Copy code
custom_config = r'--psm 4'
5 (Assumir uma única coluna de texto de uma imagem com OCR):

Descrição: Similar ao modo 4, mas também executa a OCR.
Observações: Útil quando você deseja obter texto de uma única coluna de texto.
python
Copy code
custom_config = r'--psm 5'

6 (Assumir uma única linha de texto de uma imagem):

Descrição: Tesseract assume que há uma única linha de texto na imagem.
Observações: Útil quando a imagem contém uma única linha de texto.
python
Copy code
custom_config = r'--psm 6'
7 (Assumir uma única palavra de texto de uma imagem):

Descrição: Tesseract assume que há uma única palavra de texto na imagem.
Observações: Pode ser útil para segmentar e reconhecer palavras isoladas.
python
Copy code
custom_config = r'--psm 7'
8 (Assumir uma única palavra de texto de uma imagem com OCR):

Descrição: Similar ao modo 7, mas também executa a OCR.
Observações: Útil quando você deseja reconhecer uma única palavra em uma imagem.
python
Copy code
custom_config = r'--psm 8'
9 (Assumir uma única palavra de texto de uma imagem, tentando encontrar uma coleção de caracteres):

Descrição: Tesseract tenta encontrar uma coleção de caracteres correspondentes a uma palavra.
Observações: Pode ser útil em situações em que as palavras não estão completamente separadas.
python
Copy code
custom_config = r'--psm 9'
10 (Assumir um único caractere):

Descrição: Tesseract assume que há um único caractere na imagem.
Observações: Pode ser usado para segmentar e reconhecer caracteres individuais.
python
Copy code
custom_config = r'--psm 10'
11 (Sparse text. Encontrar todos os pequenos componentes de texto):

Descrição: Tesseract tenta encontrar todos os pequenos componentes de texto na imagem.
Observações: Útil quando há texto esparsamente distribuído na imagem.
python
Copy code
custom_config = r'--psm 11'
12 (Sparse text with OSD):

Descrição: Similar ao modo 11, mas inclui a detecção de orientação e detecção de blocos de texto.
Observações: Adequado quando há texto esparsamente distribuído, e você precisa de informações sobre orientação e blocos de texto.
python
Copy code
custom_config = r'--psm 12'
13 (Raw line. Tratar a imagem como uma única linha de texto):

Descrição: Trata a imagem como uma única linha de texto, sem realizar a segmentação de palavras.
Observações: Útil quando o texto na imagem é uma única linha contínua.
python
Copy code
custom_config = r'--psm 13'
14 (Raw line with OSD):

Descrição: Similar ao modo 13, mas inclui a detecção de orientação e detecção de blocos de texto.
Observações: Adequado quando o texto na imagem é uma única linha contínua e você precisa de informações sobre orientação e blocos de texto.
python
Copy code
custom_config = r'--psm 14'

15 (Assumir um único bloco de texto vertical de uma imagem):

Descrição: Tesseract assume que há um único bloco de texto vertical na imagem.
Observações: Útil quando o texto está disposto verticalmente.
python
Copy code
custom_config = r'--psm 15'
16 (Assumir um único bloco de texto vertical de uma imagem com OCR):

Descrição: Similar ao modo 15, mas também executa a OCR.
Observações: Adequado quando você deseja reconhecer um único bloco de texto vertical.
python
Copy code
custom_config = r'--psm 16'
17 (Assumir um único bloco de texto de uma imagem):

Descrição: Tesseract assume que há um único bloco de texto na imagem.
Observações: Útil quando há uma única região contendo texto na imagem.
python
Copy code
custom_config = r'--psm 17'
18 (Assumir um único bloco de texto de uma imagem com OCR):

Descrição: Similar ao modo 17, mas também executa a OCR.
Observações: Adequado quando você deseja reconhecer um único bloco de texto na imagem.
python
Copy code
custom_config = r'--psm 18'
19 (Assumir um único bloco de texto de uma imagem, tentando encontrar uma coleção de caracteres):

Descrição: Tesseract tenta encontrar uma coleção de caracteres correspondentes a um bloco de texto.
Observações: Pode ser útil quando os caracteres estão próximos, mas não totalmente conectados.
python
Copy code
custom_config = r'--psm 19'
20 (Assumir uma única palavra de texto de uma imagem, mas com análise automática de layout):

Descrição: Similar ao modo 8, mas com análise automática de layout.
Observações: Adequado quando a imagem contém uma única palavra e a análise do layout é importante.
python
Copy code
custom_config = r'--psm 20'
21 (Assumir um único bloco de texto de uma imagem, mas com análise automática de layout):

Descrição: Similar ao modo 18, mas com análise automática de layout.
Observações: Útil quando há um único bloco de texto na imagem e a análise do layout é importante.
python
Copy code
custom_config = r'--psm 21'

22 (Assumir um único bloco de texto de uma imagem, mas com análise automática de layout e OCR):

Descrição: Similar ao modo 21, mas também executa a OCR.
Observações: Adequado quando há um único bloco de texto na imagem, a análise do layout é importante, e você deseja realizar a OCR.
python
Copy code
custom_config = r'--psm 22'
23 (Assumir um único bloco de texto vertical de uma imagem, mas com análise automática de layout):

Descrição: Similar ao modo 15, mas com análise automática de layout.
Observações: Adequado quando o texto está disposto verticalmente, e a análise do layout é importante.
python
Copy code
custom_config = r'--psm 23'
24 (Assumir um único bloco de texto vertical de uma imagem, mas com análise automática de layout e OCR):

Descrição: Similar ao modo 23, mas também executa a OCR.
Observações: Adequado quando o texto está disposto verticalmente, a análise do layout é importante, e você deseja realizar a OCR.
python
Copy code
custom_config = r'--psm 24'
25 (Assumir um script totalmente não estruturado de uma imagem):

Descrição: Tesseract tenta reconhecer um script totalmente não estruturado.
Observações: Útil quando o texto não segue uma estrutura definida.
python
Copy code
custom_config = r'--psm 25'
26 (Assumir um script totalmente não estruturado de uma imagem com OCR):

Descrição: Similar ao modo 25, mas também executa a OCR.
Observações: Adequado quando o texto não segue uma estrutura definida, e você deseja realizar a OCR.
python
Copy code
custom_config = r'--psm 26'
27 (Assumir um único bloco de texto vertical de uma imagem com análise automática de layout e OCR):

Descrição: Combina o modo 24 com a análise automática de layout.
Observações: Adequado quando o texto está disposto verticalmente, a análise do layout é importante, e você deseja realizar a OCR.
python
Copy code
custom_config = r'--psm 27'

'''

## caminho do tesseract # C:\Program Files\Tesseract-OCR
## para funcionar corretametne o Tesseract tem que estar instalado a baixo tem links de ajuda
## https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i?newreg=e845d9256ce84548ab80ff4b5f241429
## https://github.com/UB-Mannheim/tesseract/wiki
# https://www.youtube.com/watch?v=Wx3SyNwZtsA&t=751s&ab_channel=HashtagPrograma%C3%A7%C3%A3o
# tem que coloar o arquivo "por.traineddata" de idioma de protugues no caminho C:\Program Files\Tesseract-OCR\tessdata
# Caminho para o executável do Tesseract
caminho_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# verifica se o caminho do executável do Tesseract é válido
if not os.path.isfile(caminho_tesseract):
    raise Exception("Caminho do executável do Tesseract inválido")


def OCR_regiao(regiao, config, inveter_cor=True, fator_ampliacao=1, contraste_pre=1, contraste_pos=1, esca_ciza=True):
    try:
        # captura a imagem da tela
        imagem = pyautogui.screenshot()

        # recorta a região de interesse da imagem
        imagem_recortada = imagem.crop(regiao)

        # Redimensiona a imagem, se necessário
        if fator_ampliacao != 1:
            imagem_recortada = imagem_recortada.resize((imagem_recortada.width * fator_ampliacao, imagem_recortada.height * fator_ampliacao))

        # print('Imagem recortada')
        # imagem_recortada.show()

        # Converte a imagem para um array numpy
        imagem_recortada = numpy.asarray(imagem_recortada)

        # Ajusta o contraste antes da conversão para escala de cinza
        if contraste_pre != 1:  # Fator de aumento de contraste (pode ser ajustado conforme necessário)
            imagem_recortada = cv2.convertScaleAbs(imagem_recortada, alpha=contraste_pre, beta=0)

        # Converte a imagem para escala de cinza
        if esca_ciza:
            imagem_recortada = cv2.cvtColor(imagem_recortada, cv2.COLOR_BGR2GRAY)

        # Inverte as cores da imagem
        if inveter_cor:
            imagem_recortada = cv2.bitwise_not(imagem_recortada)

        # Ajusta o contraste após a conversão para escala de cinza
        if contraste_pos != 1:
            imagem_recortada = cv2.convertScaleAbs(imagem_recortada, alpha=contraste_pos, beta=0)

        # print("iamgem cor invertida pos contraste")
        # cv2.imshow("Imagem", imagem_recortada)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # Passa o OCR na imagem recortada
        pytesseract.pytesseract.tesseract_cmd = caminho_tesseract
        texto = pytesseract.image_to_string(imagem_recortada, config=config, lang="por")
        # obs: colocar o arquivo de idioma "por.traineddata" no diretorio C:\Program Files\Tesseract-OCR\tessdata

        # deleta a imagem recortada
        del imagem_recortada
        del imagem

        if texto.strip():
            # Remove os espaços em branco no início e no final do texto
            texto = texto.strip()
            return texto
        else:
            print("Nenhum texto foi detectado.")
            return None

    except Exception as e:
        print("Erro ao executar OCR: ", e)
        return None


def tratar_valor_numerico(texto):
    """
    Remove caracteres não numéricos e converte o texto para um número inteiro.

    Parameters:
    - texto (str): Texto a ser tratado.

    Returns:
    - int: Valor inteiro obtido a partir do texto, ou 0 se não for possível converter.
    """
    try:
        # texto = ''.join(c for c in texto if c.isdigit())
        texto = re.sub(r"\D+", "", str(texto))  # Remove caracteres não numéricos
        return int(texto)
    except ValueError:
        print("Erro ao converter para inteiro.")
        return 0


def valor_fichas(x_origem, y_origem, valor_planilha="", fichas_perfil=""):
    """
    Esta função realiza a leitura do valor das fichas em uma determinada região da tela.

    Parameters:
    - x_origem (int): Coordenada x da origem da região.
    - y_origem (int): Coordenada y da origem da região.

    Returns:
    - int: O valor das fichas lido, ou 0 se nenhum valor válido for encontrado.
    """
    print('\n\n valor_fichas')

    # Configurações para o processo OCR
    inveter_cor = True
    esca_ciza = False
    fator_ampliacao = 3
    contraste_pre = 1
    contraste_pos = 1.6

    # Define a região de interesse para a leitura do valor
    regiao_ficha = (x_origem + 43, y_origem + 9, x_origem + 105, y_origem + 21)

    # Define a lista de configurações a serem testadas
    configuracoes = [
        r'--psm 7 --oem 0 -c tessedit_char_whitelist=0123456789.',
        r'--psm 7 --oem 1 -c tessedit_char_whitelist=0123456789.',
        r'--psm 8 --oem 0 -c tessedit_char_whitelist=0123456789.',
        r'--oem 3 --psm 6 outputbase digits',
    ]
    for _ in range(100):
        if pyautogui.pixelMatchesColor((x_origem + 121), (y_origem + 15), (255, 210, 77), tolerance=5):
            print('Valor de ficha no lugar correto')
            time.sleep(0.3)
            break
        time.sleep(0.02)

    # Itera sobre cada configuração e realiza o OCR
    for config in configuracoes:
        # print(config)
        # Realiza o OCR com a configuração atual
        lido = OCR_regiao(regiao_ficha, config, inveter_cor, fator_ampliacao, contraste_pre, contraste_pos, esca_ciza)
        print(lido)

        if lido is not None:
            # Converte o valor lido para um formato numérico
            valor = tratar_valor_numerico(lido)
            # Verifica se o valor está dentro da faixa desejada
            if 500 < valor < 50000000:
                print(f"Valor das fichas: {valor}")
                break
                # return valor
            else:
                print('Valor fora sa feixa esperado')
                # valor = 0
        elif lido is None:
            print('OCR nao recolheceu a imagem')
            valor = valor_fichas_perfil(x_origem, y_origem)

    print('valor_planilha', valor_planilha)
    print('fichas_perfil ', fichas_perfil)

    if valor_planilha != "":
        print('fichas e valor_fichas_level ')

        valor_planilha = tratar_valor_numerico(valor_planilha)
        print('Valor planilha: ', valor_planilha)

        if valor_planilha - 15000 < valor < valor_planilha + 15000:
            print('\n valor compativel com valor_planilha \n')
            return valor

    if fichas_perfil != "":
        fichas_perfil = tratar_valor_numerico(fichas_perfil)
        if valor_planilha - 15000 < fichas_perfil < valor_planilha + 15000:
            print('\n fichas_perfil compativel com valor_planilha  \n')
            return fichas_perfil

        if (valor - 15000) < fichas_perfil < (valor + 15000):
            print('\n fichas_perfil compativel com valor \n')
            return valor

    if valor_planilha != "":
        valor_perfil = valor_fichas_perfil(x_origem, y_origem)

        if valor_planilha - 15000 < valor_perfil < valor_planilha + 15000:
            print('\n valor_perfil compativel com valor_planilha \n')
            return valor_perfil

    if fichas_perfil != "":
        if valor - 15000 < valor_perfil < valor + 15000:
            print('\n valor_perfil compativel com valor \n')
            return valor_perfil

        if fichas_perfil - 15000 < valor_perfil < fichas_perfil + 15000:
            print('\n fichas_perfil compativel com fichas_perfil  \n')
            return valor_perfil

    if valor_planilha == "":
        return valor

    return valor_planilha


def valor_fichas_perfil(x_origem, y_origem):
    """
    Extrai e retorna o valor de fichas da conta.

    Parameters:
    - x_origem (int): Coordenada x da origem da janela.
    - y_origem (int): Coordenada y da origem da janela.

    Returns:
    - int: valor de fichas da conta ou 0 se não for encontrado ou estiver fora da faixa desejada.
    """
    print('valor_fichas_perfil')
    fichas = 0
    for _ in range(50):
        # clica para abrir a tela do perfil
        pyautogui.click(16 + x_origem, 24 + y_origem)
        # testa se a tela do perfil esta aberta
        if (pyautogui.pixelMatchesColor((x_origem + 241), (y_origem + 170), (227, 18, 5), tolerance=1)
                and pyautogui.pixelMatchesColor((x_origem + 406), (y_origem + 273), (116, 130, 139), tolerance=1)):
            time.sleep(0.3)
            break
        time.sleep(0.2)

    # Configurações para o processo OCR
    inveter_cor = False
    esca_ciza = True
    fator_ampliacao = 2
    contraste_pre = 1
    contraste_pos = 1
    regiao_ficha = (x_origem + 416, y_origem + 262, x_origem + 493, y_origem + 283)  # leval

    # Define a lista de configurações a serem testadas
    configuracoes = [
        r'--psm 6 --oem 3  outputbase digits',
        r'--psm 7 --oem 1 -c tessedit_char_whitelist=0123456789.',
        r'--psm 7 --oem 0 -c tessedit_char_whitelist=0123456789.',
        r'--psm 3 --oem 0 -c tessedit_char_whitelist=0123456789.',
        r'--psm 8 --oem 0 -c tessedit_char_whitelist=0123456789.',
    ]

    # Itera sobre cada configuração e realiza o OCR
    for config in configuracoes:
        # print(config)
        # Realiza o OCR com a configuração atual
        fichas = OCR_regiao(regiao_ficha, config, inveter_cor, fator_ampliacao, contraste_pre, contraste_pos, esca_ciza)
        print(fichas)
        if fichas is not None:
            fichas = tratar_valor_numerico(fichas)
            # Verifica se o valor está na faixa desejada
            if 500 < fichas < 50000000:
                print(f"Valor das fichas perfil: {fichas}")
                # clica para fechar a tela do perfil
                pyautogui.click(772 + x_origem, 160 + y_origem)
                return fichas
                # break
            else:
                print("Valor fora da faixa desejada")
                fichas = 0
        else:
            print("Erro na leitura do OCR")
            fichas = 0
    return fichas


def tempo_roleta(x_origem, y_origem):
    print('tempo_roleta')  # Imprime o nome da função
    inverter_cor = True
    escala_cinza = True
    fator_ampliacao = 1
    contraste_pre = 1
    contraste_pos = 1
    # config = '--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789:'
    regiao = (x_origem + 662, y_origem + 44, x_origem + 711, y_origem + 56)

    configuracoes = [
        r'--oem 3 --psm 6 outputbase digits',
        r'--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789:'
        r'--psm 7 --oem 0 -c tessedit_char_whitelist=0123456789:',
        r'--psm 7 --oem 1 -c tessedit_char_whitelist=0123456789:',
        r'--psm 8 --oem 0 -c tessedit_char_whitelist=0123456789:'
    ]

    for config in configuracoes:
        print(config)
        tempo = OCR_regiao(regiao, config, inverter_cor, fator_ampliacao, contraste_pre, contraste_pos, escala_cinza)
        print(tempo)
        if tempo is not None:
            tempo = tratar_valor_numerico(tempo)
            print("Tempo lido na roleta", tempo)
            return tempo
        else:
            print('OCR não reconheceu a imagem')
    return 0


def pontuacao_tarefas(x_origem, y_origem):
    """
    Esta função realiza a obtenção da pontuação em tarefas diárias em uma determinada região da tela.

    Parameters:
    - x_origem (int): Coordenada x da origem da região.
    - y_origem (int): Coordenada y da origem da região.

    Returns:
    - int: A pontuação obtida, ou 1 se nenhuma pontuação válida for encontrada.
    """
    print('pontuacao_tarefas')
    # Clica duas vezes no ícone de tarefas diárias para abrir a janela
    pyautogui.doubleClick(x_origem + 635, y_origem + 25)

    # Configurações para o processo OCR
    inveter_cor = True
    esca_ciza = True
    fator_ampliacao = 4
    contraste_pre = 1
    contraste_pos = 1.4
    # Define os valores possíveis de pontuação
    valores_possiveis = set(range(10, 201, 10))

    # Define a região de interesse para a leitura da pontuação
    regiao = (x_origem + 778, y_origem + 516, x_origem + 830, y_origem + 535)

    # Lista de configurações
    configuracoes = [
        r'--oem 3 --psm 6 outputbase digits',
        r'--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789/',
        r'--psm 6 --oem 1 -c tessedit_char_whitelist=0123456789/',
        r'--psm 6 -c tessedit_char_whitelist=0123456789/',
    ]

    # Itera sobre cada configuração e realiza o OCR
    for config in configuracoes:
        # print(config)
        for _ in range(4):
            # Clica duas vezes no ícone de tarefas diárias para abrir a janela
            pyautogui.doubleClick(x_origem + 635, y_origem + 25)

            # Realiza o OCR com a configuração atual
            pontuacao = OCR_regiao(regiao, config, inveter_cor, fator_ampliacao, contraste_pre, contraste_pos, esca_ciza)
            # print('pontuação:', pontuacao)

            # Verifica se a pontuação foi obtida com sucesso
            if pontuacao is not None and "200" in str(pontuacao) and len(str(pontuacao)) >= 5:
                pontuacao = tratar_valor_numerico(str(pontuacao)[:-3])
                # Verifica se a pontuação está entre os valores possíveis
                if pontuacao in valores_possiveis:
                    print("Pontuação obtida com sucesso:", pontuacao)
                    return pontuacao
            elif pontuacao is not None and "/200" in pontuacao:
                pontuacao = tratar_valor_numerico(pontuacao.split("/")[0])
                # Verifica se a pontuação está entre os valores possíveis
                if pontuacao in valores_possiveis:
                    print("Pontuação obtida com sucesso:", pontuacao)
                    return pontuacao
            else:
                print('Informação OCR fora do padrao')
            time.sleep(1)

    pontuacao = 1
    return pontuacao


def tarefas_diaris_posicao1(x_origem, y_origem):
    """
    Esta função realiza a leitura das tarefas diárias em uma região específica da tela.

    Parameters:
    - x_origem (int): Coordenada x da origem da região.
    - y_origem (int): Coordenada y da origem da região.

    Returns:
    - list: Uma lista de tarefas diárias lidas.
    """
    print('tarefas_diaris_posicao1')
    # Lista para armazenar as tarefas
    lista = []

    # Configurações para o OCR
    config = '--psm 6 --oem 1'
    inveter_cor = True
    esca_ciza = True
    fator_ampliacao = 1
    contraste_pre = 1
    contraste_pos = 1

    # Região de interesse para a leitura das tarefas diárias
    regiao = (x_origem + 274, y_origem + 267, x_origem + 589, y_origem + 551)

    # Clica duas vezes no ícone de tarefas diárias para abrir a janela
    pyautogui.doubleClick(x_origem + 635, y_origem + 25)  # clica no tarefas diarias
    time.sleep(0.2)

    # Executa o OCR na região de interesse
    texto = OCR_regiao(regiao, config, inveter_cor, fator_ampliacao, contraste_pre, contraste_pos, esca_ciza)
    # Verifica se o OCR retornou algum texto
    if texto is not None:
        lista = remover_termos(texto)
        # Retorna a lista de tarefas
        return lista
    else:
        # Se não foram encontradas tarefas, retorna uma lista vazia
        return lista


def tarefas_diaris_posicao2(x_origem, y_origem):
    """
    Esta função realiza a leitura das tarefas diárias em uma região específica da tela.
    Caso haja uma barra de rolagem, a função rola para garantir a leitura completa.

    Parameters:
    - x_origem (int): Coordenada x da origem da região.
    - y_origem (int): Coordenada y da origem da região.

    Returns:
    - list: Uma lista de tarefas diárias lidas.
    """
    print('tarefas_diaris_posicao2')
    lista = []
    # Verifica se há uma barra de rolagem na lista de tarefas
    if pyautogui.pixelMatchesColor((x_origem + 707), (y_origem + 280), (87, 0, 176), tolerance=3):
        # Itera para rolar e verificar se há mais tarefas
        for _ in range(50):
            pyautogui.doubleClick(708 + x_origem, 419 + y_origem)  # rola para ver se a tarefa esta na segunda parte
            # Testa se há barra de rolagem na lista de tarefas
            if pyautogui.pixelMatchesColor((x_origem + 707), (y_origem + 410), (87, 0, 176), tolerance=3):
                break
            time.sleep(0.1)

        # Configurações para o OCR
        config = '--psm 6 --oem 1'
        inveter_cor = True
        esca_ciza = True
        fator_ampliacao = 1
        contraste_pre = 1
        contraste_pos = 1

        # Região de interesse para a leitura das tarefas diárias
        regiao = (x_origem + 274, y_origem + 267, x_origem + 589, y_origem + 551)

        # Executa o OCR na região de interesse
        texto = OCR_regiao(regiao, config, inveter_cor, fator_ampliacao, contraste_pre, contraste_pos, esca_ciza)
        if texto is not None:
            lista = remover_termos(texto)
            # Retorna a lista de tarefas
            return lista
        else:
            # Se não foram encontradas tarefas, retorna uma lista vazia
            return lista
    return lista


def tarefas_diaris(x_origem, y_origem):
    """
    Esta função realiza a leitura das tarefas diárias em uma região específica da tela.

    Parameters:
    - x_origem (int): Coordenada x da origem da região.
    - y_origem (int): Coordenada y da origem da região.

    Returns:
    - list: Uma lista de tarefas diárias lidas.
    """
    print('tarefas_diaris')
    lista = []
    lista2 = []

    # Configurações para o OCR
    config = '--psm 6 --oem 1'
    inveter_cor = True
    esca_ciza = True
    fator_ampliacao = 1
    contraste_pre = 1
    contraste_pos = 1

    # Região de interesse para a leitura das tarefas diárias
    regiao = (x_origem + 274, y_origem + 267, x_origem + 589, y_origem + 551)

    # Clica duas vezes no ícone de tarefas diárias para abrir a janela
    pyautogui.doubleClick(x_origem + 635, y_origem + 25)  # clica no tarefas diarias
    time.sleep(0.2)

    # Executa o OCR na região de interesse
    texto = OCR_regiao(regiao, config, inveter_cor, fator_ampliacao, contraste_pre, contraste_pos, esca_ciza)

    # Verifica se o OCR retornou algum texto
    if texto is not None:
        lista = remover_termos(texto)
        # Testa se há barra de rolagem na lista de tarefas
        if pyautogui.pixelMatchesColor((x_origem + 707), (y_origem + 280), (87, 0, 176), tolerance=3):
            # Itera para rolar e verificar se há mais tarefas
            for i in range(50):
                pyautogui.doubleClick(708 + x_origem, 419 + y_origem)  # rola para ver se a tarefa esta na segunda parte
                # Testa se há barra de rolagem na lista de tarefas
                if pyautogui.pixelMatchesColor((x_origem + 707), (y_origem + 410), (87, 0, 176), tolerance=3):
                    break
                time.sleep(0.1)

            # Executa o OCR na região de interesse novamente
            texto = OCR_regiao(regiao, config, inveter_cor, fator_ampliacao, contraste_pre, contraste_pos, esca_ciza)

            # Verifica se o OCR retornou algum texto
            if texto is not None:
                lista2 = remover_termos(texto)
                # Testa se há tarefas na segunda parte e inclui na lista as não repetidas
                if lista2:  # testa se esta vazia
                    for item in lista2:
                        if item not in lista:
                            # inclui na lista o itens nao repitidos
                            lista.append(item)
        time.sleep(2)

    return lista


def tarefas_diaris_trocar(x_origem, y_origem):
    """
       Esta função realiza a troca de tarefas diárias em uma região específica da tela.

       Parameters:
       - x_origem (int): Coordenada x da origem da região.
       - y_origem (int): Coordenada y da origem da região.
       """
    print('tarefas_diaris_trocar')

    for i in range(2):
        pyautogui.doubleClick(x_origem + 635, y_origem + 25)  # clica no tarefas diarias
        if not pyautogui.pixelMatchesColor((x_origem + 174), (y_origem + 278), (247, 230, 255), tolerance=5):
            # testa se tem barra de rolagem na lista de tarefas
            print('A tarefa já foi trocada anteriormente.')
            return

        # Lista de tarefas para trocar
        para_trocar = ['Participe de um GIRE & GANHE/campeonato de eliminacao 1 vezes',
                       'Participe de um GIRE & GANHE/campeonato de eliminacao 2 vezes',
                       'Participe de um GIRE & GANHE/campeonato de eliminacao 3 vezes',
                       'Ganhar um premio em um GIRE & GANHE/torneio de eliminacao',
                       'Jogue 10 maos nas mesas OMAHA com blinds acima de 200',
                       'Jogue 20 maos nas mesas OMAHA com blinds acima de 200',
                       'Jogue 40 maos nas mesas OMAHA com blinds acima de 200',
                       'Ganhe 5 maos nas mesas OMAHA com blinds acima de 200',
                       'Ganhe 10 maos nas mesas OMAHA com blinds acima de 200',
                       'Ganhe 20 maos nas mesas OMAHA com blinds acima de 200',
                       'Ganhe 10.000 fichas nas mesas OMAHA',
                       'Ganhe 50.000 fichas nas mesas OMAHA',
                       'Ganhe 200.000 fichas nas mesas OMAHA',
                       'Jogue JACKS OR BETTER 10 vezes',
                       'Jogue JACKS OR BETTER 50 vezes',
                       'Jogue JACKS OR BETTER 100 vezes',
                       'Ganhe 10.000 fichas do JACKS OR BETTER',
                       'Ganhe 50.000 fichas do JACKS OR BETTER',
                       'Ganhe 200.000 fichas do JACKS OR BETTER',
                       'Consiga Flush ou qualquer mao superior nas mesas OMAHA',
                       'Ganhar 10 maos em uma mesa com blinds acima de 25',
                       'Jogar 20 mao em uma mesa com blinds acima de 25',
                       'Tirar Sequencia 1 vezes em mesas com blinds maiores que 25',
                       'Tirar trinca 1 vez em mesa com blinds maiores que 25',
                       'Tirar um flush ou quaquer maos superior 1 vez em mesas com blinds laiores que 25',
                       'Ganhar 10 maos em uma mesa com blinds acima de 50',
                       'Ganhar 20 maos em uma mesa com blinds acima de 50',
                       'Ganhar 30.000 fichas em mesas com blinds acima da 50',
                       'Jogar 20 mao em uma mesa com blinds acima de 50',
                       'Jogar 40 mao em uma mesa com blinds acima de 50',
                       'Tirar Flush ou qualquer mao superior 1 vez em mesas com blindes maiores que 25',
                       'Tirar Sequencia 1 vez em mesas com blinds maiores que 50',
                       'Tirar Sequencia 2 vezes em mesas com blinds maiores que 50',
                       'Tirar trinca 1 vez em mesas com blinds maiores que 50',
                       'Ganhar 20 maos em uma mesa com blinds acima de 100',
                       'Ganhar 100.000 fichas em mesas com blinds acima de 50',
                       'Ganhe 200.000 fichas em mesas com blinds acima de 100',
                       'Jogar 20 mao em uma mesa com blinds acima de 100',
                       'Jogar 40 mao em uma mesa com blinds acima de 100',
                       'Tirar Flush ou qualquer mao superior 1 vez em mesas com blindes maiores que 50',
                       'Tirar Flush ou qualquer mao superior 2 vezes em mesas com blinds maiores que 100',
                       'Tirar Sequencia 2 vezes em mesas com blinds maiores que 100',
                       'Tirar Trinca 2 vezes em mesas com blinds maiores que 100']

        # Configurações para o OCR
        config = '--psm 6 --oem 1'
        inveter_cor = True
        esca_ciza = True
        fator_ampliacao = 1
        contraste_pre = 1
        contraste_pos = 1

        # Regiões de interesse para leitura das tarefas
        regiao0 = (x_origem + 274, y_origem + 268, x_origem + 591, y_origem + 310)
        regiao1 = (x_origem + 274, y_origem + 348, x_origem + 591, y_origem + 390)
        regiao2 = (x_origem + 274, y_origem + 428, x_origem + 591, y_origem + 470)
        regiao3 = (x_origem + 274, y_origem + 508, x_origem + 591, y_origem + 550)

        # Lista para armazenar as tarefas lidas
        lista_trocar_tarefa = []

        # Loop para ler as tarefas em cada região
        for i, regiao in enumerate([regiao0, regiao1, regiao2, regiao3, regiao1, regiao2, regiao3]):

            if i == 4:
                pyautogui.doubleClick(708 + x_origem, 418 + y_origem)  # rola para ver se a tarefa esta na segunda parte
                time.sleep(0.2)

            texto = OCR_regiao(regiao, config, inveter_cor, fator_ampliacao, contraste_pre, contraste_pos, esca_ciza)
            if texto is not None:
                # Mapear caracteres especiais
                texto = texto.replace('ç', 'c').replace('í', 'i').replace('ê', 'e').replace('-', ' ').replace('ã', 'a')
                texto = texto.replace('\n', ' ').rstrip('.')
                print(texto)
                lista_trocar_tarefa.append(texto)

        # Loop para encontrar tarefas para trocar
        for item in para_trocar:
            matches = difflib.get_close_matches(item, lista_trocar_tarefa, n=1, cutoff=0.985)
            if matches:
                posicao = lista_trocar_tarefa.index(matches[0])

                # Ajusta a janela
                if posicao <= 3:
                    pyautogui.doubleClick(x_origem + 635, y_origem + 25)  # clica no tarefas diarias
                    time.sleep(0.2)
                elif posicao > 3:
                    pyautogui.doubleClick(708 + x_origem, 418 + y_origem)  # rola para ver se a tarefa esta na segunda parte
                    time.sleep(0.2)
                # Clique na setinha correspondente à posiçã
                if posicao == 0:
                    pyautogui.click(x_origem + 171, y_origem + 283)  # clica na setinha
                elif posicao == 1 or posicao == 4:
                    pyautogui.click(x_origem + 171, y_origem + 363)  # clica na setinha
                elif posicao == 2 or posicao == 5:
                    pyautogui.click(x_origem + 171, y_origem + 443)  # clica na setinha
                elif posicao == 3 or posicao == 6:
                    pyautogui.click(x_origem + 171, y_origem + 523)  # clica na setinha

                time.sleep(0.3)
                pyautogui.doubleClick(x_origem + 635, y_origem + 25)  # clica no tarefas diarias
                time.sleep(0.3)
                pyautogui.click(x_origem + 545, y_origem + 401)  # clica no ok
                print("Tarefa trocada com sucesso.")
                time.sleep(1)
                break
    print('Não há tarefa na lista de troca.')


def remover_termos(texto):
    """
    Remove termos indesejados do texto, realiza formatações e retorna uma lista de itens.

    Parameters:
    - texto (str): Texto a ser processado.

    Returns:
    - list: Lista de itens processados.
    """
    print('remover_termos')
    if texto is None:
        return []

    dicionario_tarefas_fazer = {  # caça-níquel da mesa
        'Jogar o caca-niquel da mesa 150 vezes': 30,
        'Jogar o caca-niquel da mesa 70 vezes': 20,
        'Jogar o caca-niquel da mesa 10 vezes': 10,
        'Ganhar 100.000 fichas no caca niquel da mesa': 30,
        'Ganhar 30.000 fichas no caca niquel da mesa': 20,
        'Ganhar 10.000 fichas no caca niquel da mesa': 10,
        # Casino Genius
        'Jogar no Casino Genius Pro 100 vezes': 30,
        'Jogar no Casino Genius Pro 50 vezes': 20,
        'Jogar no Casino Genius Pro 10 vezes': 10,
        'Ganhar 100.000 fichas no Casino Genius Pro': 30,
        'Ganhar 30.000 fichas no Casino Genius Pro': 20,
        'Ganhar 4.000 fichas no Casino Genius Pro': 10,
        # Cartas Premiadas
        'Jogar 100 vezes nas Cartas Premiadas': 30,
        'Jogar 50 vezes nas Cartas Premiadas': 20,
        'Jogar 10 vezes nas Cartas Premiadas': 10,
        'Ganhar 100.000 fichas nas Cartas Premiadas': 30,
        'Ganhar 30.000 fichas nas Cartas Premiadas': 20,
        'Ganhar 4.000 fichas nas Cartas Premiadas': 10,
        # Poker Slot
        'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 150 vezes': 30,
        'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 70 vezes': 20,
        'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 10 vezes': 10,
        'Ganhar 100.000 fichas no caca niquel Slot Poker': 30,
        'Ganhar 30.000 fichas no caca niquel Slot Poker': 20,
        'Ganhar 10.000 fichas no caca niquel Slot Poker': 10}

    # Substituir caracteres especiais
    texto = texto + '\n'
    texto = re.sub(r'ç', 'c', texto)
    texto = re.sub(r'í', 'i', texto)
    texto = re.sub(r'\.\n', '\n', texto)
    texto = re.sub(r'caca\n\nniquel', 'caca niquel', texto)
    texto = re.sub(r'caca\nniquel', 'caca niquel', texto)

    # Dividir o texto em linhas
    linhas = texto.split('\n')

    # Filtrar linhas relevantes usando um dicionário ou condição específica
    texto_formatado = '\n'.join([linha for linha in linhas if linha.strip() in dicionario_tarefas_fazer.keys() or linha.strip() == ''])

    # Extrair itens de texto formatado
    itens = texto_formatado.split('\n')

    # Remover caracteres indesejados e formar a lista final
    lista = [re.sub(r'\s+', ' ', item.replace('\n', ' ').strip()) for item in itens if len(item) > 34]

    return lista


def remover_caracteres_especiais(texto):
    """
    Remove caracteres especiais e espaços duplos do texto.

    Parameters:
    - texto (str): Texto a ser processado.

    Returns:
    - str: Texto sem caracteres especiais e espaços duplos.
    """
    # Define a expressão regular para encontrar caracteres especiais
    caracteres_especiais = r'[Í:;.,()=+*—/]'  # Ponto, parênteses, sinal de igual, mais, traço, barra
    texto_sem_especiais = re.sub(caracteres_especiais, '', texto)

    # Remove a sequência "ms"
    texto_sem_especiais = texto_sem_especiais.replace('ms', '').replace('md', '').replace('E', '').replace('-', '')

    # Remove espaços duplos
    texto_sem_especiais = re.sub(r'\s+', ' ', texto_sem_especiais)

    # Remove espaços no início e no final da string
    texto_limpo = texto_sem_especiais.strip()
    return texto_limpo


def remover_termos_upando(texto, metodo=1):
    """
    Remove termos indesejados do texto relacionados a tarefas de upando e realiza a comparação de strings.

    Parameters:
    - texto (str): Texto a ser processado.
    - metodo (int): Método de comparação (1 para SequenceMatcher, 2 para fuzzywuzzy).

    Returns:
    - list: Lista de itens em comum entre as tarefas de upando e o texto fornecido.
    """
    print('remover_termos_upando')
    if texto is None:
        return []

    tarefas_upando = ['Gire 10 vezes no caça-níqueis', 'Jogar o Casino Poker Genius 5 vezes', 'Jogar no Casino Genius Pro 5 vezes',
                      'Jogar 1 mão em qualquer mesa', 'Jogar 5 mãos em qualquer mesa', 'Jogar 10 mãos em qualquer mesa',
                      'Conclua suas tarefas atuais para desbloquear a próxima rodada']

    lista_original = texto.split('\n')

    # Remove itens com menos de 25 caracteres da lista original
    lista_original = [item for item in lista_original if len(item) >= 25]

    # Remove caracteres especiais de cada item na lista original
    lista_original = [remover_caracteres_especiais(item) for item in lista_original]

    print('lista_original: ', lista_original)

    # Lista para armazenar os itens limpos
    itens_em_comum = []

    if metodo == 1:
        # Defina a tolerância para a comparação
        tolerancia = 0.9

        # Percorra a lista de tarefas limpas
        for item in tarefas_upando:
            # Verifique se o item está na lista original (comparação com tolerância)
            for original_item in lista_original:
                similarity_ratio = SequenceMatcher(None, item, original_item).ratio()
                if similarity_ratio >= tolerancia and item not in itens_em_comum:
                    itens_em_comum.append(item)
    else:
        # Defina a tolerância para a comparação
        tolerancia = 95  # Valor de 0 a 100

        # Percorra a lista de tarefas limpas
        for item in tarefas_upando:
            # Verifique se o item está na lista original (comparação com tolerância)
            for original_item in lista_original:
                similarity_ratio = fuzz.ratio(item, original_item)
                if similarity_ratio >= tolerancia and item not in itens_em_comum:
                    itens_em_comum.append(item)

    print('itens_em_comum')
    print(itens_em_comum)
    return itens_em_comum


def limpa_abre_tarefa_3(x_origem, y_origem):  # abre o tarefas
    print('limpa_abre_tarefa_3')
    # testa se a tarefa diaria é de conta sem upar cadeado na cartas premidas
    for _ in range(20):
        pyautogui.doubleClick(x_origem + 635, y_origem + 25)  # clica no tarefas diarias
        if (pyautogui.pixelMatchesColor((x_origem + 750), (y_origem + 38), (245, 218, 96), tolerance=10)
                or pyautogui.pixelMatchesColor((x_origem + 802), (y_origem + 38), (245, 218, 96), tolerance=10)):
            print("Tarefas diarias conta level menor que 4 com cadeado")
            # testa se a tarefa diaria é de conta sem upar ( cadeado )
            if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 133), (1, 50, 254), tolerance=20):
                print("Tarefas diarias conta missoes iniciais")
                return False
            elif pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 133), (48, 0, 96), tolerance=20):
                print("Tarefas diarias limpo conta upada, missoes padroes")
                return True

        elif (pyautogui.pixelMatchesColor((x_origem + 750), (y_origem + 38), (10, 54, 112), tolerance=10)
              or pyautogui.pixelMatchesColor((x_origem + 802), (y_origem + 38), (10, 54, 112), tolerance=10)):
            print("Tarefas diarias conta upada sem o cadeado level maior que 4")

            for _ in range(20):
                pyautogui.doubleClick(x_origem + 635, y_origem + 25)  # clica no tarefas diarias
                print("Limpa Tarefas diarias")
                time.sleep(0.5)
                pyautogui.doubleClick(x_origem + 193, y_origem + 172)  # clica dentro do tarefas diarias

                # testa se tarefa diariaria esta aberta e limpa
                if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 133), (48, 0, 96), tolerance=20):
                    print("Tarefas diarias pausa")
                    time.sleep(1.5)
                    if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 133), (48, 0, 96), tolerance=20):
                        print("Tarefas diarias limpo conta upada, missoes padroes")
                        return True
                # testa se a tarefa diaria é de conta sem upar
                elif pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 133), (1, 50, 254), tolerance=20):
                    # pyautogui.click(821 + x_origem, 138 + y_origem) #clique para fechar
                    print("Tarefas diarias, missoes iniciais")
                    return False
            return True
        time.sleep(0.5)


def tarefas_diaris_upando(x_origem, y_origem):
    """
        Verifica se há tarefas diárias relacionadas ao upando e retorna a lista de tarefas.

        Parameters:
        - x_origem (int): Coordenada x da origem da janela.
        - y_origem (int): Coordenada y da origem da janela.

        Returns:
        - tuple: Uma tupla contendo a lista de tarefas e uma mensagem indicando se há apenas a tarefa 'Gire 10 vezes no caça-níqueis'.
        """
    print('tarefas_diaris_upando')

    lista_tarefas = []

    # Configurações para o processo OCR
    config = '--psm 6 --oem 1'
    inveter_cor = True
    esca_ciza = True
    fator_ampliacao = 1
    contraste_pre = 1
    contraste_pos = 1

    # Define a região de interesse para a leitura do valor
    regiao = (x_origem + 278, y_origem + 329, x_origem + 784, y_origem + 563)
    # abre a tela do tarefa diarias e retrona se true se a conta esta upada e false se a conta esta sem upar
    if limpa_abre_tarefa_3(x_origem, y_origem):
        print('Conta upada')
        pyautogui.click(x_origem + 816, y_origem + 142)  # clica para fechar as tarefas
        lista_tarefas = ['Missões padrão']
        return lista_tarefas
    else:
        print('Conta sem upar')
        # Realiza a leitura da região de tarefas diárias
        texto = OCR_regiao(regiao, config, inveter_cor, fator_ampliacao, contraste_pre, contraste_pos, esca_ciza)

        # Fecha a janela de tarefas diárias
        pyautogui.click(x_origem + 816, y_origem + 142)  # clica para fechar as tarefas

        # Obtém a lista de tarefas removendo termos indesejados
        lista_tarefas = remover_termos_upando(texto)

        return lista_tarefas


lista_blind = (
    '500K1M', '100K200K', '50K100K', '20K40K', '10K20K', '5K10K', '2K4K', '1K2K', '5001K', '200400', '100200', '50100', '2550', '2040', '1020', '510',
    '24', '12')


def blind_sala(x_origem, y_origem):
    """
        Obtém informações sobre as blinds de uma sala em um jogo.

        Parameters:
        - x_origem (int): Coordenada x da origem da janela.
        - y_origem (int): Coordenada y da origem da janela.

        Returns:
        - str: Valor da blind da sala ou '0' se não for possível obter a informação.
        """

    # Configurações para o processo OCR
    inveter_cor = True
    esca_ciza = True
    fator_ampliacao = 3
    contraste_pre = 1
    contraste_pos = 1.5
    # Define a região onde a informação da blind está localizada
    regiao = (x_origem + 54, y_origem + 99, x_origem + 132, y_origem + 115)

    configuracoes = [
        r'--psm 7 --oem 3 -c tessedit_char_whitelist=/0123456789KM',
        r'--oem 3 --psm 6 outputbase digits/KM',
        r'--psm 6 --oem 3 -c tessedit_char_whitelist=/0123456789KM',
        r'--psm 6 --oem 1 -c tessedit_char_whitelist=/0123456789KM',
        r'--psm 6 -c tessedit_char_whitelist=/0123456789KM',
    ]
    # Itera sobre cada configuração e realiza o OCR
    for config in configuracoes:
        # Realiza a leitura da região para obter a informação da blind
        blind = OCR_regiao(regiao, config, inveter_cor, fator_ampliacao, contraste_pre, contraste_pos, esca_ciza)

        if blind is not None:
            blind = blind.upper()
            # mantém apenas os dígitos (0-9), 'K' e 'M' na string blind e descarta os outros caracteres.
            blind = str(''.join(c for c in blind if c.isdigit() or c in ['K', 'M']))
            if blind in lista_blind:
                print(f"{blind} está na lista.")
                print('blind da mesa : ', blind)
                return blind
            else:
                print(f"{blind} não está na lista.")
        else:
            print("Valor fora da faixa desejada")
    return '0'


def numero_sala(x_origem, y_origem):
    """
    Extrai e retorna o número da sala de uma aplicação gráfica.

    Parameters:
    - x_origem (int): Coordenada x da origem da janela.
    - y_origem (int): Coordenada y da origem da janela.

    Returns:
    - str: Número da sala ou "0" se não for encontrado.
    """
    # print('numero_sala')

    # Configurações para o processo OCR
    inveter_cor = True
    esca_ciza = True
    fator_ampliacao = 4
    contraste_pre = 1.1
    contraste_pos = 1.3
    regiao = (x_origem + 55, y_origem + 77, x_origem + 188, y_origem + 93)

    # Aguarda o número da sala ficar visível clicando no anel
    for _ in range(50):
        # printa se esta disponivel o numero
        if (pyautogui.pixelMatchesColor((x_origem + 86), (y_origem + 66), (43, 14, 10), tolerance=5)
                or pyautogui.pixelMatchesColor((x_origem + 86), (y_origem + 66), (54, 27, 8), tolerance=5)):
            time.sleep(0.1)
            break
        time.sleep(0.1)
        print('Esperando o número da sala ficar visível...')
        pyautogui.click(x_origem + 43, y_origem + 388)  # clica no anel

    configuracoes = ['--psm 6 --oem 1']

    # Itera sobre cada configuração e realiza o OCR
    for config in configuracoes:

        numero = OCR_regiao(regiao, config, inveter_cor, fator_ampliacao, contraste_pre, contraste_pos, esca_ciza)  # pontuação
        print('numero mesa sem tratamento: ', numero)
        if numero is not None:
            numero = numero.split(' ')[0] if ' ' in numero else numero
            # se a string contiver espaços, ele pegará a parte antes do espaço. Caso contrário, retornará a própria string original.
            numero = str(numero)[:4]
            numero = tratar_valor_numerico(numero)
            print('Número da sala:', numero)
            return str(numero)
        else:
            print("Valor fora da faixa desejada")
    return "0"


def valor_apostar(x_origem, y_origem):
    """
    Extrai e retorna o valor da aposta de uma aplicação gráfica.

    Parameters:
    - x_origem (int): Coordenada x da origem da janela.
    - y_origem (int): Coordenada y da origem da janela.

    Returns:
    - int: Valor da aposta ou 0 se não for encontrado.
    """

    # Configurações para o processo OCR
    inveter_cor = False
    esca_ciza = True
    fator_ampliacao = 1
    contraste_pre = 1
    contraste_pos = 1
    regiao = (x_origem + 420, y_origem + 644, x_origem + 474, y_origem + 658)

    # config = '--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789'  #

    configuracoes = [
        r'--oem 3 --psm 6 outputbase digits',
        r'--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789',
        r'--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789',
        r'--psm 6 --oem 1 -c tessedit_char_whitelist=0123456789',
        r'--psm 6 -c tessedit_char_whitelist=0123456789',
    ]
    # Itera sobre cada configuração e realiza o OCR
    for config in configuracoes:
        for _ in range(3):
            # Extrai o valor da aposta usando OCR
            try:
                valor = OCR_regiao(regiao, config, inveter_cor, fator_ampliacao, contraste_pre, contraste_pos, esca_ciza)

                if valor is not None:
                    # print("\nAposta: ", valor, "\n")

                    valor = int(valor)
                    return valor

            except Exception as e:
                print(e)
    return 0


def aviso_sistema(x_origem, y_origem):
    print('aviso_sistema')
    # testa sem tem o azul do atualizar a pagina do aviso do sistema
    resposta = "ok"

    if (pyautogui.pixelMatchesColor((x_origem + 500), (y_origem + 380), (224, 227, 229), tolerance=1)
            and pyautogui.pixelMatchesColor((x_origem + 321), (y_origem + 273), (0, 0, 0), tolerance=1)):
        # testa se tem cinsa claro do meio da caixa
        # testa se tem a borda preta da caixa
        print('tem a caixa com o aviso do sistema')

        if pyautogui.pixelMatchesColor((x_origem + 641), (y_origem + 278), (255, 255, 255), tolerance=10):
            # ou testar se tem o X de fachar a caixa
            print('clica no X da caixa de aviso do sistema')
            pyautogui.click(x_origem + 641, y_origem + 278)  # clica no x do aviso so sistema
            return False, resposta

        elif pyautogui.pixelMatchesColor((x_origem + 450), (y_origem + 408), (209, 211, 213), tolerance=1):
            # testa se tem cnsa mais escurao da parte debaixo da caixa e testa se nao tem botao azul
            print('testa se tem que atualizar a pagina ou se tem que sair da conta')
            inveter_cor = False
            esca_ciza = True
            fator_ampliacao = 1
            contraste_pre = 1
            contraste_pos = 1
            config = '--psm 3'
            regiao = (x_origem + 321, y_origem + 268, x_origem + 658, y_origem + 433)
            valor = None
            valor = OCR_regiao(regiao, config, inveter_cor, fator_ampliacao, contraste_pre, contraste_pos, esca_ciza)
            print("valor lido pelo OCR aviso do sistema: ", valor)
            if valor is not None and 'Aviso do sistema' in valor:
                print('foi encontrado um: Aviso do sistema')
                if 'cancelada' in valor:
                    print("Mesagem: ", valor)
                    Variaveis_Globais.alterar_global_aviso_sistema(True)  # muda o valor da variavel global destinado a sair da conta
                    resposta = "sair da conta"
                    print('tem que sair da conta')
                    return True, resposta
                elif 'atualizar' in valor:
                    print("Mesagem: ", valor)
                    resposta = "erro de comunicação"
                    IP.tem_internet()
                    print('Erro de comunicação, favor atualizar a página para continuar com o processo')
                    pyautogui.press('f5')
                    print('espera 30 segundos')
                    time.sleep(30)
                    print('continua')
                    return True, resposta
                else:
                    return False, resposta
            else:
                print('tenta clica no X da caixa de aviso do sistema')
                pyautogui.click(x_origem + 641, y_origem + 278)  # clica no x do aviso so sistema
                return False, resposta
        else:
            print('tenta clica no X da caixa de aviso do sistema')
            pyautogui.click(x_origem + 641, y_origem + 278)  # clica no x do aviso so sistema
            return False, resposta
    else:
        # print('nao tem caixa com aviso do sistema ')
        return False, resposta


def level_conta(x_origem, y_origem):
    """
    Extrai e retorna o nível da conta de uma aplicação gráfica.

    Parameters:
    - x_origem (int): Coordenada x da origem da janela.
    - y_origem (int): Coordenada y da origem da janela.

    Returns:
    - int: Nível da conta ou 0 se não for encontrado ou estiver fora da faixa desejada.
    """
    print('level_conta')

    for _ in range(50):
        # clica para abrir a tela do perfil
        pyautogui.click(16 + x_origem, 24 + y_origem)
        # testa se a tela do perfil esta aberta
        if (pyautogui.pixelMatchesColor((x_origem + 241), (y_origem + 170), (227, 18, 5), tolerance=1)
                and pyautogui.pixelMatchesColor((x_origem + 406), (y_origem + 273), (116, 130, 139), tolerance=1)):
            time.sleep(1)
            break
        time.sleep(0.2)

    # Configurações para o processo OCR
    level = 0
    fichas = 0
    inveter_cor = False
    esca_ciza = True
    fator_ampliacao = 3
    contraste_pre = 1
    contraste_pos = 1
    regiao_ficha = (x_origem + 599, y_origem + 239, x_origem + 630, y_origem + 257)  # leval
    configuracoes = [
        r'--oem 3 --psm 6 outputbase digits',
        r'--psm 7 --oem 0 -c tessedit_char_whitelist=0123456789',
        r'--psm 7 --oem 1 -c tessedit_char_whitelist=0123456789',
        r'--psm 8 --oem 0 -c tessedit_char_whitelist=0123456789'
    ]
    for _ in range(3):
        for config in configuracoes:
            pyautogui.click(16 + x_origem, 24 + y_origem)
            # print(config)
            # Realiza a leitura do nível usando OCR
            level = OCR_regiao(regiao_ficha, config, inveter_cor, fator_ampliacao, contraste_pre, contraste_pos, esca_ciza)
            # print('lido ', lido)
            if level is not None:
                level = tratar_valor_numerico(level)
                # Verifica se o valor está na faixa desejada
                if 1 < level < 30:
                    print("\n   Nível da conta:", level, '\n')
                    fichas = valor_fichas_perfil(x_origem, y_origem)

                    if pyautogui.pixelMatchesColor((x_origem + 241), (y_origem + 170), (227, 18, 5), tolerance=2):
                        pyautogui.click(771 + x_origem, 162 + y_origem)  # clica para fechar a tela do perfil

                    return level, fichas

                else:
                    print("Nível da contar fora da faixa desejada")
                    level = 1
            else:
                print("Erro na leitura do OCR")
                level = 1

    fichas = valor_fichas_perfil(x_origem, y_origem)

    if pyautogui.pixelMatchesColor((x_origem + 241), (y_origem + 170), (227, 18, 5), tolerance=2):
        pyautogui.click(771 + x_origem, 162 + y_origem)  # clica para fechar a tela do perfil
    print('Erro na leitura do nivel da comta')
    return level, fichas

# aviso_do_sistema()
# x_origem, y_origem = Origem_pg.x_y()
# valor_fichas(x_origem, y_origem)
# valor_fichas_perfil(x_origem, y_origem)
# numero_sala(x_origem, y_origem)
# blind_sala(x_origem, y_origem)
# valor_fichas_perfil(x_origem, y_origem)
# tarefas_diaris_upando(x_origem, y_origem)
# level_conta(x_origem, y_origem)
# numero_sala(x_origem, y_origem)
# tarefas_diaris_upando(x_origem, y_origem)
# pontuacao_tarefas(x_origem, y_origem)
# level_conta(x_origem, y_origem)
# pontuacao_tarefas(x_origem, y_origem)
# valor_fichas(x_origem, y_origem)
# tarefas_diaris_trocar(x_origem, y_origem)
# tarefas_diaris(x_origem, y_origem)
# print(y_origem)
# valor_apostar(x_origem, y_origem)
# blind_sala(x_origem, y_origem)
# print(valor)
# lista_tarefas_disponivel = tarefas_diaris(x_origem, y_origem)
# print(lista_tarefas_disponivel)
# tempo_roleta(x_origem, y_origem)
# lido = valor_fichas(x_origem, y_origem)
# print(lido)
# pontuacao_tarefas(x_origem, y_origem)
# def rola_tarefa_0():
# pyautogui.click(708 + x_origem, 426 + y_origem, button='left')
