while True:
    try:
        n = int(input("dammi un numero: "))
    except ValueError:
        print ("non è un numero valido!")
    else:
        r = 100/n
        print(f"r = {r}")
    
    if n == 99:
        break      
