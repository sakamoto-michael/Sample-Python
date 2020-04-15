# Error handling using try and except blocks

# File Not Found Error > General
# Try - error prone code block
try:
  f = open('new\\test.txt')
  # var = badvar # Test an exception
  # Raising a manual exception
  if f.name == 'new\\test.txt':
    raise Exception
# Exception catching
except FileNotFoundError as e:
  print(e)
except Exception as e:
  print('Error!')
  print(e)
# If no exceptions...
else:
  print(f.read())
  f.close()
# Runs no matter what happens:
finally:
  print("Executing Finally...")