# Fredy Velasquez
# 201011
# importaciones
from gl import Render

rend = Render()
rend.glCreateWindow(512, 512)
rend.glClearColor(0.45, 0.30, 0.50)
rend.glColor(0, 0, 0)  # Establecemos el color del viewPort
rend.glViewPort(12, 12, 490, 490)  # Generamos el viewPort

# linea de puntos dentro del margen/prueba extra-probar punto sobre punto
rend.glColor(0.177, 0.30, 0.4)  # Establecemos el color de la linea de puntos
for i in range(512):
    rend.glPointS(i, i)

# punto
rend.glColor(1, 1, 1)
# Dibujamos el punto en el viewport en el punto indicado
rend.glCenterPoint(0, 0)


rend.glFinish("output.bmp")
