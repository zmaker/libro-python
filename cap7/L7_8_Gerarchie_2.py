class Auto: 
    def __init__(self, color, year):
        self.color = color
        self.year = year

    def setSpeed(self, speed):
        self.speed = speed

    def beep(self, sound): #suona il clacson
        return f"dice: {sound}"

class Fiaz500(Auto):
    def beep(self, sound="bip!!!!!"): #suona il clacson
        return f"dice: {sound}"
    
    def doppietta(self):
        print("cambia in fretta!")

class Perrari(Auto):
    def beep(self, sound="Hooonk!!!"): #suona il clacson
        return f"dice: {sound}"


a = Perrari("rosso", 1983)
b = Fiaz500("gialla", 1970)

print(a.beep())
print(b.beep())
b.doppietta()

