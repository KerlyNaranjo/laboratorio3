import math
figura = int(input("Ingrese un numero de lados de una figura geometrica : "))

if figura == 2:
    print ('no hay figuras geometricas formadas por dos lados')

elif figura == 3:
	a = int(input("ingrese el lado 1 del triangulo: "))
	b = int(input("ingrese el lado 2 del triangulo: "))
	c = int(input("ingrese el lado 3 del triangulo: "))
	
	s = (a + b + c)/2

	def areaT():
		area = math.sqrt(s*(s - a)*(s - b)*(s - c))
		print ("Area = " + str(area))

	def perimetroT():
		per = a + b +c
		print ("Perimetro = " + str(per))

	perimetroT()
	areaT()

elif figura == 4:
	lado = int(input("Ingrese el lado del cuadrado: "))

	def areaCir():
		area = lado**2
		print ("Area = " + str(area))

	def perimetroC():
		per = lado * 4
		print("Perimetro = " + str(per))

	areaCir()
	perimetroC()N