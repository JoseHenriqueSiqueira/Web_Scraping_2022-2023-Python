from selenium.webdriver.common.by import By
from ChromeWebDriver import ChromeDriver

class TopônimosGentilicos(ChromeDriver):
    def __init__(self):
         super().__init__()
         self.driver.get('http://funag.gov.br/manual/index.php?title=Top%C3%B4nimos_e_gent%C3%ADlicos')

    def informacoes_completas(self):
        Dados = []
        linhas = self.driver.find_elements(By.XPATH, "//*[@id='mw-content-text']/div/table/tbody/tr")
        for linha in linhas[1:]:
            colunas = linha.find_elements(By.XPATH, "td")
            informacao_temporaria = [coluna.text for coluna in colunas[:4]]
            Dados.append(informacao_temporaria)
        return Dados

    def procurar_pais(self, NomeDoPais: str) -> list[str]:
        ERRO = [f"Não foi possível encontrar informações sobre o país '{NomeDoPais}', verifique se o nome está correto."]
        if not isinstance(NomeDoPais, str):
            raise TypeError("O parâmetro deve ser uma string representando o nome do país.")
        if NomeDoPais == "o":
            return ERRO
        try:
            linha = self.driver.find_element(By.XPATH, f"//*[@id='mw-content-text']/div/table/tbody/tr[td[contains(text(), '{NomeDoPais}')]]")
            colunas = linha.find_elements(By.XPATH, "td[position() <= 4]")
            dados = [coluna.text for coluna in colunas]
            return dados
        except:
            return ERRO