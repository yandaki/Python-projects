import random


def guess(x):
    random_nombre = random.randint(1, x)
    devine = 0
    vie = 10
    while devine != random_nombre and vie > 0:
        devine = int(input(f"Saisir le nombre entre 1 et {x}: "))
        if devine < random_nombre:
            print("Trop petit par rapport au nombre à deviner")
            vie -= 1
        elif devine > random_nombre:
            print("Trop grand par rapport au nombre à déviner")
            vie -= 1
    if vie > 0:
        print(f"Félicitations, vous avez trouvé le nombre {random_nombre}")
    else:
        print(f'Vous avez perdu. Le nombre à trouver était {random_nombre}')


def guess_computer(x):
    random_nombre = 0
    min = 1
    max = x
    valid = ''
    vie = 10
    while valid != 'e' and vie > 0:
        if min != max:
            random_nombre = random.randint(min, max)
        else:
            random_nombre = min
        valid = input(f"Le nombre {random_nombre} est-il plus grand(g), plus petit(p) ou egale(e) au nombre à deviner ? : ").lower()
        if valid == 'g':
            max = random_nombre - 1
            vie -= 1
        elif valid == 'p':
            min = random_nombre + 1
            vie -= 1
        elif valid != 'g' and valid != 'p' and valid != 'e':
            print('Vous avez saisi un mauvais caractère. Réessayez !!')
    if vie > 0:
        print(f"\nL\'ordinateur a trouvé le nombre {random_nombre}")
    else:
        print(f'Vous avez perdu. Le nombre à trouver était {random_nombre}')


continuer = "O"
while continuer == "O":
    limite = int(input('Inscrivez la limite pour le nombre à choisir : '))

    nombre = int(input("Choisissez 1 pour deviner le nombre de l'ordinateur et 2 pour que l'ordinateur devine votre nombre : "))
    while nombre != 1 and nombre != 2:
        print("Vous devez choisir entre 1 et 2.")
        nombre = int(input("Choisissez 1 pour deviner le nombre de l'ordinateur et 2 pour que l'ordinateur devine votre nombre : "))

    if nombre == 1:
        guess(limite)
    elif nombre == 2:
        guess_computer(limite)

    continuer = input("Voulez-vous continuer à jouer : O pour oui et N pour non ? ")
    continuer = continuer.upper()
    print("\n")

