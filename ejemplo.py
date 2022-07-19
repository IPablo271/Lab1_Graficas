import struct

#Set de utilidades. Estas funciones se pueden hacer en otro archivo para mayor comodidad.

#Se usa el = para convertir de manera correcta.

#Recibe un string y lo convierte en una lista de bytes.
def char(c):
    #Ocupa 1 byte.
    #=c es para que sea un caracter. El encode es para convertir el caracter a bits. El =c es para convertir esos bits a bytes.
    return struct.pack("=c", c.encode('ascii'))

#Recibe un número como parámetro.
def word(w):
    #Ocupa 2 bytes.
    #El formato para un word es 'h'. Este gasta 2 bytes, que es lo que se quiere.
    return struct.pack("=h", w)

#Recibe un número como parámetro.
def dword(d): #Double word.
    #Ocupa 4 bytes. El l es para un num de 4 bytes.
    return struct.pack("=l", d)

def color(r, g, b): #Función que crea el color.
    #3 bytes. Retorna el color en bytes.
    return bytes([b, g, r])

#Colorea un punto de la imagen.
BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)

#Render podría ser un archivo aparte. Este archivo importaría las funciones de utilidades y los métodos que ya se crearon en el archivo SR1.py.
class Render(object):
    #Puede quedar vacío. El width y el height son los parámetros que se le pasan al constructor; estos pueden existisr hasta el momento en el que se crea el window.
    def __init__(self,width, height):
        self.width = width
        self.height = height
        self.current_color = WHITE
        self.clear() #Limpiar la pantalla.

    #Método que se usará para dibujar un punto en la pantalla.
    def clear(self):
        #Generador del color.
        self.framebuffer = [
            #Los colores tienen que ir de 0 a 255.
            [BLACK for x in range(self.width)] 
            for y in range(self.height)
        ]
    
    def write(self, filename):
        #Esta no necesita recibir ningún nombre de archivo.
        #Abrir en bw: binary write.
        f = open(filename, "bw")
        
        #Pixel header.
        f.write(char('B'))
        f.write(char('M'))
        #Tamaño del archivo en bytes. 
        # El 3 es para los 3 bytes que seguirán. El 14 es el tamaño del infoheader y el 40 es el tamaño del otro header.
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(word(0)) #Algo que no se usará. Este es de 2 bytes, por eso se utiliza el word.
        f.write(word(0)) #Algo que no se usará. Este es de 2 bytes, por eso se utiliza el word.
        f.write(dword(14 + 40)) #Offset a la información de la imagen. 14 bytes para el header, 40 para la información de la imagen. Aquí empieza la data.
        #Lo anterior suma 14 bytes.
        
        #Info header.
        f.write(dword(40)) #Este es el tamaño del header. Esto es de 4 bytes, por eso se utiliza el dword.
        f.write(dword(self.width)) #Ancho de la imagen. Esto es de 4 bytes, por eso se utiliza el dword.
        f.write(dword(self.height)) #Alto de la imagen. Esto es de 4 bytes, por eso se utiliza el dword.
        f.write(word(1)) #Número de planos. Esto es de 2 bytes, por eso se utiliza el word.
        f.write(word(24)) #24 bits por pixel. Esto es porque usa el true color y el RGB.
        f.write(dword(0)) #Esto es la compresión. Esto es de 4 bytes, por eso se utiliza el dword.
        f.write(dword(self.width * self.height * 3)) #Tamaño de la imagen sin el header.
        #Pixels que no se usarán mucho.
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        #Lo anterior suma 40 bytes.

        
        #Pixel data. Arreglar para que solo dibuje una línea.
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[x][y])
        f.close()

    #Función que dibuja un punto en la pantalla. Esta es una función de bajo nivel. 
    def point(self, x, y): 
        #Esta función dibuja un punto en la pantalla.
        self.framebuffer[x][y] = self.current_color #El color del punto es el color actual.
    

r = Render(1024, 1024) #Crea un objeto render con un tamaño de 1024x1024.


#r.current_color = color(200, 100, 0) #Cambia el color actual a uno diferente.

r.current_color = WHITE #Cambia el color actual a blanco.

#Esto hace la línea en diagonal.
for x in range(100, 200):
    for x in range(100, 200):
        r.current_color = color(
            255, 
            255,
            255) #Cambia el color actual a uno diferente.
        r.point(x, x) #Dibuja un cuadrado en la pantalla.

#r.current_color = color(100, 100, 255) #Cambia el color actual a uno diferente.
"""
for x in range(300, 400):
    for y in range(300, 400):
        r.point(x, y) #Dibuja un cuadrado en la pantalla.
"""
#r.point(100, 100) #Dibuja un punto en la pantalla.
r.write("a.bmp") #Escribe el archivo. El nombre del archivo es a.bmp, porque se le pasa una cadena de caracteres.