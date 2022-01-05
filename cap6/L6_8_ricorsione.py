def f(n):
    print(n, end=' ')
    if (n == 0):
        return
    else:
        f(n-1)
    
f(10)