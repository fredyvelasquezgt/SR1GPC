# Fredy Velasquez
# 201011

# importacion modulos
import struct


def char(c):
    # 1 byte char
    return struct.pack('=c', c.encode('ascii'))


def word(w):
    # 2bytes
    return struct.pack('=h', w)


def dword(d):
    # 4 bytes
    return struct.pack('=l', d)


def color(r, g, b):
    return bytes([int(b * 225),
                  int(g * 225),
                  int(r * 225)])


class Render(object):
    # glInit
    def __init__(self):
        self.clearColor = color(0, 0, 0)
        self.viewPortX = 0
        self.viewPortY = 0
        self.viewPortWidth = 0
        self.viewPortHeight = 0

    def glCreateWindow(self, width, height):
        # glCreateWindows (dimension de la imagen)
        self.width = width
        self.height = height
        self.glClear()

    def glViewPort(self, x, y, width, height):
        # glViewPort (define area)
        self.viewPortX = x
        self.viewPortY = y
        self.viewPortWidth = width
        self.viewPortHeight = height
        self.drawVPS()

    def drawVPS(self):
        # Función para dibujar el cuadrado del viewPort
        for x in range(self.viewPortX, self.viewPortX + self.viewPortWidth):
            for y in range(self.viewPortY, self.viewPortY + self.viewPortHeight):
                self.pixels[x][y] = self.currColor

    def glClearColor(self, r, g, b):
        # ClearColor(r,g,b)
        self.clearColor = color(r, g, b)
        self.glClear()

    def glColor(self, r, g, b):
        #glPoint (r,g,b)
        self.currColor = color(r, g, b)

    def glClear(self):
        # glClear
        self.pixels = [[self.clearColor for y in range(
            self.height)] for x in range(self.width)]

    def glCenterPoint(self, x, y, clr=None):
        # glpoint (cambiar el color de un punto de la pantalla)
        if((-1 <= x <= 1) and (-1 <= y <= 1)):
            newX = (x + 1) * (self.viewPortWidth // 2) + self.viewPortX
            newY = (y + 1) * (self.viewPortHeight // 2) + self.viewPortY
            self.pixels[newX][newY] = clr or self.currColor

    def glPointS(self, x, y, clr=None):
        # glPointS (x,y) liena de puntos-- Funcion de prueba/experimental
        if (0 <= x < self.viewPortWidth) and (0 <= y < self.viewPortHeight):
            self.pixels[x+self.viewPortX][y +
                                          self.viewPortY] = clr or self.currColor

    def glFinish(self, filename):
        # glFinish  escribe el archivo de imagen
        with open(filename, "wb") as file:
            # Header
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))
            file.write(dword(14 + 40 + (self.width * self.height * 3)))
            file.write(dword(0))
            file.write(dword(14 + 40))

            # InfoHeader
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0))
            file.write(dword(self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            # Color table
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.pixels[x][y])
            file.close()
