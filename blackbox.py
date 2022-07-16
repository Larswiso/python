'''
Author: Lars Wisotzky
This program is inspired by the Blackbox Chrome extension.

Setup everything:
1) pip install numpy, pytesseract, Pillow, keyboard, clipboard, win10toast, opencv-python
2) Get tesseract from here: https://github.com/UB-Mannheim/tesseract/wiki
3) Select the filepath from tesseract.exe and paste in the PATH (System Environment Variables)
4) Replace in line 57 r'...' with your filepath from tesseract.exe
'''

import time
import os

import cv2 
import numpy as np
import pytesseract
from PIL import ImageGrab
import keyboard
import clipboard
from win10toast import ToastNotifier



print("Running ...")

def blackbox():
    # make screenshot
    img = ImageGrab.grab()
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    # get 4 coordinates
    filepath = r"E:/Development/Python/resources/crop.jpg"
    cords = []

    def click_event(event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            x = int(x)
            y = int(y) 
            cords.append(x)
            cords.append(y)

    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)
    
    # crop image
    x1 = cords[0]
    y1 = cords[1]
    x2 = cords[2]
    y2 = cords[3]
    crop_image = img[y1:y2, x1:x2]
    cv2.imwrite(filepath, crop_image)

    # text recognition
    image = cv2.imread(filepath)
    pytesseract.pytesseract.tesseract_cmd = r'E:\Programme\PyTesseract\tesseract.exe'
    string = pytesseract.image_to_string(image)
    os.remove(filepath)

    # paste text into clipboard
    clipboard.copy(string)

    # Toast-Notification
    toaster = ToastNotifier()
    toaster.show_toast(title="Paste text with Ctrl + V", msg="Blackbox", duration=2.5, threaded=True)
        

while True:
    if keyboard.is_pressed('alt') == True and keyboard.is_pressed('s') == True:
        try:
            blackbox()
        except:
            pass
    else:
        pass
    time.sleep(0.1)
