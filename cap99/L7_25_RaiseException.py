import random

class LetturaFuoriScala(Exception):
    pass

while True:
    val = random.randint(0,100)
    print("lettura sensore: ", val)
    if not 20 < val < 80:
        raise LetturaFuoriScala()