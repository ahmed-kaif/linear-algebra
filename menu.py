import os
menu = '''Select Option
1. Rank of Matrix
2. EigenValues & EigenVectors
'''
print(menu)
option = int(input("Enter your choice: "))

if option == 1:
    os.system("python rank.py")
elif option == 2:
    os.system("python eigen.py")
