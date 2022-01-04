from discord.ext import tasks, commands
from urllib.request import urlopen
from datetime import datetime
import discord
import json

from modules.db_connections import *


def command_event():
    response = urlopen("https://osc-api.herokuapp.com/api/v1/event/latest")
    event_data = json.loads(response.read())

    event = event_data[0]
    embed = discord.Embed(
        title="📢  " + event["eventName"],
        url=event["eventURL"],
        description=event["eventDescription"],
        color=discord.Color.from_rgb(47, 49, 54),
        timestamp=datetime.utcnow(),
    )

    embed.set_author(
        name="Vijay",
        url="https://github.com/SVijayB",
        icon_url="https://avatars.githubusercontent.com/svijayb",
    )

    embed.add_field(
        name="📍  Event Venue",
        value=event["eventVenue"],
        inline=True,
    )

    data_and_time = event["eventDate"] + " " + event["eventStartTime"]
    embed.add_field(name="⏰  Date and Time", value=data_and_time, inline=True)

    embed.add_field(
        name=":speaker:  Speakers", value=event["eventSpeaker"], inline=False
    )

    embed.add_field(name="📖  Docs", value=event["eventDocumentation"], inline=True)

    embed.set_image(url=event["eventLogo"])

    embed.set_footer(
        text=event["eventCaption"], icon_url="https://i.ibb.co/rFv3nXZ/001-like.png"
    )
    response.close()
    return embed
