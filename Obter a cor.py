import time
import pyautogui
import Origem_pg

# Exemplo de uso
x_origem = 9
y_origem = 227

x_origem, y_origem = Origem_pg.x_y()

# x_origem, y_origem = Origem_pg.x_y_aviso_sistema()
print(x_origem, y_origem)
# x_origem, y_origem = 0, 0
# pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 580), (47, 136, 196), tolerance=19)

x = (x_origem + 38)
y = (y_origem + 526)

tolerancia = 0
pyautogui.moveTo(x, y)
cores_contagem = {}
for i in range(100):
    cor = pyautogui.pixel(x, y)
    print(f"A cor RGB do pixel em ({x}, {y}) é {cor}")

    if pyautogui.pixelMatchesColor(x, y, (215, 234, 244), tolerance=tolerancia):
        print('tem a cor, tolerancia :', tolerancia)

    tolerancia += 1

    # Adicione a cor ao dicionário e atualize a contagem
    if cor in cores_contagem:
        cores_contagem[cor] += 1
    else:
        cores_contagem[cor] = 1

    # Aguarde por um curto período de tempo antes de verificar o próximo pixel
    time.sleep(0.1)

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
