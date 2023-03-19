import os
import asyncio
import spotipy
import threading

from uuid import UUID
from time import sleep
from playsound import playsound
from twitchAPI.helper import first
from twitchAPI.pubsub import PubSub
from twitchAPI.twitch import Twitch
from twitchio.ext import commands
from unidecode import unidecode
from twitchAPI.types import AuthScope
from Blague.BlagueAPI import blague_api
from Extension.Pokemon import getpokemon
from Minijeux.JusteMouki import just_price
from dotenv import load_dotenv
from autocorrect import Speller
from Extension.bordel import endlebordel
from PimouIA.chatbot import get_response
from twitchAPI.oauth import UserAuthenticator
from Spotify.Spotify import add_track_to_playlist, skip_track_playlist
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()


# Starter_BOT:
class Bot(commands.Bot):
    def __init__(self):

        super().__init__(token=os.getenv("TMI_TOKEN"), prefix='!', initial_channels=[os.getenv("CHANNEL")])
        self.auth_manager = SpotifyClientCredentials(client_id=os.getenv("SPOTIPY_CLIENT_ID"),
                                                     client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"))
        self.spotify = spotipy.Spotify(auth_manager=self.auth_manager)
        self.loop = asyncio.get_event_loop()
        threading.Thread(target=self.refresh_spotify_token, daemon=True).start()
        self.spell = Speller(lang="fr")
        self.nb_message = 0

    # Spotify_Spotify:
    def refresh_spotify_token(self):
        while True:
            sleep(3600)  # Attendre une heure avant de rafraîchir le token
            self.auth_manager.get_access_token()  # Rafraîchir le token Spotify

    # Blague_BlagueAPI:
    def do_thing(self):
        while True:
            list_message = blague_api()
            self.loop.create_task(self.chan.send(list_message[0]))
            sleep(3)
            self.loop.create_task(self.chan.send(list_message[1]))
            sleep(6000)

# Botlaunch:

    async def event_ready(self):
        self.loop = asyncio.get_event_loop()
        self.chan = self.get_channel(os.getenv("CHANNEL"))
        threading.Thread(target=self.do_thing, daemon=True).start()
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
        print(f"Bot connected to Twitch as {bot.nick}")

    # Gere les message envoyé:

    async def event_message(self, message):
        self.sentence = message.content.lower()
        self.nb_message = self.nb_message + 1
        if message.echo:
            return

        # Pour voir le tchat:

        if self.sentence[0] == "!":
            parsed_input = unidecode(self.sentence.lstrip("!")).split(" ")
            command = parsed_input[0].lower()

            # Extension_pokemon:

            match command:
                case "pokemon":
                    pokemon = parsed_input[1].lower()
                    response = getpokemon(pokemon)
                    await message.channel.send(response)
                    return
            # Extension_bordel:

            response = endlebordel(command, message, parsed_input)
            if response is not None:
                await message.channel.send(response)
                return

        # Dialogue AI:
        # + correction:

        elif "pimoushka" in self.sentence:
            pseudo = message.author.name
            query = self.sentence.split("pimoushka")
            query = [self.spell(w) for w in (query[1].split())]
            spelled = " ".join(query)
            response_aiml = get_response(spelled, pseudo)
            await message.channel.send(pseudo + " " + response_aiml)
            return

        parsed_input = unidecode(self.sentence.lstrip("")).split(" ")
        command = parsed_input[0].lower()
        response = just_price(command, message)
        if response is not None:
            await message.channel.send(response)
            return

    async def event_channel_points_custom_reward_add(payload):
        print(f"Custom reward added: {payload}")


# ID twitch:

CLIENT_ID = os.getenv("CLIENT_ID")
TWITCH_SECRET = os.getenv("TWITCH_SECRET")
USER_SCOPE = [AuthScope.CHANNEL_READ_REDEMPTIONS]
TARGET_CHANNEL = os.getenv("CHANNEL")


# Point Twitch(Spotify):

async def callback_redeem(uuid: UUID, data: dict) -> None:
    print(data)

    redeem_ID = data["data"]["redemption"]["reward"]["id"]
    match redeem_ID:
        # alerte coucou:

        case "68497a1b-283b-47c9-be07-25abf4624c9e":
            playsound('C:\\Users\\Pimouki\\PycharmProjects\\PimouBOT\\Ressource\\coucou.mp3')
        # alerte ROUE:

        case "d1bc0a5c-350f-4d56-aebb-ea6066ad306a":
            playsound('C:\\Users\\Pimouki\\PycharmProjects\\PimouBOT\\Ressource\\uwu.mp3')
        # skip music:

        case "778a5a3a-1003-4036-90a1-3e8ad42febb4":
            skip_track_playlist()

        # Pimou <3:

        case "6ccd6826-ebbf-4813-8076-0370c0115d88":
            user_input = data["data"]["redemption"]["user_input"]
            track_name = user_input
            track_results = bot.spotify.search(q=track_name, limit=10, type='track')
            if track_results['tracks']['items']:
                track_uri = track_results['tracks']['items'][0]['uri']
                success = add_track_to_playlist(track_uri)
                if success:
                    song = track_results['tracks']['items'][0]
                    message = f"SingsNote MrDestructoid BipBoup ajout de : {song['name']} par {song['artists'][0]['name']} MrDestructoid SingsNote"
                else:
                    message = "Soit j'ai pas trouvé, soit y'a eu une erreur, déso MyAvatar"
                await bot.chan.send(message)
            else:
                pass
                await bot.chan.send(f"Je n'ai pas trouvé {track_name} sur Spotify.")
            return


# initialisation point twitch:

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
