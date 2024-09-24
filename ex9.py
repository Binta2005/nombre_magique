print("Bienvenue dans le jeu de nombre magique ! ")


import random

def niveau_fifficulte():
    print("Choisissez un niveau difficulté:")
    print("1.Facile(10 tentatives,intervalle 0-100)")
    print("2.Moyen(6 tentatives,intervalle 0-1000)")
    print("3.Difficile(3 tentatives,intervalle 0-10000)")
    max_tentatives = 0
    niveau = input("Entez un niveau: ")
    if niveau == "1":
        max_tentatives = 10
        intervalle_max = 100
    elif niveau == "2":
        max_tentatives = 6
        intervalle_max = 1000
    elif niveau == "3":
        max_tentatives = 3
        intervalle_max = 10000
    else:
        print("Niveau invalide! Veuillez redémarrer le jeu et choisir un niveau valide.")
        return

    nombre_a_deviner = random.randint(0, intervalle_max)
    nbr_tentatives = 0
    devine = False


    print(f"Devinez le nombre entre 0 et {intervalle_max}")


    while not devine and nbr_tentatives < max_tentatives:
        try:
            nbr_user = int(input("Entrez votre nombre : "))
            nbr_tentatives += 1
            if nbr_user < 0 or nbr_user > intervalle_max:
                print(f"Le nombre doit être compris entre 0 et {intervalle_max}")
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
    if not devine:
            print(f"Vous venez d'épuiser vos {max_tentatives} tentative(s)!Le nombre magic {nombre_a_deviner}.")



niveau_fifficulte()
