import tkinter as tk
import time

class Splash(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Splash")
        self.geometry("200x200")
        
        img = tk.PhotoImage(file = "splash.png") # insert file name to be display
        lab = tk.Label(self, image = img)         # create label
        lab.pack()

        self.update()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Painter App')
        self.geometry('400x300')
        
        self.withdraw()
        splash = Splash(self)

        ## simulate a delay while loading
        time.sleep(2)

        ## finished loading so destroy splash
        splash.destroy()

        ## show window again
        self.deiconify()
        
        #componenti
        
        #pulsanti
        self.rowconfigure(0, weight=20)
        self.columnconfigure(0, weight=1)
        toolbar = tk.Frame(self)
        toolbar.grid(row=0, column=0, sticky='nswe')
        tk.Button(toolbar, text="+", command=self.plusSize).pack(side=tk.LEFT, padx=1)
        tk.Button(toolbar, text="-", command=self.minusSize).pack(side=tk.LEFT, padx=1)
        
        #canvas
        self.rowconfigure(1, weight=80)
        self.columnconfigure(0, weight=1)
        self.canva = tk.Canvas(self, bg='white')
        self.canva.grid(row=1, column=0, sticky='nswe')
        
        #disegno
        self.px = None
        self.py = None
        self.canva.bind('<B1-Motion>', self.draw)
        self.canva.bind('<ButtonRelease-1>', self.stopDraw)
        
        self.size = 2
                        
    def plusSize(self):
        self.size += 1
        
    def minusSize(self):
        if (self.size > 1):
            self.size -= 1
            
    def draw(self, event):
        if self.px and self.py:
            self.canva.create_line(self.px, self.py, event.x, event.y,
                               width=self.size, fill='black')
        self.px = event.x
        self.py = event.y

    def stopDraw(self, event):
        self.px = None
        self.py = None

if __name__ == "__main__":
    app = App()
    app.mainloop()

