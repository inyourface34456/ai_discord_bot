import discord
from discord.ext import commands
import os
import webserver
import requests

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")

intents = discord.Intents.all()
# intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

url = ""

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
        "max_tokens": 1000,
    }

    await ctx.send("generating...")
    response = requests.post(f"{url}/v1/completions", json=data, headers={"Content-Type": "application/json"})
    await ctx.send(response.json()["choices"][0]["text"])

@bot.command()
async def set_url(ctx, loc_url: str):
    global url
    if ctx.author.id == 804444072063664148:
        url = loc_url
        await ctx.send("Setting URL to {}".format(url))
    else:
        await ctx.send("You are not authorized to use this command.")
        return

webserver.keep_alive()
bot.run(DISCORD_TOKEN)