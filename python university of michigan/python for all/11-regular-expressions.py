import re

texto = "Contato: arthur@gmail.com"

emails = re.findall("\w+@\w+\.\w+", texto)

print(emails)


#####
import re

text = "Meu nome é Arthur"

resultado = re.search("Arthur", texto)

if resultado:
    print("Encontrou!")
else:
    print("Não encontrou")

# import re


hand = open("mbox-short.txt")
numlist = list()

for line in hand:
    line = line.rstrip()
    stuff = re.findall("^X-DSPAM-Confidence: ([0-9.]+)", line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)

print("Maximum:", max(numlist))


# O código abre o arquivo "mbox-short.txt" e percorre cada linha.
# Usando regular expression (re.findall), ele procura linhas que começam com
# "X-DSPAM-Confidence:" e captura apenas o número que aparece depois.
# Esses números são convertidos para float e adicionados em uma lista.
# No final, o programa imprime o maior valor encontrado na lista.


import re

arquivo = open("regex_sum_2369323.txt")

soma = 0

for linha in arquivo:
    numeros = re.findall("[0-9]+", linha)
    for numero in numeros:
        soma += int(numero)

print(soma)


# importa a biblioteca de regex
# abre o arquivo com os números espalhados no texto
# percorre cada linha do arquivo
# usa re.findall('[0-9]+') para encontrar todos os números da linha
# [0-9]+ significa um ou mais dígitos
# cada número encontrado vem como string
# convertemos para inteiro com int()
# somamos todos na variável soma
# no final imprimimos o resultado
