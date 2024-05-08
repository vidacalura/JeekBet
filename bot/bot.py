from typing import Final
import logging
import logging.handlers
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from discord.ext import commands
from jeekbet import get_response

# Carrega o token do bot
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Stup do bot
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)


# Lida com as Mensagens
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(jfgjiojiojio)')
        return

    # ao colocar "?" antes do comando faz o bot mandar a resposta no PV
    #    if is_private := user_message[0] == '?':
    #        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)


# Iniciando o bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} agora está rodando!')


# Faz o logging das mensagens
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


# Entrada do main
def main():
    logger = logging.getLogger('discord')
    logger.setLevel(logging.INFO)

    handler = logging.handlers.RotatingFileHandler(
        filename='discord.log',
        encoding='utf-8',
        maxBytes=32 * 1024 * 1024,  # 32 MiB
        backupCount=5,  # Gera até 5 arquivos de logs diferentes
    )
    dt_fmt = '%m-%d-%Y %H:%M:%S'
    formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    client.run(token=TOKEN)


if __name__ == '__main__':
    main()
