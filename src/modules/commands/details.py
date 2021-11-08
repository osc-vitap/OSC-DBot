import discord


class details:
    def contact():
        data = "Hey! OSC-DBot was made with **love** ❤️ by two developers from the **Open Source Community VIT-AP**"
        embed = discord.Embed(
            title="📧  Contact details",
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
        pass

    def help():
        pass
