from randomMadlib import montecristo, lavie_lunivers_lereste, gatsby_le_magnifique
import random

if __name__ == "__main__":
    texte = random.choice([montecristo, lavie_lunivers_lereste, gatsby_le_magnifique])
    texte.madlib()
