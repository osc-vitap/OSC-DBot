# OSC-DBot

<p align="center">
    <img src="assets/OSCDbot_Logo1.png" alt="Logo">
    <br>Discord bot built for the Open Source Community VIT:AP.
</p>

---

## Table of Contents

-   [Motivation](#Motivation)
-   [Installation](#Installation)
-   [Contributing](#Contributing)
-   [License](#License)

## Motivation

The Open Source Community at VIT:AP uses discord as their main communication medium. \
Sending out announcements, events, and other information manually is tedious and time consuming. \
While there are many bots out there that send out embedded messages or announcements to channels, it was not an automated process. \
And that's where OSC-DBot comes into play. It utilizes [OSC-API](https://github.com/Open-Source-Community-VIT-AP/OSC-API) to send regular updates on upcoming events, announcements, and other information.

We obviously cannot have a bot that only sends event announcements. So we introduced a few fun games and other essential VIT:AP related automations.

To know more about the various commands present in the bot use the `help` command.

OSC-DBot is still in it's initial development stage. So please be patient while we add more features.

## Installation

To install and run the bot on your local system, follow below mentioned steps:

-   Do a `git clone https://github.com/SVijayB/OSC-DBot.git`.
-   Once you have the source code downloaded, create a virtual environment to safely download and install dependencies. To do so, use `python3 -m venv venv`, then `source venv/bin/activate` to enter the virtual environment.
-   Once done, you can install dependencies by using `pip install -r requirements.txt`.
-   Before running the bot locally, you will need to get yourself a discord bot token. For more information, check out [this guide](https://www.writebots.com/discord-bot-token/).
-   Now, rename `.env.example` file present in the root of the project to `.env` and add your token in the `INSERT_TOKEN_HERE` field.

Running `main.py` using `python3 main.py` will start the bot.

If you are facing any issues with installation, you can drop a message in our [Discord server](https://discord.link/oscvitap).

## Contributing

To contribute to OSC-DBot, fork the repository, create a new branch and send us a pull request. Make sure to read [CONTRIBUTING.md](https://github.com/SVijayB/OSC-DBot/blob/master/.github/CONTRIBUTING.md) before sending us Pull requests.

Also, thanks for contributing to Open-source!

## License

OSC-DBot is under the Apache-2.0 License. Read the [LICENSE](https://github.com/SVijayB/OSC-DBot/blob/master/LICENSE) file for more information.
