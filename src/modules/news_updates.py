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
            embed = discord.Embed(
                title="📢  " + data[i]['title'], 
                url=data[i]['url'], 
                description=data[i]['content'], 
                color=discord.Color.blue(),
                )

            embed.set_author(
                name="inshorts"
                )

            shortener = pyshorteners.Shortener()
            short_url = shortener.tinyurl.short(data[i]['readMoreUrl'])

            embed.add_field(
                name="📰   Read more at ", 
                value=short_url, 
                )

            embed.set_image(url=data[i]['imageUrl'])

            date_and_time = "📰 " + data[i]['date'] + " " + data[i]['time']
            embed.set_footer(text=date_and_time)
            response.close()

            await news_channel.send(embed=embed)