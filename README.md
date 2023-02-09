# Web_Scraping_2022/2023-Python
Este repositório é dedicado a obtenção de informações de futebol através de Web Scraping, bem como à geração de bases de dados. As informações incluem:
•Informações sobre a Copa Do Brasil 2023
•Informações sobre gentílicos e topônimos de todos os países
•Informações sobre as oitavas de final até a final da Copa do Mundo 2022
•Informações sobre o Campeonato Brasileiro 2022
![Update](https://img.shields.io/badge/update%20data-09%2F02%2F2023-brightgreen)

Criado o script "WebScrapingFutebol.py", onde possui 4 classes. "CopaDoBrasil2023", "Brasileirão2022", "CopaDoMundo2022" e "ChromeDriver"
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
    
    class ChromeDriver: Criada para optimizar o código e evitar que o usuário baixe o drive toda vez que for utilizar o script, assim deixando o script mais rapido e mais organizado.

    obs: Todos os métodos retornam uma variável do tipo 'list'

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
### Requerimentos necessários para *Main.py
<pre>
    MODULES
        -selenium
        -webdriver_manager
        -subprocess
        -time
        -os
    NAVEGADOR
        -Google Chrome
</pre>

### Requerimentos necessários para *Exemplo.py
<pre>
    MODULES
        -PyQt5
        -selenium
        -webdriver_manager
        -subprocess
        -time
        -threading
        -os
        -sys
    NAVEGADOR
        -Google Chrome
</pre>