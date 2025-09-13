import discord
from discord.ext import commands
import os
import webserver

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_message(message):
    if message.content.startswith("!"):
        bot.send_message(message.channel, "hi")

webserver.keep_alive()
bot.run(DISCORD_TOKEN)