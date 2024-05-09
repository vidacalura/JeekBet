import pathlib
from typing import Final
import os
import logging
from logging.config import dictConfig
from dotenv import load_dotenv

# Carrega o token do bot
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

BASE_DIR = pathlib.Path(__file__).parent

CMDS_DIR = BASE_DIR / "cmds"
