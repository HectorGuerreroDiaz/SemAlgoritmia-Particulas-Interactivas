from PySide2.QtWidgets import QPushButton, QApplication
import sys
from MainWindow import MainWindow


#Aplicacion de Qt
app = QApplication()

window = MainWindow()
window.show()
#Qt loop


#button = QPushButton('Hola')

#button.show()
sys.exit(app.exec_())