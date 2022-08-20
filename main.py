import cv2
import pytesseract
import pyautogui as pg
import win32api, win32con

pytesseract.pytesseract.tesseract_cmd = 'D:\\Python_Tesseract\\tesseract.exe'

up = win32api.GetKeyState(0x26)  # up arrow key
while not up:
    up = win32api.GetKeyState(0x26)  # up arrow key
img = pg.screenshot(region=(572, 686, 773, 200))

custom_config = '--psm 6 --oem 3 -c tessedit_char_blacklist=123456789|'
text = pytesseract.image_to_string(img, config=custom_config)

for letter in text:
    if letter == '\n':
        pg.press(" ")
    pg.press(letter)