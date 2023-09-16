import time
import pyautogui
import winsound
import pytesseract
import cv2
import mss
import numpy
import pyperclip

pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract'
mon = {'top': 716, 'left': 1273, 'width': 80, 'height': 30}

pasaport = input ("Pasaport tipini giriniz(bordo,gri,yesil) :")
print("\n")
il = input("Pasaport randevusu almak istediginiz ili giriniz :")
time.sleep(1)
passp = pyautogui.locateCenterOnScreen(r'D:\randevu_ss\pasaport.png')
passp1 = str(passp)
if("Point" in passp1):
    pyautogui.click(passp)
    time.sleep(0.5)
    pyautogui.click(1069,789)
time.sleep(0.5)
if(pasaport == "yesil"):
    pyautogui.click(1251,461)
if(pasaport == "bordo"):
    pyautogui.click(668,458)
if(pasaport == "gri"):
    pyautogui.click(956,467)
time.sleep(1)
pyperclip.copy(" ")
pyautogui.click(597,601)
pyautogui.write(" ")#ad
pyautogui.click(1038,601)
pyautogui.hotkey("ctrl", "v")#soyad
pyautogui.click(617,700)
pyautogui.write(" ")#tc
pyautogui.click(625,784)
pyautogui.write(" ")#telefon
pyautogui.click(1021,692)
pyautogui.write(" ")#gun
pyautogui.click(1165,692)
pyautogui.write(" ")#ay
pyautogui.click(1307,691)
pyautogui.write(" ")#yil

with mss.mss() as sct:
    while True:
        refresh = pyautogui.locateCenterOnScreen(r'D:\randevu_ss\refresh.png',confidence=0.8)
        refresh1 = str(refresh)
        hata = pyautogui.locateCenterOnScreen(r'D:\randevu_ss\hata.png',confidence=0.8)
        hata1 = str(hata)
        out = pyautogui.locateCenterOnScreen(r'D:\randevu_ss\out.png',confidence=0.8)
        out1 = str(out)
        im = numpy.asarray(sct.grab(mon))
        im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(im, config="-c tessedit_char_blacklist=abcdefghijklmnopqrstuvwxyz,.-_ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 6")
        if(len(text) == 6):
            pyautogui.click(1040,790)
            pyautogui.write(text)  
            time.sleep(1)
        elif("Point" in hata1):
            pyautogui.click(1188,608)
        else:
            pyautogui.click(refresh)
        if("Point" in out1):
            break
        cv2.imshow('Image', im)
        time.sleep(2)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
while 1:
    arama = pyautogui.locateCenterOnScreen(r'D:\randevu_ss\arama.png',confidence=0.8)
    arama1 = str(arama)
    if("Point" in arama1):
        pyautogui.click(arama)
        time.sleep(1)
        pyautogui.write(il)
        time.sleep(1)
        pyautogui.click(841,465)
        break
a = 500
b = 100
while 1:
    pyautogui.press("f5")
    time.sleep(0.7)
    pyautogui.click(1018,209)
    x = pyautogui.locateCenterOnScreen(r'D:\randevu_ss\1.png',confidence=0.8)
    x1 = str(x)
    y = pyautogui.locateCenterOnScreen(r'D:\randevu_ss\ileri.png',confidence=0.8)
    y1 = str(x)
    z = pyautogui.locateCenterOnScreen(r'D:\randevu_ss\kendisi.png',confidence=0.8)
    z1 = str(z)

    if("Point" in x1):
        pyautogui.click(x)
        time.sleep(1)
        pyautogui.click(y)
        winsound.Beep(a, b)
        break
time.sleep(1)
pyautogui.click(672,448)
time.sleep(0.5)
pyautogui.click(1478,910)
time.sleep(0.5)
pyautogui.click(601,505)
time.sleep(1.2)
pyautogui.click(881,515)
time.sleep(1.3)
pyautogui.click(1484,977)
print("Sorun olabilme ihtimaline karsi telefon dogrulama kismini sana pasladim acele etme randevu sende :)")
        

