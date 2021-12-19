testo = []

print ("Editor di testi")
while True:
    line = input("> ")
    if not line:
        break
    elif line == 'o':
        testo = []
        #open file
        f = open("documento.txt", 'r')
        lines = f.readlines()
        for ll in lines:
            testo.append(ll.replace('\n', ''))
        f.close()
        
    elif line == 'w':
        #write file
        f = open("documento.txt", 'w')
        for ll in testo:
            f.write(ll+'\n')
        f.close()    
    
    elif line == 'l':
        i = 0
        for el in testo:
            print(f"{i}: {el}")
            i+=1
    elif line == 'd':
        rm = int(input("linea da eliminare: "))
        if (rm < 0):
            print("?!")
        elif (rm > len(testo)-1):
            print("non esiste")
        else:
            testo.pop(rm)
    else:
        testo.append(line)
    
    

