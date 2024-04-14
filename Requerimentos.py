import os
import socket

# Obter o nome do computador
nome_computador = socket.gethostname()
# Obter o nome de usuário
nome_usuario = os.getlogin()
# nome do computador e do usuario
nome_completo = str(nome_computador) + "_" + str(nome_usuario)

dicionari_token_credencial_n = {
    'PC-I5-8600K_PokerIP': ("token1.json", "credentials0.json", 1, 'gayaluisaalmeida@gmail.com', 'lglg32379089', "IP!F3"),
    'PC-I5-8600K_lgagu': ("token2.json", "credentials0.json", 2, 'lga.gustavo.a@gmail.com', 'LGlg32379089@', "IP!F3"),
    'PC-I5-8600K_Poker': ("token3.json", "credentials0.json", 3, 'luis.gustavo@engenharia.ufjf.br', 'LGlg32379089@#', "IP!F3"),

    'PC-I5-9400A_PokerIP': ("token4.json", "credentials1.json", 4, 'gayaluisaalmeida@gmail.com', 'lglg32379089', "IP!F6"),
    'PC-I5-9400A_lgagu': ("token5.json", "credentials1.json", 5, 'lga.gustavo.a@gmail.com', 'LGlg32379089@', "IP!F6"),
    'PC-I5-9400A_Poker': ("token6.json", "credentials1.json", 6, 'luis.gustavo@engenharia.ufjf.br', 'LGlg32379089@#', "IP!F6"),

    'PC-I5-9400B_PokerIP': ("token7.json", "credentials2.json", 7, 'gayaluisaalmeida@gmail.com', 'lglg32379089', "IP!F9"),
    'PC-I5-9400B_lgagu': ("token8.json", "credentials2.json", 8, 'lga.gustavo.a@gmail.com', 'LGlg32379089@', "IP!F9"),
    'PC-I5-9400B_Poker': ("token9.json", "credentials2.json", 9, 'luis.gustavo@engenharia.ufjf.br', 'LGlg32379089@#', "IP!F9"),

    'PC-I5-9400C_PokerIP': ("token10.json", "credentials3.json", 10, 'gayaluisaalmeida@gmail.com', 'lglg32379089', "IP!F12"),
    'PC-I5-9400C_lgagu': ("token11.json", "credentials3.json", 11, 'lga.gustavo.a@gmail.com', 'LGlg32379089@', "IP!F12"),
    'PC-I5-9400C_Poker': ("token12.json", "credentials3.json", 12, 'luis.gustavo@engenharia.ufjf.br', 'LGlg32379089@#', "IP!F12"),

    'PC-R5-7600A_PokerIP': ("token13.json", "credentials4.json", 13, 'gayaluisaalmeida@gmail.com', 'lglg32379089', "IP!F15"),
    'PC-R5-7600A_lgagu': ("token14.json", "credentials4.json", 14, 'lga.gustavo.a@gmail.com', 'LGlg32379089@', "IP!F15"),
    'PC-R5-7600A_Poker': ("token15.json", "credentials4.json", 15, 'luis.gustavo@engenharia.ufjf.br', 'LGlg32379089@#', "IP!F15"),

    'PC-I5-13400A_PokerIP': ("token16.json", "credentials5.json", 16, 'gayaluisaalmeida@gmail.com', 'lglg32379089', "IP!F18"),
    'PC-I5-13400A_lgagu': ("token17.json", "credentials5.json", 17, 'lga.gustavo.a@gmail.com', 'LGlg32379089@', "IP!F18"),
    'PC-I5-13400A_Poker': ("token18.json", "credentials5.json", 18, 'luis.gustavo@engenharia.ufjf.br', 'LGlg32379089@#', "IP!F18"),

    'PC-I5-13400B_PokerIP': ("token19.json", "credentials0.json", 19, 'gayaluisaalmeida@gmail.com', 'lglg32379089', "IP!F21"),
    'PC-I5-13400B_lgagu': ("token20.json", "credentials0.json", 20, 'lga.gustavo.a@gmail.com', 'LGlg32379089@', "IP!F21"),
    'PC-I5-13400B_Poker': ("token21.json", "credentials0.json", 21, 'luis.gustavo@engenharia.ufjf.br', 'LGlg32379089@#', "IP!F21"),

    'PC-I5-13400C_PokerIP': ("token22.json", "credentials1.json", 22, 'gayaluisaalmeida@gmail.com', 'lglg32379089', "IP!F24"),
    'PC-I5-13400C_lgagu': ("token23.json", "credentials1.json", 23, 'lga.gustavo.a@gmail.com', 'LGlg32379089@', "IP!F24"),
    'PC-I5-13400C_Poker': ("token24.json", "credentials1.json", 24, 'luis.gustavo@engenharia.ufjf.br', 'LGlg32379089@#', "IP!F24"),

    'PC-I5-13400D_PokerIP': ("token25.json", "credentials2.json", 25, 'gayaluisaalmeida@gmail.com', 'lglg32379089', "IP!F27"),
    'PC-I5-13400D_lgagu': ("token26.json", "credentials2.json", 26, 'lga.gustavo.a@gmail.com', 'LGlg32379089@', "IP!F27"),
    'PC-I5-13400D_Poker': ("token27.json", "credentials2.json", 27, 'luis.gustavo@engenharia.ufjf.br', 'LGlg32379089@#', "IP!F27"),

    'PC-R5-5600G_PokerIP': ("token28.json", "credentials3.json", 28, 'gayaluisaalmeida@gmail.com', 'lglg32379089', "IP!F30"),
    'PC-R5-5600G_lgagu': ("token29.json", "credentials3.json", 29, 'lga.gustavo.a@gmail.com', 'LGlg32379089@', "IP!F30"),
    'PC-R5-5600G_Poker': ("token30.json", "credentials3.json", 30, 'luis.gustavo@engenharia.ufjf.br', 'LGlg32379089@#', "IP!F30"),

    'PC-I5-13400E_PokerIP': ("token31.json", "credentials4.json", 31, 'gayaluisaalmeida@gmail.com', 'lglg32379089', "IP!F33"),
    'PC-I5-13400E_lgagu': ("token32.json", "credentials4.json", 32, 'lga.gustavo.a@gmail.com', 'LGlg32379089@', "IP!F33"),
    'PC-I5-13400E_Poker': ("token33.json", "credentials4.json", 33, 'luis.gustavo@engenharia.ufjf.br', 'LGlg32379089@#', "IP!F33"),

    'PC-I5-13400F_PokerIP': ("token34.json", "credentials5.json", 34, 'gayaluisaalmeida@gmail.com', 'lglg32379089', "IP!F36"),
    'PC-I5-13400F_lgagu': ("token35.json", "credentials5.json", 35, 'lga.gustavo.a@gmail.com', 'LGlg32379089@', "IP!F36"),
    'PC-I5-13400F_Poker': ("token36.json", "credentials5.json", 36, 'luis.gustavo@engenharia.ufjf.br', 'LGlg32379089@#', "IP!F36"),

    'PC-i3-8145U_PokerIP': ("token37.json", "credentials0.json", 37, 'gayaluisaalmeida@gmail.com', 'lglg32379089', "IP!F39"),

    'PC-I7-9700KF_PokerIP': ("token40.json", "credentials5.json", 40, 'gayaluisaalmeida@gmail.com', 'lglg32379089', "IP!F42"),
    'PC-I7-9700KF_lgagu': ("token41.json", "credentials5.json", 41, 'lga.gustavo.a@gmail.com', 'LGlg32379089@', "IP!F42"),
    'PC-I7-9700KF_Poker': ("token42.json", "credentials5.json", 42, 'luis.gustavo@engenharia.ufjf.br', 'LGlg32379089@#', "IP!F42")
}

numero_pc = f"PC{dicionari_token_credencial_n[nome_completo][2] :02d}"

# valor_dicionario = dicionari_token_credencial_n[nome_completo]