import pyautogui
import pygetwindow as gw
from time import sleep
from datetime import datetime

screen = gw.getActiveWindow()
pyautogui.moveTo(screen.width / 2, screen.height / 2)


while True:
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    pyautogui.rightClick()
    sleep(10)
