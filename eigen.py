import numpy as np 

Rows = int(input("Give the number of rows: "))  
Columns = int(input("Give the number of columns: "))  
  
example_matrix = []  
for i in range(Rows):  
    single_row = list(map(int, input().split()))  
    example_matrix.append(single_row)

matrixx = np.array(example_matrix).reshape(Rows,Columns) # converting matrix to np.array

eigenVals , eigenVecs = np.linalg.eig(matrixx)

print("EigenValues:\n",eigenVals, "\n")
print("EigenVecs:\n",eigenVecs, "\n")
