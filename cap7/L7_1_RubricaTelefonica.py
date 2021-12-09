LOOP = True
rubrica = dict()

def esci():
global LOOP
print("bye!")
LOOP = False
def aggiungi():
global rubrica
nome = input("nome:")
tel = input("telefono:")
rubrica[nome] = tel
print("aggiunto")

def stampa():
global rubrica
for el in rubrica.keys():
tel = rubrica[el]
print(el, tel)

while (LOOP):
cmd = input("comando?")
if cmd == 'q':
esci()
elif cmd == 'a':
aggiungi()
elif cmd == 'l':
stampa()

Lo dividiamo su due file. Il primo:
modrubrica.py

def esci():
print("bye!")
return False
def aggiungi(rub): 
nome = input("nome:")
tel = input("telefono:")
rub[nome] = tel
print("aggiunto")

def stampa(rub):
for el in rub.keys():
tel = rub[el]
print(el, tel)

def main():
print("questo è un modulo")

if __name__ == "__main__":
main()

Il secondo
005-rub.py

import modrubrica as rr

def main():
LOOP = True
rubrica = dict()

print("Rubrica elettronica")
while (LOOP):
cmd = input("comando?") 
if cmd == 'q':
LOOP = rr.esci()
elif cmd == 'a':
rr.aggiungi(rubrica)
elif cmd == 'l':
rr.stampa(rubrica)


if __name__ == "__main__":
main()
