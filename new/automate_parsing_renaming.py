import os

# Change directory to the one containing files to be renamed
os.chdir('C:\\Users\\sakam\\Desktop\\python\\files to be renamed')

# Print all file names in the directory
# for f in os.listdir():
#   print(f) 

# Split the extension from the file name
for f in os.listdir():
  f_name, f_extension = os.path.splitext(f) # Returns tuple wiith file name and extension.
  
  f_letter, f_title, f_number = f_name.split('-') # Split on each hyphon

  # Remove the whitespaces
  f_title = f_title.strip()
  f_letter = f_letter.strip()
  f_number = f_number.strip()[1:].zfill(2) # This strips the pound symbol and zero fills to 2 digits

  # Create the new file name
  new_name = f'{f_number}-{f_letter}{f_extension}'

  # Rename the file of the current iteration of the loop
  os.rename(f, new_name)
