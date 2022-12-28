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
            QMessageBox.information(self,"FIM","INFORMAÇÕES DA COPA DO MUNDO 2022, VERIFIQUE O TERMINAL")
        if response[0]=="SinalProgressBar":
            self.pbar.setMaximum(5)
            self.pbar.setValue(response[1])

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
        options.add_argument("--window-size=1920,1080")
        url = 'https://ge.globo.com/futebol/copa-do-mundo/2022/'
        driver=webdriver.Chrome(service=SERVICE,options=options)
        driver.get(url)
        Retorno=[]
        x=0
        self.statusBar.showMessage("PROCESSANDO. . .")
        while x<5:
            Placar=driver.find_elements(By.CLASS_NAME, "placar")
            Esquerda=driver.find_element(By.CLASS_NAME, "navegacao-fase__seta-esquerda")
            Fase=driver.find_element(By.CLASS_NAME, "navegacao-fase__fase")
            Temp=[]
            for elemento in Placar:
                if '\n' in elemento.text:
                    valor=elemento.text
                    valor=valor.replace('\n'," ")
                    if 'Estados Unidos' in valor:
                        valor=valor.replace('Estados Unidos','Estados-Unidos')
                    if 'Coreia do Sul' in valor:
                        valor=valor.replace('Coreia do Sul','Coreia-do-Sul')
                    valor=valor.split()
                    Temp=Temp+[valor]
            Temp.insert(0,Fase.text)
            Retorno=Retorno+[Temp]
            Esquerda.click()
            sleep(1)
            x=x+1
            self.signal.emit(['SinalProgressBar',x])
        Final=Retorno[0]
        TerceiroLugar=Retorno[1]
        SemiFinal=Retorno[2]
        Quartas=Retorno[3]
        Oitavas=Retorno[4]
        print(*Final, sep = "\n")
        print(*TerceiroLugar, sep = "\n")
        print(*SemiFinal, sep = "\n")
        print(*Quartas, sep = "\n")
        print(*Oitavas, sep = "\n")
        self.signal.emit(['Finished'])


if __name__ == "__main__":
    app = QApplication([])
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())