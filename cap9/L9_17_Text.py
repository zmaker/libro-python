import tkinter as tk

app = tk.Tk()
app.geometry("300x200")
app.title('Text')

text = tk.Text(app)
text.insert(tk.END, "Nel mezzo del cammin\n")
text.insert(tk.END, "di nostra vita\n")
text.insert(tk.END, "mi ritrovai...\n")
text['cursor'] = 'xterm'

str = text.get('2.3', '2.10')
text.insert(tk.END, str)

text.delete('3.8','3.12')

text.tag_config("mark", background="yellow", foreground="red")
text.tag_add("mark", "1.0", "1.3")

text.pack()
app.mainloop()