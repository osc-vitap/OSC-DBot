import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '>hey':
        response = "Hello world"
        await message.channel.send(response)

client.run(TOKEN)