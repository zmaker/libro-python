A = [0,1,0,1,0,1,0,1]
B = [0,0,1,1,0,0,1,1]
C = [0,0,0,0,1,1,1,1]

print('A B C | O ')
print('------|---')

for i in range(len(A)):
    ris = ( (bool(A[i]) and not bool(C[i]) ) and (not bool(B[i]) and bool(A[i])))
    print(f"{A[i]} {B[i]} {C[i]} | {int(ris)}")
