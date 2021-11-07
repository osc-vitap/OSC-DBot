from urllib.request import urlopen
from datetime import datetime
import discord
import json


def quotes():
    response = urlopen("https://quote-garden.herokuapp.com/api/v3/quotes/random")
    data = json.loads(response.read())
    data = data["data"][0]
    print(data["quoteText"])

    embed = discord.Embed(
        title="✌️  Quotes",
        description=data["quoteText"],
        color=discord.Color.blue(),
    )
    embed.set_footer(text="Quote by " + data["quoteAuthor"])
    return embed
