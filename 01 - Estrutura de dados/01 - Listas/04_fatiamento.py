lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"]
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]

# a informação dentro de colchetes [X : X : X] se refere da seguinte forma:
# [X : :] -> valor inicial a ser contado
# [: X :] -> valor final, até onde vai ser contado
# [: : X] -> "passo", ou seja, de quanto em quanto será a contagem