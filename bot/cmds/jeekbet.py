import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord import app_commands
from models.Usuario import Usuario, get_ranking_usuarios
from models.Aposta import Aposta


class Plebe(app_commands.Group):
    @app_commands.command()
    async def salve(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Salvee {interaction.user.mention}!")

    @app_commands.command(name="criar-conta",
                      description="Cadastra um novo usuário no JeekBet")
    async def criar_conta(self, interaction: discord.Interaction):
        usu = Usuario(interaction.user.id, interaction.user.name, 0)

        try:
            usu.cadastrar_usuario()
            await interaction.response.send_message("Conta cadastrada com sucesso!")
        except Exception as e:
            await interaction.response.send_message(str(e))

    @app_commands.command(description="Mostra quanto de dinheiro o usuário tem")
    async def dinheiro(self, interaction: discord.Interaction):
        usu = Usuario(interaction.user.id, interaction.user.name, 0)

        try:
            await interaction.response.send_message(f"Você tem {usu.get_dinheiro()} Jeek points")
        except Exception as e:
            await interaction.response.send_message(str(e))

    @app_commands.command(description="Mostra o ranking da Jeeconomia")
    async def ranking(self, interaction: discord.Interaction):
        try:
            i = 1
            usu_arr = get_ranking_usuarios()
            for usu in usu_arr:
                await interaction.response.send_message(f"{i}. {usu.nome} - {usu.dinheiro} Jeek Points")
                i += 1
        except Exception as e:
            await interaction.response.send_message(str(e))


class Adm(app_commands.Group):
    @app_commands.command(description="Adm teste")
    @has_permissions(administrator=True)
    async def adm(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Parabéns {interaction.user.mention} vc é adm!")


async def setup(bot):
    bot.tree.add_command(Adm(name="adm", description="Comandos dos adms"))
    bot.tree.add_command(Plebe(name="aposta", description="Comandos da plebe"))
