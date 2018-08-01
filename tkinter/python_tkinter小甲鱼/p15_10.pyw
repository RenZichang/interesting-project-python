from tkinter import *

root = Tk()
group = LabelFrame(root, text = '最好的脚本语言是？', padx = 10, pady = 10)
group.pack(padx = 20, pady = 20)
LANGS = {('Python', 1),
         ('Lua', 2),
         ('Perl', 3),
         ('Ruby', 4)}
v = IntVar()
v.set(1)
for item in LANGS:
    Radiobutton(group, text = item[0], value = item[1], variable = v).pack(anchor = W)

mainloop()
