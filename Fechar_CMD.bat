@echo off
REM Enable UTF-8 character support
chcp 65001 > nul
REM Executa o script AutoHotkey para posicionar e redimensionar a janela do prompt de comando
echo    O CMD aberto anteriormente será fechado e o código python local atualizado com o GitHub
timeout /t 2 >nul
python fecha_cmd.py
timeout /t 2 >nul
start "" "move_janela.bat.ahk"

REM Adiciona exceção para o diretório BotGit
git config --global --add safe.directory C:/GitHub/BotPoker
echo.
echo    Repositorio será atualizado!
echo.
timeout /t 10 >nul
echo.
git pull origin main
echo.
echo    Repositorio atualizado com sucesso!
echo.
echo.
echo   **************************************************************
echo   **                                                          **
echo   **                     Bem-vindo a                          **
echo   **                                                          **
echo   **            S P E C T R O   S O L U T I O N               **
echo   **                                                          **
echo   **************************************************************
:inicio
REM Enable UTF-8 character support
chcp 65001 > nul
echo.
git fetch origin
echo.
REM Opções
echo   **                 O que voce deseja fazer?                 **
echo.
echo        1. Iniciar o Script Principal.
echo        2. Remover o Poker Brasil.
echo        3. Recolher Manual.
echo        4. Recolher Automático.
echo        5. Entrar no Facebook.
echo        6. Interface de comando e controle.
echo        7. Instalar bibliotecas Python via comando pip.
echo        8. Atualizar repositório local com GitHub.
echo        9. Substitui repositório local pelo do GitHub.
echo.
git status | findstr /C:"Your branch is behind" >nul
if errorlevel 1 (
    echo.
    echo    - Programa local atualizado com o GitHub.
    echo.
) else (
    echo.
    echo                - A T E N Ç Ã O -
    echo.
    echo    - Novas atualizações disponíveis no GitHub!
    echo.
)
echo.
REM Define o tempo de espera em segundos
set "tempo_espera=15"
REM Pergunta ao usuário
echo    Aguardando resposta...
echo.
echo    Voce tem %tempo_espera% segundos para escolher ou sera iniciado o
echo    'Script Principal'.
echo.
choice /c 123456789 /t %tempo_espera% /d 1 /m "   Escolha: "
REM se nao imfornar nada cai no primeiro item da lista
REM Verifica a escolha do usuário
REM     timeout /t 1 /nobreak >nul
if errorlevel 9 (
    echo.
    echo    Substitui repositorio local pelo do GitHub.
    echo.
    git fetch origin
    echo.
    timeout /t 1 /nobreak > nul
    echo.
    git reset --hard origin/main
    echo.
    echo    Repositorio substitution com sucesso!
    echo.
    pause
    goto :inicio
) else if errorlevel 8 (
    echo.
    echo    Atualizar repositorio local com GitHub selecionado.
    echo.
    git pull origin main
    echo.
    echo    Repositorio atualizado com sucesso!
    echo.
    pause
    goto :inicio
) else if errorlevel 7 (
    echo.
    echo    Instalar bibliotecas Python selecionado.
    echo.
    pip install -r requirements.txt
    echo.
    echo    Bibliotecas instaladas / atualizadas com sucesso via comando pip!
    echo.
    goto :inicio
) else if errorlevel 6 (
    echo.
    echo    Interface de comando selecionado.
    echo.
    chcp 850 > nul
    python Tela.py
) else if errorlevel 5 (
    echo.
    echo    Entrar no facebook selecionado.
    echo.
    chcp 850 > nul
    python InicializarFace.py
    python main.py
) else if errorlevel 4 (
    echo.
    echo    Recolher automático selecionado.
    echo.
    chcp 850
    python InicializarRecolherAuto.py
    python main.py
) else if errorlevel 3 (
    echo.
    echo    Recolher manual selecionado.
    echo.
    chcp 850 > nul
    python InicializarRecolher.py
    python main.py
) else if errorlevel 2 (
    echo.
    echo    Remover Poker selecionado.
    echo.
    chcp 850 > nul
    python InicializarRemover.py
    python main.py
) else if errorlevel 1 (
    echo.
    python InicializarAtualizarBiblioteca.py
    echo.
    echo.
    echo    Script Principal selecionado.
    echo.
    echo.
    echo.
    chcp 850 > nul
    python InicializarRoleta.py
    python main.py
)
pause
goto :inicio
pause
exit /b

