import disnake
from disnake.ext import commands
import config
from config import *
import os

bot = commands.Bot(command_prefix = commands.Bot(command_prefix="."),intents= disnake.Intents.all())
bot.remove_command('help')

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(Token)


