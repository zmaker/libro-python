import sys

def main():
    n = len(sys.argv)
    if (n == 3):
        nome, primo, secondo = sys.argv
        print(f"1: {primo}")
        print(f"2: {secondo}")
    else:
        print("questo programma richiede 2 parametri")


if __name__ == "__main__":
    main()


