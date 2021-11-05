from discord.ext import tasks, commands
from urllib.request import urlopen
from dotenv import load_dotenv
from datetime import datetime
import discord
import json
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='>')
client = discord.Client()

@tasks.loop(hours=12)
async def oscEventNotif(message_channel):
    url = os.getenv('API')
    response = urlopen(url)

    event_data = json.loads(response.read())

    with open ('data.json', 'r') as f:
        local_data = json.load(f)
    if(local_data['eventID'] == event_data['id']):
        print("SERVER LOGS: NO NEW EVENT FOUND")
    else:
        local_data['eventID'] = event_data['id']
        with open('data.json', 'w') as f:
            json.dump(local_data, f, indent=4, separators=(',', ': '))
        
        event = event_data
        embed = discord.Embed(
            title="📢  " + event['eventName'], 
            url=event['eventURL'], 
            description=event['eventDescription'], 
            color=discord.Color.blue(),
            timestamp=datetime.utcnow()
            )

        embed.set_author(
            name="Vijay", 
            url="https://github.com/SVijayB", 
            icon_url="https://avatars.githubusercontent.com/svijayb"
            )

        embed.add_field(
            name="📍  Event Venue", 
            value=event['eventVenue'], 
            inline=True,
            )

        data_and_time = event['eventDate'] + " " + event['eventStartTime']
        embed.add_field(
            name="⏰  Date and Time", 
            value=data_and_time, 
            inline=True)

        embed.add_field(
            name=":speaker:  Speakers",
            value=event['eventSpeaker'],
            inline=False
        )

        embed.add_field(
            name="📖  Docs",
            value=event['eventDocumentation'],
            inline=True
        )

        img = "https://drive.google.com/uc?export=view&id={}".format(str(event['eventLogo'].split("/")[5]))
        embed.set_image(url=img)

        embed.set_footer(text=event['eventCaption'], icon_url="https://i.ibb.co/rFv3nXZ/001-like.png")
        
        await message_channel.send("@everyone", embed=embed)
        print("SERVER LOGS: EVENT ALERT SENT")