import urllib.request
import requests
from interface import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from datetime import datetime

class Placa_relay(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ip = self.ui.lineEdit_ip
        self.senha = self.ui.lineEdit_2_senha
        self.ui.pushButton_conectar.clicked.connect(self.verifica_conexao)
        self.ui.pushButton_2_ligar_r01.clicked.connect(self.ligar_relay01)
        self.ui.pushButton_3_desligar_01.clicked.connect(self.desligar_relay01)
        self.ui.pushButton_4_ligar_r02.clicked.connect(self.ligar_relay02)
        self.ui.pushButton_5_desligar_r02.clicked.connect(self.desligar_relay02)
        
        
    def verifica_conexao(self): 
        self.pagina = requests.get(f"http://{self.ip.text()}?" )
        try:
            if self.pagina.status_code == 200:
                print(f"Conectado: {self.ip.text()}")
                self.ui.label_3_status_conexao.setText("Conectado")
                return True
        
        except ConnectionError :
            pass
              

    def ligar_relay01(self):
        if self.verifica_conexao() == True:
            self.url_ligar = f"http://{self.ip.text()}/relay_cgi.cgi?type=0&relay=0&on=1&time=5&pwd={self.senha.text()}&"
            self.set_url_ligar = urllib.request.urlopen(self.url_ligar)
            print("Relay 01 - Ligado")
            self.ui.label_3_status_r01.setText("Relay 01 - Ligado")
           


    def desligar_relay01(self):
        if self.verifica_conexao() == True:
            self.url_desligar = f"http://{self.ip.text()}/relay_cgi.cgi?type=0&relay=0&on=0&time=5&pwd={self.senha.text()}&"
            self.set_url_desligar = urllib.request.urlopen(self.url_desligar)
            print("Relay 01 - Desligado")
            self.ui.label_3_status_r01.setText("Relay 01 - Desligado")
          
            

    def ligar_relay02(self):
        if self.verifica_conexao() == True:
            self.url_ligar = f"http://{self.ip.text()}/relay_cgi.cgi?type=0&relay=1&on=1&time=5&pwd={self.senha.text()}&"
            self.set_url_ligar = urllib.request.urlopen(self.url_ligar)
            print("Relay 02 - Ligado")
            self.ui.label_4_status_r02.setText("Relay 02 - Ligado")
            


    def desligar_relay02(self):
        if self.verifica_conexao() == True:
            self.url_desligar = f"http://{self.ip.text()}/relay_cgi.cgi?type=0&relay=1&on=0&time=5&pwd={self.senha.text()}&"
            self.set_url_desligar = urllib.request.urlopen(self.url_desligar)
            print("Relay 02 - Desligado")
            self.ui.label_4_status_r02.setText("Relay 02 - Desligado")

"""
    def historico(self):
        data = datetime.now()
        self.lista = ['ligado', 'desligado',"ligado"]
        #self.data = datetime.now()
        for linha in self.lista:
            self.ui.textBrowser.append(linha + str(data))
"""


#Inicia a Aplicação 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    t = Placa_relay()
    t.show()
    sys.exit(app.exec_())


