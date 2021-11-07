from discord.client import Client
from modules.osc_event_notif import command_event
import json


class commands:
    def validate(message):
        """
        Validates all the commands
        :param message: The message to be parsed
        """
        with open("data.json", "r") as f:
            data = json.load(f)
        response = "No command found. Use !help for more details"
        prefix = data["prefix"]

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
            # Serving message request
            message = message[1:]  # Removing prefix after validation
            message_request = data["commands"][0]["Messages"]
            if message in message_request.keys():
                response = commands.message(message, message_request)

            # Checking if command
            command_request = data["commands"][0]["Commands"]
            if message in command_request:
                response = commands.functions(message)
        return response

    def message(message, message_request):
        for key in message_request.keys():
            if message == key:
                response = message_request[key]
                return response

    def functions(message):
        if message == "event":
            response = command_event()
            return response
