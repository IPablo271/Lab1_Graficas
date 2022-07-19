from Render import *
from Utilities import *


rend = None




def glinit():
    pass

def glCreateWindow(width, height):
    global rend
    if width % 4 == 0:
        rend = Render(width, height)
    else:
        print('No se puede procesar la ventana')

def glViewPort(x, y, height, width):
    global rend 
    # if r.height < height:
    #     print("El height del viewport es mayor a la ventana")
    # elif r.width < width:
    #     print("El width del viewport es mayor a la ventana")
    # elif width + x < r.width:
    #     print("El viewport no se encuentra en la pantalla")
    # elif height + y < r.height:
    #     print("El viewport no se encuentra en la pantalla")
    # else:
    rend.viewport(x, y, width, height)

    

def  glClear():
    global rend
    rend.clear()
def  glClearColor(r, g, b):
    global rend
    rend.clear_color = color(r, g, b)
    glClear()


def glVertex(x, y):

    if x >= -1 <= 1 and y >= -1 <= 1:
        global rend
    # Sumarle un numero a la cantidad de -1 a 1
        x_ini = x + 1
        y_ini = y + 1

        # calculada = (Sumada * width) / numero sumado

        calcux = (x_ini * rend.viewportwidth) / 2
        calcuy = (y_ini * rend.viewortheight) / 2

        #  xfinal = (coordenada inicial del viewport + calculada )

        xfinal = round(rend.viewportx + calcux)
        yfinal = round(rend.viewporty + calcuy)



        rend.point(xfinal , yfinal )
    else:
        print('No se puede operar')



def glColor(r, g, b):
    r = round(r * 255)
    g = round(g * 255)
    b = round(b * 255)
    rend.current_color = color(r,g,b)



def glFinish():
    rend.write("a.bmp") 

