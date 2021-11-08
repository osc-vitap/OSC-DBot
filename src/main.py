from modules.osc_event_notif import *
from modules.news_updates import *
from modules.utils import commands
from dotenv import load_dotenv
import time
import discord
import os

if __name__ == "__main__":
    load_dotenv()  # load .env file
    TOKEN = os.getenv("DISCORD_TOKEN")
    client = discord.Client()  # init discord client

    @client.event
    async def on_ready():
        print(f"{client.user} has connected to Discord!")
        activity = discord.Activity(type=discord.ActivityType.listening, name=">help")
        await client.change_presence(activity=activity)

        message_channel = client.get_channel(904455110212591676)
        oscEventNotif.start(message_channel)

        news_channel = client.get_channel(904455110212591676)
        news_updates.start(news_channel)

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        response = commands(message.content)
        if response:
            await message.channel.send(response)

    client.run(TOKEN)  # run discord client
