import sys
import subprocess
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QGridLayout, QWidget
from PyQt5.QtCore import QSize

class Janela(QMainWindow):
    def __init__(self):
        super(Janela, self).__init__()
        self.setup_main_Window()
        self.initUI()

    #criando um QLabel texto
    def setup_main_Window(self):
        self.x = 640
        self.y = 480
        self.setMinimumSize(QSize(self.x, self.y))
        self.setWindowTitle("Processamento Digital de Imagens")
        self.Wid = QWidget(self)
        self.setCentralWidget(self.Wid)
        self.layout = QGridLayout()
        self.Wid.setLayout(self.layout)

    def initUI(self):
        self.texto = QLabel("Jailson Quirino de Paula")
        self.texto.adjustSize()
        self.largura = self.texto.frameGeometry().width()
        self.altura = self.texto.frameGeometry().height()
        self.texto.setAlignment(QtCore.Qt.AlignCenter)
        #botão
        self.botao1 = QtWidgets.QPushButton(self)
        self.botao1.setText("Original")
        self.botao1.clicked.connect(self.open_file)

        self.botao2 = QtWidgets.QPushButton(self)
        self.botao2.setText("Transformar")
        self.botao2.clicked.connect(self.transform_me)

        #imagens QLabel
        self.imagem1 = QLabel(self)
        self.endereco1 = 'imagens/carro4.png'
        self.pixmap1 = QtGui.QPixmap(self.endereco1)
        self.pixmap1 = self.pixmap1.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem1.setPixmap(self.pixmap1)
        self.imagem1.setAlignment(QtCore.Qt.AlignCenter)

        self.imagem2 = QLabel(self)
        self.endereco2 = 'imagens/carro4.png'
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap1.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)
        #organizando
        self.layout.addWidget(self.texto, 0, 0, 1, 2)
        self.layout.addWidget(self.botao1, 2, 0)
        self.layout.addWidget(self.botao2, 2, 1)
        self.layout.addWidget(self.imagem1, 1, 0)
        self.layout.addWidget(self.imagem2, 1, 1)
        self.layout.setRowStretch(0, 0)
        self.layout.setRowStretch(1, 1)
        self.layout.setRowStretch(2, 0)

    #açao do botao
    def open_file(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, caption= 'open image',
                    directory=QtCore.QDir.currentPath(),
                    filter='all files (*.*);; images (*.png; *.jpg;)',
                    initialFilter='images (*.png; *.jpg;)')

        print(fileName)
        if fileName != '':
            self.endereco1 = fileName
            self.pixmap1 = QtGui.QPixmap(self.endereco1)
            self.pixmap1 = self.pixmap1.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
            self.imagem1.setPixmap(self.pixmap1)

    def transform_me(self):
        self.entrada = self.endereco1
        self.saida = 'imagens/nova.png'
        self.script = '.\outro_ton.py'
        self.janela2 = 'python ' + self.script +' \"' + self.entrada + '\" ' + self.saida
        print(self.janela2)
        subprocess.run(self.janela2, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

       
app = QApplication(sys.argv)   
win = Janela()
win.show()
sys.exit(app.exec_())