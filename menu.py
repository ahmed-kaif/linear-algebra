import os
from rich.prompt import Prompt 
from rich.console import Console
from rich.markdown import Markdown
menu = '''# Linear Algebra Calculator
Select Option
1. Rank of Matrix
2. EigenValues & EigenVectors
3. Quit
'''
md = Markdown(menu)
console = Console()
console.print(md)
option = Prompt.ask("Enter your choice",choices=["1","2","3"])
try:
    if option == "1":
        os.system("python rank.py")
    elif option == "2":
        os.system("python eigen.py")
    elif option == "3":
        exit(0)
except:
    print("Bye")
