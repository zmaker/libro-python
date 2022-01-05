from datetime import date
from time import sleep

print("Elaborazione del giorno:")
today = date.today()
yy = today.year
mm = today.month
dd = today.day
print(f"data: {dd}/{mm}/{yy}")

while (True):
    cmd = input("comando: ")
    if not cmd:
        break;
    sleep(1)
    print("Elaborazione: ok")
    today = date.today()
    yy = today.year
    mm = today.month
    dd = today.day
    print(f"data: {dd}/{mm}/{yy}") 
    
print("Fine programma")