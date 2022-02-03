from sys import argv
from L8_11_calclib import Calc

def main():
    parms = argv

    if not len(parms) == 4:
        print("parametri non corretti! usare: calc a + b")
    else:
        mycalc = Calc()
        mycalc.setOperando1(parms[1])
        mycalc.setOperando2(parms[3])
        mycalc.setOperazione(parms[2])
        v = mycalc.getResult()
        print(mycalc)

if __name__ == "__main__":
    main()
