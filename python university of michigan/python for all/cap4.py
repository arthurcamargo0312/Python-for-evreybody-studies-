print(max("abcXYZ"))
# vai dar o "c" pq de acordo com o python o ""c" tem o maior numero de carecteres dentro da linguagem
def greet(lang):
    if lang == "es":
        return "Hola"
    elif lang == "fr":
        return "Bonjour"
    else:
        return "Hello"


print(greet("fr"), "Michael")
# o def guarda a informação como se fosse uma variavel normal , o "lang" podia ser chamado de x


def computepay(h, r):
    if h <= 40:
        return h * r
    else:
        return (40 * r) + ((h - 40) * (r * 1.5))


hrs = input("Enter Hours:")
rate = input("rate per hour")
h = float(hrs)
r = float(rate)


pay = computepay(h, r)
print("Pay", pay)
# Calculei o pagamento usando uma função: até 40h é normal, acima de 40h paga 1.5x (hora extra)
