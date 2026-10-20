from array import array as arr
#Impresion de una tabla
def print_table(input_table):
 #imprimiendo cada elemento
    for row in table:
        for column in row:
            print(column, end=",")
    print("",end=" \b")
table = [
    arr('i',[1,2,3],),
    arr('i',[4,5,6],),
    arr('i',[7,8,9],),
]
print_table(table)
#Insercion
row= 1
column= 2
value= 99
#Insertar en la fila 1 columna 2 el valor 99
table[row].insert(column, value)
#Imprimiendo mensaje
print(" ")
print("---Despues de la insersion---")
print_table(table)#DontRepeatYourself
#Insertando una fila completa
new_row= arr('i',[100,200,300])
pos=1
table.insert(pos, new_row)
#Imprimiendo mensaje
print(" ")
print("---Despues de la insersion de la fila---")
print_table(table)#DontRepeatYourself
#Eliminacion de elementos
del table[2]
#Imprimiendo mensaje
print(" ")
print("---Despues de la eliminación de la fila---")
print_table(table)#DontRepeatYourself
