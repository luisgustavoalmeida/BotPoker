import subprocess

# Função para obter os pacotes instalados
def get_installed_packages():
    try:
        resultado = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE, text=True, encoding='utf-8')
        return resultado.stdout.strip().split('\n')
    except subprocess.CalledProcessError as e:
        print(f"\nOcorreu um erro ao obter os pacotes instalados: \n{e}\n")
        return []

# Função para atualizar ou instalar apenas os pacotes necessários
def update_or_install_required_packages(requirements_file):
    # Obter pacotes instalados
    installed_packages = get_installed_packages()

    # Ler os pacotes requeridos do arquivo requirements.txt
    with open(requirements_file, 'r', encoding='utf-16') as file:
        required_packages = [line.strip() for line in file]

    # Verificar e instalar os pacotes necessários
    for package in required_packages:
        if package not in installed_packages:
            try:
                subprocess.run(['pip', 'install', package, '--no-warn-script-location'], check=True)
                print(f"\nPacote {package} instalado com sucesso.\n")
            except subprocess.CalledProcessError as e:
                print(f"\nOcorreu um erro ao instalar o pacote {package}: \n{e}\n")
        # else:
        #     print(f"Pacote {package} já está instalado.")

    print('\nBibliotecas instaladas / atualizadas com sucesso!\n')

if __name__ == "__main__":
    print('\nProcura por atualizações em bibliotecas\n')
    requirements_file = 'requirements.txt'  # Nome do arquivo requirements.txt
    update_or_install_required_packages(requirements_file)
