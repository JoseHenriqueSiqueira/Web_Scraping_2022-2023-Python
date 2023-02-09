from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
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

class CopaDoBrasil2023(ChromeDriver):
    def __init__(self) -> None:
        super().__init__()
        self.driver.set_window_size(1920, 1080)
        self.driver.get("https://ge.globo.com/futebol/copa-do-brasil/")
        self.etapas = {
            "PrimeiraFase":0, "SegundaFase":1, "TerceiraFase":2, "Oitavas":3, "Quartas":4, "SemiFinal":5, "Final":6
        }

    def Etapa(self, etapa: str) -> list:
        Dados=[]  
        Botao = self.driver.find_element(By.CLASS_NAME, "navegacao-fase__seta-direita")
        try:
            for _ in range(self.etapas.get(etapa)):
                Botao.click()
        except:
            return ["Parâmetro 'etapa' Inválido, verifique os parâmetros permitidos na documentação"]
        Tabela = self.driver.find_elements(By.CLASS_NAME, "mata-mata__chave") 
        for partida in Tabela:
            Dados.append(partida.text.split('\n'))
        return Dados

class Brasileirao2022(ChromeDriver):
    def __init__(self) -> None:
        super().__init__()
        self.driver.get('https://ge.globo.com/futebol/brasileirao-serie-a/')
        self.driver.maximize_window()
    
    def TabelaClassificação(self) -> list:
        Dados=[]
        Posições = self.driver.find_elements(By.CLASS_NAME, "classificacao__equipes--posicao")
        Nomes = self.driver.find_elements(By.CLASS_NAME, "classificacao__equipes--nome")
        Pontos = self.driver.find_element(By.XPATH, "//*[@id='classificacao__wrapper']/article/section[1]/div/table[2]/tbody").text.split('\n')
        for posicao, nome, resultados in zip(Posições, Nomes, Pontos):
            Dados.append([posicao.text,nome.text,resultados])
        return Dados

    def Rodadas(self, rodada:int) -> list:
        if type(rodada) != int or rodada <= 0 or rodada >= 39:
            return ["Parâmetro 'rodada' Inválido, verifique os parâmetros permitidos na documentação"]
        Dados=[]
        Botao = self.driver.find_element(By.CLASS_NAME, "lista-jogos__navegacao--seta-esquerda svg")
        for _ in range(38-(rodada)):
            Botao.click()
        UltimaRodada = self.driver.find_elements(By.CLASS_NAME, 'placar')
        for Placar in UltimaRodada:
            Dados.append(Placar.text.split('\n'))
        return Dados

class CopaDoMundo2022(ChromeDriver):
    def __init__(self):
        super().__init__()
        self.driver.get('https://ge.globo.com/futebol/copa-do-mundo/2022/')
        self.etapas = {
            "Final":0, "TerceiroLugar":1, "SemiFinal":2, "Quartas":3, "Oitavas":4
        }

    def FaseDeGrupos(self) -> list:
        Dados = []
        Seta = self.driver.find_element(By.CLASS_NAME, "navegacao-fase__seta-esquerda")
        for _ in range(6):
            Seta.click()
        Posiçoes = self.driver.find_elements(By.CLASS_NAME, "classificacao__equipes--posicao")
        Nomes = self.driver.find_elements(By.CLASS_NAME, "classificacao__equipes--time")
        Pontos = []
        for n in range(1,9):
            Pontos = Pontos + self.driver.find_element(By.XPATH, f"//*[@id='classificacao__wrapper']/article[{n}]/section[1]/div/table[2]/tbody").text.split("\n")
        for posição, nome, pontos in zip(Posiçoes, Nomes, Pontos):
            Dados.append([posição.text, nome.text, pontos])
        return Dados

    def Eliminatorias(self, etapa:str) -> list:
        Dados = []
        Seta = self.driver.find_element(By.CLASS_NAME, "navegacao-fase__seta-esquerda")
        try:
            for _ in range(self.etapas.get(etapa)):
                Seta.click()
        except:
            return ["Parâmetro 'etapa' Inválido, verifique os parâmetros permitidos na documentação"]
        Placares = self.driver.find_elements(By.CLASS_NAME, "placar")
        for placar in Placares:
            Dados.append(placar.text.split("\n"))
        return Dados
        