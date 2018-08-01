from tkinter import*
from tkinter import messagebox
from tkinter import filedialog
import socket
import threading
import os
import re



friendAddr = ''
friendPort = ''
friendSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddr = ''
serverPort = ''
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
filePath = ''
safety = True


#所有的状态码
# &f:发送文件请求
# &y:同意接收
# &n:拒绝接收
# &e:文件传输结束
#监听函数与进程，无限循环，直到对方断开连接，负责处理各种对方的响应，包括文件发送请求和普通信息请求
def receive():
    global safety
    while True:
        try:
            friendInfo = friendSock.recv(1024)
            #对于接收方来说，收到&f意味着要做出决定，是否接收？
            if friendInfo == b'&f':
                fileAccept = messagebox.askyesno(title="文件接收请求", message="对方请求发送文件，是否接收？")
                #如果接收，就应该开始准备迎接文件了
                if fileAccept:
                    #发送确认信息
                    friendSock.send(b'&y')
                    #说明自己正在等待
                    t = threading.Thread(target=listB.insert, args=(0, '-' * 25 + "正在传输" + '-' * 25))
                    t.setDaemon(True)
                    t.start()
                    #接收来自对面的 文件数据、文件传输处理数据
                    fileName = friendSock.recv(1024)#首先是文件名
                    file = open("fileRecv/" + fileName.decode("utf-8"), 'wb')
                    fileInfo = friendSock.recv(1024)#然后是文件内容
                    while fileInfo != b'&e':
                        file.write(fileInfo)
                        fileInfo = friendSock.recv(1024)
                    file.close()
                    listB.insert(0, '-' * 25 + "传输完成" + '-' * 25)
                #如果拒绝，就很简单，直接发送拒绝信息即可
                else:
                    listB.insert(0, '-' * 25 + "传输已拒绝" + '-' * 25)
                    friendSock.send(b'&n')
            #对于发送方来说，一般是不会凭空接收到&y和&n的，一旦接收到，一般是自己的熊孩子函数sendFile发送了文件请求，剩下的事需要自己来处理
            #接收到了&y，就直接发送文件好了，sendFile函数应该已经给弄好了                  
            elif friendInfo == b'&y':
                listB.insert(0, '-' * 25 + "开始传输" + '-' * 25)
                fileName = filePath.split('/')[-1]
                friendSock.send(bytes(fileName, encoding = 'utf-8'))#文件名
                f = open(filePath, "rb")
                while True:
                    fileCon = f.readline(1024)
                    if fileCon == b'':
                        break
                    friendSock.send(fileCon)#文件内容
                f.close()
                friendSock.send(b"&e")
                listB.insert(0, '-' * 25 + "传输完毕" + '-' * 25)
            #接收到了&n，就说明对方拒绝了自己sendFile这个熊孩子，默不作声就行了
            elif friendInfo == b'&n':
                listB.insert(0, '-' * 25 + "对方拒绝接收" + '-' * 25)
            #普通对话信息
            else:
                listB.insert(0, "--" + friendInfo.decode("utf-8"))
        except ConnectionResetError:
            stateInfo.set('对方已下线！')
            break
    safety = True
receiveThread = threading.Thread(target=receive)
receiveThread_t = threading.Thread(target=receive)
receiveThread.setDaemon(True)
receiveThread_t.setDaemon(True)
#等待连接函数与进程，一直处于阻塞状态直到对方连接成功
def wait():
    global friendAddr, friendPort, friendSock
    serverSock.listen(1)
    friendSock, (friendAddr, friendPort) = serverSock.accept()
    stateInfo.set("与" + friendAddr + "连接成功！")
    receiveThread.start()  # 创建新进程，开始无限监听
waitThread = threading.Thread(target=wait)
waitThread.setDaemon(True)
#发送函数，发送普通信息
def send(event):
    #空字符串不要传送
    if sendInfo.get() == '':
        return
    sendString = bytes(sendInfo.get(), encoding="utf-8")
    try:
        friendSock.send(sendString)
        listB.insert(0, sendInfo.get())
        sendInfo.set('')
    except ConnectionResetError:
        stateInfo.set('对方离线，信息发送失败！')
        return
#发送文件函数，负责处理是否接收和如何发送等等文件发送方面的内容
def sendFile():
    global filePath
    #第一步，弹出对话框，获取文件路径和文件名称
    filePath = filedialog.askopenfilename()
    #----若未选择文件，则直接退出
    if filePath == '':
        return
    #第二步在永不停息的receiveThread进程中
    friendSock.send(b'&f')
    listB.insert(0, '-' * 25 + "等待对方接收" + '-' * 25)
#创建连接，创建一个无限监听进程，用于接收信息和文件
def createLink():
    global serverAddr, serverPort, safety
    serverAddr = addr.get()
    serverPort = port.get()
    try:
        serverSock.bind((serverAddr, int(serverPort)))
    except OSError:  # IP地址输入错误会返回
        stateInfo.set("创建出错，请输入有效的IPv4地址！")
        return
    except ValueError:  # 输入格式错误
        stateInfo.set("创建出错，请检查格式！")
        return
    stateInfo.set('创建成功，请耐心等待对方连接')
    safety = False
    waitThread.start()  # 创建等待连接进程，保证GUI界面的流畅性

#连接别人，连接成功后创建一个无限监听进程，用于双向交流
def linkOthers():
    global friendAddr, friendPort
    if safety:
        friendAddr = addr.get()
        friendPort = port.get()
        try:
            friendSock.connect((friendAddr, int(friendPort)))
            stateInfo.set("与" + friendAddr + "连接成功！")
        except OSError as e:  # 不存在这样的链接
            print(e)
            stateInfo.set("尝试连接失败，请确认信息无误或对方已建立连接！")
            return
        except ValueError:  # 输入格式错误
            stateInfo.set("输入错误，请检查格式！")
            return
        receiveThread.start()  # friendSock修改成功，创建无限监听进程
    else:
        messagebox.showwarning(title="警告", message="本地连接已经建立，不可再连接他人！")

# 菜单函数
def linkAuthor():
    global serverAddr, serverPort
    serverAddr = "尚未搭建服务器"
    addr.set(serverAddr)
    serverPort = "..."
    port.set(serverPort)
def localIP():
    global serverAddr, serverPort
    #调用os来获取IPv4地址
    r = os.popen("ipconfig/all")
    info = r.readlines()
    for line in info:
        if "IPv4" in line:
            serverAddr = re.search(r'\d+.\d+.\d+.\d+',line).group(0)
    serverPort = '1025'
    addr.set(serverAddr)
    port.set(serverPort)
def helpDscp():
    text = "1.互联网上两台机器互联，需要定位，这个定位信息就是IP地址。本程序使用IPv4地址。获取方法：在window命令行界面输入 ipconfig/all 即可\n2.不同程序将从系统申请不同的端口，用以帮助操作系统确定从互联网上获得的信息该分发给哪个程序。本程序的端口号可以随便起，推荐为四位整数，大于1024\n\n简言之，IP地址自己查，端口号随便起"
    messagebox.showinfo(title = "帮助", message = text)
def moreDscp():
    text = "2018年7月25日于北京邮电大学\n著作人：任子昌\n版权所有，禁止一切未经允许的抄袭和改动，请勿用于商业目的\n联系方式：QQ2522465840，加好友请声明"
    messagebox.showinfo(title = "著作信息", message = text)
root = Tk()
root.title('chatty')
# 输入框
addr = StringVar()
port = StringVar()
Entry(root, textvariable=addr).grid(row=0, column=1, columnspan=2, sticky=W)
Entry(root, textvariable=port).grid(row=1, column=1, columnspan=2, sticky=W)
Label(root, text='输入IPv4地址：').grid(row=0, column=0, sticky=E, padx=10)
Label(root, text='输入开放端口：').grid(row=1, column=0, sticky=E, padx=10)
stateInfo = StringVar()
stateInfo.set("连接状态：")
Entry(root, textvariable=stateInfo, state="readonly").grid(row=2, column=0, columnspan=3, sticky=EW, padx=10)
Button(root, text='连接好友', command=linkOthers).grid(row=3, column=0, sticky=N)
Button(root, text='创建连接', command=createLink).grid(row=3, column=2, sticky=N)
# 交谈框
Label(root, text='在下框中输入想要发送的信息，按Enter键发送').grid(row=4, column=0, columnspan=3, sticky=S)
sendInfo = StringVar()
e = Entry(root, textvariable=sendInfo)
e.grid(row=5, column=0, columnspan=3, sticky=EW, padx=10)
e.bind("<KeyPress-Return>", send)
# 发送文件
Button(root, text='发送文件', command=sendFile).grid(row=6, rowspan=2, column=0, sticky=NSEW, padx=10)
# 对话框
bar = Scrollbar(root)
listB = Listbox(root, width=50, height=20, yscrollcommand=bar.set)
listB.grid(row=0, rowspan=10, column=3, padx=10, pady=10)
bar.grid(row=0, rowspan=10, column=4, pady=10, sticky=NS)
bar.config(command=listB.yview)
# 菜单栏
mainMenu = Menu(root, tearoff=False)
root.config(menu=mainMenu)
# 帮助栏
helpMenu = Menu(mainMenu, tearoff=False)
mainMenu.add_cascade(label="帮助", menu=helpMenu)
# 帮助栏的另一弹出菜单，内置IP和port=====================================
supportIP = Menu(helpMenu, tearoff=False)
helpMenu.add_cascade(label="获取内置IP和port", menu=supportIP)
supportIP.add_command(label="连接作者", command=linkAuthor)
# 内置IP可以后期进行更新================================================
# 帮助栏的帮助信息
helpMenu.add_command(label="获取本机IP", command=localIP)
helpMenu.add_separator()
helpMenu.add_command(label="使用说明", command=helpDscp)
# 信息栏
infoMenu = Menu(mainMenu, tearoff=False)
mainMenu.add_cascade(label="更多", menu=infoMenu)
# 添加信息
infoMenu.add_command(label="关于chatty", command=moreDscp)
infoMenu.add_separator()
infoMenu.add_command(label="更多内容敬请期待...")

root.mainloop()
