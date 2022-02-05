import tkinter as tk

def handle_click(event):
    n = nome.get()
    msg["text"] = "Ciao, " + n + "!"

app = tk.Tk()
app.title("Hello!")

app.geometry("300x200")

l1 = tk.Label(text="Come ti chiami?")
l1.pack()

nome = tk.Entry(width=50)
nome.pack()

button = tk.Button(text="Premi qui!")
button.pack()
button.bind("<Button-1>", handle_click)

msg = tk.Label(text="")
msg.pack()

app.mainloop()




