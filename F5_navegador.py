import os
import socket
import time

import pyautogui

# import Google

# Desabilitar o fail-safe
pyautogui.FAILSAFE = False

# Obter o nome do computador
nome_computador = socket.gethostname()
# Obter o nome de usuário
nome_usuario = os.getlogin()

# Define o nome do arquivo da imagem a ser buscada
botao_parar_carregamento = r'Imagens\botao_parar_carregamento.png'
botao_recarregar = r'Imagens\botao_recarregar.png'

# Define a região da tela onde a imagem será buscada
regiao_busca = (50, 35, 140, 100)  # (x, y, largura, altura)
precisao = 0.9


def localizar_imagem(imagem, regiao, precisao):
    try:
        posicao = pyautogui.locateOnScreen(imagem, region=regiao, confidence=precisao, grayscale=True)
        return posicao
    except:
        print("Ocorreu um erro ao localizar a imagem")
        time.sleep(2)
        return None


def atualizar_navegador():
    for _ in range(10):
        print('atualizando navegador...')
        clicou_atualizar = False
        for _ in range(10):
            print('localizando botões')
            if not clicou_atualizar:
                posicao = localizar_imagem(botao_recarregar, regiao_busca, precisao)
                if posicao is not None:  # Verifica se a imagem foi encontrada
                    pyautogui.click(94, 59)  # clica no atualizar
                    print('clicou no atualizar')
                    time.sleep(0.5)
                    clicou_atualizar = True

            posicao = localizar_imagem(botao_parar_carregamento, regiao_busca, precisao)
            if posicao is not None:  # Verifica se a imagem foi encontrada
                print('pagina recarregando...')
                break
            time.sleep(1)

        for _ in range(30):
            print('esperando resposta do navegador...')
            posicao = localizar_imagem(botao_recarregar, regiao_busca, precisao)
            if posicao is not None:  # Verifica se a imagem foi encontrada
                print('pagina recarregada!')
                return
            time.sleep(1)
        print('clica burro no atualizar, e espera 15 segundos')
        pyautogui.click(94, 59)  # clica no atualizar
        time.sleep(15)
    return

atualizar_navegador()
