#convertitore per inch/cm

import tkinter as tk
from tkinter.messagebox import showinfo

class Logic():
    def inch2cm(self, inch):
        n = 0
        try:
            n = float(inch) * 2.54
        except:
            n = 0
        return "{:.1f}".format(n)

    def cm2inch(self, cm):
        n = 0
        try:
            n = float(cm) / 2.54
        except:
            n = 0
        return "{:.1f}".format(n)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title('inch converter App')
        self.geometry('300x200')
        frame = MainFrame(self)


class MainFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=2)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        #riga 1
        self.label = tk.Label(self, text='Convertitore pollici / cm')
        self.label.grid(column=0, row=0, columnspan=4)

        #riga 2
        tk.Label(self, text='pollici:').grid(column=0, row=1)

        self.vInch = tk.StringVar()
        self.txPollici = tk.Entry(self, width=4)
        self.txPollici.grid(column=1, row=1)
        self.txPollici['textvariable'] = self.vInch
        self.txPollici.focus()

        tk.Label(self, text='cm:').grid(column=2, row=1)

        self.vCm = tk.StringVar()
        self.txCm = tk.Entry(self, width=5)
        self.txCm.grid(column=3, row=1)
        self.txCm['textvariable'] = self.vCm

        #riga 3
        self.bt1 = tk.Button(self, text="inch->cm")
        self.bt1.grid(column=0, row=2, columnspan=2)
        self.bt1['command'] = self.inch2cm

        self.bt2 = tk.Button(self, text="cm->inch")
        self.bt2.grid(column=2, row=2, columnspan=2)
        self.bt2['command'] = self.cm2inch

        #aggiungo il frame
        self.pack()
        
        self.logic = Logic()

    def inch2cm(self):
        self.vCm.set(self.logic.inch2cm(self.vInch.get()))


    def cm2inch(self):
        self.vInch.set(self.logic.cm2inch(self.vCm.get()))


if __name__ == "__main__":
    app = App()
    app.mainloop()