# Web_Scraping_2022/2023-Python
Este repositório é destinado ao aprendizado e demonstração de técnicas de Web Scraping em Python, usando como exemplo sites de futebol e de gentilicos. Aqui, você poderá encontrar informações relevantes sobre a Copa do Brasil 2023, como resultados e classificações, assim como dados sobre os gentilicos e topônimos de todos os países do mundo. Além disso, também serão disponibilizadas informações detalhadas sobre a evolução do Campeonato Brasileiro 2022 e da Copa do Mundo 2022, desde as oitavas de final até a grande final. Este repositório é uma excelente fonte de conhecimento para aqueles que desejam se aprofundar no uso de Web Scraping com Python.

![Update](https://img.shields.io/badge/update%20data-13%2F02%2F2023-brightgreen)

   Criado o script **TopônimosGentílicosPaíses.py**, onde possui 1 classe. **TopônimosGentilicos**</br>

       class TopônimosGentilicos: Possui dois métodos, um chamado "informacoes_completas" e "procurar_pais".
            informacoes_completas(): Retorna uma list com  a "Forma breve", "Nome oficial", "Capital" e  "Gentílico" de TODOS os países.
            procurar_pais(NomeDoPais:str): Retorna uma list com  a "Forma breve", "Nome oficial", "Capital" e "Gentílico" do país passado como parâmetro pelo o usuário.

   Criado o script **ChromeWebDriver.py**, onde possui 1 classe. **ChromeDriver**</br>
        Obs: Essa mudança é para tornar mais organizado, assim não precisando criar essa mesma classe para cada script.

        class ChromeDriver: Criada para optimizar o código e evitar que o usuário baixe o driver toda vez que for utilizar o script, assim deixando o script mais rapido e mais organizado.

         Removido a classe "ChromeDriver" do script "WebScrapingFutebol"
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


![Update](https://img.shields.io/badge/update%20data-30%2F12%2F2022-brightgreen)
<pre>
    Obtendo informações dos Gentílicos e Topônimos de todos os Países
</pre>
![Update](https://img.shields.io/badge/update%20data-28%2F12%2F2022-brightgreen)
<pre>
    Obtendo informações das oitavas de finais até a Final da Copa do Mundo 2022.
</pre>
![Update](https://img.shields.io/badge/update%20data-22%2F12%2F2022-brightgreen)
<pre>
    Obtendo informações do Campeonato Brasileiro 2022.
</pre>

## Requirements
![Python](https://img.shields.io/badge/Python-v3.9-blue)

### Requerimentos necessários para /Main's
[Selenium](https://pypi.org/project/selenium/)</br>
[Webdriver_manager](https://pypi.org/project/webdriver-manager/)</br>
[Subprocess](https://docs.python.org/3/library/subprocess.html)</br>
[Os](https://docs.python.org/3/library/os.html)</br>
[Google Chrome](https://www.google.com/intl/pt-BR/chrome/)</br>

### Requerimentos necessários para *Exemplo.py
[PyQt5](https://pypi.org/project/PyQt5/)</br>
[Selenium](https://pypi.org/project/selenium/)</br>
[Webdriver_manager](https://pypi.org/project/webdriver-manager/)</br>
[Subprocess](https://docs.python.org/3/library/subprocess.html)</br>
[Time](https://docs.python.org/3/library/time.html)</br>
[Threading](https://docs.python.org/3/library/threading.html)</br>
[os](https://docs.python.org/3/library/os.html)</br>
[sys](https://docs.python.org/3/library/sys.html)</br>
[Google Chrome](https://www.google.com/intl/pt-BR/chrome/)</br>

## Autores
[José Henrique da Silva Siqueira](https://www.linkedin.com/in/jos%C3%A9-henrique-siqueira-852664218/)

## Licença
   This project is licensed under the [MIT License](/LICENSE).

## Agradecimentos
[Globo Esporte](https://ge.globo.com/) - Site providencia informações sobre diversos campeonatos de futebol, assim sendo usado como base para algumas classes do projeto.