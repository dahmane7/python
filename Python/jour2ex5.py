
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def maximum(liste):
    maxi = liste[9]
    for i in liste:
        if i >= maxi:
            maxi = i
    return maxi
print(maximum(liste))

