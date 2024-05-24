import discord
from discord.ext import commands
import settings


def run():
    # Stup do bot
    intents = discord.Intents.all()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    bot.remove_command("help")

    # Inicia o bot e carrega os comandos
    @bot.event
    async def on_ready():
        print(f'{bot.user} agora está rodando!')
        try:
            for cmd_file in settings.CMDS_DIR.glob("*.py"):
                if cmd_file.name != "__init__.py":
                    await bot.load_extension(f"cmds.{cmd_file.name[:-3]}")

            bot.tree.copy_global_to(guild=settings.GUILDS_ID)
            synced = await bot.tree.sync(guild=settings.GUILDS_ID)
            print(f"synced {len(synced)} commands")
        except Exception as e:
            print(e)

    bot.run(settings.TOKEN)


# Liga o bot
if __name__ == '__main__':
    run()
