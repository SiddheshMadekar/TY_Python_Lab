import tkinter as tk

window = tk.Tk()

def hello():
    print("Siddhesh")

button = tk.Button(window, text="Click Me", command=hello)
button.pack()

window.mainloop()
#Siddhesh_67