import time
import os

import cv2 
import numpy as np
import pytesseract
from PIL import ImageGrab
import matplotlib.pyplot as plt
import keyboard
import clipboard

def blackbox():
    # make screenshot
    img = ImageGrab.grab()
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    # get 4 coordinates
    filepath = r"E:/Development/Python/resources/crop.jpg"
    fig, ax = plt.subplots()
    cords = []
    def onclick(event):
        x, y= event.xdata, event.ydata 
        x = int(x)
        y = int(y) 
        cords.append(x)
        cords.append(y)
    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.title("click twice and then close")
    plt.imshow(img)
    plt.show()

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

while True:
    if keyboard.is_pressed('alt') == True and keyboard.is_pressed('s') == True:
        try:
            blackbox()
        except:
            pass
    else:
        pass
    time.sleep(0.1)