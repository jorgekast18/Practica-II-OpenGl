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
#2.1.1
#Programa que Genera un cuadrado con radio r = 0.7 de color verde. EL circulo que se va a generar estara centrado
#en el origen, por lo que del origen hacia la izquierda tendra una distancia de 0.35 igualmente hacia la derecha

def initGL(width, height):
	glClearColor(0.5, 0.5, 0.5, 0.0)
	glColor3f(0.0, 0.5, 0.0)
	glMatrixMode(GL_PROJECTION)

def dibujarCuadrado():
	glClear(GL_COLOR_BUFFER_BIT)

	glBegin(GL_QUADS)
	glVertex2f(-0.35, 0.35)
	glVertex2f(0.35, 0.35)
	glVertex2f(0.35, -0.35)
	glVertex2f(-0.35, -0.35)
	glEnd()
	glFlush()
	#glutSwapBuffers();

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
		matrizShade = [1, 0.3, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]#matriz shade calculada a mano
		glMultMatrixf(matrizShade)

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
