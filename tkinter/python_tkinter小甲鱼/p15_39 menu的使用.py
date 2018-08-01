from tkinter import *


def show():
    print("Here I am, and you've called me.")

root = Tk()
root.geometry("300x150")
root.title('this is a test')
firstmenu = Menu(root, tearoff = True)
filemenu = Menu(firstmenu, tearoff = False)
filemenu.add_command(label = "第一个", command = show)
filemenu.add_command(label = "第二个", command = show)
filemenu.add_command(label = "第三个", command = show)
filemenu.add_command(label = "第四个", command = root.quit)
firstmenu.add_cascade(label = "filemenu", menu = filemenu)
root.config(menu = firstmenu)
secondmenu = Menu(firstmenu, tearoff = False)
filemenu.add_cascade(label = '叠加菜单', menu = secondmenu)
secondmenu.add_command(label = '第1个', command = show)
secondmenu.add_command(label = '第2个', command = show)
root.mainloop()

"""
Menu(window, tearoff)——创建一个window上菜单，
    window可以是窗口，也可以是另一个menu
menuob.add_command(label = '...', command = function)——在menuob上增添
    一个命令，标签是label，函数是command
root.add_cascade(label = '...', menu = menuob)——使root上的menuob生效，
    而root必须是menu，否则应该使用root.config()
"""

'''
加帘子，用Menu(target, tearoff)
加项目，用target.add_command(label, command)
使菜单中的菜单生效，用bigMenu.add_cascade(label, insideMenu)
使菜单栏生效，用root.config(menu)
'''
