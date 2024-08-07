import time
import HoraT

import Mesa
from OCR_tela import tarefas_diaris_upando
from Tarefas import recolher_tarefa_upando
from Upar import genius_joga_vezes_upando, cartas_premidas_joga_vezes_upando, slot_joga_vezes_upando


def upar(x_origem, y_origem, blind_mesa='100200'):
    """
    Função principal para realizar a automação de tarefas de upando em um jogo de poker online.

    Parameters:
    - x_origem (int): Coordenada x da origem da janela do jogo.
    - y_origem (int): Coordenada y da origem da janela do jogo.

    Returns:
    - str: Mensagem indicando se a conta foi upada ou não.
    """
    print('upar')

    for _ in range(20):
        recolher_tarefa_upando(x_origem, y_origem)
        time.sleep(2)
        lista_tarefa_upar = tarefas_diaris_upando(x_origem, y_origem)

        if HoraT.fim_tempo_tarefa():
            print('Fim do horario destinado a tarefas')
            return 'Conta upada'

        if 'Missões padrão' in lista_tarefa_upar:
            return 'Conta upada'

        elif not lista_tarefa_upar:
            lista_tarefa_upar = tarefas_diaris_upando(x_origem, y_origem)
            if not lista_tarefa_upar:
                return 'Conta upada'

        elif 'Jogar 1 mãos em qualquer mesa' in lista_tarefa_upar:
            print("\n\n Jogar 1 mãos em qualquer mesa \n\n")
            Mesa.mesa_upar_jogar_recolher_slote(x_origem, y_origem, funcoes='upar', numero_jogadas=1)
            # Mesa.mesa_upar_jogar(x_origem, y_origem, 1, False, blind_mesa, False)
            recolher_tarefa_upando(x_origem, y_origem)
            lista_tarefa_upar = tarefas_diaris_upando(x_origem, y_origem)

        elif 'Jogar 5 mãos em qualquer mesa' in lista_tarefa_upar:
            print("\n\n Jogar 5 mãos em qualquer mesa \n\n")
            Mesa.mesa_upar_jogar_recolher_slote(x_origem, y_origem, funcoes='upar', numero_jogadas=5)
            # Mesa.mesa_upar_jogar(x_origem, y_origem, 5, False, blind_mesa, False)
            recolher_tarefa_upando(x_origem, y_origem)
            time.sleep(2)
            lista_tarefa_upar = tarefas_diaris_upando(x_origem, y_origem)

        elif 'Jogar 10 mãos em qualquer mesa' in lista_tarefa_upar:
            print("\n\n Jogar 10 mãos em qualquer mesa \n\n")
            Mesa.mesa_upar_jogar_recolher_slote(x_origem, y_origem, funcoes='upar', numero_jogadas=10)
            # Mesa.mesa_upar_jogar(x_origem, y_origem, 10, False, blind_mesa, False)
            recolher_tarefa_upando(x_origem, y_origem)
            time.sleep(2)
            lista_tarefa_upar = tarefas_diaris_upando(x_origem, y_origem)

        elif 'Alcançar Nível 3' in lista_tarefa_upar:
            print("\n\n Alcançar Nível 3 \n\n")
            Mesa.mesa_upar_jogar_recolher_slote(x_origem, y_origem, funcoes='upar', numero_jogadas=10)
            # Mesa.mesa_upar_jogar(x_origem, y_origem, 10, False, blind_mesa, False)
            recolher_tarefa_upando(x_origem, y_origem)
            time.sleep(2)
            lista_tarefa_upar = tarefas_diaris_upando(x_origem, y_origem)

        elif 'Alcançar Nível 4' in lista_tarefa_upar:
            print("\n\n Alcançar Nível 3 \n\n")
            Mesa.mesa_upar_jogar_recolher_slote(x_origem, y_origem, funcoes='upar', numero_jogadas=10)
            # Mesa.mesa_upar_jogar(x_origem, y_origem, 10, False, blind_mesa, False)
            recolher_tarefa_upando(x_origem, y_origem)
            time.sleep(2)
            lista_tarefa_upar = tarefas_diaris_upando(x_origem, y_origem)

        if 'Gire 10 vezes no caça-níqueis' in lista_tarefa_upar:
            print("\n\n 'Gire 10 vezes no caça-níqueis' \n\n")
            slot_joga_vezes_upando(x_origem, y_origem)
            recolher_tarefa_upando(x_origem, y_origem)
            lista_tarefa_upar = tarefas_diaris_upando(x_origem, y_origem)

        if 'Jogar o Casino Poker Genius 5 vezes' in lista_tarefa_upar:
            print("\n\n Jogar Cartas Premiadas 5 vezes \n\n")
            cartas_premidas_joga_vezes_upando(x_origem, y_origem)
            recolher_tarefa_upando(x_origem, y_origem)
            time.sleep(2)
            lista_tarefa_upar = tarefas_diaris_upando(x_origem, y_origem)

        if 'Jogar no Casino Genius Pro 5 vezes' in lista_tarefa_upar:
            print("\n\n 'Jogar no Casino Genius Pro 5 vezes' \n\n")
            genius_joga_vezes_upando(x_origem, y_origem)
            recolher_tarefa_upando(x_origem, y_origem)
            time.sleep(2)
            lista_tarefa_upar = tarefas_diaris_upando(x_origem, y_origem)

    return 'Conta upada'

# import Origem_pg
# x_origem, y_origem = Origem_pg.x_y()
# upar(x_origem, y_origem)
