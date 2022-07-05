import qrcode
from pyzbar.pyzbar import decode
from PIL import Image


def encodeur(data, chemin):
    img = qrcode.make(data)
    img.save(chemin)
    # Il est possible d'ajouter beaucoup de détails au qrcode comme la taille, la couleur, version et autres données
    # Je ne ferai pas ces parties car pas très importante


def decodeur(chemin):
    img = Image.open(chemin)
    resultat = decode(img)
    print(resultat)


if __name__ == '__main__':
    utilisateur = ''
    while utilisateur != 'E' and utilisateur != 'D':
        utilisateur = input('Que voulez-vous faire ? (E pour encoder un QRCode ou D pour decoder un QRCode) : ').upper()
    if utilisateur == 'E':
        data = input('Saisir la donnée à encoder : ')
        chemin = input('Saisir le chemin où sera stocké le QRCode : ')
        encodeur(data, chemin)
    else:
        chemin = input('Saisir le chemin du QRCode à décoder : ')
        decodeur(chemin)

