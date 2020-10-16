import sys
from monitor import Monitor
 
try:
     print('Bienvenido al Openathon VII!')
 
     refresh = sys.argv[1]   
     refresh = int(refresh)
     if refresh < 100 or refresh > 1000:
         raise ValueError
     print('La frecuencia de refresco es {}'.format(refresh))

     Monitor(refresh)
     
except IndexError as index_error:
     print('Por favor, tienes que indicar la velocidad de refresco como parámetro de entrada')
     sys.exit(-1)
except ValueError as value_error:
     print('{} no es un valor válido'.format(refresh))
     print('Por favor, la velocidad de refresco tiene que ser un número entre 100 y 1000')
     sys.exit(-1)