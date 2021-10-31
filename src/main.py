import os
import discord
from dotenv import load_dotenv
from modules.utils import commands

if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    client = discord.Client()

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        response = commands(message.content)
        await message.channel.send(response)

    client.run(TOKEN)
