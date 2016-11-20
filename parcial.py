#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 #Importamos el modulo de SQLite este ya lo incluye por default debian
conn = sqlite3.connect('/home/user/Documentos/BD/datos_empleados.db') #Abrimos la base de datos 
print "Base de datos conectada con éxito"; # Imprimimos Mensaje de éxito 
sql1='''
 SELECT * FROM empleado'''

cursor1 = conn.execute(sql1)
tramo1=[]
tramo2=[]
tramo3=[]
tramo4=[]
for row in cursor1:
	if row[6] > 0.01 and row[6] <= 472.00:
		tramo1.append(row[6])
		'''print tramo1,"T1"'''
	elif row[6] > 472.00 and row[6] <= 895.24:
		tramo2.append(row[6])
		'''print tramo2,"T2"'''
	elif row[6] > 895.24 and row[6] <= 2038.10:
		tramo3.append(row[6])
		'''print tramo3,"T3"'''
	elif row[6] > 2038.10:
		 tramo4.append(row[6])
		 '''print tramo4,"T4"'''
print tramo1
print tramo2		 
print tramo3		 
print tramo4		 

conn.close()
