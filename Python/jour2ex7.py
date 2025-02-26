max_deux_nombres = [12,99]
def maximum(max_deux_nombres):
    maxi = max_deux_nombres[1]
    for i in max_deux_nombres:
        if i >= maxi:
            maxi = i
    return maxi
print(maximum(max_deux_nombres))
