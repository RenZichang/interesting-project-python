import tkinter


def show():
    print('你好！')

window = tkinter.Tk()
window.title('p15_2')
frame = tkinter.Frame(window)
frame.pack()
btn = tkinter.Button(window, text = '打招呼', fg = 'blue', command = show)
btn.pack(side = tkinter.LEFT)
window.mainloop()
