import threading
import time

def mythread(name, wait):
    print(f"{name}: avvio")
    time.sleep(int(wait))
    print(f"{name}: ha finito")

if __name__ == "__main__":

    th = threading.Thread(target=mythread, args=('Thr1',2))
    #, daemon=True)
    print("main: avvio")
    th.start()
    
    th.join()    
    print("main: END")