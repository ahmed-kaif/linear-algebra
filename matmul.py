import numpy as np 
from rich.prompt import Prompt 
from rich.console import Console
from rich.markdown import Markdown

def matrix_input():
    Rows = int(input("Give the number of rows: "))  
    Columns = int(input("Give the number of columns: "))  
    example_matrix = []  
    for i in range(Rows):  
        single_row = list(map(int, input().split()))  
        example_matrix.append(single_row)

    matrixx = np.array(example_matrix).reshape(Rows,Columns) # converting matrix to np.array
    return matrixx

menu = '''## Matrix Multiplication
Select Option
1. Multiply 2 Matrix
2. Matrix Power
3. Square of a Matrix
'''
md = Markdown(menu)
console = Console()
console.print(md)
option = Prompt.ask("Enter your choice",choices=["1","2","3"])
if option == "1":
    matrix1 = matrix_input()
    matrix2 = matrix_input()
    try:
        result = matrix1 @ matrix2
        console.print(result)
    except Exception as e:
        print("error:", e, "\n")
elif option == "2":
    expression= Prompt.ask("Enter the expression: ")
    print(expression)
elif option == "3":
    matrix1 = matrix_input()
    result = matrix1 @ matrix1
    console.print(result)
