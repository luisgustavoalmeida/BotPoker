import os
import socket

# link do video explicativo https://www.youtube.com/watch?v=l7pL_Y3fw-o

# Obter o nome do computador
nome_computador = socket.gethostname()
# Obter o nome de usuário
nome_usuario = os.getlogin()
# nome do computador e do usuario
nome_completo = str(nome_computador) + "_" + str(nome_usuario)
#modem, celular, vero, celular_root, proxy
dicionari_token_credencial_n = {
    'PC-I5-8600K_PokerIP': ("token1.json", "credentials0.json", 1, 'gayaluisaalmeida@gmail.com', '', "IP!F3", "proxy"),
    'PC-I5-8600K_lgagu': ("token2.json", "credentials0.json", 2, 'lga.gustavo.a@gmail.com', '', "IP!F3", "proxy"),
    'PC-I5-8600K_Poker': ("token3.json", "credentials0.json", 3, 'luis.gustavo@engenharia.ufjf.br', '', "IP!F3", "proxy"),

    'PC-I5-9400A_PokerIP': ("token4.json", "credentials1.json", 4, 'gayaluisaalmeida@gmail.com', '', "IP!F6", "proxy"),
    'PC-I5-9400A_lgagu': ("token5.json", "credentials1.json", 5, 'lga.gustavo.a@gmail.com', '', "IP!F6", "proxy"),
    'PC-I5-9400A_Poker': ("token6.json", "credentials1.json", 6, 'luis.gustavo@engenharia.ufjf.br', '', "IP!F6", "proxy"),

    'PC-I5-9400B_PokerIP': ("token7.json", "credentials2.json", 7, 'gayaluisaalmeida@gmail.com', '', "IP!F9", "proxy"),
    'PC-I5-9400B_lgagu': ("token8.json", "credentials2.json", 8, 'lga.gustavo.a@gmail.com', '', "IP!F9", "proxy"),
    'PC-I5-9400B_Poker': ("token9.json", "credentials2.json", 9, 'luis.gustavo@engenharia.ufjf.br', '', "IP!F9", "proxy"),

    'PC-I5-9400C_PokerIP': ("token10.json", "credentials3.json", 10, 'gayaluisaalmeida@gmail.com', '', "IP!F12", "proxy"),
    'PC-I5-9400C_lgagu': ("token11.json", "credentials3.json", 11, 'lga.gustavo.a@gmail.com', '', "IP!F12", "proxy"),
    'PC-I5-9400C_Poker': ("token12.json", "credentials3.json", 12, 'luis.gustavo@engenharia.ufjf.br', '', "IP!F12", "proxy"),

    'PC-I5-13400H_PokerIP': ("token13.json", "credentials4.json", 13, 'gayaluisaalmeida@gmail.com', '', "IP!F15", "proxy"),
    'PC-I5-13400H_lgagu': ("token14.json", "credentials4.json", 14, 'lga.gustavo.a@gmail.com', '', "IP!F15", "proxy"),
    'PC-I5-13400H_Poker': ("token15.json", "credentials4.json", 15, 'luis.gustavo@engenharia.ufjf.br', '', "IP!F15", "proxy"),

    'PC-I5-13400A_PokerIP': ("token16.json", "credentials5.json", 16, 'gayaluisaalmeida@gmail.com', '', "IP!F18", "proxy"),
    'PC-I5-13400A_lgagu': ("token17.json", "credentials5.json", 17, 'lga.gustavo.a@gmail.com', '', "IP!F18", "proxy"),
    'PC-I5-13400A_Poker': ("token18.json", "credentials5.json", 18, 'luis.gustavo@engenharia.ufjf.br', '', "IP!F18", "proxy"),

    'PC-I5-13400B_PokerIP': ("token19.json", "credentials6.json", 19, 'gayaluisaalmeida@gmail.com', '', "IP!F21", "proxy"),
    'PC-I5-13400B_lgagu': ("token20.json", "credentials6.json", 20, 'lga.gustavo.a@gmail.com', '', "IP!F21", "proxy"),
    'PC-I5-13400B_Poker': ("token21.json", "credentials6.json", 21, 'luis.gustavo@engenharia.ufjf.br', '', "IP!F21", "proxy"),

    'PC-I5-13400C_PokerIP': ("token22.json", "credentials7.json", 22, 'gayaluisaalmeida@gmail.com', '', "IP!F24", "proxy"),
    'PC-I5-13400C_lgagu': ("token23.json", "credentials7.json", 23, 'lga.gustavo.a@gmail.com', '', "IP!F24", "proxy"),
    'PC-I5-13400C_Poker': ("token24.json", "credentials7.json", 24, 'luis.gustavo@engenharia.ufjf.br', '', "IP!F24", "proxy"),

    'PC-I5-13400D_PokerIP': ("token25.json", "credentials8.json", 25, 'gayaluisaalmeida@gmail.com', '', "IP!F27", "proxy"),
    'PC-I5-13400D_lgagu': ("token26.json", "credentials8.json", 26, 'lga.gustavo.a@gmail.com', '', "IP!F27", "proxy"),
    'PC-I5-13400D_Poker': ("token27.json", "credentials8.json", 27, 'luis.gustavo@engenharia.ufjf.br', '', "IP!F27", "proxy"),

    'PC-R5-5600G_PokerIP': ("token28.json", "credentials9.json", 28, 'gayaluisaalmeida@gmail.com', '', "IP!F30", "proxy"),
    'PC-R5-5600G_lgagu': ("token29.json", "credentials9.json", 29, 'lga.gustavo.a@gmail.com', '', "IP!F30", "proxy"),
    'PC-R5-5600G_Poker': ("token30.json", "credentials9.json", 30, 'luis.gustavo@engenharia.ufjf.br', '', "IP!F30", "proxy"),

    'PC-I5-13400E_PokerIP': ("token31.json", "credentials10.json", 31, 'gayaluisaalmeida@gmail.com', '', "IP!F33", "proxy"),
    'PC-I5-13400E_lgagu': ("token32.json", "credentials10.json", 32, 'lga.gustavo.a@gmail.com', '', "IP!F33", "proxy"),
    'PC-I5-13400E_Poker': ("token33.json", "credentials10.json", 33, 'luis.gustavo@engenharia.ufjf.br', '', "IP!F33", "proxy"),

    'PC-I5-13400F_PokerIP': ("token34.json", "credentials11.json", 34, 'gayaluisaalmeida@gmail.com', '', "IP!F36", "proxy"),
    'PC-I5-13400F_lgagu': ("token35.json", "credentials11.json", 35, 'lga.gustavo.a@gmail.com', '', "IP!F36", "proxy"),
    'PC-I5-13400F_Poker': ("token36.json", "credentials11.json", 36, 'luis.gustavo@engenharia.ufjf.br', '', "IP!F36", "proxy"),

    'PC-I5-13400G_PokerIP': ("token37.json", "credentials12.json", 37, 'gayaluisaalmeida@gmail.com', '', "IP!F39", "proxy"),
    'PC-I5-13400G_lgagu': ("token38.json", "credentials12.json", 38, 'lga.gustavo.a@gmail.com', '', "IP!F39", "proxy"),
    'PC-I5-13400G_Poker': ("token39.json", "credentials12.json", 39, 'luis.gustavo@engenharia.ufjf.br', '', "IP!F39", "proxy"),

    'PC-I5-13400I_PokerIP': ("token40.json", "credentials13.json", 40, 'gayaluisaalmeida@gmail.com', '', "IP!F42", "proxy"),
    'PC-I5-13400I_lgagu': ("token41.json", "credentials13.json", 41, 'lga.gustavo.a@gmail.com', '', "IP!F42", "proxy"),
    'PC-I5-13400I_Poker': ("token42.json", "credentials13.json", 42, 'luis.gustavo@engenharia.ufjf.br', '', "IP!F42", "proxy"),

    'PC-R5-7600_PokerIP': ("token43.json", "credentials14.json", 43, 'gayaluisaalmeida@gmail.com', '', "IP!F45", "proxy"),
    'PC-R5-7600_lgagu': ("token44.json", "credentials14.json", 44, 'lga.gustavo.a@gmail.com', '', "IP!F45", "proxy"),
    'PC-R5-7600_Poker': ("token45.json", "credentials14.json", 45, 'luis.gustavo@engenharia.ufjf.br', '', "IP!F45", "proxy"),

    'PC-i3-8145U_PokerIP': ("token46.json", "credentials14.json", 46, 'gayaluisaalmeida@gmail.com', '', "IP!F48", "proxy"),
    # 'PC-i3-8145U_lgagu': ("token47.json", "credentials14.json", 47, 'lga.gustavo.a@gmail.com', '', "IP!F48", "modem"),
    # 'PC-i3-8145U_Poker': ("token48.json", "credentials14.json", 48, 'luis.gustavo@engenharia.ufjf.br', '', "IP!F48", "modem"),

    # 'PC-I7-9700KF_PokerIP': ("token49.json", "credentials14.json", 49, 'gayaluisaalmeida@gmail.com', '', "IP!F51", "vero"),
    'PC-I7-9700KF_lgagu': ("token50.json", "credentials14.json", 50, 'lga.gustavo.a@gmail.com', '', "IP!F51", "proxy"),
    # 'PC-I7-9700KF_Poker': ("token51.json", "credentials14.json", 51, 'luis.gustavo@engenharia.ufjf.br', '', "IP!F51", "vero")
}

numero_pc = f"PC{dicionari_token_credencial_n[nome_completo][2] :02d}"
endereco_IP = f"{dicionari_token_credencial_n[nome_completo][5]}"
tipo_conexao = f"{dicionari_token_credencial_n[nome_completo][6]}"

# valor_dicionario = dicionari_token_credencial_n[nome_completo]
