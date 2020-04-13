'''
LEGB:
  Local - variables defined within a function
  Enclosing - variables within local scope of enclosing functions
  Global - variables defined at the top level of a module (explicit using global keyword)
  Built-in - names that are pre-assigned in Python
'''

import builtins

# Global, because it's in the main body of the file.
x = 'global x'

def test():
  y = 'local y' # Local to this test function
  print(y)
  x = 'local x' # Local to this test function! Not using the global x.
  print(x)

def test_2():
  global x # Now accessing the global x
  x = 'changed x'
  print(x)

# test()
# print(x)
# test_2()

# Be very careful with using global variables. Having local variables makes code easier to maintain and understand.

def test_with_params(z):
  print(z)

# test_with_params('local z')

# Built-in function
m = min([5, 1, 4, 2, 3])
# print(m)

# Return all the builtins
# print(dir(builtins))

# Creating function with same name as builtin
# This prioritizes this min() function (global scope) over the builtin.
def min():
  pass

# Enclosing scope
# Example of nested functions with enclosing scope:
def outer():
  x = 'outer x'

  def inner():
    # nonlocal x # Accessing the outer x variable
    x = 'inner x'
    print(x)

  inner()
  print(x) 
  

outer()
print(x)

'''
Again, the program will look for variables in this priority: L> E> G> B.
'''

