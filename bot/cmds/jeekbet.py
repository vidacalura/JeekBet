from discord.ext import commands
from discord.ext.commands import has_permissions
from models.Usuario import Usuario
from models.Usuario import get_ranking_usuarios


@commands.group()
async def comandos(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f"No, {ctx.subcommand_passed} does not belong to simple")


@commands.command(description="Responde pong")
async def ping(ctx):
    await ctx.send("pong")

@commands.command(name="criar-conta",
                  description="Cadastra um novo usuário no JeekBet")
async def criar_conta(ctx):
    usu = Usuario(ctx.message.author.id, ctx.message.author.name, 0)

    try:
        usu.cadastrar_usuario()
        await ctx.send("Conta cadastrada com sucesso!")
    except Exception as e:
        await ctx.send(str(e))

@commands.command(description="Mostra quanto de dinheiro o usuário tem")
async def dinheiro(ctx):
    usu = Usuario(ctx.message.author.id, ctx.message.author.name, 0)

    try:
        await ctx.send(f"Você tem {usu.get_dinheiro()} Jeek points")
    except Exception as e:
        await ctx.send(str(e))

@commands.command(description="Mostra o ranking da Jeeconomia")
async def ranking(ctx):
    try:
        i = 1
        usu_arr = get_ranking_usuarios()
        for usu in usu_arr:
            await ctx.send(f"{i}. {usu.nome} - {usu.dinheiro} Jeek Points")
            i += 1
    except Exception as e:
        await ctx.send(str(e))

@commands.command(description="Adm teste")
@has_permissions(administrator=True)
async def adm(ctx):
    await ctx.send("Parabéns vc é adm!")


async def setup(bot):
    bot.add_command(ping)
    bot.add_command(criar_conta)
    bot.add_command(dinheiro)
    bot.add_command(ranking)
    bot.add_command(adm)
