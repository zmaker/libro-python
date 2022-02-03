class Colorato():
    def __init__(self, color):
        self.color = color
 
class Forma():
    def __init__(self, l, w):
        self.l = l
        self.w = w

class Rettangolo(Forma):
    def __init__(self, l, w):
        super().__init__(l,w)

    def area(self):
        return self.l * self.w
    
    def perimetro(self):
        return 2 * (self.l + self.w)
    
class Quadrato(Rettangolo, Colorato):
    def __init__(self, l, color):   	 
        Rettangolo.__init__(self, l, l)
        Colorato.__init__(self, color)
 
    def __str__(self):
        return f"Quadrato {self.color} l = {self.l}" 

q = Quadrato(2, "rosso")
print(q.area())
print(q)

