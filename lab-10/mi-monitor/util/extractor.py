import psutil

class Extractor:

    def __init__(self):
        print('Se ha creado la clase Extractor')

    def get_virtual_memory_percent(self):
        return psutil.virtual_memory()._asdict()['percent']

    def get_cpu_percent(self):
        return psutil.cpu_percent()
