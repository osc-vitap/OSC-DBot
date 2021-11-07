from discord.ext import tasks, commands
from urllib.request import urlopen
from datetime import datetime
import pyshorteners
import discord
import json


@tasks.loop(hours=12)
async def news_updates(news_channel):
    urls = ["https://inshortsapi.vercel.app/news?category=technology"]
    for url in urls:
        response = urlopen(url)
        data = json.loads(response.read())["data"]

        for i in range(2):
            curr = data[i]
            embed = discord.Embed(
                title="📢  " + curr["title"],
                url=curr["url"],
                description=curr["content"],
                color=discord.Color.blue(),
            )

            embed.set_author(name="inshorts")

            shortener = pyshorteners.Shortener()
            short_url = shortener.tinyurl.short(curr["readMoreUrl"])

            embed.add_field(
                name="📰   Read more at ",
                value=short_url,
            )

            embed.set_image(url=curr["imageUrl"])

            date_and_time = "📰 " + curr["date"] + " " + curr["time"]
            embed.set_footer(text=date_and_time)
            response.close()

            await news_channel.send(embed=embed)
