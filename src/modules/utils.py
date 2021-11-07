import json

class commands:
    def commands(message):
        """
        Handles all the commands
        :param message: The message to be parsed
        """
        with open("data.json", "r") as f:
            data = json.load(f)
        response = "No command found. Use !help for more details"
        prefix = data["prefix"]

        for temp in data["commands"][0].keys():
            # if the message is a command for the bot
            if message == prefix + temp:
                response = data["commands"][0][temp]
                return response
            # if the message doesn't start with prefix, if only prefix is typed, if prefix is typed with a space and message
            elif (
                not message.startswith(prefix)
                or message.strip() == prefix
                or message.strip().split(" ")[0] == prefix
            ):
                return ""
        # if command not found
        return response
