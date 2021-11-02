from discord.ext import tasks, commands
from urllib.request import urlopen
from dotenv import load_dotenv
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
            title=event['eventName'], 
            url=event['eventURL'], 
            description=event['eventDescription'], 
            color=discord.Color.blue()
            )

        embed.set_author(
            name="Vijay", 
            url="https://github.com/SVijayB", 
            icon_url="https://avatars.githubusercontent.com/svijayb"
            )

        embed.add_field(
            name="Event Mode", 
            value=event['eventVenue'], 
            inline=True)

        embed.add_field(
            name="Date and Time", 
            value=event['eventDate'], 
            inline=True)
        
        await message_channel.send(embed=embed)
        print("SERVER LOGS: EVENT ALERT SENT")