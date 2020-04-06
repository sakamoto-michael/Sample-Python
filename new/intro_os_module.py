import os # Built-in module
from datetime import datetime

# Show all attributes and methods in OS module
#print(dir(os))

print(os.getcwd())

# Changing the working directory
os.chdir('/Users/sakam/Desktop/')
print(os.getcwd())

# Listing the files in the working directory
print(os.listdir())

# Making a directory
os.mkdir('OS-Demo')
os.makedirs('OS-Demo-2/Sub-Dir-1')

# Deleting a directory
os.rmdir('OS-Demo')
os.removedirs('OS-Demo-2/Sub-Dir-1') # Dangerous, because it deletes recursively

# Renaming a file/folder
os.rename('css_sandbox','css_sandbox1')
os.rename('css_sandbox1', 'css_sandbox')

# Get file stats
#file_stats = os.stat('css_sandbox')
mod_time = os.stat('css_sandbox').st_mtime
print(datetime.fromtimestamp(mod_time))

# Using the os.walk() function - searches through the files and folders 
for dirpath, dirnames, filenames in os.walk('/Users/sakam/Desktop/'):
  print('Current Path:', dirpath)
  print('Directories:', dirnames)
  print('Files:', filenames)

# Getting environment variables - this is the home environment
print(os.environ.get('USERPROFILE'))

# Creating a new path for a new file
file_path = os.path.join(os.environ.get('USERPROFILE'), 'test.txt')
print(file_path)

# Creating files to be covered in further studies

# Getting the basename of a path
base_name = os.path.basename('/tmp/test.txt')
print(base_name)

# Getting the dirname of a path
dir_name = os.path.dirname('/tmp/text.txt')
print(dir_name)

# Getting both dir and base names
split_names = os.path.split('/tmp/test.txt')
print(split_names)

# Check if path exists
print(os.path.exists('/tmp/test.txt'))

# Check if folder or file
os.path.isdir('/tmp/test.txt')
os.path.isfile('/tmp/asdfjkl')

# Split path root and extension
print(os.path.splitext('/tmp/test.txt'))

