# Working with dictionaries
student = {'name': 'Tanaka', 'age': 23, 'courses': ['Math', 'CompSci']}
print(student)

# Accessing by key
print(student['name'])

# Acessing by key using GET method
print(student.get('phone', 'Not Found'))

# Setting a key-value - Creates/Updates existing keys
student['name'] = 'Yamashita'

# Updating multiple keys at once
student.update({'name': 'Watanabe', 'age': 22, 'phone': '555-5555'})
print(student)

# Deleting key (specify key)
del student['phone']

# Deleting key (pop)
age = student.pop('age')
print(student)
print(age)

# Number of keys
print(len(student))

# Keys of dict
print(student.keys())

# Values of dict
print(student.values())

# Key value pairs of dict
print(student.items())

# Loop through keys and values
for key in student:
  print(key)

for key, value in student.items():
  print(key, value)