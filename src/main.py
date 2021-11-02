from modules.osc_event_notif import *
from modules.utils import commands
from dotenv import load_dotenv
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
        if response:
            await message.channel.send(response)

    oscEventNotif.start()
    client.run(TOKEN)