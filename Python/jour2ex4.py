# from random import randint

# nbrMax = 20
# nMyst = randint(1,nbrMax)

# print("J'ai choisi un nombre mystère entre 1 et ",nbrMax, " à toi de le deviner")

# nUtil = int(input("Propose un nombre : "))
# if nUtil < nMyst:
#     print("Le nombre est trop petit")
#     print("Voici une indication")
#     print("Si tu ajoute 2 fois mon nombre à ton nombre tu dois trouver", 2*nMyst + nUtil)
#     nUtil2 = int(input("Propose un autre nombre : "))
# elif nUtil > nMyst:
#     print("Le nombre est trop grand")
#     print("Voici une indication")
#     print("Si tu ajoute 3 fois mon nombre à ton nombre tu dois trouver", 3 * nMyst + nUtil)
#     nUtil2 = int(input("Propose un autre nombre : "))
# else:
#     print("Félicitations ! Tu as trouvé ",nMyst," mon nombre mystère.")
#     nUtil2 = 99 + nbrMax
# if nUtil2 == nMyst and nUtil != nMyst :
#     print("Félicitations ! Tu as trouvé ", nMyst, " mon nombre mystère en 2 essais!")
# elif nUtil2 != nMyst and nUtil2 != 99 + nbrMax:
#     print("Dommage! tu n'as pas trouvé.")
#     print("Mon nombre mystère est : ",nMyst,".")

nombre_magique = 7
essai = 0
while nombre_magique != essai:
    essai = int(input("Deviner le nombre magique : "))
    if essai == nombre_magique:
        print("Bravo ! Tu as trouvé le nombre magique !")
    else:
        print("Tu as essayé de deviner le nombre magique mais tu n'as pas réussi.")
        
