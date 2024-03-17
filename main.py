import os
import sys
from enum import Enum

import numpy as np
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.style import Style
from sympy import Add, collect, expand, symbols, sympify


class Option(Enum):
    RANK = 1
    EIGEN = 2
    MATMUL = 3


# Rich
console = Console()
red_style = Style(color="red")
green_style = Style(color="green")


def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")


def menu() -> int:
    menu = """# Linear Algebra Calculator
    Select Option
    1. Rank of Matrix
    2. EigenValues & EigenVectors
    3. Matrix Multiplication
    4. Quit
    """
    md = Markdown(menu)
    clear()
    console.print(md)
    option = Prompt.ask("Enter your choice", choices=["1", "2", "3", "4"])
    return int(option)


def matrix_input() -> np.ndarray:
    try:
        Rows = int(input("Give the number of rows: "))
        Columns = int(input("Give the number of columns: "))
        example_matrix = []
        for _ in range(Rows):  # pyright: ignore
            single_row = list(map(int, input().split()))
            example_matrix.append(single_row)
        # converting matrix to np.array
        matrix = np.array(example_matrix).reshape(Rows, Columns)
        return matrix
    except:
        console.print("Enter a valid matrix", style=red_style)
        return None  # pyright: ignore


def calculate_rank(matrix: np.ndarray) -> None:
    if matrix is not None:
        try:
            rank = np.linalg.matrix_rank(matrix)
            console.print("Rank:", rank, "\n")
        except Exception as e:
            console.print("Error:", e, style=red_style)


def calculate_eig(matrix: np.ndarray) -> None:
    if matrix is not None:
        try:
            eigenVals, eigenVecs = np.linalg.eig(matrix)
            console.print("EigenValues:\n", eigenVals, "\n")
            console.print("EigenVectors:\n", eigenVecs, "\n")
        except np.linalg.LinAlgError as e:
            console.print("Error:", e, style=red_style)


def matrix_multiplication() -> None:
    menu = """## Matrix Multiplication
    Select Option
    1. Multiply 2 Matrix
    2. Matrix Expression
    3. Matrix Power
    """
    md = Markdown(menu)
    clear()
    console.print(md)
    option = Prompt.ask("Enter your choice", choices=["1", "2", "3"])
    # Multiply 2 matrices
    if option == "1":
        console.print("Matrix A:", style=green_style)
        matrix1 = matrix_input()
        console.print("Matrix B:", style=green_style)
        matrix2 = matrix_input()
        try:
            result = matrix1 @ matrix2
            console.print("Resultant Matrix:\n", result)
        except:
            console.print("Error:Invalid dimension of matrices\n", style=red_style)
    # Matrix Expression Calc
    elif option == "2":
        matrixA = matrix_input()
        A = symbols("A")
        expr_str = Prompt.ask("Enter an expression in terms of A")
        try:
            expr = sympify(expr_str)
        except:
            print("Invalid expression.")
            return
        expanded_expr = expand(expr)
        collected_expr = collect(expanded_expr, A)
        result = np.zeros_like(matrixA, dtype=np.int64)
        try:
            if isinstance(collected_expr, Add):
                terms = collected_expr.as_ordered_terms()
                for term in terms:
                    power = term.as_poly().degree()  # pyright: ignore
                    coefficient = term.as_coefficient(A**power)  # pyright: ignore
                    result = result + (
                        coefficient * np.linalg.matrix_power(matrixA, power)
                    )
                console.print("Resultant matrix:\n", result)
            else:
                power = collected_expr.as_poly().degree()
                coefficient = collected_expr.as_coefficient(A**power)
                result = result + (coefficient * np.linalg.matrix_power(matrixA, power))
                console.print("Resultant matrix:\n", result)
        except np.linalg.LinAlgError:
            console.print("Error: Please enter a square matrix", style=red_style)

    # Matrix power
    elif option == "3":
        matrix1 = matrix_input()
        power = int(input("Power: "))
        try:
            result = np.linalg.matrix_power(matrix1, power)
            console.print("Resultant Matrix:\n", result)
        except np.linalg.LinAlgError:
            console.print("Error: Please enter a square matrix", style=red_style)


def select(opt: int) -> None:
    if opt == Option["RANK"].value:
        clear()
        console.print(Markdown("## Rank"))
        matrix = matrix_input()
        calculate_rank(matrix)
    if opt == Option["EIGEN"].value:
        clear()
        console.print(Markdown("## EigenValue"))
        matrix = matrix_input()
        calculate_eig(matrix)
    if opt == Option["MATMUL"].value:
        matrix_multiplication()
    input("Press any key to continue...")


def main():
    while True:
        option = menu()
        if option == 4:
            console.print("Good Bye", style=green_style)
            sys.exit(0)
        select(option)


if __name__ == "__main__":
    main()
