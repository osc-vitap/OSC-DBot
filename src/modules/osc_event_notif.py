from discord.ext import tasks, commands
from urllib.request import urlopen
from dotenv import load_dotenv
from datetime import datetime
import discord
import json
from os import getenv

TOKEN = getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix=">")
client = discord.Client()


@tasks.loop(hours=4)
async def oscEventNotif(message_channel):
    response = urlopen("https://osc-api.herokuapp.com/event/latest")
    event_data = json.loads(response.read())
    with open("data.json", "r") as f:
        local_data = json.load(f)

    if local_data["eventID"] == event_data["id"]:
        print("[!] Server logs: No new event found")
    else:
        embed = command_event()
        await message_channel.send("@everyone", embed=embed)
        print("[!] Server logs: Event alert sent")


def command_event():
    response = urlopen("https://osc-api.herokuapp.com/event/latest")
    event_data = json.loads(response.read())
    with open("data.json", "r") as f:
        local_data = json.load(f)

    local_data["eventID"] = event_data["id"]
    with open("data.json", "w") as f:
        json.dump(local_data, f, indent=4, separators=(",", ": "))

    event = event_data
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
