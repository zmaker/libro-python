import tkinter as tk

app = tk.Tk()
app.geometry("300x200")
app.title('Label con Font')

label = tk.Label(app)
label['text'] = 'Una scritta particolare!'
label['font'] = ("DieDieDie", 20)
label.pack()

label2 = tk.Label(app)
label2['text'] = 'Una scritta particolare!'
label2['font'] = ("Ubuntu", 20)
label2.pack()

app.mainloop()