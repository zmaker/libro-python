import tkinter as tk

app = tk.Tk()

label = [['7','8','9'],['4','5','6'],['1','2','3'],['0','+','=']]

display = tk.Entry(app)
display.grid(row=0, column=0, columnspan=3)

for rw in range(4):
    app.rowconfigure(rw+1, weight=1, minsize=50)
    for cl in range(3):
        app.columnconfigure(cl, weight=1, minsize=75)
        frame = tk.Frame(app)
        frame.grid(row=rw+1, column=cl, padx=2, pady=2)
        bt = tk.Button(frame, text=label[rw][cl], width=5)
        bt.pack()

app.mainloop()
