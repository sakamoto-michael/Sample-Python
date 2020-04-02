# Conditionals in Python

# Basic conditional statement
if True:
  print('Conditional was true')

# Conditional based on variable
language = 'Java'

if language == 'Python':
  print('The language is Python')

# Multiple conditions
if language == 'Python':
  print ('The language is Python!')
elif language == 'Java':
  print('The language is Java.')
else:
  print('The language is unknown.')

# Boolean operators: and, or, not

user = 'Power User'
logged_in = True

if user == 'Admin' and logged_in == True:
  print('Admin Page')
else:
  print('Bad creds!')

if not user == 'Moderator' and not user == 'Admin':
  print('Please contact an administrator.')

# Object identity: is
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
print('ID a: ' + str(id(a)))
print('ID b: ' + str(id(b)))

b = a

print(a == b)
print(a is b)
print('ID a: ' + str(id(a)))
print('ID b: ' + str(id(b)))

# False values:
#   False
#   None
#   Zero (any numeric type)
#   '', (), [], {}

condition = 0
if condition:
  print('True')
else:
  print('False')