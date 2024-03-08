import cv2


def gerar_lista_coordenadas_cores(img):
    """
    Gera uma lista de tuplas contendo a coordenada e a cor RGB de cada pixel da imagem.

    Args:
      img: A imagem.

    Returns:
      Uma lista de tuplas contendo a coordenada e o padrão de cor RGB (como tupla).
    """

    # Converte a imagem para RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Gera lista de coordenadas e cores (como tuplas)
    coordenadas_cores = []
    for i in range(img_rgb.shape[0]):
        for j in range(img_rgb.shape[1]):
            coordenadas_cores.append((j, i, tuple(img_rgb[i, j])))  # Extrai cor como tupla

    return coordenadas_cores


def comparar_item_a_item(lista1, lista2):
    """
    Compara cada item da lista1 com cada item da lista2 e imprime os que forem iguais.

    Args:
      lista1: A primeira lista.
      lista2: A segunda lista.
    """

    for item1 in lista1:
        for item2 in lista2:
            if item1 == item2:
                print(f"Item igual: {item1}")


# Carrega as imagens
img1 = cv2.imread('imagem1.jpg')
img2 = cv2.imread('imagem2.jpg')

# Gera listas de coordenadas e cores
coordenadas_cores_img1 = gerar_lista_coordenadas_cores(img1)
coordenadas_cores_img2 = gerar_lista_coordenadas_cores(img2)

# Comparar as listas
comparar_item_a_item(coordenadas_cores_img1, coordenadas_cores_img2)
