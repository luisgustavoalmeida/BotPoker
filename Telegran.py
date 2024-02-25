import asyncio

from telegram import Bot

from Google import numero_pc


# Site para encontar os emojes https://emojipedia.org/pt   https://emojipedia.org/pt/google

async def enviar_mensagem(mensagem, token='6446494638:AAE5lkb9s74m_5R8DE-z2uDqt5PrYEQUTo8', chat_id='-1001971264843', ):
    try:
        # Inicializa o bot com o token fornecido
        bot = Bot(token)

        # Envia a mensagem para o chat especificado
        await bot.send_message(chat_id=chat_id, text=mensagem, disable_notification=False)
    except Exception as e:
        # Registra o erro e a mensagem
        print(f"Erro ao enviar mensagem: {e}")


def monta_mensagem(mensagem):
    mensagem_montada = '🤖  ' + numero_pc + ': ' + str(mensagem)
    # Executa a função de envio de mensagem assíncrona
    asyncio.run(enviar_mensagem(mensagem_montada))


async def enviar_mensagem_silenciosa(mensagem, token='6446494638:AAE5lkb9s74m_5R8DE-z2uDqt5PrYEQUTo8', chat_id='-1001971264843', ):
    try:
        # Inicializa o bot com o token fornecido
        bot = Bot(token)

        # Envia a mensagem para o chat especificado sem notificação
        await bot.send_message(chat_id=chat_id, text=mensagem, disable_notification=True)
    except Exception as e:
        # Registra o erro e a mensagem
        print(f"Erro ao enviar mensagem: {e}")


def monta_mensagem_silenciosa(mensagem):
    mensagem_montada = '🤖  ' + numero_pc + ': ' + str(mensagem) + '  🔇'
    # Executa a função de envio de mensagem silenciosa assíncrona
    asyncio.run(enviar_mensagem_silenciosa(mensagem_montada))

# Exemplo de envio de mensagem silenciosa
# monta_mensagem_silenciosa("Esta é uma mensagem silenciosa.")


#
# # monta_mensagem('ta ligado. \U0001F4BB')
# # monta_mensagem('Codigi iniciado \U0001F680')
# monta_mensagem('Codigi iniciado ⚡')
