#!/bin/env python
# -*- coding: utf-8 -*-

"""
依赖 pywin32  win32gui PIL
需要自己下载扫雷，http://www.saolei.net/BBS/，右上角，下载
打开扫雷，然后运行本脚本，全自动扫雷
Win 键强制退出脚本

"""
import random
import win32api
import win32gui
import pytesseract
import win32con
import sys
import os
import time 
from PIL import ImageGrab

# 查找扫雷游戏窗口
class_name = "SunAwtFrame"
title_name = "Mine"
hwnd = win32gui.FindWindow(class_name, title_name)

#hwnd = win32gui.GetForegroundWindow()
#clsname = win32gui.GetClassName(hwnd) 
#print(clsname)
 

# 窗口坐标
left = 0
top = 0
right = 0
bottom = 0

if hwnd:
    print("find mine_map")
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    # win32gui.SetForegroundWindow(hwnd)
    print("windws location:")
    print(str(left)+' '+str(right)+' '+str(top)+' '+str(bottom))
else:
    print("No find windows")

# 雷区坐标，扫雷软件相对比较稳定，雷区位置不变

left += 126
top += 98
right -= 150

bottom -= 78

# 截图雷区图像
rect = (left, top, right, bottom)
img = ImageGrab.grab().crop(rect)
#img.save('test_image.png')
print(str(left)+' '+str(right)+' '+str(top)+' '+str(bottom))
# 雷区每个方块16*16
block_width, block_height = 30, 31
# 计算横向有blocks_x个方块
blocks_x = int((right - left) / block_width)
# 计算纵向有blocks_y个方块
blocks_y = int((bottom - top) / block_height)
print(str(blocks_x)+str(blocks_y))

# 各种旗帜颜色，多点判断
rgba_ed = set([(255, 255, 255)])
rgba_red =set([(255, 0, 0)])

rgba_0 =set([(179, 179, 179), (178, 178, 178),(160, 160, 160)])

rgba_boom = set([(0, 0, 0)])
rgba_boom_red = [(4, (255, 255, 255)), (144, (255, 0, 0)), (31, (128, 128, 128)), (77, (0, 0, 0))]
# 数字1-8
# 0 未被打开
# -1 被打开 空白
# -4 红旗

mine_map = [[0 for i in range(blocks_x)] for i in range(blocks_y)]

# 用于统计是否需要随机点击
random_click = 0
# 是否游戏结束
game_over = 0


# 扫描雷区图像,雷区切块并且判断该块雷的数量
def show_mine_map():
    pic = ImageGrab.grab().crop(rect)
    for y in range(blocks_y):
        for x in range(blocks_x):
            if mine_map[y][x] == -1 or mine_map[y][x] ==- -4:
                continue
            this_image = pic.crop((x * block_width+5, y * block_height+5, (x + 1) * block_width-5, (y + 1) * block_height-5))
            #this_image.save('test_image'+str(x)+str(y)+'.png')
            my_color = set([i[1] for i in this_image.getcolors()])
            # print("[+]location: " + str((y, x)))
            # print(my_color)
            if len(rgba_0&my_color) >= 2 :
                mine_map[y][x] = 0
            elif my_color == rgba_ed:
                mine_map[y][x] = -1
            elif my_color == rgba_red:
                mine_map[y][x] = -4
                print(mine_map)
            elif len(my_color - rgba_boom) < 3 or this_image.getcolors() == rgba_boom_red:
                global game_over
                game_over = 1
                break
            elif len(my_color) > 10:
                if 1<= mine_map[y][x] <=9:
                    continue
                recon_image = pic.crop((x * block_width, y * block_height, (x + 1) * block_width, (y + 1) * block_height))
                text = pytesseract.image_to_string(recon_image,config='--psm 10 sfz')
                print(list(text))
                print("location" + str((y, x)) + "color")
                # print(my_color)
                if text[0] == '1':
                    mine_map[y][x] = 1
                elif text[0] == '2':
                    mine_map[y][x] = 2
                elif text[0] == '3':
                    mine_map[y][x] = 3
                elif text[0] == '4':
                    mine_map[y][x] = 4
                elif text[0] == '5':
                    mine_map[y][x] = 5
                elif text[0] == '6':
                    mine_map[y][x] = 6
                elif text[0] == '7':
                    mine_map[y][x] = 7
                elif text[0] == '8':
                    mine_map[y][x] = 8
                elif text[0] == '\x0c':
                    recon_image.save('ss.png')
                    print(my_color)
                    print("[+]location: " + str((y, x)))
                    print("recognition failed\n")
                    sys.exit(0)

            else:
                print("NO recognition")
                print("[+]location: " + str((y, x)))
                recon_image = pic.crop((x * block_width, y * block_height, (x + 1) * block_width, (y + 1) * block_height))
                # recon_image = recon_image.convert('L')
                # pixels = recon_image.load()
                # for x in range(recon_image.width):
                #     for y in range(recon_image.height):
                #         if pixels[x, y] > 150:
                #             pixels[x, y] = 255
                #         else:
                #             pixels[x, y] = 0
                # recon_image.save('ss.png')
                print(this_image.getcolors())
                sys.exit(0)
                


# 插红旗
def red_flag():
    show_mine_map()
    for y in range(blocks_y):
        for x in range(blocks_x):
            if 1 <= mine_map[y][x] <= 5:
                boom_number = mine_map[y][x]
                block_white = 0
                block_qi = 0
                for yy in range(y-1, y+2):
                    for xx in range(x-1, x+2):
                        if 0 <= yy and 0 <= xx and yy < blocks_y and xx < blocks_x:
                            if not (yy == y and xx == x):
                                if mine_map[yy][xx] == 0:
                                    block_white += 1
                                elif mine_map[yy][xx] == -4:
                                    block_qi += 1
                if boom_number == block_white + block_qi:
                    for yy in range(y - 1, y + 2):
                        for xx in range(x - 1, x + 2):
                            if 0 <= yy and 0 <= xx and yy < blocks_y and xx < blocks_x:
                                if not (yy == y and xx == x):
                                    if mine_map[yy][xx] == 0:
                                        os.system('cls')
                                        print("\n\nauto sweep mine\n\nuse Win 键强制退出\ninsert red flag" + str(yy + 1) + ',' + str(xx + 1))
                                        win32api.SetCursorPos([left+xx*block_width+10, top+yy*block_height+10])
                                        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
                                        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
                                        show_mine_map()


# 点击空白
def dig():
    show_mine_map()
    is_random_click = 0
    for y in range(blocks_y):
        for x in range(blocks_x):
            if 1 <= mine_map[y][x] <= 5:
                boom_number = mine_map[y][x]
                block_white = 0
                block_qi = 0
                for yy in range(y - 1, y + 2):
                    for xx in range(x - 1, x + 2):
                        if 0 <= yy and 0 <= xx and yy < blocks_y and xx < blocks_x:
                            if not (yy == y and xx == x):
                                if mine_map[yy][xx] == 0:
                                    block_white += 1
                                elif mine_map[yy][xx] == -4:
                                    block_qi += 1
                if boom_number == block_qi and block_white > 0:
                    for yy in range(y - 1, y + 2):
                        for xx in range(x - 1, x + 2):
                            if 0 <= yy and 0 <= xx and yy < blocks_y and xx < blocks_x:
                                if not(yy == y and xx == x):
                                    if mine_map[yy][xx] == 0:
                                        print("click:" + str(yy + 1) + ',' + str(xx + 1))
                                        win32api.SetCursorPos([left + xx * block_width+10, top + yy * block_height+10])
                                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
                                        is_random_click = 1
    if is_random_click == 0:
        random_click()


# 随机点击
def random_click():
    fl = 1
    while fl:
        random_x = random.randint(0, blocks_x - 1)
        random_y = random.randint(0, blocks_y - 1)
        if not mine_map[random_y][random_x]:
            print("random_click" + str(random_y + 1) + ',' + str(random_x + 1))
            win32api.SetCursorPos([left + random_x * block_width+10, top + random_y * block_height+10])
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            fl = 0


def main():
    win32api.SetCursorPos([left, top])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    show_mine_map()
    print("show mine map")
    global game_over
    while 1:
        if not game_over:
            red_flag()
            print("red_flag")
            red_flag()
            dig()
        else:
            game_over = 0
            win32api.keybd_event(113, 0, 0, 0)
            win32api.SetCursorPos([left, top])
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            show_mine_map()


if __name__ == "__main__":
    main()
