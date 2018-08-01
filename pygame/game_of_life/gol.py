print('importing pygame, please waite')
import pygame
from pygame.locals import *
from sys import exit
import random
cell_width = input('''Please enter the size of the cell as you prefer
(5 to 20 is allowed)\n''')

print('initializing 30%', end = '')
pygame.init()
print('\rinitializing 50%', end = '')
#细胞大小、颜色
cell_width = int(cell_width)
if cell_width > 20: cell_width = 30
elif cell_width < 5: cell_width = 3
live_cell = (255, 255, 0)
#屏幕大小、列表大小
size = width, height = 1366, 768
Lsize = Lwidth, Lheight = 2000 // cell_width, 1000 // cell_width
#初始化列表
L = []
for x in range(0, Lheight):
    l = []
    for y in range(0, Lwidth):
        l.append({'surround': 0, 'status':0 })
    L.append(l)
print('\rinitializing 70%', end = '')
#初始化屏幕，标题和背景
screen = pygame.display.set_mode(size, RESIZABLE)
picture = pygame.image.load('image\\back.jpg').convert()
menu = pygame.image.load('image\\menu.jpg').convert()
screen.blit(picture, (0, 0))
pygame.display.set_caption('This is the game of life!')
#繁殖
def cell_gener():
    #边界置空，扫描
    for x in range(1, Lheight - 1):
        for y in range(1, Lwidth - 1):
            L[x][y]['surround'] = 0
            for surx in range(x - 1, x + 2):
                for sury in range(y - 1, y + 2):
                    L[x][y]['surround'] += L[surx][sury]['status']
            L[x][y]['surround'] -= L[x][y]['status']
    #生成下一代
    for x in range(1, Lheight):
        for y in range(1, Lwidth):
            if L[x][y]['surround'] == 3:
                L[x][y]['status'] = 1
            elif L[x][y]['surround'] != 2:
                L[x][y]['status'] = 0
    for x in [0, Lheight - 1]:
        for y in range(0, Lwidth):
            L[x][y]['status'] = 0
    for y in [0, Lwidth - 1]:
        for x in range(0, Lheight):
            L[x][y]['status'] = 0
#显示
def cell_show(screen):
    screen.blit(picture, (0, 0))
    for x in range(0, height // cell_width):
        for y in range(0, width // cell_width):
            if L[x + 3][y + 3]['status'] == 1:
                pygame.draw.rect(screen, live_cell, (y * cell_width, x * cell_width, cell_width - 1, cell_width - 1))
    pygame.display.flip()
#随机生成
def set_cell_randomly(screen):
    for i in range(int(1000 * (12 / cell_width) ** 2)):
        x = random.randint(1, height // cell_width)
        y = random.randint(1, width // cell_width)
        L[x][y]['status'] = 1
    cell_gener()
    cell_show(screen)
#清空
def cell_clear(screen):
    for x in range(0, Lheight):
        for y in range(0, Lwidth):
            L[x][y]['status'] = 0
    screen.blit(picture, (0, 0))
    pygame.display.flip()
#例子
def e_g(screen):
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_m:
                cell_show(screen)
                return
            elif event.type == MOUSEBUTTONDOWN:
                xy = event.pos
                #Glider
                if 530 <= xy[0] <= 670 and 220 <= xy[1] <= 250:
                    cell_clear(screen)
                    f = open('backup\\glider.gol', 'r')
                    line_num = 0
                    for line in f:
                        y_num = 0
                        for y in line:
                            if line[y_num] != '\n':
                                L[line_num + 200 // cell_width][y_num + 500 // cell_width]['status'] = int(line[y_num])
                            y_num += 1
                        line_num += 1
                    cell_show(screen); return
                #Gosper Glider Gun
                elif 755 <= xy[0] <= 970 and 280 <= xy[1] <= 350:
                    cell_clear(screen)
                    f = open('backup\\glider_gun.gol', 'r')
                    line_num = 0
                    for line in f:
                        y_num = 0
                        for y in line:
                            if line[y_num] != '\n':
                                L[line_num + 200 // cell_width][y_num + 500 // cell_width]['status'] = int(line[y_num])
                            y_num += 1
                        line_num += 1
                    cell_show(screen); return
                #Tumbler
                elif 760 <= xy[0] <= 920 and 220 <= xy[1] <= 260:
                    cell_clear(screen)
                    f = open('backup\\tumbler.gol', 'r')
                    line_num = 0
                    for line in f:
                        y_num = 0
                        for y in line:
                            if line[y_num] != '\n':
                                L[line_num + 200 // cell_width][y_num + 500 // cell_width]['status'] = int(line[y_num])
                            y_num += 1
                        line_num += 1
                    cell_show(screen); return
                #LightWeightSpaceShip
                elif 530 <= xy[0] <= 730 and 390 <= xy[1] <= 460:
                    cell_clear(screen)
                    f = open('backup\\light_spaceship.gol', 'r')
                    line_num = 0
                    for line in f:
                        y_num = 0
                        for y in line:
                            if line[y_num] != '\n':
                                L[line_num + 200 // cell_width][y_num + 500 // cell_width]['status'] = int(line[y_num])
                            y_num += 1
                        line_num += 1
                    cell_show(screen); return
                #10_Cell_Row
                elif 530 <= xy[0] <= 710 and 330 <= xy[1] <= 370:
                    cell_clear(screen)
                    f = open('backup\\10_cell_row.gol', 'r')
                    line_num = 0
                    for line in f:
                        y_num = 0
                        for y in line:
                            if line[y_num] != '\n':
                                L[line_num + 200 // cell_width][y_num + 500 // cell_width]['status'] = int(line[y_num])
                            y_num += 1
                        line_num += 1
                    cell_show(screen); return
                #Exploder
                elif 530 <= xy[0] <= 690 and 280 <= xy[1] <= 350:
                    cell_clear(screen)
                    f = open('backup\\exploder.gol', 'r')
                    line_num = 0
                    for line in f:
                        y_num = 0
                        for y in line:
                            if line[y_num] != '\n':
                                L[line_num + 200 // cell_width][y_num + 500 // cell_width]['status'] = int(line[y_num])
                            y_num += 1
                        line_num += 1
                    cell_show(screen); return
                #DIY
                elif 755 <= xy[0] <= 970 and 390 <= xy[1] <= 460:
                    cell_clear(screen)
                    f = open('diy\\DIY.txt', 'r')
                    line_num = 0
                    for line in f:
                        y_num = 0
                        for y in line:
                            if line[y_num] != '\n':
                                L[line_num + 200 // cell_width][y_num + 500 // cell_width]['status'] = int(line[y_num])
                            y_num += 1
                        line_num += 1
                    cell_show(screen); return
                else:
                    return
#设置
def set_cell(screen):
    #进入事件等待死循环
    while True:
        for event in pygame.event.get():
            #调整窗口大小
            if event.type == VIDEORESIZE:
                size = event.size
                width, height = size
                screen = pygame.display.set_mode(size, RESIZABLE)
            #退出
            elif event.type == QUIT:
                exit()
            #键盘事件
            elif event.type == KEYDOWN:
                #按m键进入菜单
                if event.key == K_m:
                    screen.blit(picture, (0, 0))
                    screen.blit(menu, (500, 200))
                    pygame.display.flip()
                    e_g(screen)
                #回车键确定，退出
                elif event.key == K_RETURN or event.key == K_KP_ENTER or event.key == K_SPACE:
                    return
                #R键随机设置细胞
                elif event.key == K_r:
                    set_cell_randomly(screen)
                #C键清空
                elif event.key == K_c:
                    cell_clear(screen)
            #鼠标事件
            elif event.type == MOUSEBUTTONDOWN:
                #设置细胞
                num_y = event.pos[0] // cell_width
                mouse_x = num_y * cell_width
                num_x = event.pos[1] // cell_width
                mouse_y = num_x * cell_width
                if event.button == 1:
                    L[num_x + 3][num_y + 3]['status'] = 1
                    cell_show(screen)
                elif event.button == 3:
                    L[num_x + 3][num_y + 3]['status'] = 0
                    cell_show(screen)


print('\rinitializing 100%')
print('author:Ren Zichang')
print('Enjoy youself!')
print('You can DIY your own image in the file "DIY.txt".')
print("If you can't quit the game, try to shut down the command-line interface.")
#主程序
speed = 300
set_cell_randomly(screen)
while True:
    for event in pygame.event.get():
        if event.type == VIDEORESIZE:
            size = event.size
            width, height = size
            screen = pygame.display.set_mode(size, RESIZABLE)
        elif event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            #按空格进入设置状态
            if event.key == K_SPACE:
                set_cell(screen)
            #上箭头键加速
            elif event.key == K_UP:
                speed -= 300
                if speed <= 10:
                    speed = 10
            #下箭头减速
            elif event.key == K_DOWN:
                speed += 300
                if speed >= 500:
                    speed = 500
    screen.blit(picture, (0, 0))
    cell_gener()
    cell_show(screen)
    pygame.time.delay(speed)
