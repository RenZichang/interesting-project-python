from tkinter import *


window = Tk()
sb = Scrollbar(window)
lb = Listbox(window, yscrollcommand = sb.set)
sb.config(command = lb.yview)

for i in range(1000):
    lb.insert(END, str(i))

lb.pack(side = RIGHT, fill = BOTH)
sb.pack(side = LEFT, fill = Y)

window.mainloop()
