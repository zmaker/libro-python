import sys

def somma(a, b):
    return a + b

def diff(a, b):
    return a - b

def molt(a, b):
    return a * b

def div(a, b):
    if (b == 0):
        return 0
    else:
        return a/b


def main():
    n = len(sys.argv)
    if (n == 4):
        nome, a, op, b = sys.argv
        a = int(a)
        b = int(b)
        ret = 0
        if op == '+':
            ret = somma(a, b)
        elif op == '-':
            ret = diff(a, b)
        elif op == '*':
            ret = molt(a, b)
        elif op == ':':
            ret = div(a, b)
        print("ans = ", ret)
    else:
        print("calcolatrice")
        print("operazioni: + - * :")
        print("calc a + b")


if __name__ == "__main__":
    main()



