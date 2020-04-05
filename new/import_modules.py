# Explore importing modules
# Import statements (this works because it is in the same directory)

# Can use this to shorten the imported module when calling its functions 
# import my_module as mm 

# Importing specific function/variable from a module
from my_module import find_index, test
import sys

# from my_module import * is frowned upon because it imports everything

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses,'Physics')
print(index)
print(test)

print(sys.path)