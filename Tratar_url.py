import re

def rodar_links(url_link):
    """Função para capturar o número entre 'mfid=' e '&ref=', e gerar um dicionário com as URLs sequenciais mudando o último dígito."""

    # Testa se a string começa com o prefixo desejado
    if url_link.startswith("https://apps.facebook.com/poker_italia?"):
        print("A URL começa com 'https://apps.facebook.com/poker_italia?'")

        # Define o padrão da expressão regular para capturar o número entre "mfid=" e "&ref="
        padrao = r'mfid=(\d+)&ref='

        # Usa re.search para encontrar o número
        resultado = re.search(padrao, url_link)

        if resultado:
            # Exibe o número original
            numero_original = resultado.group(1)
            print(f"Número original encontrado: {numero_original}")

            # Dicionário para armazenar as URLs com chaves de 0 a 9
            urls_dict = {}

            # Gera um sequencial mudando o último dígito de 0 a 9
            for i in range(10):
                # Substitui o último dígito do número original
                novo_numero = numero_original[:-1] + str(i)

                # Substitui o número original na URL pelo novo número
                nova_url = re.sub(padrao, f"mfid={novo_numero}&ref=", url_link)

                # Armazena a nova URL no dicionário com a chave sendo o valor de i
                urls_dict[i] = nova_url

            # Retorna o dicionário
            print(urls_dict)
            return urls_dict

    else:
        # Cria um dicionário onde todas as chaves de 0 a 9 apontam para a URL original
        print('A URL não começa com o padrão esperado.')
        urls_dict = {i: url_link for i in range(10)}
        print(urls_dict)
        return urls_dict

#
# # Exemplo de uso
# url = "https://apps.facebook.com/poker_italia?isinvite=0&ft=MoneyFeed_HappyTogetherShare&activity=mf&mfid=7226390&ref=MoneyFeed_HappyTogetherShare"
#
# urls_geradas = rodar_links(url)
#
# # Exibe o dicionário com as URLs
# if urls_geradas:
#     for chave, valor in urls_geradas.items():
#         print(f"Chave {chave}: {valor}")
