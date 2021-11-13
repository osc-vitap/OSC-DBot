import json
import discord
from modules.db_connections import get_data


class Help_command:
    def __init__(self, data):
        self.data = data
        self.prefix = get_data("prefix")

    def validate(self):
        try:
            args = self.data[1]
        except:
            return self.default_response()
        link_args = {
            "joke": self.joke,
            "meme": self.meme,
            "quote": self.quote,
            "tod": self.tod,
            "event": self.event,
        }
        if args in link_args:
            return link_args[args]()
        else:
            embed = discord.Embed(
                title="📖  Help",
                description=f"""Please verify that the command you are searching for exists.
                For more information, use **{self.prefix}info**""",
                color=discord.Color.from_rgb(47, 49, 54),
            )
        return embed

    def default_response(self):
        info = f"""

           **{self.prefix}help command_name**
           Get more information about a specific command
           
           **{self.prefix}info**
           For **more information** about me.
           
           **{self.prefix}contact**
           **Reveal the octocats** that gave me life.

           **{self.prefix}event**
           I hack OSC VIT-AP database and **fetch you the latest event details**.
        
        """

        fun_commands = f"""

           **{self.prefix}joke**
           I tell a **Joke** and you laugh, it's a fair deal.
           
           **{self.prefix}meme**
           Gets you **latest** and **hotest** memes from the meme world.
           
           **{self.prefix}quote**
           Fetches you a **random quote** from the internet.

           **{self.prefix}tod**
            Play a game of Truth or dare. Go on, try it. I dare you.
        
        """

        prefooter_content = f"""

         For more help, contact beluga.
         Just kidding, use **{self.prefix}info** to get access to more information on the bot.

         More commands coming soon.

        """

        data = """Are you lost little lamb? Fret not, following are the commands that you will need to memorize to use me."""
        embed = discord.Embed(
            title="📖  Help",
            description=data,
            color=discord.Color.from_rgb(47, 49, 54),
        )
        embed.add_field(
            name="🔹 Utility Commands (For Noobs)",
            value=info,
            inline=False,
        )

        embed.add_field(
            name="🔹 Fun Commands (For Boomers)",
            value=fun_commands,
            inline=False,
        )

        embed.add_field(
            name="🔹 More ...",
            value=prefooter_content,
            inline=False,
        )

        file = discord.File("assets/Icon.png", filename="logo.png")

        embed.set_footer(
            text=" The Open Source Community",
            icon_url="https://i.ibb.co/L86y3Qj/Icon.png",
        )
        return embed

    def joke(self):
        embed = discord.Embed(
            title="📖  Help | Joke",
            description=f"""
            Command: **{self.prefix}joke args** 
            I collect data from several sources and tell you a very **funny joke**.
            You read my joke and laugh out loud. It's a win-win.

            I also provides jokes on several categories.
            **{self.prefix}joke coding**: Programmer jokes.
            **{self.prefix}joke dark**: Into dark humor? You'll love these!
            **{self.prefix}joke pun**: These puns will have you rolling on the floor.
            **{self.prefix}joke spooky**: Scary, spooky, but funny.
            """,
            color=discord.Color.from_rgb(47, 49, 54),
        )
        return embed

    def meme(self):
        embed = discord.Embed(
            title="📖  Help | Meme",
            description=f"""
            Command: **{self.prefix}meme** 
            I bring you the latest and hotest memes from the world of reddit.

            I currently get memes from the following subreddits:
            https://www.reddit.com/r/memes/
            https://www.reddit.com/r/ProgrammerHumor/
            """,
            color=discord.Color.from_rgb(47, 49, 54),
        )
        return embed

    def quote(self):
        embed = discord.Embed(
            title="📖  Help | Quote",
            description=f"""
            Command: **{self.prefix}quote** 
            You may die but the words you speak or spoke will live on. Forever.

            "Quotes inspire you, Quotes make you happy and solves all problems in life"
            - Sun Tzu

            In honour of Sun Tzu, I bring you the greatest quotes from the internet.
            """,
            color=discord.Color.from_rgb(47, 49, 54),
        )
        return embed

    def tod(self):
        embed = discord.Embed(
            title="📖  Help | TOD",
            description=f"""
            Command: **{self.prefix}tod gamemode rating** 
            Want to play a game of **Truth or dare**?
            How about *Would you rather* or *Never have I ever*?
            Oh you do? Well, I got you covered.

            TOD command syntax:
            **{self.prefix}tod truth**: I dare you to say something truthful.
            **{self.prefix}tod dare**: I send you a dare and you do it. Simple.
            **{self.prefix}tod wyr**: Would you rather?
            **{self.prefix}tod nhie**: Never have I ever.
            **{self.prefix}tod paranoia**: I send you some spicy paranoia questions.
            
            You can also add ratings to add some spice to the game!
            **{self.prefix}tod gamemode rating**.
            Different ratings - R, PG13, PG.
            Example: 
            **{self.prefix}tod truth r**
            **{self.prefix}tod wyr pg13**
            """,
            color=discord.Color.from_rgb(47, 49, 54),
        )
        return embed

    def event(self):
        embed = discord.Embed(
            title="📖  Help | Event",
            description=f"""
            Command: **{self.prefix}event** 
            Need info on the latest OSC event? I gotcha covered.

            I hack the OSC VIT-AP database and fetch you **latest event** details.
            Just don't snitch on me and I'll keep you updated.
            """,
            color=discord.Color.from_rgb(47, 49, 54),
        )
        return embed
