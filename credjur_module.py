from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import time
import pyautogui as pya
import os
from tkinter import *
import pyscreeze
from automacao import *
from datetime import datetime
from imgfunction import searchimage
data_atual = datetime.now().strftime("%d/%m/%Y")

def Credjuridico(p):
    time.sleep(3)
    p.locator('//*[@id="content"]/div/div[3]/div/div/div[2]/div/div[1]/div/ul/li/div/div/div[2]/div[4]/div[2]/div[3]/div/div/div[1]/div[1]/input').click()
    time.sleep(1)
    p.keyboard.press("Backspace")
    p.keyboard.press("Backspace")
    p.keyboard.type('RECUPERAÇÃO ') #recuperação
    searchimage('img/credjur.jpeg', "disparado!")
    p.evaluate("window.scrollBy(0, window.innerHeight);")
    p.wait_for_timeout(1000)
    time.sleep(1)
    #Clicar em aplicar
    p.locator('//*[@id="content"]/div/div[3]/div/div/div[2]/div/div[1]/div/ul/li/div/div/div[4]/button[2]').click()
    print('Cliquei')
    time.sleep(1)
    p.locator('//*[@id="ProcessosTable"]/div[2]/div/div/table/thead/tr[1]/th[1]/div/div/div/div/div').click()
    print('codigo')
    time.sleep(1)
    p.evaluate("window.scrollBy(0, -window.innerHeight);")

def EmailCred(p,cred):
    #Titulo
    searchimage('img/titulo.jpeg',"titulo clicado!")
    time.sleep(2)
    searchimage('img/escrevertitulo.jpeg',"escrevertitulo clicado!")
    time.sleep(1)
    p.keyboard.type("PUBLICAÇÕES - RECUPERAÇÃO DE CRÉDITO JUDICIAL -" + data_atual)
    time.sleep(2)
    #emails
    searchimage('img/fotoemail.jpeg',"fotoemail clicado!")
    searchimage('img/email.jpeg',"email clicado!")
    p.keyboard.type(cred)
    time.sleep(1)
    p.locator('//*[@id="app"]/div[*]/div/div/div[11]/button[2]').click()
    time.sleep(1)
