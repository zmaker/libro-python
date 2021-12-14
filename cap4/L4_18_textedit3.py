testo = []

print ("[INVIO] quit\n [l] print")
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
    else:
        testo.append(line)
    
    
