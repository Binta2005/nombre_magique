

def menu():
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
def calculer(a, b, operation):
        if operation == '1':
            return a + b
        elif operation == '2':
            return a - b
        elif operation == '3':
            return a * b
        elif operation == '4':
            return a / b
        else:
            return "operation non valide"
continuer = 'oui'
while continuer.lower() == 'oui':
    menu()
    operation = input("Choisissez une operation :")
    a = float(input("Entrez le premier nombre  :"))
    b = float(input("Entrez le second nombre  :"))
    result = calculer(a,b,operation)
    print(result)
    continuer = input("Vous voulez continuer?(OUI/NON) :")
print("Au revoir et merci d'avoir utiliser mon programme!")