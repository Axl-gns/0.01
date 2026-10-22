from array import array as arr
#Parametros de mi cuadricula
rows = 8
columns = 2*rows-1
#Creando la grid 2D(Bidimencional)
matrix=[]
#Construyendo el grid
for rows in range (rows):
    new_row=arr('i',[0]*columns)
    matrix.append(new_row)
#Validando la construccion del grid
print(f"Cantidad de filas:{len(matrix)}")
print(f"Cantidad de columnas:{len(matrix[0])}")
for rows in matrix:
    print(list(rows))