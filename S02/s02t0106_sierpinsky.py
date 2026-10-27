from array import array as arr
#Parametros de mi cuadricula
rows = 8
columns = 2*rows-1
#Funcion para imprimir matrix

def print_matrix(input_matrix):
    for row in input_matrix:
        print(list(row))
#Creando la grid 2D(Bidimencional)
matrix=[]
#Construyendo el grid
for rows in range (rows):
    new_row=arr('i',[0]*columns)
    matrix.append(new_row)
#Validando la construccion del grid
print(f"Cantidad de filas:{len(matrix)}")
print(f"Cantidad de columnas:{len(matrix[0])}")

#Calculando el centro de la primera fila
center= row // 2 #Se hace division entera
#Estableciendo el centro en 1
matrix[0][center]=1
print_matrix(matrix)
#Se calcula el resto de la matrix
#Siguiendo la logica del sierpinsky Gasket
for row in range(1,rows):
    for col in range(0,columns): 
        print(f"{row}-{col}",end=",")
        left_upper_cell=0
        right_upper_cell=0
        #Si la columna donde estamos es mayor a 0
        if col>0:
            left_upper_cell=matrix[row-1][col-1]
#Si la columna esta un elemento antes del borde derecho
if col < columns-1:
    right_upper_cell=matrix[row-1][col+1]
#Guardo el arreglo
if left_upper_cell!=right_upper_cell:
    matrix[row][col]=1
else:
    matrix[row][col]    
print()
print_matrix(matrix)

    
