# Functions in Python
# Good practice - keep your code DRY - don't repeat yourself.

# Empty function - must include 'pass', cannot leave blank
def empty_func():
  pass

empty_func()

# Basic print function
def hello_func():
  print('Hello Function')

hello_func()

# Function with return value
def return_func():
  return 'This is a returned string!'

print(return_func())

# Passing arguments to a function
def arguments_func(greeting, name):
  return f'{greeting}, {name}!'
  
print(arguments_func('Hello', 'John'))

# Passing arguments to a function, otherwise given default values
def arguments2_func(greeting, name = 'you'):
  return f'{greeting}, {name}!'

print(arguments2_func('Hello'))

# *args (arguments) and **kwargs (keyword arguments)
def student_info(*args, **kwargs):
  print(args)
  print(kwargs)

courses = ['Math', 'Music']
info = {'name': 'John', 'age': 23}

# The * (for list) and ** (for dictinoary) here unpacks the information contained in the arguments 
student_info(*courses, **info)

def new_func():
  """This is a doc string. E.g. VERB X and RETURN Y"""
  pass

