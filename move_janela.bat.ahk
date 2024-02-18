#SingleInstance force

; Calcula as dimensões da tela
SysGet, screenWidth, 0
SysGet, screenHeight, 1

; Define as dimensões desejadas para a janela do prompt de comando
novoWidth := 560
novoHeight := 1050

; Calcula a posição x para a janela (à direita da tela)
posX := screenWidth - novoWidth

; Move e redimensiona a janela do prompt de comando
WinMove, ahk_class ConsoleWindowClass,, posX, 0, novoWidth, novoHeight

; Define a janela para sempre estar no topo
WinSet, AlwaysOnTop, On, ahk_class ConsoleWindowClass
