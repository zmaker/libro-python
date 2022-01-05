def somma(n, m):
    return n+m

def differenza(n, m):
    return n-m

def moltiplica(n, m):
    return n*m

def dividi(n, m):
    return n/m


while (True):
    print("dammi due numeri")
    a = int(input("A: "))
    b = int(input("B: "))
    op = input("operazione: +,-,*,:")
    res = 0
    
    if (op == "+"):
        res = somma(a,b)
    elif (op == "-"):
        res = differenza(a,b)
    elif (op == "*"):
        res = moltiplica(a,b)
    elif (op == ":"):
        res = dividi(a,b)
    
    print("risultato: ", res)
    
    ans = input("ancora (s/n)? ")
    if ans != 's':
        break
