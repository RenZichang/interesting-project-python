from tkinter import *

def show():
    if a.get() == 'xtad1327114':
        La['text'] = '正确'
    else:
        La['text'] = '错误'
root = Tk()
root.title('p15_12')
La = LabelFrame(root, text = '', padx = 10, pady = 10)
La.pack(padx = 10, pady = 10)
a = StringVar()
Entry(La, textvariable = a, show = '*').pack()
b = Button(La, text = '确定', command = show)
b.pack()
root.mainloop()
