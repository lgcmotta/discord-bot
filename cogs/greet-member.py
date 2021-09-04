import os
from discord.ext import commands
from random import randint


class GreetMember(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.GREET_CHANNEL = int(os.getenv('GREET_CHANNEL'))

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

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if not before.channel and after.channel:
            channel = member.bot.get_channel(self.GREET_CHANNEL)
            await channel.send(self.get_greet_message(member.display_name))


def setup(bot):
    bot.add_cog(GreetMember(bot))
