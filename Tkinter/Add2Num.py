import tkinter as tk

window = tk.Tk()

def add():
    a = int(e1.get())
    b = int(e2.get())
    label.config(text=a + b)

e1 = tk.Entry(window)
e1.pack()

e2 = tk.Entry(window)
e2.pack()

button = tk.Button(window, text="Add", command=add)
button.pack()

label = tk.Label(window, text="")
label.pack()

window.mainloop()
#Siddhesh_67