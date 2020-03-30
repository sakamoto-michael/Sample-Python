# Comments are denoted by a pound symbol
# Python operates on whitespace

# Simple print statement
print('Hello World')

# Print statements including quotation marks
print("Apostrophe's World")
print("Apostrophe's World")

# Multi-line String
multiline_quote = """Testing printing
over
multiple
lines
."""
print(multiline_quote)

# String Length
message = "Hello World #2"
print(len(message))

# Accessing indexes of string
print(message[0])
print(message[0:5])
print(message[6:])

# Changing string case
print(message.lower())
print(message.upper())

# Count instances within string
print(message.count('Hello'))
print(message.count('l'))

# Find instance within string
print(message.find('World'))
print(message.find('Universe'))

# Replace instance within string
new_message = message.replace('World','Universe')
print(new_message)

# Concatenating strings
greeting = 'What\'s up'
name = 'Smith'
message = greeting + ', ' + name + '?'

print(message)

# Concatenating strings 2
message_2 = '{}, {}?'.format(greeting,name)

print(message_2)

# f Strings - Can apply functions within!
f_message = f'{greeting}, {name.upper()}?'
print(f_message)

# Applicable functions to strings
# print(dir(name))

# Broad overview on specific function
print(help(str.lower))