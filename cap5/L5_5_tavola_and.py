A = [0,1,0,1]
B = [0,0,1,1]

print("A B | O")
print("-------")
for i in range(4):
    O = A[i] and B[i]
    print(f"{A[i]} {B[i]} | {O}")
