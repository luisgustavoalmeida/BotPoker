@echo off

REM Pausa por 1 segundo
timeout /t 1 /nobreak >nul
echo Bem vindo!

REM Executa o script AutoHotkey para posicionar e redimensionar a janela do prompt de comando
start "" "move_janela.bat.ahk"

echo Pressione qualquer tecla para iniciar...
pause >nul

REM Pausa por 1 segundo
timeout /t 1 /nobreak >nul

REM Inicia o script Python
python main.py

pause
