from urllib.request import urlopen
from datetime import datetime
import discord
import json


def jokes(arg):
    url = "https://v2.jokeapi.dev/joke/Any"
    if arg == "misc":
        url = "https://v2.jokeapi.dev/joke/Misc"
    elif arg == "programming":
        url = "https://v2.jokeapi.dev/joke/Programming"
    elif arg == "dark":
        url = "https://v2.jokeapi.dev/joke/Dark"
    elif arg == "pun":
        url = "https://v2.jokeapi.dev/joke/Pun"
    elif arg == "spooky":
        url = "https://v2.jokeapi.dev/joke/Spooky"
    response = urlopen(url)
    joke_data = json.loads(response.read())
    if joke_data["type"] == "single":
        embed = discord.Embed(
            title="😜  Jokes | " + joke_data["category"],
            description=joke_data["joke"],
            color=discord.Color.blue(),
            timestamp=datetime.utcnow(),
        )
    if joke_data["type"] == "twopart":
        embed = discord.Embed(
            title="😜  Jokes | " + joke_data["category"],
            color=discord.Color.blue(),
            timestamp=datetime.utcnow(),
        )
        embed.add_field(
            name=joke_data["setup"], value=joke_data["delivery"], inline=False
        )
    return embed
