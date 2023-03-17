import requests
import json
import os
from playsound import playsound


def getpokemon(nompokemon):
    r = requests.get(f'https://mon-api-pokemon.vercel.app/api/v1/pokemon/{nompokemon}')
    if nompokemon == "pokemon":
        return "le petit zizi de ice"
    elif nompokemon == "pimouki":
        return "Pimouki il est trop fort j'ai pas pu le capturer dans mon Pokédex"
    if r.status_code == 200:
        try:
            reponse = ""
            j = json.loads(r.text)
            evolve = j['evolution']
            nomfrancais = j['name']['fr']
            if evolve is not None and evolve['next'] is not None and len(evolve['next']) > 0:
                evolution = evolve['next'][0]['name']
                reponse += f"{nomfrancais} évolue en {evolution} ,"
            else:
                reponse += f"{nomfrancais} n'a pas d'évolution ,"
            weight = j['weight']
            reponse += f' pèse: {weight}'
            nomjap = j['name']['jp']
            reponse += f' et se nomme {nomjap} en japonais'
            nomeng = j['name']['en']
            #getpokemonscream(nomeng)

            return reponse
        except Exception as val:
            print(val)
            return "une erreur a eu lieu dans la recherche du pokemon :'( "
    else:
        return "une erreur a eu lieu dans la recherche du pokemon :'( "


def getpokemonscream(pokemoneng):
    url = f"https://play.pokemonshowdown.com/audio/cries/{pokemoneng.lower()}.mp3"
    print(url)
    r = requests.get(url)
    print(r.content[0:40])
    with open('pokemon.mp3', 'wb') as f:
        f.write(r.content)
    f.close()
    playsound('C:\\Users\\Pimouki\\PycharmProjects\\pythonProject\\pokemon.mp3')
    os.remove("C:\\Users\\Pimouki\\PycharmProjects\\pythonProject\\pokemon.mp3")
