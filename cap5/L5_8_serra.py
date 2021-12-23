import time

#letture sensori
t = 0 #temperatura
l = 0 #luce
h = 0 #umidità

#soglie per attivazioni
thr_t = 30
thr_h = 50
thr_l = 45

ACQUA = False
LUCE = False
TERMO = False

while (True):
    #leggo la temp
    t = int(input("temp: "))
    h = int(input("hum (0-100): "))
    l = int(input("luce (0-100): "))
    
    if h > 100:
        h = 100
    elif h < 0:
        h = 0

    if l > 100:
        l = 100
    elif l < 0:
        l = 0

    print(f" t: {t}°C h: {h}% l: {l}%")
    
    FLAG_T = (t > thr_t)
    FLAG_H = (h > thr_h)
    FLAG_L = (l > thr_l)
    
    print(FLAG_T)
    
    if not FLAG_T and not FLAG_H and FLAG_L:
    	LUCE = True
    if FLAG_T and not FLAG_H and not FLAG_L:
    	ACQUA = True
    if FLAG_T and not FLAG_H and FLAG_L:
    	ACQUA = True
    if FLAG_T and FLAG_H and not FLAG_L:
    	LUCE = True

    if FLAG_T:
    	TERMO = False
    else:
    	TERMO = True
                   	 
    if ACQUA:
    	print("apro valvola")
    	time.sleep(1)
    	print("chiudo valvola")
    	ACQUA = False

    if LUCE:
    	print("Accendo LUCE")
    	time.sleep(1)
    	print("Spengo LUCE")
    	LUCE = False
    
    if TERMO:
    	print("RISCALDO")
    

