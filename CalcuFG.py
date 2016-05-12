import math

print ('\t\t\n        CALCULADORA: AREAS Y PERIMETROS\n')
print (' AUTOR/ES: Kerly Naranjo')
print ('           Katherine Lasluisa')

print ('\nEscoja el numero de la figura: \n')
print ('1. Circulo')
print ('2. Triangulo')
print ('3. Cuadrado')
print ('4. Pentagono')

figura = int(input("\nLa opcion es: "))

if figura == 1:
	radio = int(input("\nIngrese el radio del circulo = "))

	def circulo():
		res = round((math.pi*(radio**2)),3)
		print ("\nArea = " + str(res))

	circulo()

elif figura == 2:
	a = int(input("\nIngrese el lado 1 del triangulo: "))
	b = int(input("Ingrese el lado 2 del triangulo: "))
	c = int(input("Ingrese el lado 3 del triangulo: "))
	
	s = (a + b + c)/2

	def areaT():
		area = math.sqrt(s*(s - a)*(s - b)*(s - c))
		print ("\nArea = " + str(area))

	def perimetroT():
		per = a + b +c
		print ("Perimetro = " + str(per))

	perimetroT()
	areaT()

elif figura == 3:
	lado = int(input("\nIngrese el lado del cuadrado: "))

	def areaCir():
		area = lado**2
		print ("\nArea = " + str(area))

	def perimetroC():
		per = lado * 4
		print("Perimetro = " + str(per))

	areaCir()
	perimetroC()

elif figura == 4:
	lado1= int (input("\nIngrese el lado del pentagono:"))
	centro= int (input("Ingrese el centro del pentagono:"))
	
	def perimetro_areaP():
		Perm =5*lado1
		cn= lado1/2
		a= (centro * centro)- (cn * cn)
		b= math.sqrt(a)
		Apotema = (Perm *b)/2
		print ("\nPerimetro = " + str(round(Perm,2)))
		print ("Area = " + str(round(Apotema,2)))
	
	perimetro_areaP()