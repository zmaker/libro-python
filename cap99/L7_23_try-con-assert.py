while True:
    try:
        n = int(input("dammi un numero: "))
        assert n != 0
    except ValueError:
        print ("non è un numero valido!")
    except AssertionError:
        print(f"r = Infinito")
    else:
        r = 100/n
        print(f"r = {r}")
    
    if n == 99:
        break      
