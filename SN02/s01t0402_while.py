"""
Escribir un programa que calcule
la suma de los "n" números naturales.
Por ejemplo si n=100, el programa
calculara la suma del 1 al 100
42 usando un ciclo while
"""
# Importamos biblioteca time
import time

# Función que suma los primeros "n" números naturales
def sum_of_n(n):
    total_sum = 0
    number = 1
    
    # Ciclo while básico para sumar hasta n
    while number <= n:
        total_sum = total_sum + number
        number = number + 1  # Avanzamos el número de uno en uno
        
    return total_sum
   
# Variable para guardar el dataset
dataset = [] 

# Generando el contenido de dataset (sabemos que son 10 repeticiones)
repetition = 1
while repetition <= 10:
    # Tomo el tiempo inicial
    timestamp_01 = time.time()
    
    # Calculo n
    n = repetition * 100
    
    # Sumo los "n" números llamando a la función
    results = sum_of_n(n)
    
    # Tomo el tiempo final
    timestap_02 = time.time()
    
    # Calculamos el tiempo (dejamos el round porque ya venía en tu código original)
    elapsed_time = round((timestap_02 - timestamp_01) * 1000000, 2)
    
    # Guardamos los datos en la lista
    dataset.append((n, elapsed_time, results))
    
    # Aumentamos la repetición para avanzar
    repetition = repetition + 1

# Imprimiendo el dataset usando un while básico (sabemos que tiene 10 elementos)
indice = 0
while indice < 10:
    print(dataset[indice])
    indice = indice + 1