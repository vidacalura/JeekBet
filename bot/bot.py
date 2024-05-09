import discord
from discord import Message
from discord.ext import commands
import settings


def run():
    # Stup do bot
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

# Inicia o bot e carrega os comandos
    @bot.event
    async def on_ready():
        print(f'{bot.user} agora está rodando!')

        for cmd_file in settings.CMDS_DIR.glob("*.py"):
            if cmd_file.name != "__init__.py":
                await bot.load_extension(f"cmds.{cmd_file.name[:-3]}")

    bot.run(settings.TOKEN)


# Liga o bot
if __name__ == '__main__':
    run()
