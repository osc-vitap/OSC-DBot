import discord
import json
from modules.db_connections import get_data


class ebDetails:
    def __init__(self, data):
        self.data = data
        self.prefix = get_data("prefix")

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
                title="🎓  EB",
                description=f"""Please verify that you have entered the correct argument.
                For more information, use **{self.prefix}help eb**""",
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
