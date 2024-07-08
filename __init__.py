# __init__.py

# Import the Inventory class from the inventory module
from .inventory import Inventory

# Import the FoodItem class from the fooditems module
from .fooditems import FoodItem

#Explanation:
#from .inventory import Inventory: This line imports the Inventory class from a module named inventory. The dot (.) before inventory indicates that the module is in the same package or directory as the current module (__init__.py).

#from .fooditems import FoodItem: This line imports the FoodItem class from a module named fooditems, similarly using a relative import from the current package or directory.