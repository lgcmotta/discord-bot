import os
from discord.ext import commands
from dotenv import load_dotenv
from os import listdir
from os.path import isfile, join

commands_dir = 'commands'
cogs_dir = 'cogs'

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Bot is online!')


def load_commands():
    for command in [file.replace('.py', '') for file in listdir(commands_dir) if isfile(join(commands_dir, file))]:
        bot.load_extension(f'{commands_dir}.{command}')


def load_events():
    for cog in [file.replace('.py', '') for file in listdir(cogs_dir) if isfile(join(cogs_dir, file))]:
        bot.load_extension(f'{cogs_dir}.{cog}')


load_commands()
load_events()

bot.run(TOKEN)
