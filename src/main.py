from dotenv import load_dotenv
from modules.utils import commands
from modules.osc_event_notif import *
import discord
import os

if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        response = commands(message.content)
        await message.channel.send(response)

    oscEventNotif.start()
    client.run(TOKEN)