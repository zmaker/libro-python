class Automobile:
    marca = "supercar"
    
    def __init__(self, colore, targa):
        self.colore = colore
        self.targa = targa
        self.carburante = 0
        self.x = 0
        
    def addCarburante(self):
        self.carburante += 1
        if (self.carburante > 10):
            self.carburante = 10
            
    def marcia(self):
        if (self.carburante > 0):
            self.x += 1
            self.carburante -= 1
            return True
        else:
            return False
        
    def getCarburante(self):
        return self.carburante
    
    def __str__(self):
        return f"{self.targa}: pos:{self.x} fuel:{self.carburante}"

car = Automobile("rossa", "BC313")
print(car)
print("rifornimento")
for i in range(10):
    car.addCarburante()
print(car)
print("partiamo")
while car.marcia():
    print(car)


        