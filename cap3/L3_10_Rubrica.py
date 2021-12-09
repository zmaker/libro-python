print("rubrica telefonica")

elenco = dict()

while (True):
    cmd = input("comando: ")
    if (cmd == 'q'):
        break
    elif (cmd == 'h'):
        print('q per finire')
        print('h help')
        print('i inserire')
        print('l stampa tutto')
        print('s cerca nome')
        print('d elimina nome')
    elif (cmd == 'l'):
        print(elenco)
    elif (cmd == 'i'):
        nome = input("nome: ")
        num = input("numero: ")
        elenco[nome] = num
    elif (cmd == 's'):
        nome = input("nome da cercare: ")
        if nome in elenco:
            tel = elenco[nome]
            print(f"tel: {tel}")
        else:
            print("non presente")
        
    elif (cmd == 'd'):
        nome = input("nome da eliminare: ")
        if nome in elenco:
            del elenco[nome]
            print("eliminato")
        else:
            print("non presente")
    else:
        print("comando sconosciuto")
        
print("fine")