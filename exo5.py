
a = float(input("Entrer le nombre A: "))
b = float(input("Entrer le nombre B: "))

def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if b != 0:
        return a/b
    else:
        return "Division impossible"

def menu():
      print("choississez une opération :")
      print("1.addition")
      print("2.subtraction")
      print("3.multiplication")
      print("4.division")
      print("5.exit")
menu()
choix = input("Entrez un choix parmi les operations du menu: ")
if choix in ["1","2","3","4","5"]:
    if choix == "1":
        print(addition(a,b))
    elif choix == "2":
        print(subtraction(a,b))
    elif choix == "3":
        print(multiplication(a,b))
    elif choix == "4":
        print(division(a,b))
    elif choix == "5":
        print("exit")





