from selenium.webdriver.common.by import By
from ChromeWebDriver import ChromeDriver

class CopaDoBrasil2023(ChromeDriver):
    def __init__(self) -> None:
        super().__init__()
        self.driver.set_window_size(1920, 1080)
        self.driver.get("https://ge.globo.com/futebol/copa-do-brasil/")
        self.etapas = {
            "PrimeiraFase":6, "SegundaFase":5, "TerceiraFase":4, "Oitavas":3, "Quartas":2, "SemiFinal":1, "Final":0
        }

    def Etapa(self, etapa: str) -> list[str]:
        if not isinstance(etapa, str):
            raise TypeError("O parâmetro 'etapa' deve ser uma string")
        Dados=[]  
        SetaEsquerda = self.driver.find_element(By.CLASS_NAME, "navegacao-fase__seta-esquerda")
        SetaDireita = self.driver.find_element(By.CLASS_NAME, "navegacao-fase__seta-direita")
        for _ in range(6):
            SetaDireita.click()
        try:
            for _ in range(self.etapas.get(etapa)):
                SetaEsquerda.click()
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
    
    def TabelaClassificação(self) -> list[str]:
        Dados=[]
        Posições = self.driver.find_elements(By.CLASS_NAME, "classificacao__equipes--posicao")
        Nomes = self.driver.find_elements(By.CLASS_NAME, "classificacao__equipes--nome")
        Pontos = self.driver.find_element(By.XPATH, "//*[@id='classificacao__wrapper']/article/section[1]/div/table[2]/tbody").text.split('\n')
        for posicao, nome, resultados in zip(Posições, Nomes, Pontos):
            Dados.append([posicao.text,nome.text,resultados])
        return Dados

    def Rodadas(self, rodada:int) -> list[str]:
        if not isinstance(rodada, int):
            raise TypeError("O parâmetro 'rodada' deve ser uma string")
        if rodada <= 0 or rodada >= 39:
            raise Exception("Parâmetro 'rodada' Inválido, verifique os parâmetros permitidos na documentação")
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

    def FaseDeGrupos(self) -> list[str]:
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

    def Eliminatorias(self, etapa:str) -> list[str]:
        if not isinstance(etapa, str):
            raise TypeError("O parâmetro 'etapa' deve ser uma string")
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

class ChampionsLeague2223(ChromeDriver):
    def __init__(self):
        super().__init__()
        self.driver.get("https://ge.globo.com/futebol/futebol-internacional/liga-dos-campeoes/")
        self.driver.set_window_size(1920, 1080)
        self.etapas = {
            "Final":0, "SemiFinal":1, "Quartas":2, "Oitavas":3
        }

    def FaseDeGrupos(self) -> list[str]:
        Dados = []
        Pontos = []
        SetaEsquerda = self.driver.find_element(By.CLASS_NAME, "navegacao-fase__seta-esquerda")
        SetaDireita = self.driver.find_element(By.CLASS_NAME, "navegacao-fase__seta-direita")
        for _ in range(6):
            SetaEsquerda.click()
        SetaDireita.click()
        Posiçoes = self.driver.find_elements(By.CLASS_NAME, "classificacao__equipes--posicao")
        Nomes = self.driver.find_elements(By.CLASS_NAME, "classificacao__equipes--time")
        for n in range(1,9):
            Pontos = Pontos + self.driver.find_element(By.XPATH, f"//*[@id='classificacao__wrapper']/article[{n}]/section[1]/div/table[2]/tbody").text.split("\n")
        for posição, nome, pontos in zip(Posiçoes, Nomes, Pontos):
            Dados.append([posição.text, nome.text, pontos])
        return Dados

    def Eliminatorias(self, etapa:str) -> list[str]:
        if not isinstance(etapa, str):
            raise TypeError("O parâmetro 'etapa' deve ser uma string")
        Dados = []
        SetaEsquerda = self.driver.find_element(By.CLASS_NAME, "navegacao-fase__seta-esquerda")
        SetaDireita = self.driver.find_element(By.CLASS_NAME, "navegacao-fase__seta-direita")
        for _ in range(6):
            SetaDireita.click()
        try:
            for _ in range(self.etapas.get(etapa)):
                SetaEsquerda.click()
        except:
            return ["Parâmetro 'etapa' Inválido, verifique os parâmetros permitidos na documentação"]
        Placares = self.driver.find_elements(By.CLASS_NAME, "placar")
        for placar in Placares:
            Dados.append(placar.text.split("\n"))
        return Dados
