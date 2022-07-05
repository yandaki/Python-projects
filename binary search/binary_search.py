"""""
Script pour la recherche binaire. On créera deux fonctions : une recherche recursive classique et une
recherche binaire pour une liste à 1000 éléments et voir quelle recherche est la plus rapide.
Pour l'algorithme de recherche binaire, il faut que la liste de nombres soit rangée dans l'ordre croissant. 
"""""

import time
import random

def recherche_recursive(l, val):
    for i in range(len(l)):
        if l[i] == val:
            #print(f'On a trouvé {val} à la position {i}.')
            return i
    return -1

def recherche_binaire(l, val, max=None, min=None):
    if min == None:
        min = 0
    if max == None:
        max = len(l)-1

    if max < min:
        return -1

    milieu = (min+max)//2
    if l[milieu] == val:
        return milieu
    elif l[milieu] > val:
        max = milieu - 1
        return recherche_binaire(l, val, min, max)
    else:
        min = milieu + 1
        return recherche_binaire(l, val, min, max)


if __name__ == '__main__':
    liste = []
    while len(liste) < 1000:
        liste.append(random.randint(-1000, 1000))

    liste = sorted(liste)

    start = time.time()
    for i in range(1000):
        recherche_recursive(liste, i)
    end = time.time()
    print('Temps écoulé : ', (end - start)/1000)

    start = time.time()
    for i in range(1000):
        recherche_binaire(liste, i)
    end = time.time()
    print('Temps écoulé : ', (end - start)/1000)

