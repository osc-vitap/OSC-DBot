from modules.osc_event_notif import command_event
from modules.commands.fun import *
from modules.commands.details import *
from modules.commands.vc_commands import *
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
                response = commands.functions(message, input_data)
        return response

    def message(message, message_request):
        for key in message_request.keys():
            if message == key:
                response = message_request[key]
                return response

    def functions(message, input_data):
        with open("data.json", "r") as f:
            data = json.load(f)
        response = f"No command found. Use {data['prefix']}help for more details"
        functions_without_args = {
            "event": command_event,
            "quote": fun.quotes,
            "meme": fun.memes,
            "help": details.help,
            "contact": details.contact,
            "info": details.info,
        }
        functions_with_args = {
            "joke": fun.jokes,
        }

        if message in functions_without_args.keys():
            operation = functions_without_args[message]
            response = operation()
        else:
            operation = functions_with_args[message]
            response = operation(input_data)

        return response
