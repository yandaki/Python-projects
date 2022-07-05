import random


def pierre_feuille_ciseau():
    nombre_de_tour = 1
    point_utilisateur = 0
    point_ordinateur = 0
    while nombre_de_tour <= 3:
        utilisateur = input("Faites votre choix; pierre(p), feuille(f), ciseau(c) : \n").lower()
        ordinateur = random.choice(['p', 'f', 'c'])

        if est_gagant(utilisateur, ordinateur):
            print("Utilisateur : " + utilisateur + " Ordinateur : " + ordinateur)
            point_utilisateur += 1
        elif est_gagant(ordinateur, utilisateur):
            print("Utilisateur : " + utilisateur + " Ordinateur : " + ordinateur)
            point_ordinateur += 1
        else:
            print("Utilisateur : " + utilisateur + " Ordinateur : " + ordinateur)
        nombre_de_tour += 1

    if point_ordinateur == point_utilisateur:
        return 'Egalité, match nul'
    elif point_utilisateur > point_ordinateur:
        return 'Victoire, vous avez gagné'
    else:
        return 'Défaite, l\'ordinateur a gagné'


def est_gagant(x1, x2):
    if(x1 == 'p' and x2 == 'c') or (x1 == 'c' and x2 == 'f') or (x1 == 'f' and x2 == 'p'):
        return True

print(pierre_feuille_ciseau())

