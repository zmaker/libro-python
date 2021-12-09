#ricerca
txt = "Nel mezzo del cammin di nostra vita"
if "del" in txt:
  print("ok")

#indice di una stringa
txt = "nel mezzo del cammin"
n = txt.index("del")

#rimuovo gli spazi
txt = "  nel mezzo del cammin di nostra vita  "
print(f"#{txt}#")
txt = txt.strip()
print(f"#{txt}#")

#effetto di upper e lower
txt = "Nel Mezzo Del Cammin Di Nostra Vita…"
print("maiuscolo:", txt.upper())
print("minuscolo:", txt.lower())

#ricerca case-insensitive
txt = "Nel Mezzo Del Cammin Di Nostra Vita…"
key = input("Che termine verifico? ")
if key.upper() in txt.upper():
  print("ok")
else:
  print("non trovato")

#sostituzioni
txt = "  nel mezzo del cammin di nostra vita  "
print(txt.replace("e","*"))
print(txt.replace("vita","gita"))

#valori separati da virgola
a = "12,23,435,56,67,34,45"
b = "mele pere fragole kiwi"

b = "mele pere fragole kiwi"
lista = b.split(" ")
for token in lista:
  print(token)

#CSV
txt = "12,23,435,56,,67,34.4,45"
lista = txt.split(",")
for token in lista:
  print(token)
