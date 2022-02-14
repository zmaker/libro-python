import tkinter as tk

def azioneDaCompiere(event):
    print("clic")
    print(event)
    
app = tk.Tk()
app.geometry('300x200')
bt = tk.Button(app, text="Azione!")
bt.pack(fill=tk.BOTH, expand=True)
bt.bind('<Button-1>', azioneDaCompiere)
bt.bind('<Button-2>', azioneDaCompiere)

app.mainloop()