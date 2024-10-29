from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import time
import pyautogui as pya
import os
from tkinter import *

userw = os.getenv('USERN')
passw = os.getenv('PASSWORD')

def Logar(p,username,password):
    #indo na pagina do site
    p.goto('https://login.controljus.com.br/login')
    time.sleep(5)
    #Logando
    p.locator('//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div[2]/form/div[1]/input').click()
    p.keyboard.type(username)
    time.sleep(3)
    p.locator('//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div[2]/form/div[2]/input').click()
    time.sleep(3)
    p.keyboard.type(password)
    p.get_by_role('button').click()
    time.sleep(3)

    time.sleep(5)
def Pesquisar(p):
    if p.locator('//*[@id="hs-eu-cookie-confirmation-inner"]'):
        p.locator('//*[@id="hs-eu-confirmation-button"]').click()
    p.goto('https://app.controljus.com.br/processos/lista')
    p.locator('//*[@id="content"]/div/div[3]/div/div/div[2]/div/div[1]/div/div/div[2]/div/button/span').click()
    time.sleep(5)

def Desparo(p):
    p.locator('//*[@id="processosFiltroEtiquetas"]/div/div/div/div[1]/div[2]/div/i').click()
    time.sleep(3)
    print('passei aq')
    img = pya.locateOnScreen('img/pesquisar.png', confidence=0.7)
    print('passei')
    pya.click(img)
    p.keyboard.type('7') #7Setembro
    p.locator('//*[@id="app"]/div[13]/div/div/div[2]/a/div[1]/div/div/div[1]/div/div').click()
    time.sleep(3)

def rodar_automacao():
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False)
        context = navegador.new_context(viewport={"width": 1920, "height": 1080})
        pagina = navegador.new_page()
        Logar(pagina, userw, passw)
        Pesquisar(pagina)
        Desparo(pagina)


janela = Tk()
janela.title("AutoJus")
text = Label(janela, text = "Automação Jus")
text.grid(column=0, row = 0)
button = Button(janela, text="Rodar automação", command= rodar_automacao)
button.grid(column=0,row=2)
janela.mainloop()