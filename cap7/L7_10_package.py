from mypack.matematica.operazioni import somma
from mypack.saluti.hello import saluta

def main():
    #richiamo le funzioni del modulo
    saluta("Paolo")
    
    s = somma(10, 20)
    print(f"somma= {s}")
    pass

if __name__ == "__main__":
    main()
