from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from subprocess import CREATE_NO_WINDOW
from time import *
from threading import Thread
import os, sys

class MainWindow(QMainWindow):
    signal=pyqtSignal(list)
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(200,120)
        self.btn = QPushButton(self)
        self.btn.setGeometry(QRect(77, 30, 50, 30))
        self.btn.setText("APERTE")
        self.signal.connect(self.signalResponse)
        self.btn.clicked.connect(self.doSomething)
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(23, 70, 180, 25)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.setWindowTitle("TABELA BRASILEIRÃO")

    def doSomething(self,event):
        self.statusBar.showMessage("INICIANDO . . .")
        self.btn.disconnect()
        worker=Thread(target=self.main)
        worker.start()

    def signalResponse(self,response):
        if response[0]=="Finished":
            self.btn.clicked.connect(self.doSomething)
            QMessageBox.information(self,"FIM","INFORMAÇÕES DO BRASILEIRÃO RETORNADAS, VERIFIQUE O TERMINAL")
        if response[0]=="SinalProgressBar":
            self.pbar.setMaximum(response[1])
            self.pbar.setValue(response[2])

    def main(self):
        SERVICE=None
        wddir = os.environ["USERPROFILE"] + "\.wdm\drivers\chromedriver\win32"
        if os.path.exists(wddir):
                wdname = "chromedriver.exe"
                for root,dir,files in os.walk(wddir):
                    if wdname in files:
                        SERVICE=Service(os.path.join(root, wdname))
        else:
                SERVICE=Service(ChromeDriverManager().install())
        SERVICE.creationflags = CREATE_NO_WINDOW
        options = Options()
        options.headless = True
        url = 'https://ge.globo.com/futebol/brasileirao-serie-a/'
        driver=webdriver.Chrome(service=SERVICE,options=options)
        driver.get(url)
        Esquerda = driver.find_element(By.CLASS_NAME, "lista-jogos__navegacao--seta-esquerda svg")
        Direita = driver.find_element(By.CLASS_NAME, "lista-jogos__navegacao--setas:last-of-type")
        TabelaRetorno=driver.find_elements(By.CLASS_NAME, "classificacao__tabela--linha")
        RodadaAtual=driver.find_element(By.CLASS_NAME, 'lista-jogos__navegacao--rodada')
        RodadaAtual=RodadaAtual.text.replace('ª RODADA','')
        RodadaAtual=int(RodadaAtual)
        TabelaClassificação=[]
        TabelaRodadas=[]
        Times=[]
        Pontos=[]
        cont=1
        self.statusBar.showMessage("PROCESSANDO. . .")
        for elemento in TabelaRetorno:
            if '\n' in elemento.text:
                valor=elemento.text
                valor=valor.replace('\n'," ")
                if 'São Paulo' in valor:
                    valor=valor.replace('São Paulo',"São-Paulo")
                Times=Times+[valor.split()]
            else:
                Pontos=Pontos+[elemento.text.split()]
            cont=cont+1
            self.signal.emit(["SinalProgressBar",117,cont])
        for time, ponto in zip(Times, Pontos):
            TabelaClassificação=TabelaClassificação+[time+ponto]
        i=RodadaAtual
        while i>=0:
            Esquerda.click()
            i=i-1
            cont=cont+1
            sleep(0.5)
            self.signal.emit(["SinalProgressBar",117,cont])
        Rodada=1
        for i in range(RodadaAtual):
            TabelaJogos=[]
            TabelaJogos=TabelaJogos+[Rodada]
            TabelaJogosRetorno=driver.find_elements(By.CLASS_NAME, "placar")
            for element in TabelaJogosRetorno:
                if '\n' in element.text:
                    valor=element.text
                    valor=valor.replace('\n'," ")
                    if 'São Paulo' in valor:
                        valor=valor.replace('São Paulo',"São-Paulo")
                    TabelaJogos=TabelaJogos+[valor.split()]
                else:
                    TabelaJogos=TabelaJogos+[valor.split()]
            TabelaRodadas=TabelaRodadas+[TabelaJogos]
            Direita.click()
            Rodada=Rodada+1
            self.signal.emit(["SinalProgressBar",117,cont])
            cont=cont+1
            sleep(0.5)
        print("-----TABELA CLASSIFICAÇÃO-----")
        for elem in TabelaClassificação:
            print(elem)
        Rodada=1
        for elem in TabelaRodadas:
            print("-----RODADA "+str(Rodada)+"-----")
            print(elem)
            Rodada=Rodada+1
        self.signal.emit(["Finished"])


if __name__ == "__main__":
    app = QApplication([])
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())