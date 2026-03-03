n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')
# como funciona o while
while True:
    line = input('> ')
    if line == 'done':
        break
print(line)
print('Done!')
# o loop fica infinito até alguém responder "done" daí vem o break
while True:
    line = input('> ')
    if line[0] == '#':
        continue

    if line == 'done':
        break

print(line)
print('Done!')

# Loop infinito: lê uma linha do usuário, ignora linhas que começam com '#', para quando digitar 'done' e imprime o resto.
largest_so_far = -1
print('Before', largest_so_far)

for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('After', largest_so_far)
## Percorre a lista e vai guardando em largest_so_far o maior número encontrado até agora.
largest = None
smallest = None

while True:
    num = input("Enter a number: ")

    if num == "done":
        break

    try:
        num = int(num)
    except:
        print("Invalid input")
        continue

    if largest is None or num > largest:
        largest = num

    if smallest is None or num < smallest:
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)
# Lê números até "done", usa try/except para ignorar entradas inválidas e atualiza maior e menor comparando cada número válido
