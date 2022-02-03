class Led:
    marca = "ledbright"
    def __init__(self, coloreLed, statoLed):
        self.colore = coloreLed
        self.stato = statoLed
    
led1 = Led("rosso", "on")

print(led1.marca, led1.colore, led1.stato)