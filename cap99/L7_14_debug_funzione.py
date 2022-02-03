def sum(A, B):
    S = A + B
    return S

C = 0
M = int(input("quante ripetizioni? "))
if M <= 0:
    M = 1
while (C < M):
    x = sum(C, 10)
    print(x)
    C += 1
print("end")

