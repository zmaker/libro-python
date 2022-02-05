import tkinter as tk

app = tk.Tk()
app.geometry("300x200")
app.title('Pulsanti')

bt = tk.Button(app, text='OFF')
bt['state'] = 'disabled'
bt.pack()

bt2 = tk.Button(app, text='ON')
bt2['state'] = 'active'
bt2.pack()


app.mainloop()

