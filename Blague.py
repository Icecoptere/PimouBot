from random import randint


def get_blague():
    liste_msg = [
        "Si une horloge sonne 13 fois, quelle heure est-il?  Il est l’heure d’acheter une nouvelle horloge!",
        "C'est l'histoire du ptit dej, tu la connais ?  Pas de bol",
        "Que demande un footballeur à son coiffeur ?  La coupe du monde",
        "C'est quoi une chauve-souris avec une perruque ?  Une souris",
        "Que fait un crocodile quand il rencontre une superbe femelle ?  Il Lacoste",
        "Tu connais la blague de la chaise ?  Elle est pliante",
        "Tu connais la blague de la feuille ?  Elle déchire",
        "Quel est le crustacé le plus léger de la mer ?   La palourde",
        "Pourquoi est-ce que Napoléon n'a pas voulu acheter de maison ?   Parce qu’il avait déjà un Bonaparte",
        "Où va Messi quand il se blesse ?   À la pharmessi",
        "Qu'est-ce qui est vert avec une cape ?    Un concombre qui imite Super Tomate.",
        "Comment appelle-t-on un chien qui n'a pas de pattes ?   On ne l’appelle pas, on va le chercher",
        "Un mec rentre dans un café et plouf",
        "Que prend un éléphant dans un café ?   De la place",
        "C'est l'histoire d'un aveugle qui rentre dans un bar. Puis dans une table, et dans une chaise...",
        "C'est l'histoire d'un mec qui a 5 penis. Son slip lui va comme un gant",
        "Avec quelle monnaie les marins payent-ils ?   Avec des sous marins",
        "Que dit un chien japonais pour dire bonjour ?   Konichihuahua",
        "C'est un mec qui entre dans un bar et qui dit 'Salut c'est moi !'   Mais en fait c'était pas lui",
        "Quel est le point commun entre un lapin et une bouteille en plastique ?   Ils sont tous les deux en plastique,"
        " sauf le lapin",
        "Avec quoi ramasse-t-on une papaye ?   Avec une foufourche",
        "Qu'est-ce qui est vert et qui pousse dans le jardin ?   Un extraterrestre qui fait caca",
        "Que fait un poussin de 200kg ?   PIOUUUUUU PIOUUUUUU !!!",
        "Comment fait un chat pour s'essuyer les fesses quand il fait caca dans le désert ?   Tu donnes ta langue "
        "au chat ?",
        "Pourquoi les girafes ont un long cou ?   Parce qu'elles puent du cul",
        "Que dit une mère à son fils geek quand le dîner est servi ?   Alt Tab !",
        "Où vont les biscottes pour danser ?   En biscothèque",
        "Comment appelle-t-on un chat qui va dans l'espace ?   Un chatellite",
        "Combien faut-il de Français pour dévisser une ampoule ?     Un seul, pour tenir l'ampoule : il croit que le "
        "monde tourne autour de lui !",
        "Combien de dev faut-il pour changer une ampoule ?   Zéro, c'est un problème de Hardware",
        "Quelle princesse a les lèvres gercées ?      Labello bois dormant",
        "Comment appelle-t-on un combat entre un petit pois et une carotte ?   Un bon duel",
        "D'où viennent les gens les plus dangereux ?   D’Angers",
        "Comment les musiciens choisissent-ils leur parquet ?   Ils choisissent un parquet Fa Si La Si Ré",
        "Monsieur et madame Pote ont une fille, comment s'appelle-t-elle ?   Jessica",
        "Qu'est-ce qui est pire que le vent ?   Un vampire",
        "C'est en sciant que Léonard devint scie",
        "Comment un geek cri ?   Il url",
        "Comment s'appelle la femelle du gnou ?   La rtule"
    ]
    message = liste_msg[randint(0, len(liste_msg) - 1)]
    return message
