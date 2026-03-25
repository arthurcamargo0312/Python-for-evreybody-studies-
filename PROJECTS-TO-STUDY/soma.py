import re

arquivo = open("regex_sum_2369323.txt")

soma = 0

for linha in arquivo:
    numeros = re.findall("[0-9]+", linha)
    for numero in numeros:
        soma += int(numero)

print(soma)
