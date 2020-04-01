# Lists
courses = ['History', 'Math', 'Physics', 'CompSci']

# Length of list
print(len(courses))

# Print List
print(courses)

# Access index of list - STARTS AT ZERO
print(courses[0])

# Negative indexes - starts from end of list (-1)
print(courses[-1])

# Index ranges - start is inclusive, end is not
print(courses[0:2])

# Slicing
print(courses[:2])
print(courses[2:])

# List methods for modification
# Appending an item to end
courses.append('Music')
print(f'Adding Music...')
print(courses)

# Inserting an item at index, doesn't override
courses.insert(0, 'Art')
print('Inserting Art at index 0...')
print(courses)

# Adding items of list to a list - extend
courses_2 = ['Biology', 'P.E.']
courses.extend(courses_2)
print('Extending list...')
print(courses)

# Removing items
courses.remove('Math')
print('Removing Math...')
print(courses)

# Pop item (like stack)
popped = courses.pop()
print(f'Removed {popped} from the list.')
print(courses)

# Reversing a list
courses.reverse()
print('Reversing the list...')
print(courses)

###################
print('#####')

courses = ['History', 'Math', 'CompSci']
nums = [1, 5, 2, 4, 3]

# Sorting list
#courses.sort()
nums.sort()

print(courses)
print(nums)

# Returning sorted version without altering original
sorted_courses = sorted(courses)
print(sorted_courses)
print(courses)

# Min, Max, Sum
print('Min: ' + str(min(nums)))
print('Max: ' + str(max(nums)))
print('Sum: ' + str(sum(nums)))

# Finding value in list - returns the index if found
print(courses.index('Math'))

# Verify existence of value in list
print('Math' in courses)
print('Art' in courses)

#####

# Loops for lists
for course in courses:
  print(course)

# Keeping track of index in loop - start index determines numbering
for index, course in enumerate(courses, start=1):
  print(index, course)

# Combining list items into a string
course_str = ', '.join(courses)
print(course_str)

# Splitting a string into a list
new_list = course_str.split(', ')
print(new_list)

#####

# Tuples - like lists but cannot be modified (immutable)
# Mutable issue
list_1 = ['History', 'Math']
list_2 = list_1
print(list_1)
print(list_2)

list_1[0] = 'Art'
print(list_1)
print(list_2)

# Sets
sets_courses = {'History', 'Math', 'P.E.'}
print(sets_courses) # Does not preserve order!

# Sets remove duplicates
sets_courses = {'History', 'History', 'Math'}
print(sets_courses)

# Sets are OPTIMIZED for finding existence of a value
print('Math' in sets_courses)

# Set operators
set_1 = {'History', 'Art', 'CompSci', 'P.E.'}
set_2 = {'History', 'Math', 'P.E.'}

# Intersection
print(set_1.intersection(set_2))

# Difference
print(set_1.difference(set_2))

# Union
print(set_1.union(set_2))

#####

# Empty lists
empty_list = []
empty_list = list()

# Empty tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty sets
# empty_set = {} IS INCORRECT - this creates a dictionary
empty_set = set()