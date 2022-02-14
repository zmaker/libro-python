import tkinter as tk

def sinistro(event):
    print("clic sx")
    print(event)

def destro(event):
    print("clic dx")
    print(event)

def doppioClic(event):
    print("doppio clic")
    print(event)

app = tk.Tk()
app.geometry('300x200')
bt = tk.Label(app, text="Azione!", bg='red')
bt.pack(fill=tk.BOTH, expand=True)
bt.bind('<Button-1>', sinistro)
bt.bind('<Button-2>', destro)
bt.bind('<Double-Button-1>', doppioClic)


app.mainloop()
