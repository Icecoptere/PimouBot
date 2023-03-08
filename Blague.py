from random import randint


def get_blague():
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
        "C'est un mec qui entre dans un bar et qui dit 'Salut c'est moi !' _ Mais en fait c'était pas lui",
        "Quel est le point commun entre un lapin et une bouteille en plastique ? _ Ils sont tous les deux en plastique,"
        " sauf le lapin",
        "Avec quoi ramasse-t-on une papaye ? _ Avec une foufourche",
        "Qu'est-ce qui est vert et qui pousse dans le jardin ? _ Un extraterrestre qui fait caca",
        "Que fait un poussin de 200kg ? _ PIOUUUUUU PIOUUUUUU !!!",
        "Comment fait un chat pour s'essuyer les fesses quand il fait caca dans le désert ? _ Tu donnes ta langue "
        "au chat ?",
        "Pourquoi les girafes ont un long cou ? _ Parce qu'elles puent du cul",
        "Que dit une mère à son fils geek quand le dîner est servi ? _ Alt Tab !",
        "Où vont les biscottes pour danser ? _ En biscothèque",
        "Comment appelle-t-on un chat qui va dans l'espace ? _ Un chatellite",
        "Combien faut-il de Français pour dévisser une ampoule ?  _  Un seul, pour tenir l'ampoule : il croit que le "
        "monde tourne autour de lui !",
        "Combien de dev faut-il pour changer une ampoule ? _ Zéro, c'est un problème de Hardware",
        "Quelle princesse a les lèvres gercées ?  _   Labello bois dormant",
        "Comment appelle-t-on un combat entre un petit pois et une carotte ? _ Un bon duel",
        "D'où viennent les gens les plus dangereux ? _ D’Angers",
        "Comment les musiciens choisissent-ils leur parquet ? _ Ils choisissent un parquet Fa Si La Si Ré",
        "Monsieur et madame Pote ont une fille, comment s'appelle-t-elle ? _ Jessica",
        "Qu'est-ce qui est pire que le vent ? _ Un vampire",
        "C'est en sciant que Léonard devint scie",
        "Comment un geek cri ? _ Il url",
        "Comment s'appelle la femelle du gnou ? _ La rtule"
    ]
    message = liste_msg[randint(0, len(liste_msg) - 1)]
    return message
