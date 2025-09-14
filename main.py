import discord
from discord.ext import commands
import webserver
import os
import requests_async

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
MY_USER_ID = 804444072063664148

intents = discord.Intents.all()
# intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

url = ""
length = 7000

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
        "max_tokens": length,
        "temperature": 1,
        "min_p": 0.2,
    }

    await ctx.send("generating...")
    await ctx.typing()
    response = await requests_async.post(f"{url}/v1/completions", json=data, headers={"Content-Type": "application/json"}, timeout=180)
    text = response.json()["choices"][0]["text"]
    for chuck in [text[i:i + 2000] for i in range(0, len(text), 2000)]:
        await ctx.send(chuck)

@bot.command()
async def set_url(ctx, loc_url: str):
    global url
    if ctx.author.id == MY_USER_ID:
        url = loc_url
        await ctx.send(f"Set URL to {url}")
    else:
        await ctx.send("You are not authorized to use this command.")
        return

@bot.command()
async def set_length(ctx, loc_length: int):
    global length
    if ctx.author.id == MY_USER_ID:
        length = loc_length
        await ctx.send(f"Set length to {length}")
    else:
        await ctx.send("You are not authorized to use this command.")
        return

webserver.keep_alive()
bot.run(DISCORD_TOKEN)