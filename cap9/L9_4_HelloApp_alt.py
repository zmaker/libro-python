import tkinter as tk

def pulsantePremuto():
    print("Clic!")

app = tk.Tk()
app.title("Hello!")

app.geometry("300x200")

button = tk.Button(text="Vuoi un saluto?", command = pulsantePremuto)
button.pack()

app.mainloop()


