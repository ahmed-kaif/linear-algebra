import numpy as np 

Rows = int(input("Give the number of rows: "))  
Columns = int(input("Give the number of columns: "))  
  
example_matrix = []  
for i in range(Rows):  
    single_row = list(map(int, input().split()))  
    example_matrix.append(single_row)

matrixx = np.array(example_matrix).reshape(Rows,Columns) # converting matrix to np.array

try:
    rank = np.linalg.matrix_rank(matrixx)
    print("Rank:",rank, "\n")
except Exception as e:
    print("error:", e, "\n")
