nomefile = 'binfile.bin'
f = open(nomefile,'wb')
num = [5, 10, 15, 20, 25]
arr = bytearray(num)
f.write(arr)
f.close()

f = open(nomefile, 'rb')
dati = f.read()
print(dati)
f.close()
