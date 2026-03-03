hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
if h <= 40:
    salario = h * r
elif h > 40:
    salario = 40 * r + (h - 40) * r * 1.5

print(salario)
# 3.1

score = input("Enter Score: ")
s = float(score)
if s > 10:
    print("error")
elif s >= 0.9:
    print("A")
elif s >= 0.8:
    print("B")
elif s >= 0.7:
    print("C")
elif s >= 0.6:
    print("D")
elif s < 0.6:
    print("F")
#3.2