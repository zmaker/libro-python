class Led:
    marca = "ledbright"
    def __init__(self, coloreLed):
        self.colore = coloreLed
        self.stato = "off"

    def accendi(self):
        self.stato = "on"
    
    def spegni(self):
        self.stato = "off"
        
    def __str__(self):
        return f"Led({self.marca}) {self.colore}: {self.stato}"
        

led1 = Led("rosso")
print(led1)


