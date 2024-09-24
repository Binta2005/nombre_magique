
mot1 = input("Entrez le mot1 :")
mot2 = input("Entrez le mot2 :")

if len(mot1) > len(mot2):
      print(f"le mot le plus long est {mot1}")
elif len(mot2) > len(mot1):
        print(f"le mot le plus short est {mot2}")
else:
       print(f"les deux  mots sont de la meme longueur.")
