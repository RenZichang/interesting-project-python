from tkinter import *
from tkinter import messagebox


    #常量
firstPosition = (20, 20)
boxWidth = 35
pieceSizeR = 15
#维护矩阵，元素-1表示空，1表示黑棋，0表示白棋
board = []
for i in range(15):
    l = []
    for j in range(15):
        l.append(-1)
    board.append(l)
#悔棋数组
regret = []
#黑棋白棋轮换变量
judge = True


    #函数
def warning():
    messagebox.showwarning(title = '非法操作', message = '你不能在这里放置棋子！')
#绘制棋子；接受矩阵行列元组，按照棋盘行列绘制棋子
def drawPiece(matrixPosition):
    x = matrixPosition[0]
    y = matrixPosition[1]
    if judge:
        color = 'black'
    else:
        color = 'white'
    row = firstPosition[0] + y * boxWidth
    column = firstPosition[1] + x * boxWidth
    piece = chessboardCanvas.create_oval(row - pieceSizeR, column - pieceSizeR, row + pieceSizeR, column + pieceSizeR, fill = color)
    regret.append((x, y, piece))
#解析鼠标事件，包括边界检测， 返回矩阵行列元组
def eventAnalize(event):
    x = int(round((event.y - firstPosition[1]) / boxWidth, 0))
    if x < 0:
        x = 0
    elif x > 14:
        x = 14
    y = int(round((event.x - firstPosition[0]) / boxWidth, 0))
    if y < 0:
        y = 0
    elif y > 14:
        y = 14
    return (x, y)
#放置棋子，接受矩阵行列元组或event对象
def putPiece(event):
    global judge
    #边界处理
    if type(event) != tuple:
        matrixPosition = eventAnalize(event)
    else:
        matrixPosition = event
    x = matrixPosition[0]
    y = matrixPosition[1]
    if board[x][y] != -1:
        warning()
        return
    board[x][y] = int(judge)
    drawPiece(matrixPosition)
    whetherNewGame = judgeWin(matrixPosition)
    if not whetherNewGame:
        judge = not judge
    else:
        return
#赢和输的界面
def winOrLose(win):
    if win:
        text = '您已赢得比赛^_^，是否继续新局？'
    else:
        text = '您不幸输掉了T_T，是否继续新局？'
    tempJudge = messagebox.askquestion(title = '五子棋', message = text)
    if tempJudge == "yes":
        newGame()
        return True
#判断输赢函数
def judgeWin(matrixPosition):
    #判断正斜线是否五子
    x = matrixPosition[0]
    y = matrixPosition[1]
    sum = 0
    while 0 <= x <= 14 and 0 <= y <= 14 and board[x][y] == judge:
        x -= 1
        y -= 1
        sum += 1
    x = matrixPosition[0]; x += 1
    y = matrixPosition[1]; y += 1
    while 0 <= x <= 14 and 0 <= y <= 14 and board[x][y] == judge:
        x += 1
        y += 1
        sum += 1
    if sum >= 5:
        return winOrLose(True)
    #判断反斜线是否五子
    x = matrixPosition[0]
    y = matrixPosition[1]
    sum = 0
    while 0 <= x <= 14 and 0 <= y <= 14 and board[x][y] == judge:
        x -= 1
        y += 1
        sum += 1
    x = matrixPosition[0]; x += 1
    y = matrixPosition[1]; y -= 1
    while 0 <= x <= 14 and 0 <= y <= 14 and board[x][y] == judge:
        x += 1
        y -= 1
        sum += 1
    if sum >= 5:
        return winOrLose(True)
    #判断横向是否五子
    x = matrixPosition[0]
    y = matrixPosition[1]
    sum = 0
    while 0 <= x <= 14 and 0 <= y <= 14 and board[x][y] == judge:
        x += 1
        sum += 1
    x = matrixPosition[0]; x -= 1
    while 0 <= x <= 14 and 0 <= y <= 14 and board[x][y] == judge:
        x -= 1
        sum += 1
    if sum >= 5:
        return winOrLose(True)
    #判断纵向是否五子
    x = matrixPosition[0]
    y = matrixPosition[1]
    sum = 0
    while 0 <= x <= 14 and 0 <= y <= 14 and board[x][y] == judge:
        y += 1
        sum += 1
    y = matrixPosition[1]; y -= 1
    while 0 <= x <= 14 and 0 <= y <= 14 and board[x][y] == judge:
        y -= 1
        sum += 1
    if sum >= 5:
        return winOrLose(True)
#初始化棋盘
def initBoard():
    for i in range(15):
        row = firstPosition[0] + i * boxWidth
        column = firstPosition[1]
        l = 14 * boxWidth
        chessboardCanvas.create_line(row, column, row, column + l, fill = 'black')
    for i in range(15):
        row = firstPosition[0]
        column = firstPosition[1] + i * boxWidth
        l = 14 * boxWidth
        chessboardCanvas.create_line(row, column, row + l, column, fill = 'black')
    chessboardCanvas.create_rectangle(7 * boxWidth - 3 + firstPosition[0], 7 * boxWidth - 3 + firstPosition[1], 7 * boxWidth + 3 + firstPosition[0], 7 * boxWidth + 3 + firstPosition[1], fill = 'black')
    chessboardCanvas.create_rectangle(3 * boxWidth - 3 + firstPosition[0], 3 * boxWidth - 3 + firstPosition[1], 3 * boxWidth + 3 + firstPosition[0], 3 * boxWidth + 3 + firstPosition[1], fill = 'black')
    chessboardCanvas.create_rectangle(11 * boxWidth - 3 + firstPosition[0], 3 * boxWidth - 3 + firstPosition[1], 11 * boxWidth + 3 + firstPosition[0], 3 * boxWidth + 3 + firstPosition[1], fill = 'black')
    chessboardCanvas.create_rectangle(3 * boxWidth - 3 + firstPosition[0], 11 * boxWidth - 3 + firstPosition[1], 3 * boxWidth + 3 + firstPosition[0], 11 * boxWidth + 3 + firstPosition[1], fill = 'black')
    chessboardCanvas.create_rectangle(11 * boxWidth - 3 + firstPosition[0], 11 * boxWidth - 3 + firstPosition[1], 11 * boxWidth + 3 + firstPosition[0], 11 * boxWidth + 3 + firstPosition[1], fill = 'black')
#按钮大全
def newGame():
    global judge
    judge = True
    chessboardCanvas.delete(ALL)
    initBoard()
    for i in range(15):
        for j in range(15):
            board[i][j] = -1
def regretGame():
    global judge
    end = len(regret) - 1
    x = regret[end][0]
    y = regret[end][1]
    chessboardCanvas.delete(regret[end][2])
    board[x][y] = -1
    del(regret[end])
    judge = not judge
def hintGame():
    pass
#菜单大全
def soloGame():
    newGame()
def AIGame():
    pass
def comGame():
    pass
def openAuthorFile():
    messagebox.showinfo(title = "著作信息", message = "2018年7月22日于北京邮电大学\n著作人：任子昌\n版权所有，禁止一切未经允许的抄袭和改动，请勿用于商业目的\n联系方式：QQ2522465840，加好友请声明")
def showProcessing():
    messagebox.showwarning(title = "正在开发的主要项目", message = "AI对战以及联网对战")

#程序初始化
root = Tk()
root.title("五子棋")

chessMenu = Menu(root, tearoff = False)
soloGameMenu = Menu(chessMenu, tearoff = False)
soloGameMenu.add_command(label = "新局", command = soloGame)
chessMenu.add_cascade(label = "单人练习", menu = soloGameMenu)
AIGameMenu = Menu(chessMenu, tearoff = False)
AIGameMenu.add_command(label = "新局", command = AIGame)
chessMenu.add_cascade(label = "人机对战", menu = AIGameMenu)
comGameMenu = Menu(chessMenu, tearoff = False)
comGameMenu.add_command(label = "新局", command = comGame)
chessMenu.add_cascade(label = "联网对战", menu = comGameMenu)
settingMenu = Menu(chessMenu, tearoff = False)
settingMenu.add_command(label = "正在开发中...", command = showProcessing)
settingMenu.add_command(label = "关于本程序", command = openAuthorFile)
chessMenu.add_cascade(label = "设置", menu = settingMenu)
root.config(menu = chessMenu)

chessboardCanvas = Canvas(root, width = 14 * boxWidth + firstPosition[0] * 2, height = 14 * boxWidth + firstPosition[1] * 2, bg = 'pale goldenrod')
chessboardCanvas.bind("<Button-1>", putPiece)
chessboardCanvas.grid(row = 2, column = 0, rowspan = 5, columnspan = 6)
initBoard()
Button(root, text = '新局', command = newGame, bg = 'light goldenrod yellow').grid(row = 0, column = 0, columnspan = 2, sticky = NSEW)
Button(root, text = '悔棋', command = regretGame, bg = 'light goldenrod yellow').grid(row = 0, column = 2, columnspan = 2, sticky = NSEW)
Button(root, text = '提示', command = hintGame, bg = 'light goldenrod yellow').grid(row = 0, column = 4, columnspan = 2, sticky = NSEW)

root.mainloop()
