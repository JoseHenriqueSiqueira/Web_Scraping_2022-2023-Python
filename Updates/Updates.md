![Update](https://img.shields.io/badge/update%20data-18%2F11%2F2023-brightgreen)

Refatorando código!
Agora o web scraping do futebol ficou mais limpo e completo! Literalmente uma API atualizada em tempo real! Muito rápida!
Agora o navegador para webscraping é o Edge. Também atualizei como ele é aberto, deixando o código muito mais simples: **EdgeWebDriver.py**.
Algumas classes foram alteradas como a **Brasileirão**, **CopaDoMundo** e **ChampionsLeague**. Por agora removi a **CopaDoBrasil**.

![Update](https://img.shields.io/badge/update%20data-08%2F03%2F2023-brightgreen)

Criado um script com scripts testes [WebScraping.py](/tests/WebScraping.py).

![Update](https://img.shields.io/badge/update%20data-19%2F02%2F2023-brightgreen)

Duas classes criadas no *WebScrapingFutebol.py*. **Brasileirao** e **CopaDoMundo**</br>
Atualizado o tipo de retorno de dados. Agora é retornado uma lista, contendo varias tuplas e cada tupla tem dados string</br>
Removido as classe **Brasileirão2022**  e **CopaDoMundo2022** do script *WebScrapingFutebol.py*</br>
Optimização das demais classes e métodos</br>

![Update](https://img.shields.io/badge/update%20data-13%2F02%2F2023-brightgreen)

Criado o script **TopônimosGentílicosPaíses.py**, onde possui 1 classe. **TopônimosGentilicos**</br>
Criado o script **ChromeWebDriver.py**, onde possui 1 classe. **ChromeDriver**</br>
Removido a classe **ChromeDriver** do script *WebScrapingFutebol*
Removido os scripts de Exemplos. Eles não estavam bem programados, e não tinha muita utilidade. Caso algum usuário necessite um exemplo, eu adiciono ao repositório.


![Update](https://img.shields.io/badge/update%20data-09%2F02%2F2023-brightgreen)

Criado o script **WebScrapingFutebol.py**, onde possui 4 classes. **CopaDoBrasil2023**, **Brasileirão2022**, **CopaDoMundo2022** e **ChromeDriver**</br>
Removido os arquivos "BrasileiraoMain.py" e "CopaDoMundo22Main.py", pois não são mais necessários no projeto.
Futuros Update: Atualizar os scripts exemplos, melhorar o Script "TopônimosGentílicosPaísesMain.py" (Possivelmente transformá-lo em uma Classe) e adicionar mais WebScraping.