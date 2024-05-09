from discord.ext import commands
from discord.ext.commands import has_permissions


@commands.group()
async def comandos(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f"No, {ctx.subcommand_passed} does not belong to simple")


@commands.command()
async def ping(ctx):
    """Responde pong"""
    await ctx.send("pong")


@commands.command(description="Mostra o ranking da Jeekeconomia")
async def ranking(ctx):
    await ctx.send('[Lista bem poggers aqui]')


@commands.command(description="Adm teste")
@has_permissions(administrator=True)
async def adm(ctx):
    await ctx.send("Parabéns vc é adm!")


async def setup(bot):
    bot.add_command(ping)
    bot.add_command(ranking)
    bot.add_command(adm)
