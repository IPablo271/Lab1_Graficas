
from Utilities import * 
BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)
GREEN = color(0, 255 , 0)

class Render(object):
   
    def __init__(self,width, height):
        self.width = width
        self.height = height
        self.current_color = WHITE
        self.clear_color = BLACK
        self.viewportx = 0
        self.viewporty = 0
        self.viewportwidth = 0
        self.viewortheight = 0
        self.viewportcolor = GREEN
        self.clear() #Limpiar la pantalla.
    def viewport(self,x, y,width,height):
        self.viewportx = x
        self.viewporty = y
        self.viewportwidth = width
        self.viewortheight = height
   
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

        
        
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[x][y])
        f.close()


    #Función que dibuja un punto en la pantalla. Esta es una función de bajo nivel. 
    def point(self, x, y): 
        #Esta función dibuja un punto en la pantalla.
        self.framebuffer[x][y] = self.current_color #El color del punto es el color actual.