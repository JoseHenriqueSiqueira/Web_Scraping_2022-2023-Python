# Web_Scraping_2022/2023-Python
Este repositório tem como objetivo fornecer exemplos e técnicas de Web Scraping em Python, utilizando campeonatos de futebol e informações de países como casos de estudo. Aqui você pode aprender como obter informações para atender às suas necessidades, seja para criar um banco de dados, gerar gráficos ou fazer análises. Não esqueça de deixar seu feedback!!

![Update](https://img.shields.io/badge/update%20data-19%2F02%2F2023-brightgreen)

Duas classes criadas no *WebScrapingFutebol.py*. **Brasileirao** e **CopaDoMundo**</br>
       class Brasileirao(ano:str): Possui um parâmetro obrigatório 'ano'. Possui dois métodos, um chamado "tabela_classificacao" e "rodadas".
          'ano': parâmetro do tipo STR, aceitando valores de '2003' a '2023'. Esse parâmetro é responsavel por qual edição do Brasileirão você quer ter informações.
                tabela_classificacao() -> list[tuple[str]]: Esse método retorna a tabela geral de classificação dos times.
                rodadas(rodada:int) -> list[tuple[str]]: Esse método retorna todos os placares da rodada passada como parâmetro pelo usuário.
                    'rodada': parâmetro do tipo INT, aceitando valores de '1' a '38'.

       class CopaDoMundo(ano:str): Possui um parâmetro obrigatório 'ano'. Possui dois métodos, um chamado "fase_de_grupos" e "eliminatorias".
          'ano': parâmetro do tipo STR, aceitando valores de '1986' a '2022'. Os valores devem ser fornecidos em intervalos de quatro em quatro anos. Por exemplo. '1986', '1990', '1994', etc. Esse parâmetro é responsavel por qual edição da Copa Do Mundo você quer ter informações.
                fase_de_grupos() -> list[tuple[str]]: Esse método retorna a classificação geral e pontos gerais de todos os grupos da Copa Do Mundo.
                eliminatorias(etapa:str) -> list[tuple[str]]: Retorna os jogos e placares de uma etapa específica passada como parâmetro pelo usuário
                    'etapa': Parâmetro do tipo STR, aceitando individualmente um dos seguintes valores:
                        {"Final", "TerceiroLugar", "SemiFinal", "Quartas", "Oitavas"}

Atualizado o tipo de retorno de dados. Agora é retornado uma lista, contendo varias tuplas e cada tupla tem dados string</br>
Removido as classe **Brasileirão2022**  e **CopaDoMundo2022** do script *WebScrapingFutebol.py*</br>
Optimização das demais classes e métodos</br>




![Update](https://img.shields.io/badge/update%20data-13%2F02%2F2023-brightgreen)

   Criado o script **TopônimosGentílicosPaíses.py**, onde possui 1 classe. **TopônimosGentilicos**</br>

       class TopônimosGentilicos: Possui dois métodos, um chamado "informacoes_completas" e "procurar_pais".
            informacoes_completas(): Retorna uma list com  a "Forma breve", "Nome oficial", "Capital" e  "Gentílico" de TODOS os países.
            procurar_pais(NomeDoPais:str): Retorna uma list com  a "Forma breve", "Nome oficial", "Capital" e "Gentílico" do país passado como parâmetro pelo o usuário.

   Criado o script **ChromeWebDriver.py**, onde possui 1 classe. **ChromeDriver**</br>
        Obs: Essa mudança é para tornar mais organizado, assim não precisando criar essa mesma classe para cada script.

        class ChromeDriver: Criada para optimizar o código e evitar que o usuário baixe o driver toda vez que for utilizar o script, assim deixando o script mais rapido e mais organizado.

Removido a classe **ChromeDriver** do script *WebScrapingFutebol*
Removido os scripts de Exemplos. Eles não estavam bem programados, e não tinha muita utilidade. Caso algum usuário necessite um exemplo, eu adiciono ao repositório.




![Update](https://img.shields.io/badge/update%20data-09%2F02%2F2023-brightgreen)

   Criado o script **WebScrapingFutebol.py**, onde possui 4 classes. **CopaDoBrasil2023**, **Brasileirão2022**, **CopaDoMundo2022** e **ChromeDriver**</br>
   
        class CopaDoBrasil2023: Possui um método chamado "Etapa".
            Etapa(etapa:str): Retorna os jogos, chave e placares de uma etapa específica passada como parâmetro pelo usuário
                'etapa': Parâmetro do tipo STR, aceitando individualmente um dos seguintes valores:
                    {"PrimeiraFase", "SegundaFase", "TerceiraFase", "Oitavas", "Quartas", "SemiFinal" e "Final"}

        class Brasileirão2022: Possui dois métodos, um chamado "TabelaClassificação" e "Rodadas".
            TabelaClassificação(): Esse método retorna a tabela geral de classificação dos times.
            Rodadas(rodada:int): Esse método retorna todos os placares da rodada passada como parâmetro pelo usuário.
                'rodada': parâmetro do tipo INT, aceitando valores de '1' a '38'.

        class CopaDoMundo2022: Possui dois métodos, um chamado "FaseDeGrupos" e "Eliminatorias".
            FaseDeGrupos(): Esse método retorna a classificação geral e pontos gerais de todos os grupos da Copa Do Mundo 2022.
            Eliminatorias(etapa:str): Retorna os jogos e placares de uma etapa específica passada como parâmetro pelo usuário
                'etapa': Parâmetro do tipo STR, aceitando individualmente um dos seguintes valores:
                    {"Final", "TerceiroLugar", "SemiFinal", "Quartas", "Oitavas"}
        
        class ChromeDriver: Criada para optimizar o código e evitar que o usuário baixe o driver toda vez que for utilizar o script, assim deixando o script mais rapido e mais organizado.
        
Obs: Todos os métodos retornam uma variável do tipo 'list'
Removido os arquivos "BrasileiraoMain.py" e "CopaDoMundo22Main.py", pois não são mais necessários no projeto.
Futuros Update: Atualizar os scripts exemplos, melhorar o Script "TopônimosGentílicosPaísesMain.py" (Possivelmente transformá-lo em uma Classe) e adicionar mais WebScraping.

## Requirements
 - [Python3.9](https://www.python.org/)
 - [Selenium](https://pypi.org/project/selenium/)
 - [Webdriver_manager](https://pypi.org/project/webdriver-manager/)
 - [Subprocess](https://docs.python.org/3/library/subprocess.html)
 - [os](https://docs.python.org/3/library/os.html)
 - [Google Chrome](https://www.google.com/intl/pt-BR/chrome/)

## Autores
[José Henrique da Silva Siqueira](https://www.linkedin.com/in/jos%C3%A9-henrique-siqueira-852664218/)

## Licença
   This project is licensed under the [MIT License](/LICENSE).

## Agradecimentos
[Globo Esporte](https://ge.globo.com/) - Site providencia informações sobre diversos campeonatos de futebol, assim sendo usado como base para algumas classes do projeto.