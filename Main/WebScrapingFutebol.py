from selenium.webdriver.common.by import By
from ChromeWebDriver import ChromeDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CopaDoBrasil2023(ChromeDriver):
    def __init__(self) -> None:
        super().__init__()
        self.driver.set_window_size(1920, 1080)
        self.driver.get("https://ge.globo.com/futebol/copa-do-brasil/")

    def etapa(self, etapa: str) -> list[tuple[str]]:
        if not isinstance(etapa, str):
            raise TypeError("O parâmetro 'etapa' deve ser uma string")
        etapas = {
            "PrimeiraFase":6, "SegundaFase":5, "TerceiraFase":4, "Oitavas":3, "Quartas":2, "SemiFinal":1, "Final":0
        }
        try:
            num_cliques = etapas[etapa]
        except:
            raise ValueError(f"Parâmetro 'etapa' Inválido: {etapa}. Verifique os parâmetros permitidos na documentação.")
        wait = WebDriverWait(self.driver, 15)
        seta_esquerda = self.driver.find_element(By.CLASS_NAME, "navegacao-fase__seta-esquerda")
        seta_direita = self.driver.find_elements(By.CLASS_NAME, "navegacao-fase__seta-direita")
        for seta in seta_direita:
            while "navegacao-fase__setas-ativa" in seta.get_attribute("class"):
                wait.until(EC.element_to_be_clickable(seta))
                seta.click()
        for _ in range(num_cliques):
            wait.until(EC.element_to_be_clickable(seta_esquerda))
            seta_esquerda.click()
        placares = self.driver.find_elements(By.CLASS_NAME, "placar") 
        dados = [tuple(placar.text.split('\n')) for placar in placares]
        return dados

class ChampionsLeague2023(ChromeDriver):
    def __init__(self):
        super().__init__()
        self.driver.get("https://ge.globo.com/futebol/futebol-internacional/liga-dos-campeoes/")
        self.driver.set_window_size(1920, 1080)
        self.seta_esquerda = self.driver.find_elements(By.CLASS_NAME, "navegacao-fase__seta-esquerda")
        self.seta_direita = self.driver.find_elements(By.CLASS_NAME, "navegacao-fase__seta-direita")
        self.wait = WebDriverWait(self.driver, 15)

    def fase_de_grupos(self) -> list[tuple[str]]:
        for seta in self.seta_esquerda:
            while "navegacao-fase__setas-ativa" in seta.get_attribute("class"):
                self.wait.until(EC.element_to_be_clickable(seta))
                seta.click()
        self.wait.until(EC.element_to_be_clickable(self.seta_direita[0]))
        self.seta_direita[0].click()
        Posiçoes = self.driver.find_elements(By.CLASS_NAME, "classificacao__equipes--posicao")
        Nomes = self.driver.find_elements(By.CLASS_NAME, "classificacao__equipes--time")
        Pontos = self.driver.find_elements(By.XPATH, f"//*[@id='classificacao__wrapper']/article[*]/section[1]/div/table[2]/tbody")
        Pontos = [ponto for pontos in Pontos for ponto in pontos.text.split('\n')]
        dados = [(posição.text, nome.text, pontos) for posição, nome, pontos in zip(Posiçoes, Nomes, Pontos)]
        return dados

    def eliminatorias(self, etapa:str) -> list[tuple[str]]:
        if not isinstance(etapa, str):
            raise TypeError("O parâmetro 'etapa' deve ser uma string")
        etapas = {
            "Final":0, "SemiFinal":1, "Quartas":2, "Oitavas":3
        }
        try:
            num_cliques = etapas[etapa]
        except:
            raise ValueError(f"Parâmetro 'etapa' Inválido: {etapa}. Verifique os parâmetros permitidos na documentação.")
        for seta in self.seta_direita:
            while "navegacao-fase__setas-ativa" in seta.get_attribute("class"):
                self.wait.until(EC.element_to_be_clickable(seta))
                seta.click()
        for _ in range(num_cliques):
            self.wait.until(EC.element_to_be_clickable(self.seta_esquerda[0]))
            self.seta_esquerda[0].click()
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'placar')))
        placares = self.driver.find_elements(By.CLASS_NAME, "placar")
        dados = [tuple(placar.text.split('\n')) for placar in placares]
        return dados

class Brasileirao(ChromeDriver):
    def __init__(self, ano:str) -> None:
        super().__init__()
        if not isinstance(ano, str):
            raise TypeError("Parâmetro 'ano' deve ser uma string")
        ANOS_PERMITIDOS = list(map(str, range(2003, 2024)))
        if ano not in ANOS_PERMITIDOS:
            raise ValueError(f"Ano inválido. Permitidos {ANOS_PERMITIDOS}")
        if ano == '2022':
            raise Exception("Informações do campeonato brasileiro 2022 ainda nao disponiveis")
        url = f'https://ge.globo.com/futebol/brasileirao-serie-a/{ano}' if ano != '2023' else 'https://ge.globo.com/futebol/brasileirao-serie-a/'
        self.driver.get(url)
    
    def tabela_classificacao(self) -> list[tuple[str]]:
        Posições = self.driver.find_elements(By.CLASS_NAME, "classificacao__equipes--posicao")
        Nomes = self.driver.find_elements(By.CLASS_NAME, "classificacao__equipes--nome")
        Pontos = self.driver.find_element(By.XPATH, "//*[@id='classificacao__wrapper']/article/section[1]/div/table[2]/tbody").text.split('\n')
        dados = [(posição.text, nome.text, pontos) for posição, nome, pontos in zip(Posições, Nomes, Pontos)]
        return dados

    def rodadas(self, rodada:int) -> list[tuple[str]]:
        if not isinstance(rodada, int):
            raise TypeError("O parâmetro 'rodada' deve ser um inteiro")
        rodada_maxima = int(self.driver.find_element(By.CLASS_NAME, "lista-jogos__navegacao--rodada").text.replace('ª RODADA',''))
        if rodada <= 0 or rodada > rodada_maxima:
            raise Exception(f"Parâmetro 'rodada' Inválido, verifique a documentação se necessário. Rodada maxima do Campeonato: '{rodada_maxima}'")  
        wait = WebDriverWait(self.driver, 15)   
        seta_esquerda = self.driver.find_element(By.CLASS_NAME, "lista-jogos__navegacao--seta-esquerda svg")
        for _ in range(rodada_maxima - (rodada)):
            wait.until(EC.element_to_be_clickable(seta_esquerda))
            seta_esquerda.click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'placar')))
        placares = self.driver.find_elements(By.CLASS_NAME, 'placar')
        dados = [tuple(placar.text.split('\n')) for placar in placares]
        return dados

class CopaDoMundo(ChromeDriver):
    def __init__(self, ano:str):
        super().__init__()
        if not isinstance(ano, str):
            raise TypeError("Parâmetro 'ano' deve ser uma string")
        ANOS_PERMITIDOS = list(map(str, range(1986, 2023, 4)))
        if ano not in ANOS_PERMITIDOS:
            raise ValueError(f"Ano inválido. Permitidos {ANOS_PERMITIDOS}")
        self.driver.set_window_size(1920, 1080)
        self.driver.get(f'https://ge.globo.com/futebol/copa-do-mundo/{ano}/')
        self.seta_esquerda = self.driver.find_elements(By.CLASS_NAME, "navegacao-fase__seta-esquerda")
        self.seta_direita = self.driver.find_elements(By.CLASS_NAME, "navegacao-fase__seta-direita")
        self.wait = WebDriverWait(self.driver, 15)

    def fase_de_grupos(self) -> list[tuple[str]]:
        for seta in self.seta_esquerda:
            while "navegacao-fase__setas-ativa" in seta.get_attribute("class"):
                self.wait.until(EC.element_to_be_clickable(seta))
                seta.click()
        Posiçoes = self.driver.find_elements(By.CLASS_NAME, "classificacao__equipes--posicao")
        Nomes = self.driver.find_elements(By.CLASS_NAME, "classificacao__equipes--time")
        Pontos = self.driver.find_elements(By.XPATH, f"//*[@id='classificacao__wrapper']/article[*]/section[1]/div/table[2]/tbody")
        Pontos = [ponto for pontos in Pontos for ponto in pontos.text.split('\n')]
        dados = [(posição.text, nome.text, pontos) for posição, nome, pontos in zip(Posiçoes, Nomes, Pontos)]
        return dados

    def eliminatorias(self, etapa:str) -> list[tuple[str]]:
        if not isinstance(etapa, str):
            raise TypeError("O parâmetro 'etapa' deve ser uma string")
        etapas = {
            "Final":0, "TerceiroLugar":1, "SemiFinal":2, "Quartas":3, "Oitavas":4
        }
        try:
            num_cliques = etapas[etapa]
        except:
            raise ValueError(f"Parâmetro 'etapa' Inválido: {etapa}. Verifique os parâmetros permitidos na documentação.")
        for seta in self.seta_direita:
            while "navegacao-fase__setas-ativa" in seta.get_attribute("class"):
                self.wait.until(EC.element_to_be_clickable(seta))
                seta.click()
        for _ in range(num_cliques):
            self.wait.until(EC.element_to_be_clickable(self.seta_esquerda[0]))
            self.seta_esquerda[0].click()
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'placar')))
        placares = self.driver.find_elements(By.CLASS_NAME, "placar")
        dados = [tuple(placar.text.split('\n')) for placar in placares]
        return dados