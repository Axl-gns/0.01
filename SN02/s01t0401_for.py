"""
Escribir un programa que calcule
la suma de los "n" números naturales.
Por ejemplo si n=100, el programa
calculara la suma del 1 al 100
42
"""
# Importamos biblioteca time
import time
#Creando una marca de tiempo
timestamp_01=time.time()

#Programa que calcula la suma de los "n"
#Números naturales
n=100
sum=0
#Ciclo for
for number in range (1,n+1):
    print(str(number) + "")