import discord
from discord.ext import commands
		
TOKEN=('bot_token')
		
bot = commands.Bot(command_prefix='!')
		
@bot.command()
async def Hello(ctx):
		await ctx.send('Hi, the bot is running well!')
		
bot.run(TOKEN)
