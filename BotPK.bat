@echo off

REM Pausa por 1 segundo
timeout /t 1 /nobreak >nul
echo Bem vindo!

REM Executa o script AutoHotkey para posicionar e redimensionar a janela do prompt de comando
start "" "move_janela.bat.ahk"
echo Iniciando em:
REM Pausa por 1 segundo
timeout /t 1 /nobreak >nul
echo 5
REM Pausa por 1 segundo
timeout /t 1 /nobreak >nul
echo 4
REM Pausa por 1 segundo
timeout /t 1 /nobreak >nul
echo 3
REM Pausa por 1 segundo
timeout /t 1 /nobreak >nul
echo 2
REM Pausa por 1 segundo
timeout /t 1 /nobreak >nul
echo 1
REM Pausa por 1 segundo
timeout /t 1 /nobreak >nul

REM echo Pressione qualquer tecla para iniciar...
Rem pause >nul

REM Inicia o script Python
python main.py

pause
