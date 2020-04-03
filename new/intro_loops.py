# Python Loops and Iterations
nums = [1, 2, 3, 4, 5]

# Looping through each value in a list
for num in nums:
  print(num)

# Finding a value in a list, breaking upon condition
for num in nums:
  if num == 3:
    print('Found!')
    break
  print(num)

# Finding a value, the continuing execution
for num in nums:
  if num == 3:
    print('Found')
    continue
  print(num)

# Loops within loops
for num in nums:
  for letter in 'abc':
    print(num, letter)

# Iterations - range(starting point, end point)
for i in range(1, 11):
  print(i)

# While loop - must include a breaking condition. Can also included manual break within loop upon a different condition
x = 0
while x < 10:
  if x == 5:
    break
  print(x)
  x += 1

