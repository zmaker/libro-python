import tkinter as tk

def pulsantePremuto(event):
    msg.delete(0, tk.END)
    msg.insert(0, "Ciao!")

app = tk.Tk()
app.title("Hello!")

app.geometry("300x200")

button = tk.Button(text="Vuoi un saluto?")
button.pack()
button.bind("<Button-1>", pulsantePremuto)

msg = tk.Entry(width=50)
msg.pack()

app.mainloop()



