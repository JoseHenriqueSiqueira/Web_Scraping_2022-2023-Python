
self.ranking = [element.text for element in self.driver.find_elements(By.CLASS_NAME, 'ranking-item-wrapper')] # Retorna o ranking daquele ano (Não formatado)

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

    if not self.ranking:
        self.__navegador(ano)



    lista = [ jogador.replace('\n', ',').split(',') for jogador in self.ranking ]

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

    def __init__(self):
        pass
       # super().__init__()
       # self.driver.get("https://ge.globo.com/futebol/futebol-internacional/liga-dos-campeoes/")
       # self.driver.set_window_size(1920, 1080)
       # self._seta_esquerda = self.driver.find_elements(By.CLASS_NAME, "navegacao-fase__seta-esquerda")
       # self._seta_direita = self.driver.find_elements(By.CLASS_NAME, "navegacao-fase__seta-direita")
       # self.wait = WebDriverWait(self.driver, 15)
       # self.uuid = self.driver.execute_script("return window.cdaaas.PAGE_ANALYTICS_DATA.contentId")

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