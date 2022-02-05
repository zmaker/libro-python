while True:
    try:
        n = int(input("dammi un numero: "))
        if n == 99:
            break
        r = 100/n
        print(f"r = {r}")
                
    except ValueError:
        print ("non è un numero valido!")
    except ZeroDivisionError:
        print(f"r = Infinito")
    except:
        print("errore imprevisto")
