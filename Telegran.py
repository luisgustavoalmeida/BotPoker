import asyncio

from telegram import Bot

from Google import numero_pc

token = '6446494638:AAE5lkb9s74m_5R8DE-z2uDqt5PrYEQUTo8'
chat_id = '-1001971264843'

MAX_TENTATIVAS = 3
DELAY_ENTRE_TENTATIVAS = 2


# Site para encontar os emojes https://emojipedia.org/pt   https://emojipedia.org/pt/google

async def enviar_mensagem(mensagem, disable_notification=False):
    """
    Envia a mensagem.

    Args:
        mensagem: A mensagem a ser enviada.
        disable_notification: Se True, a mensagem será enviada sem notificação.

    Returns:
        True se a mensagem foi enviada com sucesso, False caso contrário.
    """
    try:
        # Inicializa o bot com o token fornecido
        bot = Bot(token)
        # Envia a mensagem para o chat especificado
        await bot.send_message(chat_id=chat_id, text=mensagem, disable_notification=disable_notification)
        return True
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")
        await asyncio.sleep(DELAY_ENTRE_TENTATIVAS)


async def enviar_mensagem_com_reenvio(mensagem, disable_notification=False):
    """
    Envia a mensagem com reenvio automático em caso de falha temporária.

    Args:
        mensagem: A mensagem a ser enviada.
        disable_notification: Se True, a mensagem será enviada sem notificação.

    Returns:
        True se a mensagem foi enviada com sucesso, False caso contrário.
    """

    tentativas = 0
    while tentativas < MAX_TENTATIVAS:
        try:
            await enviar_mensagem(mensagem, disable_notification)
            return True
        except Exception as e:
            print(f"Erro ao enviar mensagem (tentativa {tentativas + 1}/{MAX_TENTATIVAS}): {e}")
            await asyncio.sleep(DELAY_ENTRE_TENTATIVAS)
            tentativas += 1
    else:
        print(f"Falha ao enviar mensagem após {MAX_TENTATIVAS} tentativas.")
        # logger.error(f"Falha ao enviar mensagem após {MAX_TENTATIVAS} tentativas.")
        return False


def monta_mensagem(mensagem, disabilitar_notificacao=False):
    if disabilitar_notificacao:
        icone_som = '🔊'
    else:
        icone_som = '🔇'
    mensagem_montada = f'🤖   {numero_pc}: {str(mensagem)}. {icone_som}'
    # Executa a função de envio de mensagem assíncrona
    # asyncio.run(enviar_mensagem(mensagem_montada, False))
    asyncio.run(enviar_mensagem_com_reenvio(mensagem_montada, disabilitar_notificacao))

# monta_mensagem("Esta é uma mensagem de teste.", True)
