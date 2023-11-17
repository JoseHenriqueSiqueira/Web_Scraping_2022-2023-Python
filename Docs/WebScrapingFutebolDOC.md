## class ChampionsLeague (ChromeWebDriver):
### def __init\__():
Método construtor da classe, referência para os demais métodos.
   
### def fase_de_grupos() :
Método responsável por obter a classificação geral e pontos gerais de todos os grupos da Champions League 2022/2023.
|Retorno| Tipo       | Descrição                                   |
|-------| :--------- | :------------------------------------------ |
|`dados`| `list` | Retorna uma lista de tuplas, onde cada tupla contém um conjunto de strings.|

### def eliminatorias(etapa) :
Método responsavel por obter jogos e placares de uma etapa específica passada como parâmetro pelo usuário
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `etapa`      | `string` | **Obrigatório**. Esse parâmetro é responsavel por qual fase da Champions League você quer ter informações. Aceitando valores "Final", "SemiFinal", "Quartas", "Oitavas".|

|Retorno| Tipo       | Descrição                                   |
|-------| :--------- | :------------------------------------------ |
|`dados`| `list` | Retorna uma lista de tuplas, onde cada tupla contém um conjunto de strings.|

## class Brasileirao (ChromeWebDriver):
### def __init\__(ano):
Método construtor da classe, referência para os demais métodos.
   | Parâmetro   | Tipo       | Descrição                                   |
   | :---------- | :--------- | :------------------------------------------ |
   | `ano`      | `string` | **Obrigatório**. Esse parâmetro é responsavel por qual edição do Brasileirão você quer ter informações. Aceitando valores de '2003' a '2023'.|
   
### def tabela_classificacao() :
Método responsavel para obter informações da tabela de classificação.
|Retorno| Tipo       | Descrição                                   |
|-------| :--------- | :------------------------------------------ |
|`dados`| `list` | Retorna uma lista de tuplas, onde cada tupla contém um conjunto de strings.|

### def rodadas(rodada) :
Método responsavel para obter placares de uma rodada passada como parâmetro pelo usuário.
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `rodada`      | `int` | **Obrigatório**. Valores aceitos: '1' a '38'.|

|Retorno| Tipo       | Descrição                                   |
|-------| :--------- | :------------------------------------------ |
|`dados`| `list` | Retorna uma lista de tuplas, onde cada tupla contém um conjunto de strings.|

## class CopaDoMundo (ChromeWebDriver):
### def __init\__(ano):
Método construtor da classe, referência para os demais métodos.
   | Parâmetro   | Tipo       | Descrição                                   |
   | :---------- | :--------- | :------------------------------------------ |
   | `ano`      | `string` | **Obrigatório**. Esse parâmetro é responsavel por qual edição da Copa Do Mundo você quer ter informações. Aceitando valores de '1986' a '2022'. Os valores devem ser fornecidos em intervalos de quatro em quatro anos. Por exemplo. '1986', '1990', '1994', etc.|
   
### def fase_de_grupos() :
Método responsável por obter a classificação geral e pontos gerais de todos os grupos da Copa Do Mundo.
|Retorno| Tipo       | Descrição                                   |
|-------| :--------- | :------------------------------------------ |
|`dados`| `list` | Retorna uma lista de tuplas, onde cada tupla contém um conjunto de strings.|

### def eliminatorias(etapa) :
Método responsavel por obter jogos e placares de uma etapa específica passada como parâmetro pelo usuário
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `etapa`      | `string` | **Obrigatório**. Esse parâmetro é responsavel por fase da Copa Do Mundo você quer ter informações. Aceitando valores "Final", "TerceiroLugar", "SemiFinal", "Quartas", "Oitavas".|

|Retorno| Tipo       | Descrição                                   |
|-------| :--------- | :------------------------------------------ |
|`dados`| `list` | Retorna uma lista de tuplas, onde cada tupla contém um conjunto de strings.|
