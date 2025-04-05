import discord
from discord.ext import commands
		
TOKEN=('bot_token')
		
bot = commands.Bot(command_prefix='!')
		
@bot.command()
async def Hello(ctx):
		await ctx.send('Hi, the bot is running well!')

@bot.command()
async def help(ctx):
    help_text = """
    **Help Menu**
    - `!help`: Display this help message.
    - `!hello`: See if the bot works.
    """
    await ctx.send(help_text)

bot.run(TOKEN)
