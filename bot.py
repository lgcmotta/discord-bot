import discord
from discord.ext import commands
import json
from random import randint

configuration = {}

client = commands.Bot(command_prefix='!')


def get_greet_message(name=str):
    greet_messages = [
        f'Greetings, {name}!!',
        f'Attention! {name} has something to say:',
        f'Silence! Stop talking about {name}',
        f'Everybody was waiting for you to join {name}',
        f'You again {name}?',
        f'{name}!!! I\'ve missed you here!',
        f'{name} is online, nonsense is coming.',
        f'I\'ve noticed you here {name}'
    ]
    return greet_messages[randint(0, len(greet_messages) - 1)]


def read_config():
    with open('config.json') as file:
        json_config = json.load(file)
        configuration['token'] = json_config['token']
        configuration['greet_channel'] = json_config['greet_channel']
        file.close()


@client.event
async def on_ready():
    print('Discord bot is up!')


@client.event
async def on_voice_state_update(member, before, after):
    if not before.channel and after.channel:
        channel = client.get_channel(configuration['greet_channel'])
        await channel.send(get_greet_message(member.display_name))

read_config()

client.run(configuration['token'])
