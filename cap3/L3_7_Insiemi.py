#insiemi
s = {"a", "b", "e", "m"}
print(s)

#insieme con duplicati
frutta = {"mela", "banana", "pera", "mela"}
print(frutta)

#costruttore con lista
primi = set([1, 3, 5, 7])
primi.add(11)
print(primi)

#rimuovo un elemento
primi.discard(1)
print(primi)

#genera un errore se l'elemento non è presente
#primi.remove(1)
#print(primi)

#svuoto l'insieme
pari = {2, 4, 6, 8}
print(pari)
pari.clear()
print(pari)

#verifico la presenza di un elemento
S = {1, 3, 4, 5, 6}
if (4 in S):
    print("4 è presente")
    
#scorro gli elementi
S = {1, 3, 4, 5, 6}
for el in S:
    print(el)


