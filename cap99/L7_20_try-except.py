import time

count = 0
while (True):
    print(f"elaborazione n.: {count}")
    time.sleep(1)
    count += 1
    try:
        print(conteggio)
    except Exception as e:
        print("Tipo di errore: ", e.__class__)

