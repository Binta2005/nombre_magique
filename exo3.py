print("Une pyramide d' étoiles")
L = int(input("Entrez le nombre de lignes: "))
for i in range(0 ,L):
    for j in range(0 ,L-i-1) :
      print(end= '  ')
    for j in range(i+ 1):
        print('* ',end='  ')
    print()