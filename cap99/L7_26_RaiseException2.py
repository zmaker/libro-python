import random

class LetturaFuoriScala(Exception):
    def __init__(self, valore, message="Valore fuori scala"):
        self.valore = valore
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.valore} è fuori dai limiti consigliati"


while True:
    val = random.randint(0,100)
    print("lettura sensore: ", val)
    if not 20 < val < 80:
        raise LetturaFuoriScala(val)
