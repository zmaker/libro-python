#dizionari
listino = {
"mele":12,
"pere":23,
"kiwi":45
}
print(listino)

#ricavo il valore associato a una chiave
print(listino["mele"])

#estraggo un valore anche con get()
print(listino.get("mele"))

#modifico un valore
listino["mele"] = 20
print(listino)

#inserisco nuova coppia
listino["fragole"] = 99
print(listino)

#elimino una coppia
listino.pop("fragole")
print(listino)

#elimino con del
listino["kiwi"] = 102
del listino["kiwi"]

#svuoto del tutto il dizionario
del listino
#in alternativa ho clear()
listino = {
"mele":12,
"pere":23,
"kiwi":45
}
listino.clear()
print(listino)

#liste di chiavi, valori e coppie
listino = {
"mele":12,
"pere":23,
"kiwi":45
}
#elenco chiavi
chiavi = listino.keys() 
print(chiavi)
#elenco non ordinato dei valori:
valori = listino.values() 
print(valori)
#elenco con le coppie chiave-valore
elementi = listino.items() 
print(elementi)

#stampo i valori scorrendo le chiavi
for k in listino.keys():
    print(k)
    
#verifico se una chiave è presente
if "mele" in listino:
    print("mele: ok")
else:
    print("mele: non trovato")

if "ciliegia" in listino:
    print("ciliegia: ok")
else:
    print("ciliegia: non trovato")

#copia di dizionari
listino2 = listino.copy()
print(listino2)
listino3 = dict(listino)
print(listino3)

    

