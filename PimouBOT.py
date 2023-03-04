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
from time import sleep
from random import randint

load_dotenv()

'''
f'Bonjour Yanikara ? comment vas tu en cet journée, moi je vais bien il faut beau chaud '
            f'tres chaud même personnellement je me prélasse devant pimouki en m\'enfournant des beignets a la '
            f'pomme, aime tu les beignets a la pomme Yanikara ? Moi j\'aime les beignets a '
            f'la pomme Hmmm le gouts de la pomme qui coule dans la bouche puis ce déverse dans la gorge Hmmm ce '
            f'doux gouts.'
            f'Il m\'arrive même des folies et en prendre un au nutella houlala que suis je fou (hihihi).',
            "Bonjour",
            "Salut",
            "Oui d'acc",
            "Ok",
            "J'ai pas compris tu peux répéter ?",
            "Tabarnak",
            "Tu connais l'histoire du petit déjeuner ? Pas de bol LUL",
            ""
            "Pas de soucis",
            "Mdr",
            "Mercure/Saturne amène l'exigence, et vous vous efforcez d'en avoir. Avec le trigone Lune/Neptune, vous essayez d'être plus créatif que d'habitude. L'inspiration est développée, vous la mettez à profit pour concrétiser vos idées. Et ça marche !",
            "Il n'y a guère que Pluton qui essaye d'altérer votre sensibilité, si développée. La planète vous agite, en amenant une exigence parfois trop importante. N'allez pas tomber dans des frustrations affectives, Jupiter réclame le bonheur. Contentez-vous de ce que vous avez, et appréciez l'instant.",
            f'phrase Apprenez à prononcer nom féminin Assemblage oral ou écrit capable de représenter l\'énoncé complet'\
            'd\'une idée. La phrase peut consister en un mot unique (ex. Viens !), mais contient habituellement un second"\
            " terme qui est le sujet de l\'énoncé (ex. Tu viens ?)."',
            f'Bonjour Yanikara '
            f'ce week end je ne pourrais pas venir te chercher par ce que j\'ai autre chose a faire j\'espere que '
            f'tu comprendras',
            "J'avais une blague sur les magasins mais la dernière fois elle a pas supermarché",
            
            f"YANIKARA TU ES BO",
            "10. mohala_art   1 sons",
            "je garde la 4ème place c'est bien",
            "en donannt des bits j'ai des points de chaine",
            "donnant *",
            "YOHHHH",
            "Je sais pas mais la je suis à 1.1k",
            "lesgooooooooo",
            "MON NIOOMMM",
            "MERDE MERDE MERDE",
            "voilà mdr",
            "je sais pas comment changer",
            "ça va 1 gros pec",
            "ca va hein, on a des gros pecs",
            "j'ai vu un super movie hier   Julie en 12 chapitres",
            "voilà ma recommandation",
            "j'ai fait un nouveau compte mdr sans connecter avec fb",
            "@buk_minster oh je veux le voir",
            "ah ba c'était trop bien",
            "lol le graphiste nul, il en a mis 11",
            "ah c'est bien fait",
            "on refait ?",
            "très beau, y'avais des très belles scènes, des très belles musiques",
            "MAI SE UN FILM OU UN LIVRE ALOR",
            "peut on parler de politique",
            "JE COMPREN PA",
            "très bon jeu d'acteur aussi",
            "bah on en crée une non ?",
            "lol non c'est parce que chapitre = livre = 1er degres",
            "je peux en créer si non",
            "12 livres",
            "d'ailleurs le titre original est nul je trouve",
            "mais c'est un livre ou un chapitre rololo",
            "je suis content que ça soit pas juste la traduction",
            "Norvégien",
            "c'est 'la pire personne du monde'",
            "j'ai encore fait 50 mots je suis s=nul",
            "wow comment ça spoil un max",
            "meuh",
            "après c'est aussi la mise en scène et l'interprétation qui est très important dans le film",
            "J'ai toujours que 1.1k ... rembourse moi stp",
            "le badge milka lol",
            "et la ?",
            "Je veux mon épisode  3...",
            "Donc je parle les points de chaine",
            "depense encore 20 balles et on le regarde",
            "Ce moment est si cute",
            "je l'ai fais j'ai fais 50...",
            "je suis adjointe de direction je suis sensé écrire vite mdr",
            "ah mais je regarde mon clavier aussi c'est pour ça",
            "ça dépend ...",
            "putain je decouvre ces reliefs",
            "t'as l'air heureux de voir cet episode",
            "je suis entrain d'écrire sans regatsder min clabuer docn ne jufer pas",
            "JE VOUS AIMES <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3",
            "Je suis entrain d'écrure sans regatder mon clabier donc ne jugez pas",
            "il y a une amélioration je trouve",
            "je vais essayé de ne pas regarder mon clabier de la jouréne",
            "dur dur dur",
            "quelle dextérité, un vrai programmationneur",
            "ouais moi j'arrête de regarder Christian clavier",
            "Allé avoue ta fièrté était en jeu ? xD",
            "Pas de jugement sur les fautes je ne rehatde plius mon clalvier",
            "c'est le premier",
            "tu es un amour besta besti bestou <3 <3",
            "si tu le veu demain tu peux",
            "être avec nous",
            "Donc je peux acheter mes épisode ?",
            "c'est un volcan dans ton casque ?",
            "je dans pas mais je chante",
            "Putain mais je vais faire ça, je regarde doctor who et pour chaque sub je rajouter un épisode",
            "let's go faire ça vendredi au lieu de la soirée cocktail mdr",
            "50*45 ça fait cb ?",
            "50 = nb épisode 45 min",
            "non mais imagine",
            "37 h pour 50 épisodes trop risquer",
            "YOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
            "Bonjour tout le mondee",
            "on regarde les winx !",
            "Venez installez vous",
            "Pour 1 sub on rajoute un épisode",
            "on voulait jouer à minecraft mais il nous bassine avec ses winx",
'''


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=os.getenv("TMI_TOKEN"), prefix='!', initial_channels=[os.getenv("CHANNEL")])

    def do_thing(self):
        liste_msg = [
            "Si une horloge sonne 13 fois, quelle heure est-il? _ Il est l’heure d’acheter une nouvelle horloge!",
            "C'est l'histoire du ptit dej, tu la connais ? _ Pas de bol",
            "Que demande un footballeur à son coiffeur ? _ La coupe du monde",
            "C'est quoi une chauve-souris avec une perruque ? _ Une souris",
            "Que fait un crocodile quand il rencontre une superbe femelle ? _ Il Lacoste",
            "Tu connais la blague de la chaise ? _ Elle est pliante",
            "Tu connais la blague de la feuille ? _ Elle déchire",
            "Quel est le crustacé le plus léger de la mer ? _ La palourde",
            "Pourquoi est-ce que Napoléon n'a pas voulu acheter de maison ? _ Parce qu’il avait déjà un Bonaparte",
            "Où va Messi quand il se blesse ? _ À la pharmessi",
            "Qu'est-ce qui est vert avec une cape ?  _ Un concombre qui imite Super Tomate.",
            "Comment appelle-t-on un chien qui n'a pas de pattes ? _ On ne l’appelle pas, on va le chercher",
            "Un mec rentre dans un café et plouf",
            "Que prend un éléphant dans un café ? _ De la place",
            "C'est l'histoire d'un aveugle qui rentre dans un bar. Puis dans une table, et dans une chaise...",
            "C'est l'histoire d'un mec qui a 5 penis. Son slip lui va comme un gant",
            "Avec quelle monnaie les marins payent-ils ? _ Avec des sous marins",
            "Que dit un chien japonais pour dire bonjour ? _ Konichihuahua",
            "C\'est un mec qui entre dans un bar et qui dit \'Salut c\'est moi !\' _ Mais en fait c\'était pas lui",
            "Quel est le point commun entre un lapin et une bouteille en plastique ? _ Ils sont tous les deux en plastique, sauf le lapin",
            "Avec quoi ramasse-t-on une papaye ? _ Avec une foufourche",
            "Qu'est-ce qui est vert et qui pousse dans le jardin ? _ Un extraterrestre qui fait caca",
            "Que fait un poussin de 200kg ? _ PIOUUUUUU PIOUUUUUU !!!",
            "Comment fait un chat pour s'essuyer les fesses quand il fait caca dans le désert ? _ Tu donnes ta langue au chat ?",
            "Pourquoi les girafes ont un long cou ? _ Parce qu'elles puent du cul",
            "Que dit une mère à son fils geek quand le dîner est servi ? _ Alt Tab !",
            "Où vont les biscottes pour danser ? _ En biscothèque",
            "Comment appelle-t-on un chat qui va dans l'espace ? _ Un chatellite",
            "Combien faut-il de Français pour dévisser une ampoule ?  _  Un seul, pour tenir l'ampoule : il croit que le monde tourne autour de lui !",
            "Combien de dev faut-il pour changer une ampoule ? _ Zéro, c'est un problème de Hardware",
            "Quelle princesse a les lèvres gercées ?  _   Labello bois dormant",
            "Comment appelle-t-on un combat entre un petit pois et une carotte ? _ Un bon duel",
            "D'où viennent les gens les plus dangereux ? _ D’Angers",
            "Comment les musiciens choisissent-ils leur parquet ? _ Ils choisissent un parquet Fa Si La Si Ré",
            "Monsieur et madame Pote ont une fille, comment s'appelle-t-elle ? _ Jessica",
            "Qu'est-ce qui est pire que le vent ? _ Un vampire",
            "C'est en sciant que Léonard devint scie",
            "Comment un geek cri ? _ Il url",
            "Comment s'appelle la femelle du gnou ? _ La rtule",
            "<3 " * randint(1, 15),
            "IntersexPride " * randint(2, 5),
            "IntersexPride " * randint(2, 5),
            "IntersexPride " * randint(2, 5),
            "IntersexPride " * randint(2, 5)
        ]
        message = liste_msg[randint(0, len(liste_msg) - 1)]
        self.loop.create_task(self.chan.send(message))
        sleep(20)
        threading.Thread(target=self.do_thing).start()

    async def event_ready(self):
        chan = self.get_channel("Pimouki")
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
