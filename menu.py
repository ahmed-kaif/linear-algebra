import os
from rich.prompt import Prompt 
from rich.console import Console
from rich.markdown import Markdown
menu = '''# Linear Algebra Calculator
Select Option
1. Rank of Matrix
2. EigenValues & EigenVectors
3. Matrix Multiplication
4. Quit
'''
md = Markdown(menu)
console = Console()
console.print(md)
option = Prompt.ask("Enter your choice",choices=["1","2","3"])
try:
    if option == "1":
        os.system("clear")
        os.system("python rank.py")
    elif option == "2":
        os.system("clear")
        os.system("python eigen.py")
    elif option == "3":
        os.system("clear")
        os.system("python matrix_expression.py")
except:
    print("Bye")
