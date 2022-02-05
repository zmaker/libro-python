import tkinter as tk

app = tk.Tk()
app.geometry("300x200")

fr = tk.Frame()
fr['width'] = 200
fr['height'] = 100
fr['borderwidth'] = 2
fr['relief'] = 'ridge'
fr['background'] = '#01906A'

fr.pack()
app.mainloop()



