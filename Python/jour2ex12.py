def moyenne_liste(liste):
    return sum(liste)/len(liste)
nb_notes = int(input("Entrez le nombre de notes : "))
notes = []
for i in range(nb_notes):
    notes.append(int(input("Entrez la note : {i+1} : ")))
    print(f"La moyenne des notes est de {(moyenne_liste(notes))}")
