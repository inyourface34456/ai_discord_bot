import discord
from discord.ext import commands
import os
import webserver
import requests

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

@bot.command()
async def prompt(ctx, *, text: str):
    data = {
        "prompt": f"{text}",
        "max_tokens": 5000,
    }

    ctx.typing()
    response = requests.post(f"https://storm-lowest-gd-receive.trycloudflare.com/v1/completions", json=data, headers={"Content-Type": "application/json", "Authorization": "Bearer  password"})
    await ctx.send(response.json())

webserver.keep_alive()
bot.run(DISCORD_TOKEN)