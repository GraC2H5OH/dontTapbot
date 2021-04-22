#эта говнина работает только на мониторах 16 на 9 и 1920x1080
#скорее всего любое отклонение от этих величин сломает программу
#и оно будет скринить с отклонением
#y=895
#x=1163
#x_pad=534
#y_pad=266
from numpy import *
import pyautogui
import win32api , win32con
import PIL
from PIL import ImageGrab
import os
import time
import datetime
from PIL import Image, ImageOps
x_pad=636
y_pad=260
#скрин игровой области
def scrGrab():
    co=(x_pad+1,y_pad+1,630,630)
    im=pyautogui.screenshot(region=co)
    return im
    #im1=pyautogui.screenshot(region=(x_pad+1,y_pad+1,630,630))
    #im1.save(os.getcwd()+'\\full_snap__'+str(int(time.time()))+'.png','PNG')
   # print(pyautogui.locateOnScreen('loa.png'))

#имитация лкм
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print('click')
#перемещение мышки в позицию
def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))
#получение координат для плиток уже юзлес
def get_cords():
    x,y=win32api.GetCursorPos()
    x= x-x_pad
    y =y-y_pad
    print(x,' ',y)
#перемещение мышки в конкретную позицию плитки
def Game1():
    #1
    mousePos((Cord.odin1))
    leftClick()
    time.sleep(.1)
def Game2():
    #2
    mousePos((Cord.odin2))
    leftClick()
    time.sleep(.1)
def Game3():
    #3
    mousePos((Cord.odin3))
    leftClick()
    time.sleep(.1)
def Game4():
    #4
    mousePos((Cord.odin4))
    leftClick()
    time.sleep(.1)
def Game5():
    #5
    mousePos((Cord.odin5))
    leftClick()
    time.sleep(.1)
def Game6():
    #6
    mousePos((Cord.odin6))
    leftClick()
    time.sleep(.1)
def Game7():
    #7
    mousePos((Cord.odin7))
    leftClick()
    time.sleep(.1)
def Game8():
    #8
    mousePos((Cord.odin8))
    leftClick()
    time.sleep(.1)
def Game9():
    #9
    mousePos((Cord.odin9))
    leftClick()
    time.sleep(.1)
def Game10():
    #10
    mousePos((Cord.odin10))
    leftClick()
    time.sleep(.1)
def Game11():
    #11
    mousePos((Cord.odin11))
    leftClick()
    time.sleep(.1)
def Game12():
    #12
    mousePos((Cord.odin12))
    leftClick()
    time.sleep(.1)
def Game13():
    #13
    mousePos((Cord.odin13))
    leftClick()
    time.sleep(.1)
def Game14():
    #14
    mousePos((Cord.odin14))
    leftClick()
    time.sleep(.1)
def Game15():
    #15
    mousePos((Cord.odin15))
    leftClick()
    time.sleep(.1)
def Game16():
    #16
    mousePos((Cord.odin16))
    leftClick()
    time.sleep(.1)
class Cord:
    odin1=(73,75)
    odin2=(235, 76)
    odin3=(394, 79)
    odin4=(537, 77)
    odin5=(80, 231)
    odin6=(239, 233)
    odin7=(393, 232)
    odin8=(556, 232)
    odin9=(79, 392)
    odin10=(237, 391)
    odin11=(391, 390)
    odin12=(550, 392)
    odin13=(73, 541)
    odin14=(243, 539)
    odin15=(391, 551)
    odin16=(543, 548)
def playGame():
    s=scrGrab()
    if s.getpixel(Cord.odin1)==(0,0,0):
        mousePos(Cord.odin1)
        time.sleep(.01)
        leftClick()
    if s.getpixel(Cord.odin2)==(0,0,0):
        mousePos(Cord.odin2)
        time.sleep(.01)
        leftClick()
    if s.getpixel(Cord.odin3)==(0,0,0):
        mousePos(Cord.odin3)
        time.sleep(.01)
        leftClick()
    if s.getpixel(Cord.odin4)==(0,0,0):
        mousePos(Cord.odin4)
        time.sleep(.01)
        leftClick()
    if s.getpixel(Cord.odin5)==(0,0,0):
        mousePos(Cord.odin5)
        time.sleep(.01)
        leftClick()
    if s.getpixel(Cord.odin6)==(0,0,0):
        mousePos(Cord.odin6)
        time.sleep(.01)
        leftClick()
    if s.getpixel(Cord.odin7)==(0,0,0):
        mousePos(Cord.odin7)
        time.sleep(.01)
        leftClick()
    if s.getpixel(Cord.odin8)==(0,0,0):
        mousePos(Cord.odin8)
        time.sleep(.01)
        leftClick()
    if s.getpixel(Cord.odin9)==(0,0,0):
        mousePos(Cord.odin9)
        time.sleep(.01)
        leftClick()
    if s.getpixel(Cord.odin10)==(0,0,0):
        mousePos(Cord.odin10)
        time.sleep(.01)
        leftClick()
    if s.getpixel(Cord.odin11)==(0,0,0):
        mousePos(Cord.odin11)
        time.sleep(.01)
        leftClick()
    if s.getpixel(Cord.odin12)==(0,0,0):
        mousePos(Cord.odin12)
        time.sleep(.01)
        leftClick()
    if s.getpixel(Cord.odin13)==(0,0,0):
        mousePos(Cord.odin13)
        time.sleep(.01)
        leftClick()
    if s.getpixel(Cord.odin14)==(0,0,0):
        mousePos(Cord.odin14)
        time.sleep(.01)
        leftClick()
    if s.getpixel(Cord.odin15)==(0,0,0):
        mousePos(Cord.odin15)
        time.sleep(.01)
        leftClick()
    if s.getpixel(Cord.odin16)==(0,0,0):
        mousePos(Cord.odin16)
        time.sleep(.01)
        leftClick()


def main():
    pass
if __name__=='__main__':
    main()
i=1
for i in range(1,228):
    playGame()