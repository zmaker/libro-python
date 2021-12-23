A = False
B = False
C = False

print("calcolo di: (A and B) or (not A and C)")

while (True):
    v = (input("A (V/F):")).upper()
    if v == 'V':
        A = True;
    v = (input("B (V/F):")).upper()
    if v == 'V':
        B = True;
    v = (input("C (V/F):")).upper()
    if v == 'V':
        C = True;

    res = (A and B) or (not A and C)
    print(f"expr = {res}")

    c = input("vuoi provare ancora (s/n)? ")
    if c == 'n':
        break
print("end")
