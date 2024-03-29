linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)


# o sort ordena nossa lista. Caso não informe paramentros, ela vai ordenar por padrão
# de forma alfabetica
# o sort reverse faz a organização de tras pra frente
# se eu quiser ordenar por tamanho de palavra, eu preciso passar uma função, no caso, aqui
# foi usada a função "lambda", o argumento "X" e por fim o que eu quero, que é o tamanho, 
# sendo usado o "len(x)"