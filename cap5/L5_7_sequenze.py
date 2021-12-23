a = False;
b = False;
c = False;
for i in range(8):
    print(f"{i}: {int(a)} {int(b)} {int(c)}")
    a = not a
    if (i%2 == 1):
        b = not b
    if (i%4 == 3):
        c = not c