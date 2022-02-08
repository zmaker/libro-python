import tkinter as tk

app = tk.Tk()
app.geometry("300x200")
app.title('CheckBox')

def leggiValore():
    v = scelta.get()
    lab['text'] = v
    print(v)

chk = tk.Checkbutton(app, command=leggiValore)
chk['text'] = 'Accetto le condizioni'
scelta = tk.StringVar()
chk['variable'] = scelta
chk['onvalue'] = 'OK'
chk['offvalue'] = 'KO'
chk['state'] = 'active'

chk.pack()

lab = tk.Label(app);
lab.pack()

app.mainloop()
