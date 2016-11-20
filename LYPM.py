#!/usr/bin/python
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import csv 
import codecs
def count_votes(resultados):
	print ("Numero de Usuario para la carrera de " + resultados)
	count = 0
	for line in open('/home/adonis/Documentos/csv/borrowers_test.csv'):
		linea= line.split(",")
		voto = linea[6]
		if resultados in voto:
			count = count + 1
	return count
import csv
datos=[]
with open('/home/adonis/Documentos/csv/borrowers_test.csv', 'r') as archivo:
	lineas = archivo.read().splitlines()
	lineas.pop(0)
	for l in lineas:
		linea =l.split(',')
		datos.append(linea[0])
fh = codecs.open('/home/adonis/Documentos/csv/borrowers_test.csv')
orden = []
for line in fh:
	linea = line.split(',')
	nombre = linea[1]
	orden.append(nombre) 


print "Menu"

while True:

    print "1- Mostrar cantidad de registros clasificando M o F"
    print "2- Buscar archivo"
    print "3- Mostrar cantidad de Usuarios por carrera"
    print "4- Mostrar cantidad de datos Erroneos"
    print "5- Agregar registro al final"
    print "6- Ordenar los registros por orden alfabético"
    print "7- Ordenar los registros por orden alfabético usando quicksort"
    print "8- ordenar por ordenamiento de insercion"
    print "9- Salir"

    elegir=int(raw_input("Ingrese opcion: "))
    
    if elegir == 1:
		print "Selecione opcion"
		while True:
			print "1-Mostrar cantidad de registros clasificando M o F"
			print "2-Grafica M y F"
			print "3-volver a menu"
			seleccione=int(raw_input("Ingrese opcion: "))
			
			if seleccione == 1:
				n_c = []
				hombre = []
				mujer = []
				sexo_null = []
				sex_null = []
				for line in open('/home/adonis/Documentos/csv/borrowers_test.csv'):
					linea = line.split(',')
					sexo_h = linea[4]
					sexo_m = linea[4]
					carrera = linea[6]	
					if sexo_h == "M":
						hombre.append(sexo_h)
					elif sexo_m == "F":
						mujer.append(sexo_m)
					elif sexo_h or sexo_m == "NULL":
						sexo_null.append(sexo_h)
					elif sexo_m  == "":
						sex_null.append(sexo_m)
						
					suma = len(hombre) + len(mujer) + len(sexo_null) + len(sex_null)
						
					
				print "El numero de Hombres que hay es: ", len (hombre) 
				print "El numero de Mujeres que hay es: ",len (mujer)
				print "El numero de NULL en la columna de sexo es: ",len(sexo_null)
				print "El numero de espacio vacios en la colunma de sexo es: ",len(sex_null)
				print "Total: ", suma
			elif seleccione == 2:
				impr = ["Hombres", "Mujeres", "Datos vacios"]
				vol = [7659, 9078, 706]
				expl =(0, 0.05, 0)
				plt.pie(vol, explode = expl, labels=impr, autopct='%1.1f%%', shadow=True)
				plt.title("Grafica Genero", bbox={"facecolor":"0.8", "pad":5})
				plt.show()
				print""
			elif seleccione == 3:
				break
			
		print ""
	
		
		
    elif elegir == 2:
		print "Selecione el metodo de busqueda"
		while True:
			print "1-busqueda lineal"
			print "2-busqueda secuencial"
			print "3-busqueda binaria"
			print "4-salir"
			seleccione=int(raw_input("Ingrese opcion: "))
			
			if seleccione == 1:
			
				L = datos
				x = raw_input ("ingrese el nombre: ")
				def linearSearch(L,x):
					for e in L:
						if e == x.upper() or e == x.lower():
							return True
					return False
				print linearSearch(L,x)
				
			elif seleccione == 2:
				datos=[]
				with open('/home/adonis/Documentos/csv/borrowers_test.csv', 'r') as archivo:
					lineas = archivo.read().splitlines()
					lineas.pop(0)
					for l in lineas:
						linea =l.split(',')
						datos.append(linea[0])

					lista = datos
					buscar = raw_input('ingrese el nombre: ')

					posicion = 0
					encontrado = False
					posicion_valor_buscar = 0

					for posicion in range(len(lista)):
						if lista[posicion]==buscar.lower() or lista[posicion]==buscar.upper():
							posicion_valor_buscar=posicion
							encontrado=True
						posicion=posicion+1
					if encontrado==True:
						print 'Valor '  + buscar + ' encontrado en posicion',posicion_valor_buscar
					else:
						print 'Valor no encontrado'
						
			elif seleccione == 3:
					datos=[]
					with open('/home/adonis/Documentos/csv/borrowers_test.csv', 'r') as archivo:
						lineas = archivo.read().splitlines()
						lineas.pop(0)
						for l in lineas:
							linea =l.split(',')
							datos.append(linea[0])

						lista = datos
						encontrado=False
						buscar=raw_input('Ingrese nombre: ')
						minimo=0
						maximo=len(lista)-1
						centro=0
						posicion=0
						while minimo <= maximo and not encontrado:
							centro=(minimo+maximo) // 2
							if lista[centro]==buscar:
								encontrado=True
								posicion=centro
							elif lista[centro] < buscar:
								minimo=centro+1
							else:
								maximo=centro-1
						print 'el nombre de ' +str(buscar)+' en la posicion: '+str(posicion)
			elif seleccione == 4:
				break
			print ""
		
    elif elegir == 3:
		print "Selecione opcion"
		while True:
			print "1-Mostrar cantidad de Usuarios por carrera"
			print "2-Grafica de carreas"
			print "3-Grafica Faculta de Arquitectura y Ingenieria."
			print "4-Grafica Faculta de Lic"
			print "5-volver a menu"
			seleccione=int(raw_input("Ingrese opcion: "))
			
			if seleccione == 1:
				print(count_votes ("Arquitectura"))
				print(count_votes ("INGENIERIA CIVIL"))
				print(count_votes ("Licenciatura en Anestesiología e Inhaloterapia"))
				print(count_votes ("Licenciatura en Sociología"))
				print(count_votes ("Doctorado en Medicina"))
				print(count_votes ("Licenciatura en Ciencias Jurídicas"))
				print(count_votes ("Licenciatura en Ciencias de la Educación en la Especialidad de Primero y Segundo Ciclo de Educación Básica"))
				print(count_votes ("LICENCIATURA EN ADMINISTRACION DE EMPRESAS"))
				print(count_votes ("Licenciatura en Fisioterapia y Terapia Ocupacional"))
				print(count_votes ("Licenciatura en  Contaduría Pública"))
				print(count_votes ("Ingeniería Industrial"))
				print(count_votes ("Licenciatura en Mercadeo Internacional"))
				print(count_votes ("Licenciatura en Matemática"))
				print(count_votes ("Especialidad Médica en Ginecología y Obstetricia"))
				print(count_votes ("Licenciatura en Laboratorio Clínico"))
				print(count_votes ("Ingeniería Agronómica"))
				print(count_votes ("LICENCIATURA EN PSICOLOGIA"))
				print(count_votes ("Ingeniería de Sistemas Informáticos"))
				print(count_votes("Licenciatura en Biología"))
				print(count_votes("Licenciatura en Letras"))
				print(count_votes("Profesorado en Educación Inicial y Parvularia"))
				print(count_votes("Licenciatura en Química y Farmacia"))
				print(count_votes("Licenciatura en Física"))
				print(count_votes("Profesorado en Matemática para Tercer Ciclo de Educación Básica y Educación Media"))
				print(count_votes("Profesorado en Idioma Inglés para Tercer Ciclo de Educación Básica y Educación Media"))
				print(count_votes("Licenciatura en Lenguas Modernas Especialidad en Francés e Inglés"))
				print(count_votes("Maestría en Administración Financiera"))
				print(count_votes("Licenciatura en Economía"))
				print(count_votes("Profesorado en Ciencias Sociales para Tercer Ciclo de Educación Básica y Educación Media"))
				print(count_votes("Maestría en Profesionalización de la Docencia Superior"))
				print(count_votes("Profesorado en Biología para Tercer Ciclo de Educación Básica y Educación Media"))
				print(count_votes("Profesorado en Educación Básica para Primero y Segundo Ciclos"))
				print(count_votes("Maestría en Gestión Ambiental"))
				print(count_votes("Maestría en Métodos y Técnicas de Investigación Social"))
				
			elif seleccione == 2:
				impr = ['Ar','ING_C','Lic_A_I','Lic_S','Doc-M','Lic_C_J','Lic_C_E_E_P y S_C_Educacion Basica','LIC_A_E','Lic_F_T_O','Lic_C_P','Ing_Ind','Lic_M_I','Lic_M','Esp_M_G_O','Lic_L_C','Ing_Agro','LIC_P','Ing_S_i','LIC_A_E','Lic_B','Lic_L','P_E_I_P','Lic_Q_F','Lic_F','Profe_M_T_C_E_B_E_M','Profe_I_I_T_C_E_B_E_M','Lic_L_M_E_F_I','M_A_F','Lic_E','Profe_C_S_T_C_E_B_E_M','M_Profe_D_S','Profe_B_T_C_E_B_E','Profe_E_B_P_S_C','M_G_A','M_M_T_I_S']
				vol = [1035,996,576,194,3249,1317,767,1236,593,875,325,570,424,13,1025,441,840,623,1236,169,185,44,203,65,247,211,503,35,29,28,36,20,133,27,9]
				expl =(0, 0.05, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
				plt.pie(vol, explode=expl, labels=impr, autopct='%1.1f%%', shadow=True)
				plt.title("Grafica Carreras", bbox={"facecolor":"0.8", "pad":5})
				plt.show()
			elif seleccione == 3:
				N = 4
				print "\n","Preparando estadisticas......" , "\n"
				menMeans = (1035,325,441,623)
				menStd =  (8)
				ind = np.arange(N)
				width = 0.35
				fig, ax = plt.subplots()
				rects1 = ax.bar(ind, menMeans, width, color='g', yerr=menStd)
						
				ax.set_ylabel('Numero de votos')
				ax.set_title('Estadisticas de la Encuesta sobre Frutas y Vegetales')
				ax.set_xticks(ind + width)
				ax.set_xticklabels(('Arquitectura','Ing_Civil','Ing_Sistemas','Ing industrial'))
						
				def autolabel(rects):
					for rect in rects:
						height = rect.get_height()
						ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
						'%d' % int(height),
						ha='center', va='bottom')
								
				autolabel(rects1)
				plt.show()
				print ""
			elif seleccione == 4:
				N = 17
				print "\n","Preparando estadisticas......" , "\n"
				menMeans = (576,194,1317,767,1236,593,875,570,424,1025,840,169,185,203,65,503,29)
				menStd =  (8)
				ind = np.arange(N)
				width = 0.35
				fig, ax = plt.subplots()
				rects1 = ax.bar(ind, menMeans, width, color='b', yerr=menStd)
						
				ax.set_ylabel('Numero de usuarios por carrera')
				ax.set_title('Estadisticas de la faculta de licenciatura')
				ax.set_xticks(ind + width)
				ax.set_xticklabels(('A_I','S','C_J', 'C_E','A_E','F','C_P','M_I','M', 'L_C','P','B','L','Q_F','F', 'L_M_E_F_I','E' ))
						
				def autolabel(rects):
					for rect in rects:
						height = rect.get_height()
						ax.text(rect.get_x() + rect.get_width()/2., 1.00*height,
						'%s' % int(height),
						ha='center', va='bottom')
							
				autolabel(rects1)
				plt.show()
				print ""
			elif seleccione == 5:
				break
		print""
		
    elif elegir == 4:
		nombre_null = []
		nombre_null1 = []
		apellido_null = []
		c_c_null = []
		fecha_null = []
		sexo1_null = []
		c_d_c_null = []
		n_c_null = []
		for line in open('/home/adonis/Documentos/csv/borrowers_test.csv'):
			linea = line.split(',')
			Nombre = linea[0]
			Apellido = linea[1]
			Codigo_Categoria = linea[2]
			Fecha = linea[3]
			Sexo = linea[4]
			Codigo_Carrera = linea[5]
			Nombre_Carrera = linea[6]	
			if Nombre == "NULL":
				nombre_null.append(Nombre)
			elif Sexo == "":
				sexo1_null.append(Sexo)
			elif Apellido  == "NULL":
				apellido_null.append(Apellido)
			elif Nombre_Carrera == "":
				n_c_null.append(Nombre_Carrera)
			elif Codigo_Categoria == "NULL":
				c_c_null.append(Codigo_Categoria)
			elif Fecha == "":
				fecha_null.append(Fecha)
			elif Codigo_Carrera == "":
				c_d_c_null.append(Codigo_Carrera)
				
		print "El numero de datos vacios en la columna de Nombre es: ",len(nombre_null)
		print "El numero de datos vacios en la columna de Apellido es: ",len(apellido_null)
		print "El numero de datos vacios en la columna de sexo es: ",len(sexo1_null)
		print "El numero de datos vacios en la columna de Nombre de carrera es: ",len(n_c_null)
		print "El numero de datos vacios en la columna de Codigo de Categoria es: ",len(c_c_null)
		print "El numero de datos vacios en la columna de Fecha es: ",len(fecha_null)
		print "El numero de datos vacios en la columna de Codigo de Carrera es: ",len(c_d_c_null)
		print""
		
    elif elegir == 5:
		fh = open('/home/adonis/Documentos/csv/borrowers_test.csv','a')
		obj=csv.writer(fh,delimiter=',', quotechar= ',', quoting=csv.QUOTE_MINIMAL) 
		nombres=raw_input("Ingrese nombres: ")
		apellidos=raw_input("Ingrese apellidos: ")
		C_c=raw_input("Ingrese codigo de categoria: ")
		n_fecha=raw_input("Ingrese fecha de registro: ")
		Sexo=raw_input("Ingrese sexo: ")
		c_carrera=raw_input("Ingrese codigo de carrera: ")
		n_carrera=raw_input("Ingrese nombre de carrera: ")
		obj.writerow([apellidos, nombres, C_c, n_fecha,Sexo, c_carrera, n_carrera])
		fh.close()
		print "Datos ingresados"
		
		print""
		
    elif elegir == 6:
		datos=[]
		with open('/home/adonis/Documentos/csv/borrowers_test.csv', 'r') as archivo:
			lineas = archivo.read().splitlines()
			lineas.pop(0)
			for l in lineas:
				linea =l.split(',')
				datos.append(linea[0])
		a = datos
		def burbuja(lista,tam):
			for i in range(1,tam):
				for j in range(0,tam-i):
					if(lista[j] > lista[j+1]):
						k = lista[j+1]
						lista[j+1] = lista[j]
						lista[j] = k;
		 
		def imprimeLista(lista,tam):
			for i in range(0,tam):
				print lista[i],

		burbuja(a,len(a))
		imprimeLista(a,len(a))
		print ""
		
    elif elegir == 7:
		
		def quickSort(alist):
			quickSortHelper(alist,0,len(alist)-1)

		def quickSortHelper(alist,first,last):
		   if first<last:

			   splitpoint = partition(alist,first,last)

			   quickSortHelper(alist,first,splitpoint-1)
			   quickSortHelper(alist,splitpoint+1,last)


		def partition(alist,first,last):
		   pivotvalue = alist[first]

		   leftmark = first+1
		   rightmark = last

		   done = False
		   while not done:

			   while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
				   leftmark = leftmark + 1

			   while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
				   rightmark = rightmark -1

			   if rightmark < leftmark:
				   done = True
			   else:
				   temp = alist[leftmark]
				   alist[leftmark] = alist[rightmark]
				   alist[rightmark] = temp

		   temp = alist[first]
		   alist[first] = alist[rightmark]
		   alist[rightmark] = temp


		   return rightmark
		alist = orden
		quickSort(alist)
		print(alist)
		
		print""
    elif elegir == 8:
		fh = open('/home/adonis/Documentos/csv/borrowers_test.csv')
		lista = []
		for line in fh:
			linea = line.split(',')
			nombre = linea[0]
			lista.append(nombre)
		def insercion (lista) :
			for indice in range(1,len(lista)):
				valor = lista[indice]
				i = indice - 1
				while i>=0:
					if valor < lista[i]:
						lista[i+1] = lista[i]
						
						lista[i] = valor
						i = i - 1
					else:
						break
		insercion(lista)
		print(lista)
		print ""
		
		
    elif elegir == 9:
		break
