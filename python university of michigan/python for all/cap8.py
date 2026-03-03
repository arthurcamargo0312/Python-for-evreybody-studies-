friends = ["jose", 'maria', 'pedro']

for friend in friends:
    print ('Happy new year', friend)


for i in range (len(friends)) : 
    friend  = friends [i]
    print ("Happy new year", friend)


## monta uma lista de palavras sem repetição a partir do arquivo

fname = input("Enter file name: ")
fh = open(fname)
palavras = []

for line in fh:
    partes = line.split()
    for palavra in partes:
        if palavra not in palavras:
            palavras.append(palavra)

palavras.sort()
print(palavras)
