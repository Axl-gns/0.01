#ELIMINACIÓN
#Importando funcion Array del modulo array y renombrando
from array import array as arr
#Importando una funcion de otro archivo
from s02t0102_1d import print_array 
my_array= arr('i',[2,10,15,20])
print("---ANTES DE LA ELIMINACIÓN---")
print_array(my_array)

#Eliminación
my_array.remove(100)
print("---DESPUES DE LA ELIMINACIÓN---")
print_array(my_array)
try:
    my_array.remove(100)
except:
    print("No se encuentra el número en el arreglo")