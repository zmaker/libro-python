import tkinter as tk

app = tk.Tk()
app.geometry("600x440")
app.title('Label con immagine')

photo = tk.PhotoImage(file='./imgs/cat.png')
label = tk.Label(app)
label['text'] = 'un gatto'
label['compound'] = 'top'
label['image'] = photo

label.pack()

app.mainloop()
