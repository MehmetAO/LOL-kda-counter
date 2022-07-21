import numpy as np
import pytesseract
import cv2
import serial
import time
from PIL import ImageGrab

arduinoData = serial.Serial("COM4", 9600)  # Arduino comm channel
time.sleep(3)  # Waiting for the arduino

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Pytesseract location on PC

death_count = 0  # Predetermined death count
kill_count = 0  # Predetermined kill count
kdaloc = (1663, 0, 1720, 25)  # K/D/A location on screen


def ardupinOn():  # Sending 1 (True) to arduino
    msg = "1"
    arduinoData.write(msg.encode())


def ardupinOff():  # Sending 0 (False) to arduino
    a = "0"
    arduinoData.write(a.encode())


def imToString(kda):  # Turning kill/death/assist to data
    cap = ImageGrab.grab(bbox=kda)
    tesstr = pytesseract.image_to_string(
        cv2.cvtColor(np.array(cap),
                     cv2.COLOR_BGR2GRAY),
        config='--psm 10 --oem 3 -c tessedit_char_whitelist=/0123456789',  # Whitelist just numbers for K/D/A
        lang='eng')

    return tesstr


while True:
    data = imToString(kdaloc)
    # print(data)
    if data != "":
        kill = data[0]
        death = data[2]
        if int(death) > int(death_count):
            ardupinOn()
            death_count = death

        if int(kill) > int(kill_count):
            time.sleep(1)
            ardupinOff()
            kill_count = kill

# 1663, 0, 1720, 25
