import tkinter as tk

def getMessage():
    tk.messagebox.showinfo('Attenzione', 'Ricordarsi di bagnare le piante')
    #tk.messagebox.showwarning('title', 'message')
    #tk.messagebox.showerror('title', 'message')

app = tk.Tk()
app.geometry("300x200")
app.title('Messaggi...')

bt = tk.Button(app)
bt['text'] ='1 Messaggio'
bt['command'] = getMessage
bt.pack()

app.mainloop()