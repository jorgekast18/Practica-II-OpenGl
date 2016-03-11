from OpenGL.GL import *
from OpenGL.GLUT import *
from random import random
from math import sin
from math import cos
from math import pi

# ====================================================================
#						      FUNCIONES
#
#
# ====================================================================
# 								DATOS
# Nombre : Jorge A. Castanio, Sebastian Velasquez, Oscar Eduardo Ramirez
# Codigo : 1153641, -----, -----
# Plan: Ingenieria de Sistemas
# Profesor: ----------
# Taller Numero 1 de Computacion Grafica
#=====================================================================
#2.1.4
#Programa que genera una figura con al menos 8 lados de color amarillo.


def initGL(width, height):
	glClearColor(0.5, 0.5, 0.5, 0.0)
	glMatrixMode(GL_PROJECTION)
	glColor3f(1.0,1.0,0)

def dibujarOctagono():
	glClear(GL_COLOR_BUFFER_BIT)

	glBegin(GL_POLYGON)
	glVertex2f(0.5, 0.2)
	glVertex2f(0.2, 0.4)
	glVertex2f(-0.4, 0.4)
	glVertex2f(-0.8, 0.2)
	glVertex2f(-0.8, -0.2)
	glVertex2f(-0.4, -0.4)
	glVertex2f(0.2, -0.4)
	glVertex2f(0.5, -0.2)
	glEnd()
	glFlush()

def gradosAradianes(grados):
	return (grados*pi)/180




contador = 0
def keyPressed(*args):
	key = args[0]

	if key == "r" or key =="R":
		matrizRotacion = [1, 0, 0, 0, 0, cos(gradosAradianes(30)), sin(gradosAradianes(30)), 0, 0, -sin(gradosAradianes(30)), cos(gradosAradianes(30)), 0, 0, 0, 0, 1]
		glMultMatrixf(matrizRotacion)
		#glRotatef(gradosAradianes(30), 1, 0, 0)
	elif key == "t" or key =="T":
		global contador
		matrizTraslacion = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0.1, 0.2, 0, 1]
		devolverse = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, -0.3, -0.6, 0, 1]

		if contador == 0 or contador == 1 or contador == 2:
			glMultMatrixf(matrizTraslacion)
			contador += 1
			#glTranslatef(0.1, 0.2, 0.0)
		else:
			glMultMatrixf(devolverse)
			contador = 0
			#glTranslatef(-0.3, -0.6, 0.0)
	elif key == "s" or key == "S":
		matrizShade = [1, 0.3, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
		glMultMatrixf(matrizShade)
	elif key == "f" or key == "F": #Este evento ocurre solo en esta figura, porque esta figura no esta centrada en el origen
		matrizReflexion = [-1, 0, 0, 0, 0, -1, 0, 0,  0, 0, 1, 0, 0, 0, 0, 1]
		glMultMatrixf(matrizReflexion)

def mouseEvent(botonMouse, estadoMouse, x, y):
	if botonMouse == GLUT_LEFT_BUTTON and estadoMouse == GLUT_DOWN:
		glColor3f(random(), random(), random())

#Funcion que me imprime la matriz actual
def imprimirMatriz():
	matriz = glGetFloatv(GL_PROJECTION_MATRIX)
	print matriz

def main():
	global window
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(200,200)

	#creando la ventana
	window = glutCreateWindow("Taller2 - Figura de 8 lados")

	glutDisplayFunc(dibujarOctagono)
	glutIdleFunc(dibujarOctagono)
	imprimirMatriz()
	glutKeyboardFunc(keyPressed)
	glutMouseFunc(mouseEvent)
	initGL(500,500)
	glutMainLoop()

if __name__ == "__main__":
	main()
