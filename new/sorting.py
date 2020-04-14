# Sorting in Python
from operator import attrgetter

##### Sorting lists
li = [9,1,8,2,7,3,6,4,5]

# sorted() returns a sorted list
s_li = sorted(li)

# Sorting in reverse
sorted(li, reverse=True)

print('Sorted list:\t', s_li)
print('Original list:\t', li)

# This sorts the original list
li.sort()
# Sorts in descending order
li.sort(reverse=True)

##### Sorting tuples
tup = (9,1,8,2,7,3,6,4,5)
# tup.sort() does not work because it is immutable
s_tup = sorted(tup)
print('Sorted tuple:\t', s_tup)

##### Sorting dictionary
di = {'name': 'Miso', 'type':'Soup', 'rating':7}
s_di = sorted(di)
print('Sorted key dict:\t', s_di)

##### Sort values on specific criteria
li = [-6,-5,-4,1,2,4]
s_li = sorted(li, key=abs)

##### Sorting objects
# Sorting based on specified key
# From Corey Schafer's Python Tutorial: Sorting Lists, Tuples, and Objects
class Employee():
  def __init__(self, name, age, salary):
    self.name = name
    self.age = age
    self.salary = salary

  def __repr__(self):
    return f'({self.name},{self.age},${self.salary})'

e1 = Employee('B', 30, 75000)
e2 = Employee('C', 35, 70000)
e3 = Employee('A', 40, 80000)

employees = [e1,e2,e3]

# Writing a custom function to specify what key to sort on
def employee_sort(employee):
  return employee.age # Key to sort on

# Sorting in ascending order
s_employees = sorted(employees, key=employee_sort)

# Using a lambda function
s2_employees = sorted(employees, key=lambda e: e.name)

# Using the attrgetter from operator module
s3_employees = sorted(employees, key=attrgetter('salary'))

print(f'Sorted by age: {s_employees}')
print(f'Sorted by name: {s2_employees}')
print(f'Sorted by salary: {s3_employees}')