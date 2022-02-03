import L7_16_modrubrica as rub

def main():
    LOOP = True
    rubrica = dict()

    print("Rubrica elettronica")
    while (LOOP):
        cmd = input("comando? ") 
        if cmd == 'q':
            LOOP = rub.esci()
        elif cmd == 'a':
            rub.aggiungi(rubrica)
        elif cmd == 'l':
            rub.stampa(rubrica)
        elif cmd == 'm':
            rub.modifica(rubrica)

if __name__ == "__main__":
    main()
