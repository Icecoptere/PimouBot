import os
import random
from dotenv import load_dotenv
load_dotenv()
global le_bon_chiffre


def just_price(cmd, message):
    try:
        global le_bon_chiffre
        if cmd == "pimoukigold":
            if message.author.name.lower() == os.getenv("CHANNEL").lower():
                le_bon_chiffre = random.randint(1, 1000)
                print(le_bon_chiffre)
                return "Le meuga jeu de la mort est lancé mettez un chiffre entre 1 et 1000 et tenté de gagnez un " \
                       "super Kdo "
        cmd = int(cmd)
        if cmd < le_bon_chiffre:
            if le_bon_chiffre - cmd > 10:
                return f' C\'est plus grand {message.author.name} pimoukAstor '
            else:
                return f' Tes pas loin {message.author.name}, mais c\'est plus pimoukGolo   '
        elif cmd > le_bon_chiffre:
            if cmd - le_bon_chiffre > 10:
                return f' C\'est plus petit {message.author.name} pimoukAstor  '
            else:
                return f' Tes pas loin {message.author.name}, mais c\'est moins pimoukAstor'
        else:
            le_bon_chiffre = None
            return f' pimoukOporc pimoukOporc  Bravo {message.author.name} tu as gagné  pimoukOrtu  pimoukOrtu '
    except:
        pass

