import tkinter as tk

app = tk.Tk()
app.geometry("300x200")
app.title('Pack 3')

fr1 = tk.Frame(app, height=50)
fr1['background'] = 'blue'
fr1.pack(fill=tk.BOTH, side=tk.TOP, expand = True)

fr2 = tk.Frame(app, height=50)
fr2['background'] = 'red'
fr2.pack(fill=tk.BOTH, side=tk.TOP, expand = True)

fr3 = tk.Frame(fr2, width=40, height=50)
fr3['background'] = 'yellow'
fr3.pack(fill=tk.BOTH, side=tk.LEFT)

'''
tk.Button(fr1, text="bt1").pack()
tk.Button(fr2, text="bt2").pack()
tk.Button(fr3, text="bt3").pack()
'''
app.mainloop()
