# 7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.


# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)

except: 
    print("file cannot be openned ")
    quit()


for line in fh:
    line = line.rstrip()
    line = line.upper()
    print(line)


# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:X-DSPAM-Confidence:    0.8475  Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
parte = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    partes = line.split(":")
    numeros = float(partes[1])
    parte = parte + numeros


print("Average spam confidence:", parte / count)


# padrão para ler arquivo, filtrar linhas, somar valores e calcular média
