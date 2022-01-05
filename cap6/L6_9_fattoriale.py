
def f(n):    
    if (n == 0):
        return 1
    else:
        return n * f(n-1)
    
n = 3
res = f(n)
print(f"Il fattoriale di {n}: {res}")
