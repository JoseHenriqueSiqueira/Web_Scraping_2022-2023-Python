from selenium.webdriver.common.by import By
from ChromeWebDriver import ChromeDriver
from EdgeWebDriver import EdgeDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

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

class ChampionsLeague2023(EdgeDriver):
    def __init__(self):
        super().__init__()
        self.driver.get("https://ge.globo.com/futebol/futebol-internacional/liga-dos-campeoes/")
        self.driver.set_window_size(1920, 1080)
        self._seta_esquerda = self.driver.find_elements(By.CLASS_NAME, "navegacao-fase__seta-esquerda")
        self._seta_direita = self.driver.find_elements(By.CLASS_NAME, "navegacao-fase__seta-direita")
        self.wait = WebDriverWait(self.driver, 15)

    def fase_de_grupos(self) -> list[tuple[str]]:
        for seta in self._seta_esquerda:
            while "navegacao-fase__setas-ativa" in seta.get_attribute("class"):
                self.wait.until(EC.element_to_be_clickable(seta))
                seta.click()
        self.wait.until(EC.element_to_be_clickable(self._seta_direita[0]))
        self._seta_direita[0].click()
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
        for seta in self._seta_direita:
            while "navegacao-fase__setas-ativa" in seta.get_attribute("class"):
                self.wait.until(EC.element_to_be_clickable(seta))
                seta.click()
        for _ in range(num_cliques):
            self.wait.until(EC.element_to_be_clickable(self._seta_esquerda[0]))
            self._seta_esquerda[0].click()
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'placar')))
        placares = self.driver.find_elements(By.CLASS_NAME, "placar")
        dados = [tuple(placar.text.split('\n')) for placar in placares]
        return dados

class Brasileirao(EdgeDriver):
    """
    Classe para obter informações sobre o Campeonato Brasileiro.
    """
    def __init__(self, ano:str) -> None:
        """
        ### Parâmetros:
            ano (str): O ano do campeonato.

        ### Raises:
            TypeError: Se o parâmetro 'ano' não for uma string.
            ValueError: Se o ano não estiver no intervalo permitido [2003 ... 2023].
            Exception: Se as informações do campeonato brasileiro 2022 ainda não estiverem disponíveis.
        """
            
        super().__init__()
        if not isinstance(ano, str):
            raise TypeError("Parâmetro 'ano' deve ser uma string")
        
        ANOS_PERMITIDOS = list(map(str, range(2003, 2024)))
        if ano not in ANOS_PERMITIDOS:
            raise ValueError(f"Ano inválido. Permitidos [2003 ... 2023]")
        
        if ano == '2022':
            raise Exception("Informações do campeonato brasileiro 2022 ainda nao disponiveis")
        url = f'https://ge.globo.com/futebol/brasileirao-serie-a/{ano}' if ano != '2023' else 'https://ge.globo.com/futebol/brasileirao-serie-a/'
        self.driver.get(url)
        self.uuid = self.driver.execute_script("return window.cdaaas.PAGE_ANALYTICS_DATA.contentId")
        self.fase = self.driver.execute_script("return fase.slug")
    
    def tabela_classificacao(self) -> list[dict[int, str]]:
        """
        Método para obter a classificação completa do ano do brasilerão especificado no constructor

        ### Retorno :
        list: Uma lista de dicionários representando a tabela do Brasileirão. Cada dicionário contém informações sobre um time.

        ### Exemplos :
        >>> tabela = Brasileirao(ano = str).tabela_classificacao()\n
        >>> print(*tabela, sep='\\n')
        {'Posição': int, 'Nome': str, 'Pontos': int, 'Jogos': int, 'Vitorias': int, 'Empates': int, 'Derrotas': int, 'Gols_Pro': int, 'Gols_Contra': int, 'Saldo_Gols': int, 'Aproveitamento': int, 'Ultimos_Jogos': [str, str, str, str, str]}\n
        """

        url = f"https://api.globoesporte.globo.com/tabela/{self.uuid}/fase/{self.fase}/classificacao/"
        resposta = requests.get(url).json()

        tabela = resposta['classificacao']

        dados = [
            {
                'Posição': time['ordem'],
                'Nome': time['nome_popular'],
                'Pontos': time['pontos'],
                'Jogos': time['jogos'],
                'Vitorias': time['vitorias'],
                'Empates': time['empates'],
                'Derrotas': time['derrotas'],
                'Gols_Pro': time['gols_pro'],
                'Gols_Contra': time['gols_contra'],
                'Saldo_Gols': time['saldo_gols'],
                'Aproveitamento': time['aproveitamento'],
                'Ultimos_Jogos': time['ultimos_jogos']
            }
            for time in tabela
        ]

        return dados

    def jogos_rodada(self, rodada:int) -> list[dict[int, str]]:
        """
        Método para obter os jogos de uma determinada rodada:

        ### Parâmetros
        rodada (int): Rodada do campeonato

        ### Retorno :
        list: Uma lista de dicionários representando um jogo da rodada. Cada dicionário contém informações sobre o jogo.

        ### Exemplos :
        >>> rodada = Brasileirao(ano = str).jogos_rodada(rodada = int)\n
        >>> print(*rodada, sep='\\n')
        {'Mandante': str, 'Visitante': str, 'Data_realizacao': str, 'Horario_realizacao': str or None, 'Jogo_rolando': bool or None, 'Placar_mandante': int or None, 'Placar_visitante': int or None, 'Placar_penaltis_mandante': int or None, 'Placar_penaltis_visitante': int or None, 'Estadio': str or None}\n
        ...
        """

        if not isinstance(rodada, int):
            raise TypeError("O parâmetro 'rodada' deve ser um inteiro")
        
        rodada_maxima = self.driver.execute_script("return classificacao['rodada']['ultima']")
        if rodada < 0 or rodada > rodada_maxima:
            raise IndexError(f"Rodada {rodada} é inválida. Rodada máxima para o ano informado é {rodada_maxima}")
        
        url = f"https://api.globoesporte.globo.com/tabela/{self.uuid}/fase/{self.fase}/rodada/{rodada}/jogos/"
        resposta = requests.get(url).json()

        dados = [
            {
                'Mandante': jogo['equipes']['mandante'].get('nome_popular', ' '),
                'Visitante': jogo['equipes']['visitante'].get('nome_popular', ' '),
                'Data_realizacao': jogo.get('data_realizacao', ' '),
                'Horario_realizacao': jogo.get('hora_realizacao', ' '),
                'Jogo_rolando': jogo.get('jogo_ja_comecou', ' '),
                'Placar_mandante': jogo.get('placar_oficial_mandante',' '),
                'Placar_visitante': jogo.get('placar_oficial_visitante', ' '),
                'Placar_penaltis_mandante': jogo.get('placar_penaltis_mandante', ' '),
                'Placar_penaltis_visitante': jogo.get('placar_penaltis_visitante', ' '),
                'Estadio': jogo['sede']['nome_popular'] if jogo.get('sede') and jogo['sede'].get('nome_popular') else None
            }
            for jogo in resposta
        ]
        
        return dados

    def artilharia(self) -> list[dict[int, str]]:
        """
        Método para obter a lista da artilharia do campeonato brasileiro

        ### Retorno :
        list: Uma lista de dicionários representando um jogador da artilharia. Cada dicionário contém informações sobre o jogador.

        ### Exemplos :
        >>> rodada = Brasileirao(ano = str).artilharia()\n
        >>> print(*artilharia, sep='\\n')
        {'Ranking': int, 'Nome': str, 'Posição': str, 'Gols': int}\n
        ...
        """

        elementos = self.driver.find_elements(By.CLASS_NAME, 'ranking-item-wrapper')
        lista = [ jogador.text.replace('\n', ',').split(',') for jogador in elementos ]

        gols_anteriores = 0
        rank_anterior = 1

        dados = []

        for jogador in lista:
            gols = int(jogador[3] if len(jogador) > 3 else jogador[2])
            ranking_atual = rank_anterior + 1 if gols < gols_anteriores else rank_anterior
            dados.append({
                'Ranking': ranking_atual,
                'Nome': jogador[1] if len(jogador) > 3 else jogador[0],
                'Posição': jogador[2] if len(jogador) > 3 else jogador[1],
                'Gols': gols,
            })
            rank_anterior = ranking_atual
            gols_anteriores = int(gols)

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
        self._seta_esquerda = self.driver.find_elements(By.CLASS_NAME, "navegacao-fase__seta-esquerda")
        self._seta_direita = self.driver.find_elements(By.CLASS_NAME, "navegacao-fase__seta-direita")
        self.wait = WebDriverWait(self.driver, 15)

    def fase_de_grupos(self) -> list[tuple[str]]:
        for seta in self._seta_esquerda:
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
        for seta in self._seta_direita:
            while "navegacao-fase__setas-ativa" in seta.get_attribute("class"):
                self.wait.until(EC.element_to_be_clickable(seta))
                seta.click()
        for _ in range(num_cliques):
            self.wait.until(EC.element_to_be_clickable(self._seta_esquerda[0]))
            self._seta_esquerda[0].click()
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'placar')))
        placares = self.driver.find_elements(By.CLASS_NAME, "placar")
        dados = [tuple(placar.text.split('\n')) for placar in placares]
        return dados

if __name__ == "__main__":
    pass