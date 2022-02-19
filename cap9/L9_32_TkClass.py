# app base

import tkinter as tk
from tkinter.messagebox import showinfo

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('OOP App')
        self.geometry('300x200')

        self.label = tk.Label(self, text='New App!')
        self.label.pack()

        self.button = tk.Button(self, text='Cliccami!')
        self.button['command'] = self.button_clicked
        self.button.pack()

    def button_clicked(self):
        showinfo(title='Information', message='Hello, Tkinter!')

if __name__ == "__main__":
    app = App()
    app.mainloop()