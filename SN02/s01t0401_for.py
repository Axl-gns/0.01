"""
Escribir un programa que calcule
la suma de los "n" números naturales.
Por ejemplo si n=100, el programa
calculara la suma del 1 al 100
42
"""
# Importamos biblioteca time
import time
#Tomando el tiempo inicial
timestamp_01=time.time()

#Programa que calcula la suma de los "n"
#Números naturales
n=100
total_sum=0
#Ciclo for
for number in range (1,n+1):
    print(str(number),end= ",")
    total_sum = total_sum + number
    #1:sum <-0+1
    #sum= 1
    #2: sum <-1+2
    #sum=3
    #3:sum <-3+3
    #...
    #100:sum <- sum (-1) +100
print("")
print(f"La Suma de 1 hasta {n} es: {total_sum}")
#Tomando el tiempo final
timestap_02=time.time()
#Impresión del tiempo de ejecución
print(f"Tiempo de ejecucion: {(timestap_02-timestamp_01)*1e6:.2f}μs")