import tkinter as tk
import time

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Thread App')
        self.geometry('300x200')

        self.button = tk.Button(self, text='Start')
        self.button['command'] = self.doWork
        self.button.pack()
        
        self.txt = tk.Label()
        self.txt.pack()
        
    def doWork(self):
        self.button['state'] = 'disabled'        
        for i in range(10):
            self.txt["text"] = str(i)
            time.sleep(1)
        self.txt["text"] = "Terminato"
        self.button['state'] = 'active'

if __name__ == "__main__":
    app = App()
    app.mainloop()
