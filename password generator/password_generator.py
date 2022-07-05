import random
import string


def generateur_password(nbre_password, longueur):
    caractere = string.ascii_letters + string.digits + string.punctuation
    for i in range(nbre_password):
        password = ''
        for j in range(longueur):
            password += random.choice(caractere)
        print(password)


nbre_password = int(input('Combien de mots de passe voulez-vous générer ? : '))
longueur = int(input('Quelle est la longueur des mots de passe générés ? : '))
generateur_password(nbre_password, longueur)

