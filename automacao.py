from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import time
import pyautogui as pya
import os
from tkinter import *
import pyscreeze
from datetime import datetime
from credjur_module import Credjuridico
from credjur_module import EmailCred
from bancario import ContBanc
from bancario import EmailBanco
from civel import CivelEstrat
from civel import EmailCivel
from imgfunction import searchimage


userw = os.getenv('USERN')
passw = os.getenv('PASSWORD')
trab = os.getenv('TRAB')
cred = os.getenv('CREDJUR')
banc = os.getenv('BANCO')
civeles = os.getenv('CIVEL')
data_atual = datetime.now().strftime("%d/%m/%Y")



def Logar(p,username,password):
    #indo na pagina do site
    p.goto('https://login.controljus.com.br/login')
    time.sleep(2)
    #Logando
    p.locator('//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div[2]/form/div[1]/input').click()
    p.keyboard.type(username)
    time.sleep(1)
    p.locator('//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div[2]/form/div[2]/input').click()
    time.sleep(1)
    p.keyboard.type(password)
    p.get_by_role('button').click()
    time.sleep(2)
    time.sleep(2)

def Pesquisar(p):
    if p.locator('//*[@id="hs-eu-cookie-confirmation-inner"]'):
        p.locator('//*[@id="hs-eu-confirmation-button"]').click()
    p.goto('https://app.controljus.com.br/processos/lista')
    p.locator('//*[@id="content"]/div/div[3]/div/div/div[2]/div/div[1]/div/div/div[2]/div/button/span').click()
    time.sleep(2)

def Etiqueta(p):
    p.locator('//*[@id="processosFiltroEtiquetas"]/div/div/div/div[1]/div[2]/div/i').click()
    time.sleep(1)
    searchimage('img/naopreenchido.png',"pesquisar clicado!")
    searchimage('img/pesquisar.png',"pesquisar clicado!")
    print('passei')
    time.sleep(1)
    searchimage('img/7Setembro.jpeg',"7Setembro clicado!")
    searchimage('img/AllDesk.jpeg',"AllDesk clicado!")
    searchimage('img/capitalize.jpeg',"capitalize clicado!")
    searchimage('img/Fac.jpeg',"Fac clicado!")
    p.keyboard.press('Control+KeyA')
    p.keyboard.down('Backspace')
    p.keyboard.type('G') #grupo
    time.sleep(1)
    searchimage('img/Grupo.jpeg',"Fac clicado!")
    p.keyboard.press('Control+KeyA')
    p.keyboard.down('Backspace')
    p.keyboard.type('KE') #Kedu
    time.sleep(1)
    searchimage('img/Kedu.jpeg',"Kedu clicado!")
    p.keyboard.press('Control+KeyA')
    p.keyboard.down('Backspace')
    p.keyboard.type('M') #Martins and MF
    time.sleep(1)
    searchimage('img/Martins.jpeg',"Martins clicado!")
    searchimage('img/MF.jpeg',"MF clicado!")
    p.keyboard.press('Control+KeyA')
    p.keyboard.down('Backspace')
    p.keyboard.type('OR') #Orla
    time.sleep(1)
    searchimage('img/Orla.jpeg',"Orla clicado!")
    p.keyboard.press('Control+KeyA')
    p.keyboard.down('Backspace')
    p.keyboard.type('TR') #Tribanco, SV, SP
    time.sleep(2)
    searchimage('img/SV.jpeg',"SV clicado!")
    searchimage('img/SP.jpeg',"SP clicado!")
    searchimage('img/TR.jpeg',"TR clicado!")
    p.keyboard.press('Control+KeyA')
    p.keyboard.down('Backspace')
    p.keyboard.type('TST') #TST
    time.sleep(1)
    searchimage('img/TST.jpeg',"TST clicado!")
    p.keyboard.press('Control+KeyA')
    p.keyboard.down('Backspace')

def data(p):
    p.locator('//*[@id="content"]/div/div[3]/div/div/div[2]/div/div[1]/div/ul/li/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div[2]/div/i').click()
    time.sleep(1)
    searchimage('img/Movimento.jpeg',"Movimento clicado!")

def DefinirMovimentacao(p):
    time.sleep(2)
    searchimage('img/exportar.png',"exportar clicado!")
    searchimage('img/movimentacao.png',"movimentacao clicado!")
    time.sleep(1)
    searchimage('img/Numero.png',"Numero clicado!")
    time.sleep(1)
    p.keyboard.press('Control+KeyA')
    time.sleep(1)
    p.keyboard.type('2')

def Trabalhista(p):
    p.locator('//*[@id="content"]/div/div[3]/div/div/div[2]/div/div[1]/div/ul/li/div/div/div[2]/div[4]/div[2]/div[3]/div/div/div[1]/div[1]/input').click()
    time.sleep(2)
    p.keyboard.type('TRABALHISTA') #Trabalhista
    searchimage('img/Trabalhista.jpeg',"Trabalhista clicado!")
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


def EmailTrab(p,trab):
    #Titulo
    time.sleep(1)
    searchimage('img/titulo.jpeg',"titulo clicado!")
    searchimage('img/escrevertitulo.jpeg',"escrevertitulo clicado!")
    p.keyboard.type("PUBLICAÇÕES - TRABALHISTA -" + data_atual)
    time.sleep(1)
    #emails
    p.locator('//*[@id="app"]/div[1]/div/div/div[9]/div/div/div/div').click()
    print('test')
    time.sleep(2)
    searchimage('img/email.jpeg',"email clicado!")
    p.keyboard.type(trab)
    time.sleep(1)
    p.locator('//*[@id="app"]/div[1]/div/div/div[11]/button[2]/div').click()

def exportar(p):
    time.sleep(1)
    searchimage('img/exportar.png',"exportar clicado!")
    searchimage('img/movimentacao.png',"movimentacao clicado!")
    time.sleep(1)

def rodar_automacao():
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False)
        context = navegador.new_context(no_viewport=True)
        pagina = navegador.new_page()
        Logar(pagina, userw, passw)
        Pesquisar(pagina)
        Etiqueta(pagina)
        data(pagina)
        Trabalhista(pagina)
        DefinirMovimentacao(pagina)
        EmailTrab(pagina,trab)
        Credjuridico(pagina)
        exportar(pagina)
        EmailCred(pagina,cred)
        ContBanc(pagina)
        exportar(pagina)
        EmailBanco(pagina,banc)
        CivelEstrat(pagina)
        exportar(pagina)
        EmailCivel(pagina,civeles)
        time.sleep(3)


janela = Tk()
janela.title("AutoJus")
text = Label(janela, text = "Automação Jus")
text.grid(column=0, row = 0)
button = Button(janela, text="Rodar automação", command= rodar_automacao)
button.grid(column=0,row=2)
janela.mainloop()