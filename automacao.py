from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import time
import pyautogui as pya
import os
from tkinter import *
import pyscreeze

userw = os.getenv('USERN')
passw = os.getenv('PASSWORD')

def Logar(p,username,password):
    #indo na pagina do site
    p.goto('https://login.controljus.com.br/login')
    time.sleep(3)
    #Logando
    p.locator('//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div[2]/form/div[1]/input').click()
    p.keyboard.type(username)
    time.sleep(1)
    p.locator('//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div[2]/form/div[2]/input').click()
    time.sleep(1)
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

def Etiqueta(p):
    p.locator('//*[@id="processosFiltroEtiquetas"]/div/div/div/div[1]/div[2]/div/i').click()
    time.sleep(3)
    img = pya.locateOnScreen('img/pesquisar.png', confidence=0.7)
    pya.click(img)
    p.keyboard.type('7') #7Setembro
    print('passei')
    time.sleep(2)
    img = pya.locateOnScreen('img/7Setembro.jpeg', confidence=0.9)
    time.sleep(2)
    pya.click(img)
    time.sleep(2)
    p.keyboard.press('Backspace')
    p.keyboard.type('ALL') #Alldesk
    time.sleep(2)
    img = pya.locateOnScreen('img/AllDesk.jpeg', confidence=0.95)
    time.sleep(2)
    pya.click(img)
    time.sleep(2)
    p.keyboard.press('Control+KeyA')
    p.keyboard.down('Backspace')
    p.keyboard.type('CAP') #Capitalize
    time.sleep(2)
    img = pya.locateOnScreen('img/capitalize.jpeg', confidence=0.95)
    time.sleep(2)
    pya.click(img)
    time.sleep(2)
    p.keyboard.press('Control+KeyA')
    p.keyboard.down('Backspace')
    p.keyboard.type('FAC') #FAC
    time.sleep(2)
    img = pya.locateOnScreen('img/Fac.jpeg', confidence=0.95)
    time.sleep(2)
    pya.click(img)
    time.sleep(2)
    p.keyboard.press('Control+KeyA')
    p.keyboard.down('Backspace')
    p.keyboard.type('G') #grupo
    time.sleep(2)
    img = pya.locateOnScreen('img/Grupo.jpeg', confidence=0.95)
    time.sleep(2)
    pya.click(img)
    time.sleep(2)
    p.keyboard.press('Control+KeyA')
    p.keyboard.down('Backspace')
    p.keyboard.type('KE') #Kedu
    time.sleep(2)
    img = pya.locateOnScreen('img/Kedu.jpeg', confidence=0.95)
    time.sleep(2)
    pya.click(img)
    time.sleep(2)
    p.keyboard.press('Control+KeyA')
    p.keyboard.down('Backspace')
    p.keyboard.type('M') #Martins and MF
    time.sleep(2)
    img = pya.locateOnScreen('img/Martins.jpeg', confidence=0.95)
    time.sleep(2)
    pya.click(img)
    time.sleep(2)
    img = pya.locateOnScreen('img/MF.jpeg', confidence=0.95)
    time.sleep(2)
    pya.click(img)
    time.sleep(2)
    p.keyboard.press('Control+KeyA')
    p.keyboard.down('Backspace')
    p.keyboard.type('OR') #Orla
    time.sleep(2)
    img = pya.locateOnScreen('img/Orla.jpeg', confidence=0.95)
    time.sleep(2)
    pya.click(img)
    time.sleep(2)
    p.keyboard.press('Control+KeyA')
    p.keyboard.down('Backspace')
    p.keyboard.type('TR') #Tribanco, SV, SP
    time.sleep(2)
    img = pya.locateOnScreen('img/SV.jpeg', confidence=0.95)
    time.sleep(2)
    pya.click(img)
    time.sleep(2)
    img = pya.locateOnScreen('img/SP.jpeg', confidence=0.95)
    time.sleep(2)
    pya.click(img)
    time.sleep(2)
    img = pya.locateOnScreen('img/TR.jpeg', confidence=0.95)
    time.sleep(2)
    pya.click(img)
    time.sleep(2)
    p.keyboard.press('Control+KeyA')
    p.keyboard.down('Backspace')
    p.keyboard.type('TST') #TST
    time.sleep(2)
    img = pya.locateOnScreen('img/TST.jpeg', confidence=0.95)
    time.sleep(2)
    pya.click(img)
    time.sleep(2)
    p.keyboard.press('Control+KeyA')
    p.keyboard.down('Backspace')
    time.sleep(2)

def Desparar(p):
    p.locator('//*[@id="content"]/div/div[3]/div/div/div[2]/div/div[1]/div/ul/li/div/div/div[2]/div[4]/div[2]/div[3]/div/div/div[1]/div[1]/input').click()
    time.sleep(2)
    p.keyboard.type('TRABALHISTA') #Trabalhista

def rodar_automacao():
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False)
        context = navegador.new_context(viewport={"width": 1920, "height": 1080})
        pagina = navegador.new_page()
        Logar(pagina, userw, passw)
        Pesquisar(pagina)
        Etiqueta(pagina)
        Desparar(pagina)


janela = Tk()
janela.title("AutoJus")
text = Label(janela, text = "Automação Jus")
text.grid(column=0, row = 0)
button = Button(janela, text="Rodar automação", command= rodar_automacao)
button.grid(column=0,row=2)
janela.mainloop()