from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import time
import pyautogui as pya
import os
from tkinter import *
import pyscreeze
from automacao import *
from datetime import datetime
data_atual = datetime.now().strftime("%d/%m/%Y")


def Credjuridico(p):
    p.locator('//*[@id="content"]/div/div[3]/div/div/div[2]/div/div[1]/div/ul/li/div/div/div[2]/div[4]/div[2]/div[3]/div/div/div[1]/div[1]/input').click()
    time.sleep(1)
    p.keyboard.press("Backspace")
    p.keyboard.press("Backspace")
    p.keyboard.type('RECUPERAÇÃO ') #recuperação
    time.sleep(1)
    img = pya.locateOnScreen('img/credjur.jpeg', confidence=0.95)
    time.sleep(1)
    pya.click(img)
    p.evaluate("window.scrollBy(0, window.innerHeight);")
    p.wait_for_timeout(1000)
    time.sleep(1)
    #Clicar em aplicar
    p.locator('//*[@id="content"]/div/div[3]/div/div/div[2]/div/div[1]/div/ul/li/div/div/div[4]/button[2]').click()
    print('Cliquei')
    time.sleep(2)
    p.locator('//*[@id="ProcessosTable"]/div[2]/div/div/table/thead/tr[1]/th[1]/div/div/div/div/div').click()
    print('codigo')
    time.sleep(2)
    p.evaluate("window.scrollBy(0, -window.innerHeight);")

def EmailCred(p,cred):
    #Titulo
    time.sleep(1)
    img = pya.locateOnScreen('img/titulo.jpeg', confidence=0.95)
    time.sleep(1)
    pya.click(img)
    time.sleep(1)
    img = pya.locateOnScreen('img/escrevertitulo.jpeg', confidence=0.95)
    time.sleep(1)
    pya.click(img)
    time.sleep(2)
    p.keyboard.type("PUBLICAÇÕES - RECUPERAÇÃO DE CRÉDITO JUDICIAL -" + data_atual)
    time.sleep(2)
    #emails
    p.locator('//*[@id="app"]/div[1]/div/div/div[9]/div/div/div/div').click()
    print('test')
    time.sleep(2)
    img = pya.locateOnScreen('img/email.jpeg', confidence=0.95)
    time.sleep(2)
    pya.click(img)
    time.sleep(2)
    p.keyboard.type(cred)
    time.sleep(2)
    p.locator('//*[@id="app"]/div[1]/div/div/div[11]/button[2]/div').click()
    time.sleep(2)