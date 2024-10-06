import pyautogui
import time

def buy_unit(index, beforeclick_delay=0, afterclick_delay=0.1):
    height_pose = 990
    cursor_poses = [580, 780, 980, 1180, 1380]

    cursor_x, cursor_y = pyautogui.position()
    pyautogui.moveTo(cursor_poses[index], height_pose, _pause=False)
    time.sleep(beforeclick_delay)
    pyautogui.mouseDown(_pause=False)
    pyautogui.mouseUp(_pause=False)
    time.sleep(afterclick_delay)

    pyautogui.moveTo(cursor_x, cursor_y)