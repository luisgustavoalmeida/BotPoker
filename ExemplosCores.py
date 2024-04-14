from colorama import Fore, Back, Style, init, deinit

# Inicializa a biblioteca colorama
init()

# Cores de texto
print(Fore.RED + 'Texto em vermelho' + Fore.RESET)
print(Fore.GREEN + 'Texto em verde' + Fore.RESET)
print(Fore.BLUE + 'Texto em azul' + Fore.RESET)
print(Fore.YELLOW + 'Texto em amarelo' + Fore.RESET)
print(Fore.MAGENTA + 'Texto em magenta' + Fore.RESET)
print(Fore.CYAN + 'Texto em ciano' + Fore.RESET)
print(Fore.WHITE + 'Texto em branco' + Fore.RESET)
print(Fore.BLACK + 'Texto em preto' + Fore.RESET)
print(Fore.LIGHTBLACK_EX + 'Texto em cinza' + Fore.RESET)
print(Fore.LIGHTBLUE_EX + 'Texto em azul claro' + Fore.RESET)
print(Fore.LIGHTCYAN_EX + 'Texto em ciano claro' + Fore.RESET)
print(Fore.LIGHTGREEN_EX + 'Texto em verde claro' + Fore.RESET)
print(Fore.LIGHTMAGENTA_EX + 'Texto em magenta claro' + Fore.RESET)
# Cores de fundo
print(Back.RED + 'Fundo vermelho' + Back.RESET)
print(Back.GREEN + 'Fundo verde' + Back.RESET)
print(Back.BLUE + 'Fundo azul' + Back.RESET)
print(Back.YELLOW + 'Fundo amarelo' + Back.RESET)
print(Back.MAGENTA + 'Fundo magenta' + Back.RESET)
print(Back.CYAN + 'Fundo ciano' + Back.RESET)
print(Back.WHITE + 'Fundo branco' + Back.RESET)
print(Back.BLACK + 'Fundo preto' + Back.RESET)
print(Back.LIGHTBLACK_EX + Fore.LIGHTGREEN_EX + 'Fundo branco' + Style.RESET_ALL)


# Estilos
print(Style.BRIGHT + 'Texto brilhante' + Style.RESET_ALL)
print(Style.NORMAL + 'Texto normal' + Style.RESET_ALL)

# Desliga a biblioteca colorama
deinit()

