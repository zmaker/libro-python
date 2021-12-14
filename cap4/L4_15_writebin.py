nomefile = 'binfile.bin'
f = open(nomefile,'wb')
num = [5, 10, 15, 20, 25]
arr = bytearray(num)
f.write(arr)
f.close()

f = open(nomefile, 'rb')
dato = f.read(1)
i = 0
while dato:
    n = int.from_bytes(dato, "big")
    print(f"{i}: {n}")
    dato = f.read(1)
    i += 1
f.close()