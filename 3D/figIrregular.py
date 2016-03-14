from OpenGL.GL import *
from OpenGL.GLUT import *
from random import random
from math import sin
from math import cos
from math import pi

# ====================================================================
#                 FUNCIONES
#
#
# ====================================================================
#                 DATOS
# Nombre : Jorge A. Castanio, Sebastian Velasquez, Oscar Eduardo Ramirez
# Codigo : 1153641, -----, -----
# Plan: Ingenieria de Sistemas
# Profesor: ----------
# Taller Numero 1 de Computacion Grafica
#=====================================================================
#2.1.1
#Programa que Genera un cuadrado con radio r = 0.7 de color verde. EL circulo que se va a generar estara centrado
#en el origen, por lo que del origen hacia la izquierda tendra una distancia de 0.35 igualmente hacia la derecha

def initGL(width, height):
  glClearColor(0.5, 0.5, 0.5, 0.0)
  glColor3f(0.0, 0.25, 0.5)
  glMatrixMode(GL_PROJECTION)

def dibujarCuadrado():

  glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
  glLoadIdentity ()

# -----Transformaciones de vista, se le da un estilo a la escena
    #punto de vista
  
  glScalef (0.5, 0.5, 0.5)

  glBegin(GL_QUADS)
  glColor3f(0.0, 0.0, 0.5)
  glVertex3f( 0.0,  1.0, 0.0)

  glColor3f(0.5, 0.0, 0.0)
  glVertex3f(-1.0, -1.0, 0.0)

  glColor3f(0.0, 0.5, 0.0)
  glVertex3f( 1.0, -1.0, 0.0)

  glColor3f(0.5, 0.5, 0.0)
  glVertex3f( 1.0, 1.0, 1.0)

  glEnd()

def gradosAradianes(grados):
  return (grados*pi)/180


contador = 0
def keyPressed(*args):
  key = args[0]
  if key == "r" or key =="R":
    glLoadIdentity()
    # cada vez que se presiona r la figura rota 20 grados con respecto a x
    matrizRotacion = [1, 0, 0, 0, 0, cos(gradosAradianes(20)), sin(gradosAradianes(20)), 0, 0, -sin(gradosAradianes(20)), cos(gradosAradianes(20)), 0, 0, 0, 0, 1]
    glMultMatrixf(matrizRotacion)

  elif key == "s" or key == "s":
    glLoadIdentity()
    #El cubo rotara 35 grados con respecto a el vector (1,3,5)
    glRotatef(gradosAradianes(35), 1, 3, 5)

  elif key == "b" or key == "B":
    # Cada vez que se presiona b se aplica una transformacion
    # compuesta de rotar 15 grados con respecto a z, trasladar
    # 0.1 con respecto a y y escalar con respecto a y en 0.95. En
    glLoadIdentity()
    glRotatef(gradosAradianes(15), 0, 0, 1)
    glTranslatef(0.0, 0.1, 0.0)
    glScale(0.5, 0.95, 0.3)

#Funcion que me imprime la matriz actual
def imprimirMatriz():
  matriz = glGetFloatv(GL_PROJECTION_MATRIX)
  print matriz

def mouseEvent(botonMouse, estadoMouse, x, y):
  if botonMouse == GLUT_LEFT_BUTTON and estadoMouse == GLUT_DOWN: #Si se clickeo con el boton izquierdo del mouse Y ESTE ESTA PRESIONADO
    glColor3f(random(), random(), random())

def main():
  global window
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
  glutInitWindowSize(500,500)
  glutInitWindowPosition(200,200)

  #creando la ventana
  window = glutCreateWindow("Taller2 - Cuadrado")
  glutKeyboardFunc(keyPressed)
  glutMouseFunc(mouseEvent)
  glutDisplayFunc(dibujarCuadrado)
  glutIdleFunc(dibujarCuadrado)
  imprimirMatriz()
  initGL(500,500)
  glutMainLoop()

if __name__ == "__main__":
  main()
