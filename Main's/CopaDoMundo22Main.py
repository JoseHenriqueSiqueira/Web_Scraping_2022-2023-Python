from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from subprocess import CREATE_NO_WINDOW
from time import *
import os

def main():
    print("INICIANDO. . .")
    SERVICE=None
    wddir = os.environ["USERPROFILE"] + "\.wdm\drivers\chromedriver\win32"
    if os.path.exists(wddir):
            wdname = "chromedriver.exe"
            for root,dir,files in os.walk(wddir):
                if wdname in files:
                    SERVICE=Service(os.path.join(root, wdname))
    else:
            SERVICE=Service(ChromeDriverManager().install())
    SERVICE.creationflags = CREATE_NO_WINDOW
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1080")
    url = 'https://ge.globo.com/futebol/copa-do-mundo/2022/'
    driver=webdriver.Chrome(service=SERVICE,options=options)
    driver.get(url)
    Retorno=[]
    x=0
    print("PROCESSANDO. . .")
    while x<5:
        Placar=driver.find_elements(By.CLASS_NAME, "placar")
        Esquerda=driver.find_element(By.CLASS_NAME, "navegacao-fase__seta-esquerda")
        Fase=driver.find_element(By.CLASS_NAME, "navegacao-fase__fase")
        Temp=[]
        for elemento in Placar:
            if '\n' in elemento.text:
                valor=elemento.text
                valor=valor.replace('\n'," ")
                if 'Estados Unidos' in valor:
                    valor=valor.replace('Estados Unidos','Estados-Unidos')
                if 'Coreia do Sul' in valor:
                    valor=valor.replace('Coreia do Sul','Coreia-do-Sul')
                valor=valor.split()
                Temp=Temp+[valor]
        Temp.insert(0,Fase.text)
        Retorno=Retorno+[Temp]
        Esquerda.click()
        sleep(1)
        x=x+1
    Final=Retorno[0]
    TerceiroLugar=Retorno[1]
    SemiFinal=Retorno[2]
    Quartas=Retorno[3]
    Oitavas=Retorno[4]
    print(*Final, sep = "\n")
    print(*TerceiroLugar, sep = "\n")
    print(*SemiFinal, sep = "\n")
    print(*Quartas, sep = "\n")
    print(*Oitavas, sep = "\n")


if __name__ == "__main__":
    main()