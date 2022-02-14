import tkinter as tk

app = tk.Tk()
app.geometry("300x200")
app.title('Griglia')


for riga in range(3):
    app.rowconfigure(riga, weight=1, minsize=20)
    for col in range(3):
        app.columnconfigure(col, weight=1, minsize=50)
        fr = tk.Frame(app, bg='red')
        fr.grid(row=riga, column=col, sticky='nsew')

        bt = tk.Button(fr, text=f"R:{riga}\nC:{col}")
        bt.pack(expand=True, fill=tk.BOTH)

app.mainloop()

