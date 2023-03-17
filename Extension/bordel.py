from random import randint


def endlebordel(cmd, message, parsed_input):
    match cmd:
        case "bonjour":
            liste_msg = [
                f'Bonjour {message.author.name} ? comment vas tu en cet journée, moi je vais bien il faut beau chaud '
                f'tres chaud même personnellement je me prélasse devant pimouki en m\'enfournant des beignets a la '
                f'pomme, aime tu les beignets a la pomme {message.author.name.upper()} ? Moi j\'aime les beignets a '
                f'la pomme Hmmm le gouts de la pomme qui coule dans la bouche puis ce déverse dans la gorge Hmmm ce '
                f'doux gouts.'
                f'Il m\'arrive même des folies et en prendre un au nutella houlala que suis je fou (hihihi).',
                "Bonjour",
                f'Bonjour {message.author.name} '
                f'ce week end je ne pourrais pas venir te chercher par ce que j\'ai autre chose a faire j\'espere que '
                f'tu comprendras']
            return liste_msg[randint(0, len(liste_msg) - 1)]
        case "aime":
            text = ' '.join(parsed_input[1:])
            return f'moi aussi j\'aime {text}'
        case "pipi":
            return "oh la le pipi"
        case "addition":
            if parsed_input[1].isdigit() and parsed_input[2].isdigit():
                resultat = int(parsed_input[1]) + int(parsed_input[2])
                return f'le résultats est {resultat}'
            else:
                return "Tu es un grand couillon tu n'as pas mis de chiffre"
        case "soustraction":
            if parsed_input[1].isdigit() and parsed_input[2].isdigit():
                resultat = int(parsed_input[1]) - int(parsed_input[2])
                return f'le résultats est {resultat}'
            else:
                return "Tu es un grand couillon tu n'as pas mis de chiffre"
        case "multiplication":
            if parsed_input[1].isdigit() and parsed_input[2].isdigit():
                resultat = int(parsed_input[1]) * int(parsed_input[2])
                return f'le résultats est {resultat}'
            else:
                return "Tu es un grand couillon tu n'as pas mis de chiffre"
        case "division":
            if parsed_input[1].isdigit() and parsed_input[2].isdigit():
                if parsed_input[2] == '0':
                    return "Ce n'est pas possible de divisé par 0."

                resultat = int(parsed_input[1]) / int(parsed_input[2])
                return f'le résultat est {resultat}'
            else:
                return "Tu es un grand couillon tu n'as pas mis de chiffre"
    return None
