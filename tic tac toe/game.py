import time

from player import JoueurHumain, JoueurOrdinateur, JoueurOrdiIntelligent


class Tictactoe:
    def __init__(self):
        self.plateau = [' ' for _ in range(9)]  # On utilise une liste pour représenter le plateau 3x3
        self.gagnant_actuel = None

    def affichage_plateau(self):
        # Affichage du plateau par ligne
        for ligne in [self.plateau[(i*3):(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(ligne) + ' |')

    @staticmethod
    def affiche_nombre_plateau():
        # |0|1|2| et ainsi de suite pour les autres lignes
        nombre_plateau = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for ligne in nombre_plateau:
            print('| ' + ' | '.join(ligne) + ' |')

    def position_libre(self):
        return [i for i, place in enumerate(self.plateau) if place == ' ']
        # Autre possibilité :
        # positions = []
        # for(i, place) in enumerate(self.plateau):
        #    # Pour ('X','0','X') -> (0,'X'), (1,'O'), (2, 'X')
        #    if place == ' ':
        #        positions.append(i)

    def place_vide(self):
        return ' ' in self.plateau  # Cette fonction True ou False sur le fait qu'il y a au moins une place vide

    def nombre_place_vide(self):
        return self.plateau.count(' ')

    def placer_pion(self, place, lettre):
        if self.plateau[place] == ' ':
            self.plateau[place] = lettre
            if self.gagnant(place, lettre):
                self.gagnant_actuel = lettre
            return True
        return False

    def gagnant(self, place, lettre):
        # On vérifie les lignes
        ind_ligne = place // 3
        ligne = self.plateau[ind_ligne*3:(ind_ligne+1)*3]
        if all(val == lettre for val in ligne):
            return True

        # On vérifie les colonnes
        ind_col = place % 3
        col = [self.plateau[ind_col+i*3] for i in range(3)]
        if all(val == lettre for val in col):
            return True

        # On vérifie les diagonales
        if place % 2 == 0:
            diagonal1 = [self.plateau[i] for i in [0, 4, 8]]
            if all(val == lettre for val in diagonal1):
                return True
            diagonal2 = [self.plateau[i] for i in [2, 4, 6]]
            if all(val == lettre for val in diagonal2):
                return True

        return False


def jouer(jeu, joueur_x, joueur_o, affiche_jeu=True):
    if affiche_jeu:
        jeu.affiche_nombre_plateau()

    lettre = 'X'
    while jeu.place_vide():
        if lettre == 'X':
            place = joueur_x.position(jeu)
        else:
            place = joueur_o.position(jeu)

        if jeu.placer_pion(place, lettre):
            if affiche_jeu:
                print(lettre + f' a bougé à la place {place}')
                jeu.affichage_plateau()
                print('')

                if jeu.gagnant_actuel:
                    if affiche_jeu:
                        print(lettre + ' gagne. Félicitations !!')
                    return lettre

                # Si la lettre est X on change en 0 et inversement
                lettre = 'O' if lettre == 'X' else 'X'

            time.sleep(0.8)

    if affiche_jeu:
        print('C\'est un match nul !')


if __name__ == '__main__':
    joueur_x = JoueurHumain('X')
    joueur_o = JoueurOrdiIntelligent('O')
    t = Tictactoe()
    jouer(t, joueur_x, joueur_o, affiche_jeu=True)
