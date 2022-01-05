#funzione semplice
def saluta():
    print("hello")
    
saluta()

#funzione con due parametri
def somma(a, b):
    s = a + b
    print(f"{a} + {b} = {s}")
    
somma(10, 5)

#lista come parametro
def printlista(cibo):
    for el in cibo:
        print(el)

elenco_cibo = ["mela", "banana", "pera"]
printlista(elenco_cibo)

#funzione vuota / segnaposto
def vuota():
    pass

#funzione con numero arbitrario di parametri
def cugini(*kids):
    n = len(kids)
    print("ci sono " + str(n) + " cugini:")  
    for k in kids:
        print("cugino " + k)  

cugini("Luigi", "Mario", "Anna", "Carla")

#parametri nominali
def assetto(pitch, roll, yaw):
    print(f"l'assetto è: {pitch},{roll},{yaw}")

assetto(10, 20, 30)
assetto(roll=12.0, yaw=1.0, pitch=120.0)

#parametri predefiniti
def pagamento(articolo, prezzo, valuta="eur"):
    print(f"{articolo}: {prezzo} {valuta}")

pagamento("pane", "1.00", "eur")
pagamento("milk", "1.50", "usd")
pagamento("uova", "1.98")

#funzioni che restituiscono valori
def somma2(a, b):
    s = a + b
    return s

a = 10
b = 5
s = somma2(a, b)
print(s)

#parametri per indirizzo
def cambiaNome(n):
    n = "Mario"
    
nome = "Paolo"
print("prima di f: " + nome)
cambiaNome(nome)
print("dopo di f: " + nome)

def cambiaNome2(n):
    n[0] = "Mario"
    
nomi = ["Paolo"]

print("prima di f: " + nomi[0])
cambiaNome2(nomi)
print("dopo di f: " + nomi[0])

#restituire più valori
def multiop(a, b):
    s = a+b
    p = a*b
    return s, p

#unpacking:
n, m = multiop(12, 34)
print("somma: " + str(n))
print("molt.: " + str(m))

