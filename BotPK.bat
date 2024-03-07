@echo off
REM Executa o script AutoHotkey para posicionar e redimensionar a janela do prompt de comando
start "" "move_janela.bat.ahk"

REM Adiciona exceção para o diretório BotGit
git config --global --add safe.directory C:/GitHub/BotPoker
echo.
echo   **************************************************************
echo   **                                                          **
echo   **                     Bem-vindo a                          **
echo   **            S P E C T R O   S O L U T I O N               **
echo   **                                                          **
echo   **************************************************************
:inicio
echo.
timeout /t 0.3 /nobreak >nul
REM Opções
echo   **                 O que voce deseja fazer?                 **
echo.
echo        1. Iniciar o Script Principal.
echo        2. Remover o Poker Brasil.
echo        3. Recolher fichas.
echo        4. Interface de comando e controle.
echo        5. Instalar bibliotecas Python.
echo        6. Atualizar repositorio local com GitHub.
echo.
REM Define o tempo de espera em segundos
set "tempo_espera=15"
timeout /t 0.3 /nobreak >nul
REM Pergunta ao usuário
echo    Aguardando resposta.
echo.
echo    Voce tem %tempo_espera% segundos para escolher ou sera iniciado o
echo    Script Principal.
echo.
choice /c 123456 /t %tempo_espera% /d 1 /m "   Escolha: "
REM se nao imfornar nada cai no primeiro item da lista
REM Verifica a escolha do usuário
if errorlevel 6 (
    echo.
    echo    Atualizar repositorio local com GitHub selecionado.
    echo.
    timeout /t 1 /nobreak >nul
    git pull origin main
    echo.
    echo    Repositorio atualizado com sucesso!
    echo.
    pause
    echo.
    goto :inicio
) else if errorlevel 5 (
    echo.
    echo    Instalar bibliotecas Python selecionado.
    echo.
    timeout /t 1 /nobreak >nul
    pip install -r requirements.txt
    echo.
    echo.
    echo    Bibliotecas instaladas / atualizadas com sucesso!
    echo.
    pause
    echo.
    goto :inicio
) else if errorlevel 4 (
    echo.
    echo    Interface de comando selecionado.
    echo.
    timeout /t 1 /nobreak >nul
    python Tela.py
) else if errorlevel 3 (
    echo.
    echo    Recolher selecionado.
    echo.
    timeout /t 1 /nobreak >nul
    python ExecutaComando.py
) else if errorlevel 2 (
    echo.
    echo    Remover Poker selecionado.
    echo.
    timeout /t 1 /nobreak >nul
    python RemoverPK.py
) else if errorlevel 1 (
    echo.
    echo    Script Principal selecionado.
    echo.
    timeout /t 1 /nobreak >nul
    python main.py
)
pause
REM goto :inicio
pause
exit /b

