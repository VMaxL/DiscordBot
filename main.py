from discord.ext import commands
from settings import *

# TODO have bot call Adam gay on command Adam

bot = commands.Bot(command_prefix="`")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)
