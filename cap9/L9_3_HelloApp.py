import tkinter as tk

def pulsantePremuto(event):
    print("Clic!")

app = tk.Tk()
app.title("Hello!")

app.geometry("300x200")

button = tk.Button(text="Vuoi un saluto?")
button.pack()
button.bind("<Button-1>", pulsantePremuto)

app.mainloop()


