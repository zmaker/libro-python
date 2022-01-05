import random
import time

n = random.randint(0, 40)
print(f"Punto iniziale: {n}")
    
while True:
    n += random.randint(-3, 3)
    
    if n < 0:
    	n = 0
    if n >= 40:
    	n = 40
   	 
    print(n)
    time.sleep(1)

