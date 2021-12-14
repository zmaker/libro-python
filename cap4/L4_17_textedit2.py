testo = []

print ("[INVIO] quit\n [l] print")
while True:
    line = input("> ")
    if not line:
        break
    elif line == 'l':
        i = 0
        for el in testo:
            print(f"{i}: {el}")
            i+=1
    else:
        testo.append(line)
    
    