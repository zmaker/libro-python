pila = []
i = 0

while (True):
    cmd = input("? ")
    if (cmd == 'q'):
        break
    elif (cmd == 'l'):
        print(f"pila: {pila}")
    elif (cmd == 'i'):
        val = input("valore: ")
        pila.append(val)
        i += 1
    elif (cmd == 'p'):
        if (i >= 1):
            i -= 1
            val = pila[i]
            del pila[i]
            print(f"v: {val}")


print("fine")