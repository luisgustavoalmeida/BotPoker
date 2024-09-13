import time

import pyautogui

# Define o nome do arquivo da imagem a ser buscada
origem = r'Imagens\Origem.png'

# Define a região da tela onde a imagem será buscada
regiao_busca = (0, 210, 120, 290)  # (x, y, largura, altura)
precisao_origem = 0.997


def localizar_imagem(imagem, regiao, precisao):
    try:
        posicao = pyautogui.locateOnScreen(imagem, region=regiao, confidence=precisao, grayscale=True)
        return posicao
    except:
        print("Ocorreu um erro ao localizar a imagem")
        time.sleep(2)
        return None


def x_y():  # apenas para testes
    while True:
        posicao = None
        print("Procurando coodenada 0 x 0...")
        for i in range(50):
            posicao = localizar_imagem(origem, regiao_busca, precisao_origem)
            if posicao is not None:  # Verifica se a imagem foi encontrada
                x_origem, y_origem = posicao.left, posicao.top
                x_origem = int(x_origem)
                y_origem = int(y_origem)
                print("x_origem: ", x_origem)
                print("y_origem: ", y_origem)

                return x_origem, y_origem


# Exemplo de uso
x_origem = 490
y_origem = 167

# x_origem, y_origem = x_y()

print(x_origem, y_origem)

a, b = 700, 167

x = (x_origem + a)
y = (y_origem + b)

x = 429
y = 894

tolerancia = 0
pyautogui.moveTo(x, y)
cores_contagem = {}
for i in range(255):
    cor = pyautogui.pixel(x, y)
    print(f"A cor RGB do pixel em ({x}, {y}) é {cor}")

    if pyautogui.pixelMatchesColor(x, y, (32, 33, 36), tolerance=tolerancia):
        print('tem a cor, tolerancia :', tolerancia)

    tolerancia += 1

    # Adicione a cor ao dicionário e atualize a contagem
    if cor in cores_contagem:
        cores_contagem[cor] += 1
    else:
        cores_contagem[cor] = 1

    # Aguarde por um curto período de tempo antes de verificar o próximo pixel
    # time.sleep(0.5)

# Encontre a cor que mais ocorreu
cor_mais_comum = max(cores_contagem, key=cores_contagem.get)
ocorrencias_mais_comum = cores_contagem[cor_mais_comum]

# Encontre a cor menos comum
cor_menos_comum = min(cores_contagem, key=cores_contagem.get)
ocorrencias_menos_comum = cores_contagem[cor_menos_comum]

print(f"A cor que mais ocorreu foi: {cor_mais_comum} com {ocorrencias_mais_comum} ocorrências.")
print(f"A cor menos comum foi: {cor_menos_comum} com {ocorrencias_menos_comum} ocorrências.")

# Realize uma busca exaustiva para encontrar a melhor tolerância
melhor_tolerancia = None
max_ocorrencias = 0



