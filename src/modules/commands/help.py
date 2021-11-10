import json
import discord


class Help_command:
    def __init__(self, data):
        self.data = data

    def validate(self):
        try:
            args = [self.data[1], self.data[2]]
        except:
            return self.default_response()

    def default_response(self):
        with open("data.json", "r") as f:
            data = json.load(f)
        prefix = data["prefix"]

        util_commands = f"""

           **{prefix}help**
           List of all the **available commands**.
           
           **{prefix}info**
           For **more information** about me.
           
           **{prefix}contact**
           **Reveal the octocats** that gave me life.

           **{prefix}event**
           I hack OSC VIT-AP database and **fetch you the latest event details**.
        
        """

        fun_commands = f"""

           **{prefix}joke**
           I tell a **Joke** and you laugh, it's a fair deal.
           
           **{prefix}meme**
           Gets you **latest** and **hotest** memes from the meme world.
           
           **{prefix}quote**
           Fetches you a **random quote** from the internet.
        
        """

        prefooter_content = f"""

         For more help, cry. 
         Just kidding, use **{prefix}info** to get access to more information on the bot.
        
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
            value=util_commands,
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
