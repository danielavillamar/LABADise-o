# import generate_AFN_from_re 
from Functions import *

try:
  # ask for the regular expression
  regular_expression = input("Enter the regular expression: ")

  # generate the AFN
  thompson_algorithm(regular_expression)
  
 except:
    print("Expresión regular no válida")





