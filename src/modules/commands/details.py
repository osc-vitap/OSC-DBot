from modules.commands.eb import ebDetails
from modules.commands.help import *
import discord


class details:
    def contact():
        data = "Hey! OSC-DBot was made with **love** ❤️ by two developers from the **Open Source Community VIT-AP**"
        embed = discord.Embed(
            title="👋  Contact details",
            description=data,
            color=discord.Color.from_rgb(47, 49, 54),
        )
        embed.add_field(
            name="S Vijay Balaji",
            value="svijayb.dev@gmail.com - <@410473185109344256>",
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
            color=discord.Color.from_rgb(47, 49, 54),
        )
        embed.add_field(
            name="GitHub Link",
            value="https://github.com/SVijayB/OSC-DBot",
            inline=False,
        )
        embed.set_footer(text="For more details go through the readme file.")
        return embed

    def help(data):
        response = Help_command(data)
        return response.validate()

    def eb(data):
        response = ebDetails(data)
        return response.validate()
