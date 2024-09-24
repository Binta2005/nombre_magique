

import random

def jeu_nbr_magic():
    nombre_a_deviner = random.randint(0 ,1000)
    tentative = None

    print("Bienvenue dans le jeu de nombre magic ! Devinez le nombre entre 0 et 1000 ")


    while tentative != nombre_a_deviner:
        try:
            tentative = int(input("entrez votre nombre : "))

            if tentative < 0 or tentative > 1000:
                 print("le nombre doit etre compris entre 0 et 1000")
            elif tentative < nombre_a_deviner:
                print("c'est plus grand que:",tentative )
            elif tentative > nombre_a_deviner:
                print("c'est moins que: ",tentative )
            else:
                print("Bravo! vous avez trouvé le nombre magic:")
        except ValueError:
            print("le nombre doit etre compris entre 0 et 1000")
jeu_nbr_magic()