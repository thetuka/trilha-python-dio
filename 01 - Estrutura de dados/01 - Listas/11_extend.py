linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]


# o extend é o mesmo que o append, inclui novos itens, porém, é possivel 
# passar mais de um item ao mesmo tempo