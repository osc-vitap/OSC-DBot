from discord.ext import tasks, commands
from urllib.request import urlopen
from datetime import date
from modules.db_connections import *
from pyshorteners import Shortener
import discord
import json


@tasks.loop(hours=2)
async def news_updates(news_channel):
    urls = ["https://inshortsapi.vercel.app/news?category=technology"]

    today = date.today().strftime("%d %b %Y")  # today date.
    max_time = ""  # stores the latest news.

    # if last news was sent yesterday, then change data in the json file.
    cache = get_data("newsTimestamp")
    if today != cache.split("|")[0].strip():
        query = today + " | " + "00:00 AM"
        update_newsTimestamp(query)

    for url in urls:
        # get json data from the api
        response = urlopen(url)
        data = json.loads(response.read())["data"]
        news_updates = dict()
        news_count = 0

        # get the news that were sent out today
        for index in range(len(data)):
            content = data[index]
            if today == content["date"].split(",")[0]:
                news_updates[news_count] = content
                news_count += 1

        time_stamps = list()

        # get the time of the news which were sent out today
        for today_content in news_updates.values():
            time_stamps.append(today_content["time"])

        # sort the time
        time_stamps = sorted(time_stamps)

        # check if the latest news is already sent out
        for item in time_stamps.copy():
            if item > cache.split(" | ")[1].strip():
                break
            time_stamps.remove(item)

        # if there is some update, then print and update the local json file.
        if time_stamps != list():
            for index in range(news_count):
                for time_stamp in time_stamps:
                    current_content = news_updates[index]
                    if current_content["time"] == time_stamp:
                        embed = discord.Embed(
                            title="📢  " + current_content["title"],
                            url=current_content["url"],
                            description=current_content["content"],
                            color=discord.Color.from_rgb(47, 49, 54),
                        )

                        embed.set_author(name="inshorts")

                        if current_content["readMoreUrl"] == None:
                            short_url = "-"
                        else:
                            shortener = Shortener()
                            short_url = shortener.tinyurl.short(
                                current_content["readMoreUrl"]
                            )

                        embed.add_field(
                            name="📰   Read more at ",
                            value=short_url,
                        )

                        if current_content["imageUrl"] == None:
                            embed.set_thumbnail(url="https://i.imgur.com/5l1Jz6S.png")
                        else:
                            embed.set_image(url=current_content["imageUrl"])

                        date_and_time = (
                            "📰 "
                            + current_content["date"]
                            + " "
                            + current_content["time"]
                        )
                        embed.set_footer(text=date_and_time)
                        response.close()

                        # prints outs log message
                        print(
                            "[!] Updating news feed: "
                            + current_content["date"]
                            + " | "
                            + current_content["time"]
                            + " -> "
                            + current_content["title"]
                        )

                        # get the latest news time
                        if max_time < current_content["time"]:
                            max_time = current_content["time"]

                        # update the latest time with the local json file
                        query = today + " | " + max_time
                        update_newsTimestamp(query)
                        print(news_channel)
                        try:
                            await news_channel.send(embed=embed)
                        except:
                            print("[!] Server logs: Error unable to find channel")
