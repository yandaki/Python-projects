from words import words
import random
import string


def choix_mot(words):
    mot_a_trouver = random.choice(words)
    return mot_a_trouver


def hangman():
    vie = 6
    mot_a_trouver = choix_mot(words)
    lettre_du_mot_a_trouver = set(mot_a_trouver)  # lettre du mot à trouver dans une liste : maman -> {a,m,n}
    alphabet = set(string.ascii_lowercase)  # Alphabet en Ascii minuscule
    lettre_utilisees = set()   # lettres de l'alphabet déjà saisies
    mot_affiche = ""
    while len(lettre_du_mot_a_trouver) > 0 and vie > 0:
        # Lister les lettres déjà saisies
        print("Il vous reste ", vie, "vie et vous avez utilisé ces lettres ", ' '.join(lettre_utilisees))

        # lister le mot sous la forme e-ol-
        # mot_affiche = [lettre if lettre in lettre_utilisees else '-' for lettre in mot_a_trouver]
        # instruction incompréhensible, peut être voir une autre solution
        mot_affiche = ""
        for lettre in mot_a_trouver:
            if lettre in lettre_utilisees:
                mot_affiche += lettre
            else:
                mot_affiche += '-'
        print("Mot actuel : ", ' '.join(mot_affiche))

        lettre_saisi = input("Saisissez une lettre : ").lower()
        if lettre_saisi in alphabet - lettre_utilisees:
            lettre_utilisees.add(lettre_saisi)
            if lettre_saisi in lettre_du_mot_a_trouver:
                lettre_du_mot_a_trouver.remove(lettre_saisi)
            else:
                vie -= 1

        elif lettre_saisi in lettre_utilisees:
            print(f"Vous avez déjà saisi la lettre {lettre_saisi}")

        else:
            print("Vous avez saisi un caractère qui n'est pas dans l'alphabet")

    # Fin de partie
    if vie == 0:
        print(f"Vous avez perdu. Le mot était {mot_a_trouver}")
    else:
        print(f"Félicitations, vous avez trouvé le mot : {mot_a_trouver}")


if __name__ == '__main__':
    jouer = 'O'
    print('-------------- Bienvenue au jeu HANGMAN ----------------------------')
    print('\n')
    while jouer == 'O':
        hangman()
        reponse = ''
        while reponse != 'O' and reponse != 'N':
            reponse = input('Voulez-vous rejouer ? (O pour oui et N pour Non) : ').upper()
        jouer = reponse
        print('\n')
    print('----------Merci d\'avoir joué. A bientôt !!-----------------------')
