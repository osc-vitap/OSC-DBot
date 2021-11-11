from modules.osc_event_notif import *
from modules.news_updates import *
from modules.utils import *
from dotenv import load_dotenv
import discord
from os import getenv

if __name__ == "__main__":
    load_dotenv()
    TOKEN = getenv("DISCORD_TOKEN")
    client = discord.Client()  # init discord client

    with open("data/settings.json", "r") as f:
        data = json.load(f)

    @client.event
    async def on_ready():
        print(f"{client.user} has connected to Discord!")
        activity = discord.Activity(
            type=discord.ActivityType.listening, name=f"{data['prefix']}help"
        )
        await client.change_presence(activity=activity)

        message_channel = client.get_channel(data["ChannelID"]["event"])
        oscEventNotif.start(message_channel)

        news_channel = client.get_channel(data["ChannelID"]["news"])
        news_updates.start(news_channel)

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        response = commands.validate(message.content)
        if type(response) == discord.embeds.Embed:
            await message.channel.send(embed=response)
        elif response:
            await message.channel.send(response)

        if isinstance(message.channel, discord.DMChannel):
            dm_channel = client.get_channel(data["ChannelID"]["dm"])
            dm_notif = (
                f"**[!] Server logs: {message.author}** sent:```\n{message.content}```"
            )
            await dm_channel.send(dm_notif)

    client.run(TOKEN)  # run discord client
