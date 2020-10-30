from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from PySide2.QtCore import Slot
from ui_MainWindow import Ui_MainWindow
from particulas import Particula
from particulas import ListaParticula

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__() #Se llama a la ventana
        
        self.administrador = ListaParticula()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Conexión del Slot
        self.ui.agregarFinal_pushButton.clicked.connect(self.click_agregar)
        self.ui.agregarInicio_pushButton.clicked.connect(self.click_agregarInicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)

        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)

        self.table()

    def table(self):
        self.ui.tabla.setColumnCount(8)
        headers = ["ID","OrigenX","OrigenY","DestinoX","DestinoY","Velocidad","Distancia","RGB"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)    

    def mostrar_particulas(self,todos,id):
        self.ui.tabla.clear()
        self.table()

        row = 0
        encontrado = False

        if todos == False:
            self.ui.tabla.setRowCount(1)
        else:
            self.ui.tabla.setRowCount(len(self.administrador))

        for Particula in self.administrador:
            if id == Particula.id or todos == True:
                id_widget = QTableWidgetItem(str(Particula.id))
                origenX_widget = QTableWidgetItem(str(Particula.origenX))
                origenY_widget = QTableWidgetItem(str(Particula.origenY))
                destinoX_widget = QTableWidgetItem(str(Particula.destinoX))
                destinoY_widget = QTableWidgetItem(str(Particula.destinoY))
                velocidad_widget = QTableWidgetItem(str(Particula.velocidad))
                distancia_widget = QTableWidgetItem(str(Particula.distancia))
                RGB_widget = QTableWidgetItem(str(Particula.RGB))

                self.ui.tabla.setItem(row, 0, id_widget)
                self.ui.tabla.setItem(row, 1, origenX_widget)
                self.ui.tabla.setItem(row, 2, origenY_widget)
                self.ui.tabla.setItem(row, 3, destinoX_widget)
                self.ui.tabla.setItem(row, 4, destinoY_widget)
                self.ui.tabla.setItem(row, 5, velocidad_widget)
                self.ui.tabla.setItem(row, 6, distancia_widget)
                self.ui.tabla.setItem(row, 7, RGB_widget)

                encontrado = True
                if todos == False:
                    return

                row += 1

        if not encontrado:
            QMessageBox.warning(
                self,
                "Atencion",
                f'La particula con id:"{id}" no fue encontrada'
            )


    @Slot()
    def buscar_id(self):
        id = self.ui.buscar_lineEdit.text()
        self.mostrar_particulas(False,id)
                

    @Slot()
    def mostrar_tabla(self):
        self.mostrar_particulas(True,0)
            
            

    @Slot()
    def action_abrir_archivo(self):
        #print('abrir_archivo')
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.administrador.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se abrio el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo abrir el archivo"
            )

    @Slot()
    def action_guardar_archivo(self):
        #print('guardar_archivo')
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.administrador.guardar(ubicacion):
             QMessageBox.information(
                 self,
                 "Exito",
                 "Se pudo crear el archivo" + ubicacion
             )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo"
            )


    @Slot()
    def click_mostrar(self):
        #self.administrador.mostrar()
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.administrador))

    @Slot() #Definición de Slot
    def click_agregar(self):
        ID = self.ui.ID_lineEdit.text()
        origenX = self.ui.origenX_spinBox.value()
        origenY = self.ui.origenY_spinBox.value()
        destinoX = self.ui.destinoX_spinBox.value()
        destinoY = self.ui.destinoY_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(ID, origenX, origenY, destinoX, destinoY, velocidad, red, green, blue)
        self.administrador.agregar_final(particula)

    @Slot() #Definición de Slot
    def click_agregarInicio(self):
        ID = self.ui.ID_lineEdit.text()
        origenX = self.ui.origenX_spinBox.value()
        origenY = self.ui.origenY_spinBox.value()
        destinoX = self.ui.destinoX_spinBox.value()
        destinoY = self.ui.destinoY_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(ID, origenX, origenY, destinoX, destinoY, velocidad, red, green, blue)
        self.administrador.agregar_inicio(particula)