
@echo off
REM Executa o script AutoHotkey para posicionar e redimensionar a janela do prompt de comando
start "" "move_janela.bat.ahk"

timeout /t 1 /nobreak >nul

echo.
echo **************************************************************
echo **                                                          **
echo **                     Bem-vindo a                          **
echo **            S P E C T R O   S O L U T I O N               **
echo **                                                          **
echo **************************************************************
echo.

REM Opções
echo **             O que voce deseja fazer hoje?                **
echo.
echo    1. Iniciar o Script Principal (main.py)
echo    2. Remover o Poker (RemoverPK.py)
echo    3. Recolher (ExecutaComando.py)
echo.


REM Define o tempo de espera em segundos
set "tempo_espera=15"

REM Pergunta ao usuário
echo Aguardando resposta.
echo Voce tem %tempo_espera% segundos para escolher ou sera iniciado o main.
choice /c 123 /t %tempo_espera% /d 1 /m "Escolha: "
REM se nao imfornar nada cai no primeiro item da lista
REM Verifica a escolha do usuário
if errorlevel 3 (
    echo.
    echo Recolher selecionado.
    echo.
    timeout /t 1 /nobreak >nul
    python ExecutaComando.py
) else if errorlevel 2 (
    echo.
    echo Remover Poker selecionado.
    echo.
    timeout /t 1 /nobreak >nul
    python RemoverPK.py
) else if errorlevel 1 (
    echo.
    echo Executando python main.py.
    echo.
    timeout /t 1 /nobreak >nul
    python main.py
)

pause
exit /b
