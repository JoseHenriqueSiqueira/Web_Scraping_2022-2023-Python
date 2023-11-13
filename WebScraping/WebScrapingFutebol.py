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

class ChampionsLeague():
    """
    Classe para obter informações sobre a Champions League.
    """

    def __playoffs(self, resposta):
        return self.__gerar_dados_jogos(resposta)
    
    def __grupos(self, resposta):

        dados = [
            {
                'Grupo': grupo['nome_grupo'],
                'Classificacao': [
                    {
                        'Nome': time['nome_popular'],
                        'Variacao': time['variacao'],
                        'Pontos': time['pontos'],
                        'Jogos': time['jogos'],
                        'Vitorias': time['vitorias'],
                        'Empates': time['empates'],
                        'Derrotas': time['derrotas'],
                        'Gols_pro': time['gols_pro'],
                        'Gols_contra': time['gols_contra'],
                        'Saldo_gols': time['saldo_gols'],
                        'Aproveitamento': time['aproveitamento'],
                        'Ultimos_jogos': time['ultimos_jogos'],
                    }
                    for time in grupo['classificacao']
                ]
            }
            for grupo in resposta['grupos']
        ]


        return dados
    
    def __oitavas(self, resposta):
        return self.__gerar_dados_jogos(resposta)

    def __quartas(self, resposta):

        dados = [
            {
                'Primeiro_Jogo' if index == 0 else 'Segundo_Jogo': 
                {
                    'Mandante': partida['equipes']['mandante'].get('nome_popular'),
                    'Visitante': partida['equipes']['visitante'].get('nome_popular'),
                    'Data_realizacao': partida['data_realizacao'],
                    'Horario_realizacao': partida['hora_realizacao'],
                    'Jogo_rolando': partida['jogo_ja_comecou'],
                    'Placar_mandante': partida['placar_oficial_mandante'],
                    'Placa_visitante': partida['placar_oficial_visitante'],
                    'Placar_penaltis_mandante': partida['placar_penaltis_mandante'],
                    'Placar_penaltis_visitante': partida['placar_penaltis_visitante'],
                }
                for index, partida in enumerate(chave['jogos'])
            }
            for jogo in resposta['secao']
            for chave in jogo['chave']
        ]

        return dados

    def __semifinal(self, resposta):
        return self.__gerar_dados_jogos(resposta)

    def __final(self, resposta):

        partida = resposta['secao'][0]['chave'][0]['jogos'][0]

        dados = {
                    'Final': 
                    {
                        'Mandante': partida['equipes']['mandante'].get('nome_popular') or partida['equipes']['mandante'].get('label'),
                        'Visitante': partida['equipes']['visitante'].get('nome_popular', 'label') or partida['equipes']['visitante'].get('label'),
                        'Data_realizacao': partida['data_realizacao'],
                        'Horario_realizacao': partida['hora_realizacao'],
                        'Jogo_rolando': partida['jogo_ja_comecou'],
                        'Placar_mandante':partida['placar_oficial_mandante'],
                        'Placa_visitante': partida['placar_oficial_visitante'],
                        'Placar_penaltis_mandante': partida['placar_penaltis_mandante'],
                        'Placar_penaltis_visitante': partida['placar_penaltis_visitante'],
                    }
                }
            
        return dados

    def __fase(self, etapa: str):

        fase = {
            'playoffs':'playoffs-liga-dos-campeoes-2023-2024',
            'grupos':'fase-de-grupos-liga-dos-campeoes-2023-2024',
            'oitavas':'oitavas-liga-dos-campeoes-2023-2024',
            'quartas':'quartas-liga-dos-campeoes-2023-2024',
            'semi_final':'semifinal-liga-dos-campeoes-2023-2024',
            'final':'final-liga-dos-campeoes-2023-2024',
        }

        return fase.get(etapa)

    def __api(self, etapa:str):

        fase = self.__fase(etapa)

        url = f"https://api.globoesporte.globo.com/tabela/18a2ea40-9c94-4098-a183-ca69f79c5548/fase/{fase}/classificacao/"

        resposta = requests.get(url).json()

        return resposta

    def __gerar_dados_jogos(self, resposta):

        dados = [
            {
                'Primeiro_Jogo' if index == 0 else 'Segundo_jogo': 
                {
                    'Mandante': partida['equipes']['mandante'].get('nome_popular') or partida['equipes']['mandante'].get('label'),
                    'Visitante': partida['equipes']['visitante'].get('nome_popular') or partida['equipes']['visitante'].get('label'),
                    'Data_realizacao': partida['data_realizacao'],
                    'Horario_realizacao': partida['hora_realizacao'],
                    'Jogo_rolando': partida['jogo_ja_comecou'],
                    'Placar_mandante':partida['placar_oficial_mandante'],
                    'Placa_visitante': partida['placar_oficial_visitante'],
                    'Placar_penaltis_mandante': partida['placar_penaltis_mandante'],
                    'Placar_penaltis_visitante': partida['placar_penaltis_visitante'],
                }
                for index, partida, in enumerate(jogo['jogos'])
            }
            for jogo in resposta['secao'][0]['chave']
        ]

        return dados

    def fase(self, etapa:str) -> list[dict[str, int, bool]]:
        """
        Método para obter informações completas de uma determinada fase da Champions League.

        ### Parâmetros
        etapa (str): Etapa da Champions League. Valores permitidos ['playoffs', 'grupos', 'oitavas', 'quartas', 'semi_final', 'final']
        
        ### Retorno :
        list: Uma lista de dicionários representando informações sobre a fase especificada.

        ### Exemplos :
        >>> playoffs = ChampionsLeague().fase('playoffs')\n
        >>> print(*playoffs, sep='\\n')
        {'Primeiro_Jogo': {'Mandante': str, 'Visitante': str, 'Data_realizacao': str or None, 'Horario_realizacao': str or None, 'Jogo_rolando': bool or None, 'Placar_mandante': int or None, 'Placa_visitante': int or None, 'Placar_penaltis_mandante': int or None, 'Placar_penaltis_visitante': int or None}, 'Segundo_jogo': {'Mandante': str, 'Visitante': str, 'Data_realizacao': str or None, 'Horario_realizacao': str, 'Jogo_rolando': bool or None, 'Placar_mandante': int or None, 'Placa_visitante': int or None, 'Placar_penaltis_mandante': int or None, 'Placar_penaltis_visitante': int or None}}\n
        """

        fase_funcoes = {
            'playoffs': self.__playoffs,
            'grupos': self.__grupos,
            'oitavas': self.__oitavas,
            'quartas': self.__quartas,
            'semi_final': self.__semifinal,
            'final': self.__final
        }

        if etapa in fase_funcoes:
            resposta = self.__api(etapa)
            return fase_funcoes[etapa](resposta)
        else:
            # Tratamento para fase inválida
            raise ValueError("Fase inválida. Fases disponíveis ['playoffs', 'grupos', 'oitavas', 'quartas', 'semi_final', 'final']") 

class Brasileirao(EdgeDriver):
    """
    Classe para obter informações sobre o Campeonato Brasileiro.
    """
    def __init__(self, ano:str, web:bool = False) -> None:
        """
        ### Parâmetros:
            ano (str): O ano do campeonato.
            web (bool): Se definido como True, os valores dos atributos 'uuid' e 'fase' serão adquiridos por meio de web scraping. No entanto, é importante notar que habilitar essa opção pode aumentar ligeiramente o tempo de execução do código devido à necessidade de raspar informações online. Recomenda-se usar essa opção somente se ocorrer alguma exceção nos métodos 'tabela_classificacao' e 'jogos_rodada'. Caso seja definido como False, os valores de 'uuid' e 'fase' serão obtidos a partir dos métodos privados '__uuid' e '__fase', onde esses valores foram previamente declarados diretamente no código.

        ### Raises:
            TypeError: Se o parâmetro 'ano' não for uma str.
            ValueError: Se o ano não estiver no intervalo permitido [2003 ... 2023].
            Exception: Se as informações do campeonato brasileiro 2022 ainda não estiverem disponíveis.
        """

        if not isinstance(web, bool): # Verifica se o parâmetro 'web' é uma instância de bool.
            raise TypeError("Parâmetro 'web' deve ser bool") 

        if not isinstance(ano, str): # Verifica se o parâmetro 'ano' é uma instância de str.
            raise TypeError("Parâmetro 'ano' deve ser str") # Caso contrário, levanta uma exceção do tipo TypeError.
        
        ANOS_PERMITIDOS = list(map(str, range(2003, 2024))) # Gera uma lista com os anos onde o brasileirão é por pontos corridos.

        if ano not in ANOS_PERMITIDOS: # Verifica se o valor do parâmetro 'ano' esta presente na lista dos anos permitidos
            raise ValueError(f"Ano inválido. Permitidos [2003 ... 2023]") # Caso contrário, levanta uma exceção do tipo ValueError.
        
        if ano == '2022': # Se o ano for 2022 o GE não disponibiliza as informações desse ano em especifico.
            raise Exception("Informações do campeonato brasileiro 2022 ainda nao disponiveis") # Lança uma exceção
        
        if web: # Se o parâmetro web estiver ativo, começa a raspagem de dados.
            url = f'https://ge.globo.com/futebol/brasileirao-serie-a/{ano}' if ano != '2023' else 'https://ge.globo.com/futebol/brasileirao-serie-a/'
            super().__init__()
            self.driver.get(url)
            self.uuid = self.driver.execute_script("return window.cdaaas.PAGE_ANALYTICS_DATA.contentId") # Retorna o UUID da API
            self.fase = self.driver.execute_script("return fase.slug") # Retorna o slug da fase para ser usado na URL da API.
            self.rodada_maxima = self.driver.execute_script("return classificacao['rodada']['ultima']") # Retorna o maximo de rodadas que o brasileirão informado tem.
            self.driver.quit() # Fecha a página.
        else: # Caso contrário, obtem as informações dos metodos privados
            self.uuid = self.__uuid(ano) # uuid do ano
            self.fase = self.__fase(ano) # fase do ano
            self.rodada_maxima = self.__rodada_maxima(ano) # rodada maxima do ano

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

        url = f"https://api.globoesporte.globo.com/tabela/{self.uuid}/fase/{self.fase}/classificacao/" # Monta a URL da API baseado nos atributos obtidos pelo o constructor.

        resposta = requests.get(url).json() # Faz a requisição e retorna em formato json.

        tabela = resposta['classificacao'] # Obtem a classificação da resposta

        dados = [ # Trata os dados para retornar ao usuario
            {
                'Posição': time['ordem'],
                'Nome': time['nome_popular'],
                'Variacao': time['variacao'],
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
        
        if rodada < 0 or rodada > self.rodada_maxima:
            raise IndexError(f"Rodada {rodada} é inválida. Rodada máxima para o ano informado é {self.rodada_maxima}")
        
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

    def __uuid(self, ano):

        uuid = {
            '2003':'3cbd93c7-1cae-4587-9e5e-300b7b28c25e',
            '2004':'8bc68a7e-69ce-4218-9c92-47297c36fde7',
            '2005':'6672602f-d469-434f-8231-926eb284b20c',
            '2006':'23d47850-5375-422b-bd58-a40823ce9c49',
            '2007':'4e1f3549-5868-42ec-b888-78a1f8bf7156',
            '2008':'2ac146a7-474f-4fd8-be77-6112c7016fc5',
            '2009':'51009819-6615-4a69-873d-2be586c6ad17',
            '2010':'c4e512d6-f170-4e35-96b2-fc85f0b2ecac',
            '2011':'4c05a679-3b3d-4036-8b38-6d7ded7f1670',
            '2012':'abb77901-ff1c-4502-8f48-e6851ac72ee7',
            '2013':'33923171-7ffd-4df6-b073-c757ba8c5783',
            '2014':'561a7104-abf4-4697-a718-58c4f26abc59',
            '2015':'bdda776d-fd7c-40d6-8bac-ebda2cdcc803',
            '2016':'46cc94c8-273c-4278-973b-277d6a7e344b',
            '2017':'59182bf8-6b52-4813-a383-6e092a03ba70',
            '2018':'57a79106-70d1-4888-a0da-dc086c404eb3',
            '2019':'8caa2df1-2eaa-4df4-8155-eae19951d294',
            '2020':'73935bac-bbc6-4254-9cf9-8e87a0c3e66d',
            '2021':'2beec312-9c9d-4923-ba01-1bb57788a4d1',
            '2023':'d1a37fa4-e948-43a6-ba53-ab24ab3a45b1',
        }

        return uuid.get(ano)

    def __fase(self, ano):

        fase = {
            '2003':f'fase-unica-brasileiro-{ano}',
            '2004':f'fase-unica-brasileiro-{ano}',
            '2005':f'fase-unica-brasileiro-{ano}',
            '2006':f'fase-unica-brasileiro-{ano}',
            '2007':f'fase-unica-brasileiro-{ano}',
            '2008':f'fase-unica-brasileiro-{ano}',
            '2009':f'fase-unica-brasileiro-{ano}',
            '2010':f'fase-unica-brasileiro-{ano}',
            '2011':f'fase-unica',
            '2012':f'fase-unica',
            '2013':f'fase-unica',
            '2014':f'fase-unica-brasileiro-{ano}',
            '2015':f'fase-unica-brasileiro-{ano}',
            '2016':f'fase-unica-seriea-{ano}',
            '2017':f'fase-unica-seriea-{ano}',
            '2018':f'fase-unica-seriea-{ano}',
            '2019':f'fase-unica-seriea-{ano}',
            '2020':f'fase-unica-seriea-{ano}',
            '2021':f'fase-unica-campeonato-brasileiro-{ano}',
            '2023':f'fase-unica-campeonato-brasileiro-{ano}',
        }

        return fase.get(ano)

    def __rodada_maxima(self, ano):

        rodada_maxima = {
            '2003': 46,
            '2004': 46,
            '2005': 42,
            '2006': 38,
            '2007': 38,
            '2008': 38,
            '2009': 38,
            '2010': 38,
            '2011': 38,
            '2012': 38,
            '2013': 38,
            '2014': 38,
            '2015': 38,
            '2016': 38,
            '2017': 38,
            '2018': 38,
            '2019': 38,
            '2020': 38,
            '2021': 38,
            '2023': 38,
        }

        return rodada_maxima.get(ano)

class CopaDoMundo(EdgeDriver):

    def __init__(self, ano:str):

        if not isinstance(ano, str):
            raise TypeError("Parâmetro 'ano' deve ser uma string")
        
        ANOS_PERMITIDOS = list(map(str, range(1986, 2023, 4)))
        if ano not in ANOS_PERMITIDOS:
            raise ValueError(f"Ano inválido. Permitidos {ANOS_PERMITIDOS}")
        
        # self.driver.set_window_size(1920, 1080)
        # self.driver.get(f'https://ge.globo.com/futebol/copa-do-mundo/{ano}/')
        # print(f"'{ano}':'{self.driver.execute_script('return classificacao.fases_navegacao[3].slug')}'")
        # self._seta_esquerda = self.driver.find_elements(By.CLASS_NAME, "navegacao-fase__seta-esquerda")
        # self._seta_direita = self.driver.find_elements(By.CLASS_NAME, "navegacao-fase__seta-direita")
        # self.wait = WebDriverWait(self.driver, 15)
        self.__ano = ano
        self.__uuid = self.__get_uuid()

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

    def __get_uuid(self):

        uuid = {
            '1986':'285c65d6-a317-4a9b-8745-7efe67253321',
            '1990':'a6edb381-ad63-45f2-8623-df281713b980',
            '1994':'cb31e4cb-4dfd-48e6-a3d6-affc92e98010',
            '1998':'fcc0471d-d5c6-42a1-a995-1b58c0c6c457',
            '2002':'de0db72b-545f-475a-9199-25128ef3a7e5',
            '2006':'bb9bfc08-516c-44be-8459-2a431d5e8138',
            '2010':'3ef474f2-40f1-4f83-8157-53490ce9b8ea',
            '2014':'901a924d-e1f7-40d3-a07d-77a20e736bd9',
            '2018':'f3b28e3c-d61b-4ae3-a970-36501dbd2140',
            '2022':'d91a3f90-c034-407a-a94f-84771a7b3783',
        }

        return uuid.get(self.__ano)

    def __fase_grupos(self):

        if self.__ano == '1998':
            return 'copa98-primeira-fase'
        if self.__ano == '2006':
            return 'copa2006-primeira-fase'
        if self.__ano == '2010':
            return 'primeira-fase'
        
        return f"fase-grupos-copa-do-mundo-{self.__ano}"
    
    def __fase_oitavas(self):

        if self.__ano == '1998':
            return 'copa98-oitavas'
        if self.__ano == '2006':
            return 'copa2006-oitavas'
        if self.__ano == '2010':
            return 'oitavas-de-final'
        
        return f"oitavas-copa-do-mundo-{self.__ano}"

    def __fase_quartas(self):

        if self.__ano == '1998':
            return 'copa98-quartas'
        if self.__ano == '2006':
            return 'copa2006-quartas'
        if self.__ano == '2010':
            return 'quartas-de-final'
        
        return f"quartas-copa-do-mundo-{self.__ano}"

    def __fase_semi_final(self):

        if self.__ano == '1998':
            return 'copa98-semifinal'
        if self.__ano == '2006':
            return 'copa2006-semifinal'
        if self.__ano == '2010':
            return 'semifinal'
        
        return f"semifinal-copa-do-mundo-{self.__ano}"

    def __fase_terceiro(self):
        return f"terceiro-copa-do-mundo-{self.__ano}"

    def __fase_final(self):

        if self.__ano == '1998':
            return 'copa98-final'
        if self.__ano == '2006':
            return 'copa2006-final'
        if self.__ano == '2010':
            return 'final'
        
        return f"final-copa-do-mundo-{self.__ano}"

    def __fase(self, etapa):

        fase = {
            'playoffs':'playoffs-liga-dos-campeoes-2023-2024',
            'grupos': self.__fase_grupos(),
            'oitavas': self.__fase_oitavas(),
            'quartas': self.__fase_quartas(),
            'semi_final': self.__fase_semi_final(),
            'terceiro': self.__fase_terceiro(),
            'final': self.__fase_final(),
        }

        return fase.get(etapa)

    def test(self, etapa):

        fase = self.__fase(etapa)
        url = f"https://api.globoesporte.globo.com/tabela/{self.__uuid}/fase/{fase}/classificacao/"
        resposta = requests.get(url).json()
        return resposta['fase']['slug']

if __name__ == "__main__":
    anos = ['1986', '1990', '1994', '1998', '2002', '2006', '2010', '2014', '2018', '2022']
    test = CopaDoMundo('2022')
    for ano in anos:
       print(CopaDoMundo(ano).test('grupos'))
       print(CopaDoMundo(ano).test('oitavas'))
       print(CopaDoMundo(ano).test('quartas'))
       print(CopaDoMundo(ano).test('semi_final'))
       print(CopaDoMundo(ano).test('terceiro'))
       print(CopaDoMundo(ano).test('final'))
    # copa = CopaDoMundo('2022')
    # print(copa.test(), sep='\n\n')
