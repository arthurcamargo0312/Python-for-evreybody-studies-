from itertools import count


fruit = "banana"
for letter in fruit:
    print(letter)

# or

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

# same thing len = retorna a quantidade de carecteres que tem um string 

greet = "Hello Bob"
nstr = greet.replace("Bob", "Jane")
print(nstr)

nstr = greet.replace("o", "X")
print(nstr)
# troca as palavras


data = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

# Localiza a posição do @
atpos = data.find("@")
print(atpos)

# Localiza o espaço (' ') começando a busca a partir da posição do @
sppos = data.find( " ", atpos)
print(sppos)

# Extrai o texto que começa um caractere após o @ até o espaço
host = data[atpos + 1 : sppos]
print(host)


# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
number1 = text.find("0")
number2 = text.find("5")
data = float(text[number1 : number2 + 1])

print(data)
