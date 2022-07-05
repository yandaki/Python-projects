def madlib():

    verbe1 = input("Verbe à la 3e personne singulier : ")
    nom1 = input("Nom commun : ")
    nombre1 = input("Nombre en lettres: ")
    adjectif1 = input("Adjectif : ")
    adjectif2 = input("Adjectif : ")
    adjectif3 = input("Adjectif : ")

    madlib = f"Il me {verbe1} avec une sorte de complicité - qui allait au-delà de la {nom1}. L'un de ces sourires\
    singuliers qu'on ne rencontre que cinq ou {nombre1} fois dans une vie, et qui vous rassure à jamais. Qui, après avoir jaugé\
    - ou feint peut-être de jauger - le genre humain dans son ensemble, choisit de s'adresser à vous, poussé par\
    un irrésistible {adjectif1} favorable à votre égard. Qui vous comprend dans la mesure {adjectif2} où vous souhaitez\
    qu'on vous comprenne, qui croit en vous comme vous aimeriez croire en vous-même, qui vous assure que\
    l'impression que vous donnez est celle que vous souhaitez donner, celle d'être au {adjectif3} de vous-même"

    print(madlib)