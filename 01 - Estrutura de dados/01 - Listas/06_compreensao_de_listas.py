# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)

# a compressão de lista oferece uma sintaxe mais curta qdo vc deseja 
# criar uma lista nova a partir de uma existente (filtro) ou gerar 
# nova lista, aplicando alguma modificação

# [numero for numero in numeros if numero % 2 == 0] = a 1 parte (numero) é o valor que eu quero
# a segunda parte (for numero in numeros) é meu iteravel

