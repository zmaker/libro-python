import random

h = random.randint(0, 24)

nome = "Paolo"
saluto = ""

if h < 12:
    saluto = "buongiorno"
else:
    saluto = "salve"

msg = saluto + " " + nome + " ore:" + str(h)
print(msg)
