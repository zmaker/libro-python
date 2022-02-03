class Widget:
 
    def __init__(self):
        print("Widget creato")
 
    def __del__(self):
        print("Bye bye Widget")
 
w = Widget()
del w