testo = []

def openFile(fname):
    dati = []
    f = open(fname, 'r')
    lines = f.readlines()
    for ll in lines:
        dati.append(ll.replace('\n', ''))
    f.close()
    return dati

def saveFile(fname, dati):
    f = open(fname, 'w')
    for ll in dati:
        f.write(ll+'\n')
    f.close()
    
def displayText(dati):
    i = 0
    for el in dati:
        print(f"{i}: {el}")
        i+=1

def removeLine(dati, pos):
    if (pos < 0):
        print("?!")
    elif (pos > len(dati)-1):
        print("non esiste")
    else:
        dati.pop(pos)

print ("Editor di testi")
while True:
    line = input("> ")
    if not line:
        break
    elif line == 'o':
        fname = input("file da aprire? ")
        testo = openFile(fname)
        
    elif line == 'w':
        fname = input("file da salvare? ")
        saveFile(fname, testo)        
    
    elif line == 'l':
        displayText(testo);
        
    elif line == 'd':
        rm = int(input("linea da eliminare: "))
        removeLine(testo, rm)

    else:
        testo.append(line)
    
    


