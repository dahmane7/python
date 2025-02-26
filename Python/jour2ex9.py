
nombre1 = int(input("Entrez le premier nombre : "))
operation = input("Entrez l'opération à effectuer : ")
nombre2 = int(input("Entrez le deuxième nombre : "))
def calculer (nombre1, nombre2, operation):
        if operation == "+":
                return nombre1 + nombre2
        elif operation == "-":
                return nombre1 - nombre2
        elif operation == "*":
                return nombre1 * nombre2
        elif operation == "/":
                    if nombre2 == 0:
                            print("Erreur : division par zéro")
                    else:
                            return nombre1 / nombre2
                            
        else:
                print("Erreur : opération non reconnue")
    
    
resultat = calculer(nombre1, nombre2, operation)
print("Le résultat de l'opération est : ", resultat)

