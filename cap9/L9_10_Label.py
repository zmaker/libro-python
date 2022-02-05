import tkinter as tk

app = tk.Tk()
app.geometry("300x200")

l1 = tk.Label(app)
l1['text'] = 'ok'
l1['height'] = 30
l1['width'] = 200
l1['foreground'] = 'red'
l1['background'] = 'gray'
l1['relief'] = 'ridge'
l1['borderwidth'] = 10

l1.pack()

app.mainloop()





