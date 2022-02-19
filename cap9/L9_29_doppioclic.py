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

def tastoInvio(event):
    print("Invio")
    print(event)

def printKey(event):
    print("Print")
    print(event)
    
def posizione(event):
  print(f"Posizione: {event.x}, {event.y}")

app = tk.Tk()
app.geometry('300x200')
bt = tk.Button(app, text="Azione!")
bt.pack(fill=tk.BOTH, expand=True)
bt.bind('<Button-1>', sinistro)
bt.bind('<Button-2>', destro)
bt.bind('<Double-Button-1>', doppioClic)
bt.bind('<Motion>',posizione)
bt2 = tk.Button(app, text="Bt2!", bg='yellow')
bt2.focus()
bt2.pack(fill=tk.BOTH, expand=True)
bt2.bind('<Return>', tastoInvio)
bt2.bind('<Return>', printKey, add='+')


app.mainloop()
