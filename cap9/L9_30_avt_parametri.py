import tkinter as tk

def fConParametri(a, b, c):
    print(a, b, c)

app = tk.Tk()
app.geometry('300x200')
bt = tk.Button(app, command = lambda a=1, b=2, c=3: fConParametri(a, b, c))
bt.pack(fill=tk.BOTH, expand=True)

app.mainloop()

