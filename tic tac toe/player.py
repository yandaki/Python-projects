import math
import random


class Joueur:
    def __init__(self, lettre):
        # lettre X ou O à mettre dans les cases
        self.lettre = lettre

    def position(self, jeu):
        pass


class JoueurOrdinateur(Joueur):
    def __init__(self, lettre):
        super().__init__(lettre)

    def position(self, jeu):
        place = random.choice(jeu.position_libre())
        return place


class JoueurHumain(Joueur):
    def __init__(self, lettre):
        super().__init__(lettre)

    def position(self, jeu):
        place_valide = False
        val = None
        while not place_valide:
            place = input(self.lettre + ' tour. Entrée votre position (0 - 8) : ')
            # On fera des vérifications afin de déterminer la justesse de la réponse entrée
            try:
                val = int(place)
                if val not in jeu.position_libre():
                    raise ValueError
                place_valide = True
            except ValueError:
                print('Place non valide essayez encore.')

        return val

class JoueurOrdiIntelligent(Joueur):
    def __init__(self, lettre):
        super().__init__(lettre)

    def position(self, jeu):
        if len(jeu.position_libre()) == 9:
            place = random.choice(jeu.position_libre())
        else:
            place = self.minimax(jeu, self.lettre)['position']
        return place

    def minimax(self, etat, joueur):  # Etat et non jeu parce quà chaque fois qu'on joue le jeu change
        max_joueur = self.lettre
        autre_joueur = 'O' if joueur == 'X' else 'X'

        if etat.gagnant_actuel == autre_joueur:
            return {'position': None,
                    'score': 1*(etat.nombre_place_vide()+1) if autre_joueur == max_joueur else -1*(etat.nombre_place_vide()+1)}
        elif not etat.place_vide():
            return {'position': None, 'score': 0}

        if joueur == max_joueur:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for position_possible in etat.position_libre():
            # Step 1
            etat.placer_pion(position_possible, joueur)
            # Step 2
            sim_score = self.minimax(etat, autre_joueur)
            # Step 3
            etat.plateau[position_possible] = ' '
            etat.gagnant_actuel = None
            sim_score['position'] = position_possible
            # Step 4
            if joueur == max_joueur:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
