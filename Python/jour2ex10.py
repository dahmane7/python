# compter_pairs(liste)
input = 134856901

input_str = str(input)

zeros = 0
odds = 0
evens = 0

for i in range(len(input_str)):
	if int(input_str[i]) == 0:
		zeros = zeros + 1
	elif int(input_str[i]) % 2 == 1:
		odds = odds + 1
	else:
		evens = evens + 1

print("Chaîne d'entrée "+str(evens)+" pairs.")


# 
# 
# 
# 
# 
# 
# l =[23,4,56,7,8,9,0,18,7,6,55,43,2]
# def extract(l):
#     pair = []
#     impair = []
#     for x in l:
#         if(x%2 == 0):
#             pair.append(x)
#         else:
#             impair.append(x)
#     print("La liste des entiers pair est : ",pair)
#     print("La liste des entiers impair est : ",impair)
# # Tester l'algorithme
# print(extract(l))