testo = ""

print ("inserisci una riga vuota per finire")
while True:
    line = input(">")
    testo += line + "\n"
    if not line:
        break

print(testo)
