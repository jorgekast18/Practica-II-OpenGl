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
#2.1.3
#Programa que Genera un circulo con radio r = 1.5 de color negro. EL circulo que voy a generar estara centrado
#en el origen, por lo que del origen hacia la izquierda tendra una distancia de 0.75t y hacia la derecha
#tambien.


def initGL(width, height):
	glClearColor(0.5, 0.5, 0.5, 0.0)
	glMatrixMode(GL_PROJECTION)
	glColor3f(0.0, 0.5, 0.0)

def dibujarCirculo():
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_POLYGON)
	for i in range(400):
		x = 0.75*sin(i) #Cordenadas polares x = r*sin(t) donde r = radio/2 (Circunferencia centrada en el origen)
		y = 0.75*cos(i) #Cordenadas polares y = r*cos(t)
		glVertex2f(x, y)
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
	window = glutCreateWindow("Taller2 - Circulo")

	glutDisplayFunc(dibujarCirculo)
	glutIdleFunc(dibujarCirculo)
	imprimirMatriz()
	glutKeyboardFunc(keyPressed)
	glutMouseFunc(mouseEvent)
	initGL(500,500)
	glutMainLoop()

if __name__ == "__main__":
	main()
