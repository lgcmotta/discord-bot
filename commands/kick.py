from discord.ext import commands


@commands.command()
async def kick(ctx, args):
    await ctx.send(f'Voting to kick {args} from the server has started.')


def setup(bot):
    bot.add_command(kick)
