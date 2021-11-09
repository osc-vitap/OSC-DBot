from modules.osc_event_notif import command_event
from modules.commands.fun import *
from modules.commands.details import *
from discord.client import Client
import json


class commands:
    def validate(message):
        """
        Validates all the commands
        :param message: The message to be parsed
        """
        with open("data.json", "r") as f:
            data = json.load(f)
        response = f"No command found. Use {data['prefix']}help for more details"
        prefix = data["prefix"]
        message = message.lower()
        input_data = message.strip().split(" ")

        if message in ["f", "bruh", "lol", "scam", "sus"]:
            return message.capitalize()

        # Checking if command follows proper syntax
        # If the message doesn't start with prefix
        # If only prefix is typed, if prefix is typed with a space and message
        if (
            not message.startswith(prefix)
            or message.strip() == prefix
            or message.strip().split(" ")[0] == prefix
        ):
            return ""
        else:
            message = input_data[0][1:]  # Removing prefix after validation

            # Validating message
            message_request = data["utils"][0]["messages"]
            if message in message_request.keys():
                response = commands.message(message, message_request)

            # Checking if command
            command_request = data["utils"][0]["commands"]
            if message in command_request:
                response = commands.functions(input_data, message)
        return response

    def message(message, message_request):
        for key in message_request.keys():
            if message == key:
                response = message_request[key]
                return response

    def functions(input_data, message):
        with open("data.json", "r") as f:
            data = json.load(f)
        response = f"No command found. Use {data['prefix']}help for more details"
        if message == "event":
            response = command_event()
        elif message == "joke":
            try:
                arg = input_data[1]
            except:
                arg = ""
            response = fun.jokes(arg)
        elif message == "quote":
            response = fun.quotes()
        elif message == "meme":
            response = fun.memes()
        elif message == "help":
            response = details.help()
        elif message == "contact":
            response = details.contact()
        elif message == "info":
            response = details.info()
        return response
