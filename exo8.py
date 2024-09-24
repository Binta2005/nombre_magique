import random

def jeu_nbr_magic():
    nombre_a_deviner = random.randint(0, 1000)
    nbr_tentatives = 0
    devine = False

    print("Bienvenue dans le jeu de nombre magique ! Devinez le nombre entre 0 et 1000")

    while not devine:
        try:
            nbr_user = int(input("Entrez votre nombre : "))
            nbr_tentatives += 1
            if nbr_user < 0 or nbr_user > 1000:
                print("Le nombre doit être compris entre 0 et 1000")
                continue



            if nbr_user < nombre_a_deviner:
                print("C'est plus grand que :", nbr_user)
            elif nbr_user > nombre_a_deviner:
                print("C'est moins que :", nbr_user)
            else:
                print(f"Bravo ! Vous avez trouvé le nombre magique {nombre_a_deviner} en {nbr_tentatives} tentative(s).")
                print(f"Votre score est : {nbr_tentatives}")
                devine = True
        except ValueError:
            print("Ce n'est pas un nombre valide. Veuillez entrer un nombre entier.")

if __name__ == '__main__':
    jeu_nbr_magic()

