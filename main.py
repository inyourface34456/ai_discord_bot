import discord
from discord.ext import commands
import os
import webserver

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")

intents = discord.Intents.all()
# intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

webserver.keep_alive()
bot.run(DISCORD_TOKEN)