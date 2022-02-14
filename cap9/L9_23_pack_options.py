import tkinter as tk

app = tk.Tk()
app.geometry("300x200")
app.title('Pack 2')

fr1 = tk.Frame(app)
fr1['background'] = '#fdffc7'
fr1.pack(fill=tk.X, side=tk.TOP, padx=5, pady=5)

fr2 = tk.Frame(app)
fr2['background'] = '#c7f9ff'
fr2.pack(fill=tk.X, side=tk.TOP)

#componenti frame 1
bt1 = tk.Button(fr1, text="BT1")
bt1.pack( side=tk.LEFT)

bt2 = tk.Button(fr1, text="BT2")
bt2.pack( side=tk.LEFT)

bt2 = tk.Button(fr1, text="BT3")
bt2.pack( side=tk.LEFT)

#componenti frame 2
bt4 = tk.Button(fr2, text="BT4")
bt4.pack()


app.mainloop()

