carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
    
    # consigo percorrer os conjuntos normalmente, igual as listas, no caso,
    # usando o enumerate
