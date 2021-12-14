f = open("miofile.txt", 'a')
while (True):
    txt = input("testo: ");
    if not txt:
        break
    else:
        f.write(txt+"\n")
print("end")    
f.close()
