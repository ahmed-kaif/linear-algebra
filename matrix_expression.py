import numpy as np 
from rich.prompt import Prompt 
from rich.console import Console
from rich.markdown import Markdown
from rich.style import Style
from sympy import symbols, expand, collect, sympify, Add

red_style = Style(color="red")
green_style = Style(color="green")

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
2. Matrix Expression
3. Matrix Power
'''
md = Markdown(menu)
console = Console()
console.print(md)
option = Prompt.ask("Enter your choice",choices=["1","2","3"])
if option == "1":
    console.print("Matrix A:\n", style=green_style)
    matrix1 = matrix_input()
    console.print("Matrix B:\n", style=green_style)
    matrix2 = matrix_input()
    try:
        result = matrix1 @ matrix2
        console.print("Resultant Matrix:\n",result)
    except:
       console.print("Error:Invalid dimension of matrices\n", style= red_style)
# Matrix Expression Calc
elif option == "2":
    matrixA = matrix_input()
    A = symbols('A')
    expr_str = Prompt.ask("Enter an expression in terms of A")
    try:
        expr = sympify(expr_str)
    except:
        print("Invalid expression.")
        exit()  
    expanded_expr = expand(expr)
    collected_expr = collect(expanded_expr, A)
    result = np.zeros_like(matrixA, dtype=np.int64)
    try:
        if isinstance(collected_expr, Add):
            terms = collected_expr.as_ordered_terms()
            for term in terms:
                power = term.as_poly().degree() # pyright: ignore
                coefficient = term.as_coefficient(A**power) # pyright: ignore
                result = result + (coefficient * np.linalg.matrix_power(matrixA, power)) 
            console.print("Resultant matrix:\n", result)
        else:
            power = collected_expr.as_poly().degree()
            coefficient = collected_expr.as_coefficient(A**power)
            result = result + (coefficient * np.linalg.matrix_power(matrixA, power)) 
            console.print("Resultant matrix:\n", result)
    except np.linalg.LinAlgError as e:
        console.print("Error: Please enter a square matrix",style=red_style)

# Matrix Square
elif option == "3":
    matrix1 = matrix_input()
    power = int(input("Power: "))
    try:
        result = np.linalg.matrix_power(matrix1, power)
        console.print("Resultant Matrix:\n",result)
    except np.linalg.LinAlgError:
        console.print("Error: Please enter a square matrix",style=red_style)
