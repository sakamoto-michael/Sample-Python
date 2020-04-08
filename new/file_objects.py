# Working with File Objects in Python - Reading and Writing to files
import os

# Specifying the file location using CWD + sub directory
file_name = os.path.join(os.getcwd(), 'new\\test.txt')

# Opening a file, defaults to read. Specifies what operations you will perform on the file.
# f = open(file_name, 'r')

# Print the name of the file
# print(f.name)

# Print the mode the file is opened with
# print(f.mode)

# Must close the file if you open it.
# f.close()

# Context managers - auto close upon exiting the block, also upon exceptions! Convenient!
with open(file_name, 'r') as f:
  # f_contents = f.read() # Reads whole file
  # f_contents = f.readline() # Reads one line of the file. If called multiple times, this will read consecutive lines.
  
  # Iterating over each line in the file
  # for line in f:
  #   print(line, end='')

  # f_contents = f.read(100) # Read the first 100 characters of the file
  # print(f_contents, end='')

  # f_contents = f.read(100) # Read the next 100 characters of the file
  # print(f_contents, end='')

  size_to_read = 10

  f_contents = f.read(size_to_read)
  print(f_contents, end='')

  f.seek(0) # Resets the position of the pointer

  f_contents = f.read(size_to_read)
  print(f_contents)

# Check if the file is closed
print('\n' + str(f.closed))

# Creating a new file / overwriting an existing file. Be careful!
with open('new\\test2.txt', 'w') as f:
  
  # Writing to the file
  f.write('Test')
  f.seek(0) # Reset pointer, will overwrite existing text. Will only overwrite as much as it needs to.
  f.write('R')

# Copying the text of one file to a new file
with open(file_name, 'r') as rf:
  with open('new\\test_copy.txt', 'w') as wf:
    for line in rf:
      wf.write(line)

# Copying a PICTURE file
# Must open this in binary mode (notice 'b' mode), cannot open the same way as text files.
with open('new\\LB 2019.png', 'rb') as rf:
  with open('new\\LB 2019 Copy.png', 'wb') as wf:
    for line in rf:
      wf.write(line)

# Copying in chunks (specify chunk size)
with open('new\\LB 2019.png', 'rb') as rf:
  with open('new\\LB 2019 Copy.png', 'wb') as wf:
    chunk_size = 4096
    rf_chunk = rf.read(chunk_size)
    while len(rf_chunk) > 0:
      wf.write(rf_chunk)
      rf_chunk = rf.read(chunk_size)