# By default Python looks for modules in Python directory
# If not found there, searches in PATH
import sys
print(sys.path)

import modulo
import moduloN

modulo.metodo()
moduloN.metodo()

# Using alias:
import modulo as A
import moduloN as B
A.metodo()
B.metodo()

# Modules can be grouped into packages = folder with module files (*.py) + __init__.py file
