from tkinter import *

root = Tk() 
root.title('选择题')

def show():
    if v.get() == 4:
        l['text'] = '正确'
    else:
        l['text'] = '错误'
l = Label(root)
l.pack()
v = IntVar()
Radiobutton(text = '任子昌很帅',
            variable = v,
            value = 1,
            command = show,
            indicator = False,
            width = 50).pack(anchor = W)
Radiobutton(text = '任子昌最帅',
            variable = v,
            value = 2,
            command = show,
            indicator = False,
            width = 50).pack(anchor = W)
Radiobutton(text = '任子昌超级帅',
            variable = v,
            value = 3,
            command = show,
            indicator = False,
            width = 50).pack(anchor = W)
Radiobutton(text = '任子昌世界第一帅',
            variable = v,
            value = 4,
            command = show,
            indicator = False,
            width = 50).pack(anchor = W)
