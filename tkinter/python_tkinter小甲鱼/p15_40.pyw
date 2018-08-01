from tkinter import *
from tkinter import messagebox

def eventShow(event):
    print(event.x, event.y)
    if 20 <= event.x <= 180 and 20 <= event.y <= 180:
        messagebox.askokcancel(message = '是否发射核弹？')
        

root = Tk()
frame = Frame(root, width = 200, height = 200)
frame.bind("<Button-2>", eventShow)
frame.pack()
root.mainloop()
