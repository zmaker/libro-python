from datetime import date
from time import sleep

print("Elaborazione del giorno:")
stampaData()

while (True):
    cmd = input("comando: ")
    if not cmd:
        break;
    
    if elaborazione():
        print("Elaborazione: ok")
        stampaData()
    else:
        print("Errore!")
    
print("Fine programma")
