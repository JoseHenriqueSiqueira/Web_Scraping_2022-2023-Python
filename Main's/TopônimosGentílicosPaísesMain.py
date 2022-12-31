from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from subprocess import CREATE_NO_WINDOW
import os

def main():
    print("INICIANDO. . .")
    SERVICE=None
    wddir = os.environ["USERPROFILE"] + "\.wdm\drivers\chromedriver\win32" #Verificando se o usuário já tem o chrome web driver baixado
    if os.path.exists(wddir): 
            wdname = "chromedriver.exe"
            for root,dir,files in os.walk(wddir):
                if wdname in files:
                    SERVICE=Service(os.path.join(root, wdname))
    else:
            SERVICE=Service(ChromeDriverManager().install()) #Baixando chrome web driver caso necessário
    SERVICE.creationflags = CREATE_NO_WINDOW
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1080")
    url = 'http://funag.gov.br/manual/index.php?title=Top%C3%B4nimos_e_gent%C3%ADlicos' #Url base
    driver=webdriver.Chrome(service=SERVICE,options=options)
    driver.get(url)
    print("PROCESSANDO. . .")
    x=1
    y=2
    Retorno=[]
    Temp=[]
    while x<5:
        Cabeçalho=driver.find_element(By.XPATH, f"/html/body/div[1]/div[1]/div/div[2]/div[4]/div/table/tbody/tr[1]/th[{x}]") #Obtendo elementos do cabeçalho da Tabela
        Temp=Temp+[Cabeçalho.text]
        x+=1
    Retorno=Retorno+[Temp]
    Temp=[]
    x=1
    while 1:
        try:
            if x<5:
                Tabela=driver.find_element(By.XPATH, f"/html/body/div[1]/div[1]/div/div[2]/div[4]/div/table/tbody/tr[{y}]/td[{x}]") #Obtendo informações sobre cada País
                Temp=Temp+[Tabela.text]
                x+=1
            else:
                Retorno=Retorno+[Temp]
                Temp=[]
                x=1
                y+=1
        except:
            break
    print(*Retorno, sep="\n") #Imprimindo "Forma breve","Nome oficial","Capital" e "Gentílico" de cada País

if __name__ == "__main__":
    main()