"""
Escribir un programa que calcule
la suma de los "n" números naturales.
Por ejemplo si n=100, el programa
calculara la suma del 1 al 100
42 usando un ciclo while
"""
#Importar la biblioteca de tiempo
import time
#Crear las variables para el problema
n = 100
the_sum = 0 
# Tomando el t1
timestamp_01=time.time()
#Iniciando la suma
# 100 
while(n > 0):
    the_sum= the_sum+n #100+99+98+...+1
    n=n-1
#tomamos la solución
timestamp_02=time.time()
#Imprimimos la solución
print(f"La suma es {the_sum}")
#Calculando el tiempo
elapsed_time = round((timestamp_02-timestamp_01)*1e6,ndigits=2)
print(f"Tiempo de ejecución: {elapsed_time}us")
