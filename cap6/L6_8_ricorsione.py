def f(n):
    print(n, end=' ')
    if (n > 0):
        return f(n-1)
    else:
        return 0
    
f(10)