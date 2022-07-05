import time


def compteur(temps):
    heures = 0
    while temps > 0:
        (minutes, secondes) = divmod(temps, 60)
        if minutes >= 60:
            (heures, minutes) = divmod(minutes, 60)
        compteur = '{:02d}:{:02d}:{:02d}'.format(heures, minutes, secondes)
        print(compteur, end='\r')
        time.sleep(1)
        temps -= 1
    print('Le compteur est à 00:00:00 !!!')


temps = int(input('Veuillez saisir le temps(en secondes) : '))
compteur(temps)

