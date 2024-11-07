import pyautogui as pya
import time

def searchimage(image_path, description):
    while True:
        try:
            image_path = pya.locateOnScreen(image_path, confidence=0.9)
            if image_path:
                pya.click(image_path)
                print(description)
                break

        except:
            print("Buscando imagem")
            time.sleep(0.5)