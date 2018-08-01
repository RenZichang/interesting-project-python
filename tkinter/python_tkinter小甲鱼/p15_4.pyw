import tkinter as tk

window = tk.Tk()
window.title('p15_4')
photo = tk.PhotoImage(file = 'spider.gif')
label = tk.Label(window,
                 text = '第一个\n混合模式',
                 justify = tk.LEFT,
                 image = photo,
                 compound = tk.CENTER,
                 font = ('楷体', 20),
                 fg = 'white'
                 )
label.pack(side = tk.LEFT)
window.mainloop()
