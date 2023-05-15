from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from subprocess import CREATE_NO_WINDOW
import os

class ChromeDriver():
    def __init__(self):
        self.SERVICE=None
        wddir = os.environ["USERPROFILE"] + "\.wdm\drivers\chromedriver\win32" #Verificando se o usuário já tem o chrome web driver baixado
        if os.path.exists(wddir):
                wdname = "chromedriver.exe"
                for root,dir,files in os.walk(wddir):
                    if wdname in files:
                        self.SERVICE=Service(os.path.join(root, wdname))
        else:
                self.SERVICE=Service(ChromeDriverManager().install()) #Baixando chrome web driver caso necessário
        self.SERVICE.creationflags = CREATE_NO_WINDOW
        options = Options()
        options.headless = True
        self.driver=webdriver.Chrome(service=self.SERVICE,options=options)


class CopaDoBrasil(ChromeDriver):
    def __init__(self, ano) -> None:
        super().__init__()
        ANOS_PERMITIDOS = list(map(str, range(2012, 2023)))
        if ano not in ANOS_PERMITIDOS:
            raise ValueError(f"Ano inválido. Permitidos {ANOS_PERMITIDOS}")
        self.driver.set_window_size(1920, 1080)
        self.driver.get(f"https://www.cbf.com.br/futebol-brasileiro/competicoes/copa-brasil-masculino/{ano}")
    
    def etapa(self, etapa: int) -> list[tuple[str]]:
        if not isinstance(etapa, int):
            raise TypeError("O parâmetro 'etapa' deve ser um inteiro")
        etapa_max = len(self.driver.find_elements(By.XPATH, '//*[@id="menu-panel"]/article/div[1]/div/div/section/ul/li[*]/a'))
        ETAPAS = list(map(int, range(1, etapa_max + 1)))
        if etapa not in ETAPAS:
            raise ValueError(f"Etapa inválida. Permitidos {ETAPAS}")
        fase = self.driver.find_element(By.XPATH, f'//*[@id="menu-panel"]/article/div[1]/div/div/section/ul/li[{etapa}]/a')
        fase.click()
        tabela = self.driver.find_elements(By.XPATH, '//*[@id="menu-panel"]/article/div[1]/div/div/section/section/div[*]/div/div[*]/a/div')
        dados = [tuple(placar.text.split('\n')) for placar in tabela]
        return dados

class Nomes(ChromeDriver):

    def __init__(self) -> None:
        super().__init__()
        self.driver.set_window_size(1920, 1080)
        self.driver.get(f"https://pt.wikipedia.org/wiki/Os_100_livros_do_s%C3%A9culo_XX_segundo_Le_Monde")

    def get(self):
        elementos = self.driver.find_elements(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[*]/td[2]')
        for element in elementos:
             print(element.text.split('\n'))
if __name__ == "__main__":
    x = Nomes()
    x.get()