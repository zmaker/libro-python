#esempio con maschera semplice
eta = 25
print(f"John ha {eta} anni")

#operazioni nella maschera 
h = 10
l = 5
print(f"Area del triangolo= {(h*l)/2}")

#definizione alternativa
txt = "Il tempo di volo è di {} ore"
t = 4
print(txt.format(t))

#uso di più parametri
t = 8
h = 7000
txt = "Il tempo di volo è di {} ore e la quota di {} m"
print(txt.format(t, h))

