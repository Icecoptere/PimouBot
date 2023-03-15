import os
import asyncio
import spotipy
import threading
global nb_message
from uuid import UUID
from time import sleep
from twitchAPI.helper import first
from twitchAPI.pubsub import PubSub
from twitchAPI.twitch import Twitch
from twitchio.ext import commands
from unidecode import unidecode
from twitchAPI.types import AuthScope
from BlagueAPI import blague_api
from Pokemon import getpokemon
from JusteMouki import just_price
from dotenv import load_dotenv
from bordel import endlebordel
from PimouIA.chatbot import get_response
from twitchAPI.oauth import UserAuthenticator
from Spotify import add_track_to_playlist
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()
nb_message = 0


class Bot(commands.Bot):
    def __init__(self):

        super().__init__(token=os.getenv("TMI_TOKEN"), prefix='!', initial_channels=[os.getenv("CHANNEL")])
        self.auth_manager = SpotifyClientCredentials(client_id=os.getenv("SPOTIPY_CLIENT_ID"),
                                                     client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"))
        self.spotify = spotipy.Spotify(auth_manager=self.auth_manager)

        threading.Thread(target=self.refresh_spotify_token, daemon=True).start()

    def refresh_spotify_token(self):
        while True:
            sleep(3600)  # Attendre une heure avant de rafraîchir le token
            self.auth_manager.get_access_token()  # Rafraîchir le token Spotify

    def do_thing(self):
        list_message = blague_api()
        self.loop.create_task(self.chan.send(list_message[0]))
        sleep(3)
        self.loop.create_task(self.chan.send(list_message[1]))
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
        print(f"Bot connected to Twitch as {bot.nick}")

    async def event_message(self, message):
        global nb_message
        if message.echo:
            return
        nb_message = nb_message + 1
        if nb_message % 100 == 0:
            response_aiml = get_response(message.content)
            await message.channel.send(response_aiml)

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

    async def event_channel_points_custom_reward_add(payload):
        print(f"Custom reward added: {payload}")


CLIENT_ID = os.getenv("CLIENT_ID")
TWITCH_SECRET = os.getenv("TWITCH_SECRET")
USER_SCOPE = [AuthScope.CHANNEL_READ_REDEMPTIONS]
TARGET_CHANNEL = 'Pimouki'


async def callback_redeem(uuid: UUID, data: dict) -> None:
    # print('got callback for UUID ' + str(uuid))
    # print(data)

    redeem_ID = data["data"]["redemption"]["reward"]["id"]
    match redeem_ID:

        case "6ccd6826-ebbf-4813-8076-0370c0115d88":
            user_input = data["data"]["redemption"]["user_input"]
            track_name = user_input
            track_results = bot.spotify.search(q=track_name, limit=10, type='track')
            if track_results['tracks']['items']:
                # print(track_results['tracks']['items'][0]["album"]["name"])
                track_uri = track_results['tracks']['items'][0]['uri']
                await bot.chan.send(
                    f" SingsNote MrDestructoid BipBoup ajout de : {track_results['tracks']['items'][0]['name']} MrDestructoid SingsNote ")
                add_track_to_playlist(track_uri)
            else:
                pass
                await bot.chan.send(f"Je n'ai pas trouvé {track_name} sur Spotify.")
            return


async def run_example():
    twitch = await Twitch(CLIENT_ID, TWITCH_SECRET)
    auth = UserAuthenticator(twitch, [AuthScope.CHANNEL_READ_REDEMPTIONS], force_verify=False)
    token, refresh_token = await auth.authenticate()

    await twitch.set_user_authentication(token, [AuthScope.CHANNEL_READ_REDEMPTIONS], refresh_token)
    user = await first(twitch.get_users(logins=[TARGET_CHANNEL]))

    pubsub = PubSub(twitch)
    pubsub.start()

    uuid = await pubsub.listen_channel_points(user.id, callback_redeem)
    input('press ENTER to close...')

    await pubsub.unlisten(uuid)
    pubsub.stop()
    await twitch.close()


def pubsub():
    asyncio.run(run_example())


threading.Thread(target=pubsub).start()

bot = Bot()
bot.run()
