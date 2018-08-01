import tkinter as tk


def show():
    if [i.get() for i in v] == [1, 1, 0, 0, 1]:
        stringVariable.set('正确')
    else:
        stringVariable.set('错误')

window = tk.Tk()
window.title('请选出最好用的语言')

v = []
l = ['python', 'c++', 'java', 'lua', 'php']

for item in l:
    v.append(tk.IntVar())
    b = tk.Checkbutton(window, text = item, variable = v[-1])
    b.pack(side = tk.LEFT)

stringVariable = tk.StringVar()
lab = tk.Entry(window, textvariable = stringVariable, state = 'readonly')

btn = tk.Button(window, text = '确定', command = show)

lab.pack(side = tk.LEFT)
btn.pack(side = tk.LEFT)

window.mainloop()
