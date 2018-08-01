from tkinter import *


def Plus():
    try:
        firstNum = eval(entStringFirst.get())
        secondNum = eval(entStringSecond.get())
        ans = str(firstNum + secondNum)
    except:
        ans = 'Invalid input'
    entAnswerString.set(ans)

def Minus():
    try:
        firstNum = eval(entStringFirst.get())
        secondNum = eval(entStringSecond.get())
        ans = str(firstNum - secondNum)
    except:
        ans = 'Invalid input'
    entAnswerString.set(ans)

def Times():
    try:
        firstNum = eval(entStringFirst.get())
        secondNum = eval(entStringSecond.get())
        ans = str(firstNum * secondNum)
    except:
        ans = 'Invalid input'
    entAnswerString.set(ans)

def Divides():
    try:
        firstNum = eval(entStringFirst.get())
        secondNum = eval(entStringSecond.get())
        ans = str(firstNum / secondNum)
    except:
        ans = 'Invalid input'
    entAnswerString.set(ans)

window = Tk()
window.title("Calculator by Ren Zichang")

btnPlus = Button(window, text = '＋', command = Plus)
btnMinus = Button(window, text = '－', command = Minus)
btnTimes = Button(window, text = '×', command = Times)
btnDivides = Button(window, text = '÷', command = Divides)

btnPlus.grid(row = 0, column = 1, sticky = NSEW)
btnMinus.grid(row = 1, column = 1, sticky = NSEW)
btnTimes.grid(row = 2, column = 1, sticky = NSEW)
btnDivides.grid(row = 3, column = 1, sticky = NSEW)

entStringFirst = StringVar()
entStringSecond = StringVar()
entFirst = Entry(window, textvariable = entStringFirst)
entSecond = Entry(window, textvariable = entStringSecond)

entFirst.grid(row = 0, column = 0, sticky = NSEW, padx = 10, pady = 5)
entSecond.grid(row = 0, column = 2, sticky = NSEW, padx = 10, pady = 5)

lbl = Label(window, text = '=')
lbl.grid(row = 0, column = 3, sticky = W)

entAnswerString = StringVar()
entAnswer = Entry(window, textvariable = entAnswerString, state = 'readonly')
entAnswer.grid(row = 0, column = 4, sticky = NSEW)

window.mainloop()
