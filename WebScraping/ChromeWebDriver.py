from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from subprocess import CREATE_NO_WINDOW
import os

class ChromeDriver():
    def __init__(self):
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
        self.driver = webdriver.Chrome(service=SERVICE, options=options)