import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Frame App')
        self.geometry('300x200')

class MainFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self['background'] = '#ccccff'
        
        self.label = tk.Label(self, text='Frame')
        self.label.pack()

        self.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = App()
    frame = MainFrame(app)
    app.mainloop()
