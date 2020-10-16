from util import Extractor
import time

class Monitor:

    def __init__(self, refresh):

        print('Se ha creado la clase Monitor')

        self.cpu = [0 for _ in range(100)]
        self.memory = [0 for _ in range(100)]

        self.extractor = Extractor()

        while True:
            self.get_cpu_data()
            self.get_memory_data()
            print("CPU: {}".format(self.cpu))
            print("RAM: {}".format(self.memory))
            time.sleep(refresh/1000)

    def update_cpu_data(self, nuevo_valor):
        # Elimina el primer valor de la lista
        self.cpu = self.cpu[1:]

        self.cpu.append(nuevo_valor)

    def update_memory_data(self, nuevo_valor):
        # Elimina el primer valor de la lista
        self.memory = self.memory[1:]

        self.memory.append(nuevo_valor)

    def get_cpu_data(self):
        self.update_cpu_data(self.extractor.get_cpu_percent())

    def get_memory_data(self):
        self.update_memory_data(self.extractor.get_virtual_memory_percent())
