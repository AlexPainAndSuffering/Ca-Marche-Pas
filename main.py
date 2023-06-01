# bot.py
import os

import discord
import json

from CustomClient import CustomClient
import utility
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True

client = CustomClient(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    with open("white_list.json", "r") as json_file:
        data = json.load(json_file)
        words = data["white_list"]
    if utility.word_exist(message.content, words):
        await message.channel.send("Ça marche pas ça n'a pas de jambes!!!")


client.run(TOKEN)