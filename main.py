from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from subprocess import CREATE_NO_WINDOW
from time import *
import os

def main():
    SERVICE=None
    wddir = os.environ["USERPROFILE"] + "\.wdm\drivers\chromedriver\win32" #Verificadno se o usuario já tem o chrome web driver baixado
    if os.path.exists(wddir):   
            wdname = "chromedriver.exe"
            for root,dir,files in os.walk(wddir):
                if wdname in files:
                    SERVICE=Service(os.path.join(root, wdname))
    else:
            print("BAIXANDO CHROME WEBDRIVER. . .")
            SERVICE=Service(ChromeDriverManager().install()) #Baixando chrome web driver caso necessário
            print("DOWNLOAD COMPLETO")
    print("INICIANDO. . .")
    SERVICE.creationflags = CREATE_NO_WINDOW
    options = Options()
    options.headless = True
    url = 'https://ge.globo.com/futebol/brasileirao-serie-a/' #Url base
    driver=webdriver.Chrome(service=SERVICE,options=options)
    driver.get(url)
    Esquerda = driver.find_element(By.CLASS_NAME, "lista-jogos__navegacao--seta-esquerda svg") #Obtendo o elemento responsável pelas páginas de Rodadas (Seta Esquerda)
    Direita = driver.find_element(By.CLASS_NAME, "lista-jogos__navegacao--setas:last-of-type") #Obtendo o elemento responsável pelas páginas de Rodadas (Seta Direita)
    TabelaRetorno=driver.find_elements(By.CLASS_NAME, "classificacao__tabela--linha") #Obtendo os elementos correspondentes as informações da Tabela de Classificação
    RodadaAtual=driver.find_element(By.CLASS_NAME, 'lista-jogos__navegacao--rodada') #Obtendo o elemento responsável com as informações das Rodadas
    RodadaAtual=RodadaAtual.text.replace('ª RODADA','')
    RodadaAtual=int(RodadaAtual)
    TabelaClassificação=[]
    TabelaRodadas=[]
    Times=[]
    Pontos=[]
    print("PROCESSANDO TABELA DE CLASSIFICAÇÃO")
    for elemento in TabelaRetorno:
        if '\n' in elemento.text:
            valor=elemento.text
            valor=valor.replace('\n'," ")
            if 'São Paulo' in valor:
                valor=valor.replace('São Paulo',"São-Paulo") #Retirando o espaçamento do nome "São Paulo"
            Times=Times+[valor.split()] #Obtendo a classificação, nome e variações de posição de cada Time
        else:
            Pontos=Pontos+[elemento.text.split()] #Obtendo os valores 'P','J','V','E','D','GP','GC','SG' e '%' de cada Time
    for time, ponto in zip(Times, Pontos):
        TabelaClassificação=TabelaClassificação+[time+ponto] #Concatenando Valores
    i=RodadaAtual
    while i>=0:
        Esquerda.click()
        i=i-1
        sleep(0.5)
    Rodada=1
    print("PROCESSANDO RODADAS")
    for i in range(RodadaAtual):
        TabelaJogos=[]
        TabelaJogos=TabelaJogos+[Rodada]
        TabelaJogosRetorno=driver.find_elements(By.CLASS_NAME, "placar") #Obtendo elemento responsável pelos placares da Rodada
        for element in TabelaJogosRetorno:
            if '\n' in element.text:
                valor=element.text
                valor=valor.replace('\n'," ")
                if 'São Paulo' in valor:
                    valor=valor.replace('São Paulo',"São-Paulo")
                TabelaJogos=TabelaJogos+[valor.split()] #Obtendo resultado placar dos jogos e nome dos Times
            else:
                TabelaJogos=TabelaJogos+[valor.split()] #Obtendo resultado placar dos jogos e nome dos Times
        TabelaRodadas=TabelaRodadas+[TabelaJogos] #Adicionado o número da rodada e os jogos que aconteceram na Rodada correspondente
        Direita.click() #Passando para a próxima Rodada
        Rodada=Rodada+1
        sleep(0.5)
    print("-----TABELA CLASSIFICAÇÃO-----")
    for elem in TabelaClassificação:
        print(elem) #Imprimindo Tabela de Classificação
    Rodada=1
    for elem in TabelaRodadas:
        print("-----RODADA "+str(Rodada)+"-----")
        print(elem) #Imprimindo Número da Rodadas e os jogos correspondentes
        Rodada=Rodada+1

if __name__ == "__main__":
    main()