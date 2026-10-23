import tkinter as tk

window = tk.Tk()

var = tk.IntVar()

def check():
    if var.get() == 1:
        label.config(text="Selected")
    else:
        label.config(text="Not Selected")

check = tk.Checkbutton(
    window,
    text="Python",
    variable=var,
    command=check
)
check.pack()

label = tk.Label(window, text="")
label.pack()

window.mainloop()
#Siddhesh_67