import discord
import json


class details:
    def contact():
        data = "Hey! OSC-DBot was made with **love** ❤️ by two developers from the **Open Source Community VIT-AP**"
        embed = discord.Embed(
            title="👋  Contact details",
            description=data,
            color=discord.Color.green(),
        )
        embed.add_field(
            name="S Vijay Balaji",
            value="vijaybalaji2477@gmail.com - <@410473185109344256>",
            inline=False,
        )
        embed.add_field(
            name="N Krishna Raj",
            value="nkrishnaraj.developer@gmail.com - <@766903441816944690>",
            inline=False,
        )
        embed.set_footer(
            text="If developers are unavailable, you can drop a mail at osc@vitap.ac.in",
        )
        return embed

    def info():
        data = """**OSC-DBot** was a fun project built for the Open Source Community VIT-AP.
        It was built to **automate** several of the communities tasks on discord,
        And act as a single hub to keep the community entertained on it's online medium."""
        embed = discord.Embed(
            title="💬  Information",
            description=data,
            color=discord.Color.green(),
        )
        embed.add_field(
            name="GitHub Link",
            value="https://github.com/SVijayB/OSC-DBot",
            inline=False,
        )
        embed.set_footer(text="For more details go through the readme file.")
        return embed

    def help():
        with open("data.json", "r") as f:
            data = json.load(f)
        prefix = data["prefix"]

        util_commands = f"""

           > **{prefix}help**
           > List of all the **available commands**.
           
           > **{prefix}info**
           > For **more information** about me.
           
           > **{prefix}contact**
           > **Reveal the octocats** that gave me life.

           > **{prefix}event**
           > I hack OSC VIT-AP database and **fetch you the latest event**, please don't tell them I hacked their database.
        
        """

        fun_commands = f"""

           > **{prefix}joke**
           > I tell a **Joke** and you laugh, it's a fair deal.
           
           > **{prefix}meme**
           > Gets you **latest** and **hotest** memes from the meme world.
           
           > **{prefix}quote**
           > Fetches you a **random quote** from the internet.
        
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
            color=discord.Color.blue(),
        )
        embed.add_field(
            name="👉🏽 Utility Commands (For Noobs)",
            value=util_commands,
            inline=False,
        )

        embed.add_field(
            name="👉🏽 Fun Commands (For Boomers)",
            value=fun_commands,
            inline=False,
        )

        embed.add_field(
            name="👉🏽 More ...",
            value=prefooter_content,
            inline=False,
        )

        file = discord.File("assets/Icon.png", filename="logo.png")

        embed.set_footer(
            text=" The Open Source Community",
            icon_url="https://i.ibb.co/L86y3Qj/Icon.png",
        )
        return embed
