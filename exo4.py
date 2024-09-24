
L = int(input("Entrez le nombre de lignes: "))
for i in range(L , 0,-1):
    for j in range(0, L-i):
        print(end=' ')
    for k in range (0 , i):
        print(' *', end=' ')
    print()