import os

# Abre o FIFO em modo de leitura
fifo_fd = os.open('meu_fifo', os.O_RDONLY)

# Lê dados do FIFO
data = os.read(fifo_fd, 4096)  # Lê até 4096 bytes de dados

# Fecha o descritor de arquivo FIFO
os.close(fifo_fd)

print("Dados lidos do FIFO:", data)
