import numpy as np 
from rich.prompt import Prompt 
from rich.console import Console
from rich.markdown import Markdown
from sympy import symbols, expand, collect, sympify

def matrix_input():
    Rows = int(input("Give the number of rows: "))  
    Columns = int(input("Give the number of columns: "))  
    example_matrix = []  
    for i in range(Rows):  
        single_row = list(map(int, input().split()))  
        example_matrix.append(single_row)
    # converting matrix to np.array
    matrixx = np.array(example_matrix).reshape(Rows,Columns) 
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
# Matrix Expression Calc
elif option == "2":
    matrixA = matrix_input()
    A = symbols('A')
    expr_str = input("Enter an expression in terms of A: ")
    try:
        expr = sympify(expr_str)
    except:
        print("Invalid expression.")
        exit()  
    expanded_expr = expand(expr)
    collected_expr = collect(expanded_expr, A)
    result = np.zeros_like(matrixA, dtype=np.int64)
    if collected_expr is not None:
        terms = collected_expr.args
        for term in terms:
            power = term.as_poly().degree()
            coefficient = term.as_coefficient(A**power)
            result = result + (coefficient * np.linalg.matrix_power(matrixA, power)) 
        console.print("Resultant matrix:\n", result)
    else:
        power = collected_expr.as_poly().degree()
        coefficient = collected_expr.as_coefficient(A**power)
        result = result + (coefficient * np.linalg.matrix_power(matrixA, power)) 
        console.print("Resultant matrix:\n", result)

# Matrix Square
elif option == "3":
    matrix1 = matrix_input()
    result = np.linalg.matrix_power(matrix1, 2)
    console.print(result)
