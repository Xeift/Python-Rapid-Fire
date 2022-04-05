# Code to check if left or right mouse buttons were pressed
import win32api
import time
import pyautogui
import keyboard


state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128

while True:
    key_down = keyboard.is_pressed('caps lock')
    if key_down == True:
        break
    a = win32api.GetKeyState(0x01)
    b = win32api.GetKeyState(0x02)

    if a != state_left:  # Button state changed
        state_left = a
        print(a)
        if a < 0:
            print('Left Button Pressed')
            pyautogui.mouseDown(button="right")
        else:
            print('Left Button Released')
            pyautogui.mouseUp(button="right")
    time.sleep(0.0001)
            
