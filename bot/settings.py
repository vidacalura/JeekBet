import pathlib
from typing import Final
import os
import discord
from dotenv import load_dotenv

# Carrega o token do bot
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
USER: Final[str] = os.getenv('USER_DB')
PASSWORD: Final[str] = os.getenv('PASSWORD')
HOST: Final[str] = os.getenv('HOST')
PORT: Final[str] = os.getenv('PORT')
DATABASE: Final[str] = os.getenv('DATABASE')

BASE_DIR = pathlib.Path(__file__).parent

CMDS_DIR = BASE_DIR / "cmds"

GUILDS_ID = discord.Object(id=int(os.getenv("GUILD")))
