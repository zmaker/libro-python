class Calc:
    def __init__(self):
        self.result = 0
        
    def setOperando1(self, operando1):
        self.operando1 = int(operando1)
        
    def setOperando2(self, operando2):
        self.operando2 = int(operando2)
    
    def setOperazione(self, operazione):
        self.operazione = operazione
    
    def calcola(self):
        if (self.operazione == '+'):
            self.result = self.operando1 + self.operando2
        elif (self.operazione == '-'):
            self.result = self.operando1 - self.operando2 
        elif (self.operazione == 'x'):
            self.result = self.operando1 * self.operando2
        elif (self.operazione == '/'):
            self.result = self.operando1 / self.operando2 

    def getResult(self):
        self.calcola()
        return self.result

    def __str__(self):
        return f"{self.operando1} {self.operazione} {self.operando2} = {self.result}"

if __name__ == "__main__":
    print("non eseguibile")
