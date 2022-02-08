import tkinter as tk

def copia():
    str = tx1.get()
    tx2.delete(0, tk.END)
    tx2.insert(0, str)

def cancella():
    tx1.delete(0, tk.END)
    tx2.delete(0, tk.END)

app = tk.Tk()
app.geometry("300x200")
app.title('Caselle di testo')

tx1 = tk.Entry(app)
tx1.focus()
tx1.pack()

bt = tk.Button(app, text='Copia', command=copia)
bt.pack()

bt2 = tk.Button(app, text='Cancella', command=cancella)
bt2.pack()

tx2 = tk.Entry(app)
tx2.pack()


app.mainloop()


