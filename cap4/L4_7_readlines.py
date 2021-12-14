testo = open("L4_6_testo.txt")
linee = testo.readlines()

for ll in linee:
    print(ll, end = "")

testo.close()
