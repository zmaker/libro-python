import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Frame App')
        self.geometry('300x200')
        
        self.container = tk.Frame(self)
        self.container.pack(fill = tk.BOTH, expand=True)

        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)

        self.page1 = Page1(self.container, self)
        self.page1.grid(row = 0, column = 0, sticky ="nsew")
        
        self.page2 = Page2(self.container, self)
        self.page2.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(0)

    def show_frame(self, n):
        if n == 0:
            self.page1.tkraise()
        elif n == 1:
            self.page2.tkraise()

class Page1(tk.Frame):
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self, parent)
        self['background'] = '#d5e1f5'
        label = tk.Label(self, text ="Page 1")
        label.pack()

        bt = tk.Button(self, text ="Page 2", command = lambda : controller.show_frame(1))
        bt.pack()

class Page2(tk.Frame):
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self, parent)
        self['background'] = '#fffed4'
        label = tk.Label(self, text ="Page 2")
        label.pack()

        bt = tk.Button(self, text ="Page 1", command = lambda : controller.show_frame(0))
        bt.pack() 

if __name__ == "__main__":
    app = App()
    app.mainloop()

