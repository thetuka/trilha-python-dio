lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

print(id(l2), id(lista))

# a função copy mostra uma cópia com os mesmos valores, mas sem alterar
# a lista original
