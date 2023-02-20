## class TopônimosGentilicos (ChromeWebDriver):
### def __init\__():
Método construtor da classe, referência para os demais métodos.
   
### def informacoes_completas():
Método responsavel por obter "Forma breve", "Nome oficial", "Capital" e  "Gentílico" de TODOS os países.
|Retorno| Tipo       | Descrição                                   |
|-------| :--------- | :------------------------------------------ |
|`dados`| `list` | Retorna uma lista de tuplas, onde cada tupla contém um conjunto de strings.|

### def procurar_pais(NomeDoPais):
Método responsavel por obter "Forma breve", "Nome oficial", "Capital" e  "Gentílico" de um único país.
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `NomeDoPais`| `string` | **Obrigatório**. Esse parâmetro é responsavel por qual país você quer ter informações.|

|Retorno| Tipo       | Descrição                                   |
|-------| :--------- | :------------------------------------------ |
|`dados`| `list` | Retorna uma lista de tuplas, onde cada tupla contém um conjunto de strings.|
