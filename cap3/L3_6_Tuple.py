#tuple
frutta = ("apple", "banana", "cherry")
costanti = ("Ciao", 100, 3.14)
print(costanti)

#stampo gli elementi
for x in costanti:
    print(x)

#Il numero di elementi è dato da:
len(costanti)

#conteggio
lettere = ("A", "B", "C", "B", "D")
print(lettere.count("B"))

#pach/unpack
dati = "cane", 100, 3.14
print(dati)

a, b, c = dati
print(a)      
print(b)      
print(c)     

#posizione di un elemento
lettere = ("A", "B", "C", "B", "D")
posizione = lettere.index("C")
print(posizione)

#operazioni con le tuple
t = (1,2,3)
p = (4,5)
print(t + p)

t = (1,2,3)
print(t * 2)


