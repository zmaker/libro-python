testo = open("testo.txt")
print(testo.read())
testo.seek(0)
print(testo.read())
testo.close()
