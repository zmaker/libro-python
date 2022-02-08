import tkinter as tk

app = tk.Tk()
app.geometry("300x200")
app.title('RadioButton')

def getSelected():
    v = selected.get()
    lab['text'] = "hai selezionato: " + v

selected = tk.StringVar()
livelli = ('off','min','med','max')
i = 0
for lv in livelli:
    r = tk.Radiobutton(app)
    r['text'] = lv
    r['value'] = i
    i += 1
    r['variable'] = selected
    r['command'] = getSelected
    r.pack()

lab = tk.Label(app)
lab.pack()


app.mainloop()