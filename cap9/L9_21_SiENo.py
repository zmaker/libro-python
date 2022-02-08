import tkinter as tk
from tkinter.messagebox import askyesno

def chiudi():
    ans = askyesno(title='conferma', message='Vuoi uscire?')
    if ans:
        app.destroy()

app = tk.Tk()
app.geometry("300x200")
app.title('Si o no?')

bt = tk.Button(app)
bt['text'] ='Chiudi'
bt['command'] = chiudi
bt.pack()

app.mainloop()
