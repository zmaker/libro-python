from L8_13_csv_reader_lib import CSV

def main():
    csv = CSV("frutta.csv")
    
    nrighe = csv.getRowsCount()
    print(f"il file contiene {nrighe} righe")

    print("Il contenuto del file:")
    print(csv)

    val = csv.getCell(1,1)
    print("la cella 1,1 = ", val)

if __name__ == "__main__":
    
    main()
