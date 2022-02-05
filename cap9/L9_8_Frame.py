import tkinter as tk

app = tk.Tk()
app.geometry("300x200")

fr1 = tk.Frame(app)
fr1['borderwidth'] = 10
fr1['relief'] = 'ridge'
fr1.pack()

fr2 = tk.Frame(app)
fr2['borderwidth'] = 10
fr2['relief'] = 'ridge'
fr2.pack()

bt1 = tk.Button(fr1, text="OK")
bt1.pack()

bt2 = tk.Button(fr2, text="Cancel")
bt2.pack()

app.mainloop()




