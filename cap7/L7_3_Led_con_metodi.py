class Led:
    marca = "ledbright"
    def __init__(self, coloreLed):
        self.colore = coloreLed
        self.stato = "off"

    def accendi(self):
        self.stato = "on"
    
    def spegni(self):
        self.stato = "off"
        

led1 = Led("rosso")
led1.accendi()
print(led1.marca, led1.colore, led1.stato)
led1.spegni()
print(led1.marca, led1.colore, led1.stato)

