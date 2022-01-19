from sys import argv

def main():
    if len(argv) > 1:
        nome = argv[1]
   
        print("ciao,", nome)
    else:
        print("ciao!")

if __name__ == "__main__":
    main()
