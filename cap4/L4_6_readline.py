testo = open("L4_6_testo.txt")
i = 1
for ll in testo:
    print(i, ll, end="")
    i += 1

testo.close()