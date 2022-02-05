# editor di testi - file principale
# editor.py

import L7_18_modeditor as edi

def main():
    testo = []
    print ("Editor di testi")
    while True:
        line = input("> ")
        if not line:
            break
        elif line == 'o':
            fname = input("file da aprire? ")
            testo = edi.openFile(fname)
            
        elif line == 'w':
            fname = input("file da salvare? ")
            edi.saveFile(fname, testo)        
        
        elif line == 'l':
            edi.displayText(testo);
            
        elif line == 'd':
            rm = int(input("linea da eliminare: "))
            edi.removeLine(testo, rm)

        else:
            testo.append(line)
    
if __name__ == "__main__":
    main()