import discord

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(
    command_prefix='!',
    description="Um bot de apostas com moeda fictícia para jogos de Jeek",
    intents=intents
)

@bot.event
async def on_ready():
    print(f"Loggado com {bot.user}")
