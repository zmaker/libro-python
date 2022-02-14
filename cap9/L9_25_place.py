import tkinter as tk

app = tk.Tk()
app.geometry("300x200")
app.title('Posizioni assolute')

label1 = tk.Label(app, text="Nome: ", bg='#c7f9ff')
label1.place(x=10, y=10)
fld1 = tk.Entry(app, bg="#fdffc7")
fld1.place(x=90, y=10)


label2 = tk.Label(app, text="Password:", bg='#d3ffc7')
label2.place(x=10, y=40)

fld2 = tk.Entry(app, bg="#fdffc7")
fld2.place(x=90, y=40)

bt1 = tk.Button(app, text="Login")
bt1.place(x=10, y=70)


app.mainloop()
