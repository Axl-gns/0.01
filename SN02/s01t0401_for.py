"""
Escribir un programa que calcule
la suma de los "n" números naturales.
Por ejemplo si n=100, el programa
calculara la suma del 1 al 100
42
"""
# Importamos biblioteca time
import time
#Función que suma los primeros "n" numeros naturales
def sum_of_n(n):
    total_sum=0
    #Sumando los "n" numeros
    #Ciclo for
    for number in range (1,n+1):
     total_sum = total_sum + number
   #Retornando 
    return total_sum
   
#Variable para guardarel data set

dataset=[] #[(n,time,sum),(n,time,sum)]
#Generando el contenido de dataset
for repetition in range(1,11):
   #Tomo el tiempo 1 (inicial)⏱️
   #Tomando el tiempo inicial
   timestamp_01=time.time()
   #Sumo los "n" numeros 
   n= repetition * 500
   #Guardo el resultado en result
   results = sum_of_n(n)
   #Tomando el tiempo final⏱️
   timestap_02=time.time()
   #Calculando el tiempo
   elapsed_time = round((timestap_02-timestamp_01)*1e6,ndigits=2)
   #Agregar la tripleta de los datos al dataset
   dataset.append( (n,elapsed_time,results) )
#Imprimiendo dataset
for tup in dataset:
   print(tup)