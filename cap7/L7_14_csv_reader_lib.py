import os.path

class CSV:
    def __init__(self, filename):
        self.filename = filename
        #se il file esiste, lo apro
        if os.path.isfile(self.filename):
            self.file = open(self.filename)
            self.lines = list()
            self.rows = 0
            
            line = self.file.readline()
            self.lines.append(Row(line))
            while line:
                line = self.file.readline() 
                self.lines.append(Row(line))
        else:
            print ("File non trovato!")

    def getRowsCount(self):
        return len(self.lines)

    def getCell(self, r, c):
        rw = self.getRow(r)
        c = rw.getCell(c)
        return c.getValue()

    def getRow(self, n):
        return self.lines[n]

    def __str__(self):
        txt = f"CSV File - {self.filename}\n"
        for r in self.lines:
            txt += str(r)
        return txt

class Row:
    def __init__(self, txt):
        items = txt.split(sep=",")
        self.cellnum = 0
        self.cells = []
        for el in items:
            self.cells.append(Cell(el))
            self.cellnum += 1

    def getCell(self, n):
        return self.cells[n]

    def __str__(self):
        txt = ""
        for el in self.cells:
            txt += str(el)
        return txt + "\n"

class Cell:
    def __init__(self, txt):
        self.value = txt.strip().replace('\n','')
    
    def getValue(self):
        return self.value
    
    def __str__(self):
        x = self.value.ljust(12)
        return x


if __name__ == "__main__":
    print("CSV reader lib - non eseguibile")
