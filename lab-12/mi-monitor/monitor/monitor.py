from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel
import pyqtgraph as pg
from util import Extractor
import time

class Monitor(QMainWindow):

    def __init__(self, refresh):

        super(Monitor, self).__init__()

        print('Se ha creado la clase Monitor')

        self.extractor = Extractor()

        self.cpu = [0 for _ in range(100)]
        self.memory = [0 for _ in range(100)]

        widget = QWidget()

        # Definimos el layout, en forma de vertical box
        vertical_box = QVBoxLayout()
        # Le indicamos que coja todo el ancho de la ventana
        vertical_box.addStretch(1)

        # Creamos un widget con el titulo para el gráfico de CPU
        self.cpu_label = QLabel()
        self.cpu_label.setText('CPU (0%)')

        # Añadimos el widget a nuestro layout
        vertical_box.addWidget(self.cpu_label)

        # Creamos un widget para mostrar el gráfico
        self.plot_cpu = pg.PlotWidget()

        self.cpu_x = list(range(100))

         # Ponemos el fondo en blanco
        self.plot_cpu.setBackground('w')
        # Definimos el rango del eje Y
        self.plot_cpu.setYRange(0, 100)
        # Definimos el color de la línea
        pen = pg.mkPen(color=(120, 0, 0))
        # Creamos la línea de la CPU
        self.data_line_cpu = self.plot_cpu.plot(self.cpu_x, self.cpu, pen=pen)

        # Añadimos el widget a nuestro layout
        vertical_box.addWidget(self.plot_cpu)

        # Creamos un widget con el titulo para el gráfico de RAM
        self.memory_label = QLabel()
        self.memory_label.setText('Memoria (0%)')

        # Añadimos el widget a nuestro layout
        vertical_box.addWidget(self.memory_label)
        
        # Creamos un widget para mostrar el gráfico
        self.plot_memory = pg.PlotWidget()

        self.memory_x = list(range(100))

         # Ponemos el fondo en blanco
        self.plot_memory.setBackground('w')
        # Definimos el rango del eje Y
        self.plot_memory.setYRange(0, 100)
        # Definimos el color de la línea
        pen = pg.mkPen(color=(255, 0, 0))
        # Creamos la línea de la CPU
        self.data_line_memory = self.plot_memory.plot(self.memory_x, self.memory, pen=pen)

        vertical_box.addWidget(self.plot_memory)

        widget.setLayout(vertical_box)

        self.setCentralWidget(widget)

        # Refrescamos los datos
        self.timer = QtCore.QTimer()
        self.timer.setInterval(refresh)
        self.timer.timeout.connect(self.get_cpu_data)
        self.timer.timeout.connect(self.get_memory_data)
        self.timer.start()
        
        self.setWindowTitle('Mi monitor (Velocidad de refresco: {} ms)'.format(refresh))
        self.show()

    def update_cpu_data(self, nuevo_valor):
        # Eliminamos el primer valor del eje de las X y añadimos uno nuevo
        self.cpu_x = self.cpu_x[1:]
        self.cpu_x.append(self.cpu_x[-1] + 1)

        # Eliminamos el primer valor del eje de las Y y añadimos uno nuevo
        self.cpu = self.cpu[1:]
        self.cpu.append(nuevo_valor)
        self.data_line_cpu.setData(self.cpu_x, self.cpu)

        # Cambiamos el título de la gráfica
        self.cpu_label.setText('CPU ({}%)'.format(nuevo_valor))

    def update_memory_data(self, event):
        """
        Actualiza la información del gráfico de memoria
        :return:
        """
        # Remove the first X element and add a new value
        self.memory_x = self.memory_x[1:]
        self.memory_x.append(self.memory_x[-1] + 1)

        # Remove the first CPU element and add a new value
        self.memory = self.memory[1:]
        self.memory.append(event)
        self.data_line_memory.setData(self.memory_x, self.memory)

        self.memory_label.setText('Memoria ({}%)'.format(event))

    def get_cpu_data(self):
        self.update_cpu_data(self.extractor.get_cpu_percent())

    def get_memory_data(self):
        self.update_memory_data(self.extractor.get_virtual_memory_percent())
