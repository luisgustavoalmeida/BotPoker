@echo off

REM Executa o script AutoHotkey para posicionar e redimensionar a janela do prompt de comando
start "" "move_janela.bat.ahk"

timeout /t 1 /nobreak >nul
echo Bem vindo!

REM Define o tempo de espera em segundos
set "tempo_espera=10"

REM Pergunta ao usuário
echo Aguardando resposta.
echo Voce tem %tempo_espera% segundos para escolher ou sera iniciado o main.
choice /c 123 /t %tempo_espera% /d 1 /m "Escolha: (1) para main, (2) Remover Poker, (3) Recolher."
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
