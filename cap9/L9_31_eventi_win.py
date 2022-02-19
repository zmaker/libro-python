import tkinter as tk
from tkinter import messagebox

def getTasto(event):
    print(event.char)

def close_win(e):
   app.destroy()
   
def show_msg(e):
   messagebox.showinfo("Hello!")

app = tk.Tk()
app.bind("<Key>", getTasto)
app.bind('<Escape>', lambda e: close_win(e))
app.bind('<Shift-Tab>', lambda e: show_msg(e))
app.bind('<Control_L>', lambda e: show_msg(e))
app.bind('<Key-A>', lambda e: show_msg(e))

app.mainloop()
