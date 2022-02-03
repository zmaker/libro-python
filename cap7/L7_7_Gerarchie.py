class Auto: 
    def __init__(self, color, year):
        self.color = color
        self.year = year

    def setSpeed(self, speed):
        self.speed = speed

    def beep(self, sound): #suona il clacson
        return f"dice: {sound}"

class Fiaz500(Auto):
    pass

class Perrari(Auto):
    pass

a = Perrari("rosso", 1983)
b = Fiaz500("gialla", 1970)

print(a.beep("ciao ciao"))
print(b.beep("bip bip"))
