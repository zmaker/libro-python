def esci():
    print("bye!")
    return False

def aggiungi(rub): 
    nome = input("nome:")
    tel = input("telefono:")
    rub[nome] = tel
    print("aggiunto")

def stampa(rub):
    i = 1
    for el in rub.keys():
        tel = rub[el]
        print(f"{i} - {el}\t:{tel}")
        i += 1

def modifica(rub): 
    nome = input("nome? ")
    if nome in rub:
        tel = input("nuovo numero: ")
        rub[nome] = tel
        print("modificato")
    
    else:
        print("non presente")   

if __name__ == "__main__":
    print("Il modulo non può essere eseguito")
