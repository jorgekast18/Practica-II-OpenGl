import sys
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from random import random 
from math import sin
from math import cos
from math import pi
# ====================================================================
#						      FUNCIONES
# gradosAradianes -->
#
# ====================================================================
# 								DATOS
# Nombre : Jorge A. Castanio, Sebastian Velasquez, Oscar Eduardo Ramirez
# Codigo : 1153641, -----, -----
# Plan: Ingenieria de Sistemas
# Profesor: ----------
# Taller Numero 1 de Computacion Grafica
#=====================================================================
#Programa que genera un cubo con l = 0.5 de color cyan.

def init():
  glMatrixMode (GL_PROJECTION)
  glClearColor(0.5, 0.5, 0.5, 0.0)
  glColor3f(0.0, 1.0, 1.0)

def dibujarCubo():
  glClear (GL_COLOR_BUFFER_BIT)
  glutSolidCube(0.5)
  glFlush ()

def gradosAradianes(grados):
  return (grados*pi)/180

# operaciones sobre la figura
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
    # glRotatef(gradosAradianes(35), 1, 3, 5)
    glScale(0.5, 0.95, 0.3)

  elif key == "t" or key == "T":
    # Cada vez que se presiona b se aplica una transformacion
    # compuesta de rotar 15 grados con respecto a z, trasladar
    # 0.1 con respecto a y y escalar con respecto a y en 0.95. En
    glLoadIdentity()
    glRotatef(gradosAradianes(15), 0, 0, 1)
    glTranslatef(0.0, 0.1, 0.0)


def mouseEvent(botonMouse, estadoMouse, x, y):
    if botonMouse == GLUT_LEFT_BUTTON and estadoMouse == GLUT_DOWN:
        glColor3f(random(), random(), random())

#Funcion que me imprime la matriz actual
def imprimirMatriz():
  matriz = glGetFloatv(GL_PROJECTION_MATRIX)
  print matriz

def main():
  glutInit(sys.argv)
  glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
  glutInitWindowSize (500, 500)
  glutInitWindowPosition (100, 100)
  glutCreateWindow ("Taller2 - Cubo")
  init ()#
  glutDisplayFunc(dibujarCubo)
  glutIdleFunc(dibujarCubo)
  glutKeyboardFunc(keyPressed)
  glutMouseFunc(mouseEvent)
  imprimirMatriz()
  glutMainLoop()

if __name__ == '__main__':
    main()