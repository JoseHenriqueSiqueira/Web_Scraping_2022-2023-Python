from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from subprocess import CREATE_NO_WINDOW
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
        self.setWindowTitle("Topônimos e Gentílicos")

    def doSomething(self,event):
        self.statusBar.showMessage("INICIANDO . . .")
        self.btn.disconnect()
        worker=Thread(target=self.main)
        worker.start()

    def signalResponse(self,response):
        if response[0]=="Finished":
            self.btn.clicked.connect(self.doSomething)
            QMessageBox.information(self,"FIM","VERIFIQUE O TERMINAL")
        if response[0]=="SinalProgressBar":
            self.pbar.setMaximum(197)
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
        url = 'http://funag.gov.br/manual/index.php?title=Top%C3%B4nimos_e_gent%C3%ADlicos'
        driver=webdriver.Chrome(service=SERVICE,options=options)
        driver.get(url)
        self.statusBar.showMessage("PROCESSANDO. . .")
        x=1
        y=2
        Retorno=[]
        Temp=[]
        while x<5:
            Cabeçalho=driver.find_element(By.XPATH, f"/html/body/div[1]/div[1]/div/div[2]/div[4]/div/table/tbody/tr[1]/th[{x}]")
            Temp=Temp+[Cabeçalho.text]
            x+=1
        self.signal.emit(["SinalProgressBar",1])
        Retorno=Retorno+[Temp]
        Temp=[]
        x=1
        while 1:
            try:
                if x<5:
                    Tabela=driver.find_element(By.XPATH, f"/html/body/div[1]/div[1]/div/div[2]/div[4]/div/table/tbody/tr[{y}]/td[{x}]")
                    Temp=Temp+[Tabela.text]
                    x+=1
                else:
                    Retorno=Retorno+[Temp]
                    Temp=[]
                    x=1
                    y+=1
                    self.signal.emit(["SinalProgressBar",y])
            except:
                break
        print(*Retorno, sep="\n")
        self.signal.emit(['Finished'])


if __name__ == "__main__":
    app = QApplication([])
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())