from tkinter import Tk, Label, Button, StringVar, Entry, LEFT
from time import sleep
#main
def show1(event):
    if btn1['text'] == '不是':
        btn1['text'], btn2['text'] = btn2['text'], btn1['text']
        btn1['bg'], btn2['bg'] = btn2['bg'], btn1['bg']
        btn1['fg'], btn2['fg'] = btn2['fg'], btn1['fg']
    else:
        pass

def show2(event):
    if btn2['text'] == '不是':
        btn1['text'], btn2['text'] = btn2['text'], btn1['text']
        btn1['bg'], btn2['bg'] = btn2['bg'], btn1['bg']
        btn1['fg'], btn2['fg'] = btn2['fg'], btn1['fg']
    else:
        pass

def show():
    printString.set('我也这么认为')

root = Tk()
root.title("小测验")

lbl = Label(root, text = '你是不是SB', width = 50)
lbl.grid(row = 0, column = 1, columnspan = 3, padx = 20, pady = 10)

btn1 = Button(root, text = '当然是', bg = 'light blue', fg = 'blue', command = show, width = 10)
btn1.bind('<Enter>', show1)
btn2 = Button(root, text = '不是', bg = 'pink', fg = 'red', command = show, width = 10)
btn2.bind('<Enter>', show2)
btn1.grid(row = 2, column = 0, columnspan = 2, padx = 10, pady = 5)
btn2.grid(row = 2, column = 3, columnspan = 2, padx = 10, pady = 5)

printString = StringVar()
printString.set('')
ent = Entry(root, textvariable = printString, state = 'readonly', width = 20)
ent.grid(padx = 5, pady = 5, row = 2, column = 2)

root.mainloop()

#next
judge = True

def no_exit():
    global judge
    judge = False
    if j != 0:
        printString_.set('所以你确实是SB，虽然有' + str(j) + '次不想承认')
    else:
        printString_.set('很诚实，我看好你哦')
j = -1
while judge:
    j += 1
    window = Tk()
    window.title('XD')

    lbl_ = Label(window, text = '关了也不能改变不了你是SB的事实', justify = LEFT)
    lbl_.grid(row = 0)

    btn_ = Button(window, text = "你说得对", command = no_exit)
    btn_.grid(row = 2)

    printString_ = StringVar()
    ent_ = Entry(window, textvariable = printString_, state = 'readonly', width = 50)
    ent_.grid(padx = 5, pady = 5, row = 3)
    window.mainloop()
#final
judge = True
sleep(2)
def exit():
    global judge
    judge = False
    if i != 0:
        printString_.set('警告！你刚才点了' + str(i) + '次退出！已创建' + str(i) + '个病毒文件！')
        for count in range(i):
            with open('惩罚X' + str(count + 1), 'w+') as f:
                f.write('期待看到更多精彩内容，请到\nhttps://download.csdn.net/download/qq_40761869/10484372\n下载文件，支持一下哦！')
    else:
        printString_.set('你真是我的小迷弟！')
i = -1
while judge:
    i += 1
    window = Tk()
    window.title('XD')

    lbl_ = Label(window, text = '最后再皮一下XD', justify = LEFT)
    lbl_.grid(row = 0)

    btn_ = Button(window, text = "作者真可爱", command = exit)
    btn_.grid(row = 2)

    printString_ = StringVar()
    ent_ = Entry(window, textvariable = printString_, state = 'readonly', width = '50')
    ent_.grid(padx = 5, pady = 5, row = 3)
    window.mainloop()
