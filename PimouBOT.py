# bot.py
import threading
import asyncio
import os  # for importing env vars for the bot to use
from twitchio.ext import commands
from dotenv import load_dotenv
from Pokemon import getpokemon
from bordel import endlebordel
from unidecode import unidecode
from JusteMouki import just_price
from Blague import get_blague
from time import sleep

load_dotenv()


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=os.getenv("TMI_TOKEN"), prefix='!', initial_channels=[os.getenv("CHANNEL")])

    def do_thing(self):
        message = get_blague()
        self.loop.create_task(self.chan.send(message))
        sleep(600)
        threading.Thread(target=self.do_thing).start()

    async def event_ready(self):
        chan = self.get_channel(os.getenv("CHANNEL"))
        loop = asyncio.get_event_loop()
        self.loop = loop
        self.chan = chan
        threading.Thread(target=self.do_thing).start()
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):

        if message.echo:
            return

        print(message.content)
        if message.content[0] == "!":
            parsed_input = unidecode(message.content.lstrip("!")).split(" ")
            print(parsed_input)
            command = parsed_input[0].lower()
            match command:
                case "pokemon":
                    pokemon = parsed_input[1].lower()
                    response = getpokemon(pokemon)
                    await message.channel.send(response)
                    return
                case "karaoke":
                    await message.channel.send("Voila le lien pour choisir le karaoke de ton choix "
                                               "youtube.com/@karafunfr")
                    return
                case "bigard":
                    await message.channel.send("SingsNote BIGARD BIGARD ! LA STAR DU STEAK HACHÉ SingsMic "
                                               "youtu.be/VALBLhsaXPE")
                    return

            response = endlebordel(command, message, parsed_input)
            if response is not None:
                await message.channel.send(response)
                return

        if True:
            message.content[0] == ""
            parsed_input = unidecode(message.content.lstrip("")).split(" ")
            print(parsed_input)
            command = parsed_input[0].lower()
            response = just_price(command, message)
            if response is not None:
                await message.channel.send(response)
                return


bot = Bot()
bot.run()

# bot.run() is blocking and will stop execution of any below code here until stopped or closed.
