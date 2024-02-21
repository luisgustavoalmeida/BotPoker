import asyncio
import os
import socket

from telegram import Bot

# Obter o nome de usuário
nome_usuario = os.getlogin()
# print("Nome de usuário:", nome_usuario)

# Obter o nome do computador
nome_computador = socket.gethostname()


async def enviar_mensagem(mensagem, token='6446494638:AAE5lkb9s74m_5R8DE-z2uDqt5PrYEQUTo8', chat_id='-1001971264843', ):
    # Inicializa o bot com o token fornecido
    bot = Bot(token)

    # Envia a mensagem para o chat especificado
    await bot.send_message(chat_id=chat_id, text=mensagem)


def monta_mensagem(mensagem):
    mensagem_montada = "O computador: " + str(nome_computador) + ' Usuario: ' + str(nome_usuario) + ': ' + str(mensagem)
    # Executa a função de envio de mensagem assíncrona
    asyncio.run(enviar_mensagem(mensagem_montada))

monta_mensagem('ta ligado.')
