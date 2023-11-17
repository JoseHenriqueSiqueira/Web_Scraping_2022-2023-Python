from selenium.webdriver.common.by import By
from EdgeWebDriver import EdgeDriver

class TopônimosGentilicos(EdgeDriver):
    def __init__(self):
         super().__init__()
         self.driver.get('http://funag.gov.br/manual/index.php?title=Top%C3%B4nimos_e_gent%C3%ADlicos')

    def informacoes_completas(self) -> list[tuple[str]]:
        dados = []
        for linha in self.driver.find_elements(By.CSS_SELECTOR, "table.wikitable tbody tr")[1:]:
            dados.append(tuple([coluna.text for coluna in linha.find_elements(By.TAG_NAME, "td")[:4]]))
        return dados

    def procurar_pais(self, NomeDoPais: str) -> list[tuple[str]]:
        if not isinstance(NomeDoPais, str):
            raise TypeError("O parâmetro deve ser uma string representando o nome do país.")
        ERRO = f"Não foi possível encontrar informações sobre o país '{NomeDoPais}', verifique se o nome está correto."
        if NomeDoPais == "o":
            raise ValueError(ERRO)
        try:
            linha = self.driver.find_element(By.XPATH, f"//*[@id='mw-content-text']/div/table/tbody/tr[td[contains(text(), '{NomeDoPais}')]]")
            colunas = linha.find_elements(By.XPATH, "td[position() <= 4]")
            dados = tuple([coluna.text for coluna in colunas])
            return dados
        except:
            raise Exception(ERRO)
