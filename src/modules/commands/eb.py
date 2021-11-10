import discord
import json


class ebDetails:
    def __init__(self, data):
        self.data = data
        with open("data.json", "r") as f:
            data = json.load(f)
        self.prefix = data["prefix"]

    def validate(self):
        try:
            args = self.data[1]
        except:
            return self.default_response()
        link_args = {
            "name": self.personName,
            "role": self.role,
            "dept": self.dept,
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
        pass

    def personName(self):
        pass

    def role(self):
        pass

    def dept(self):
        pass
