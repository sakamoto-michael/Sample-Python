import csv

html_output = ''
names = []

# Open the CSV file in read mode
with open('new\\names.csv', 'r') as data_file:
  csv_data = csv.reader(data_file)
  
  # Skip the header row
  next(csv_data)

  # Take the name from each row and append to a name list
  for line in csv_data:
    names.append(f"{line[0]}{line[1]}")

# HTML Description of list
html_output+= f'<p>This is a list of {len(names)} names parsed from a CSV file. Woohoo!</p>'

# Open the list
html_output += '\n<ul>'

# HTML-formatted List of names
for name in names:
  html_output += f'\n\t<li>{name}</li>'

# Close the list
html_output += '\n</ul>'

print(html_output)

# #############################
# SOLUTION USING DICTREADER

html_output = ''
names = []

with open('new\\names.csv', 'r') as csv_file:
  csv_data = csv.DictReader(csv_file)

  # Skip header row  
  next(csv_data)

  for line in csv_data:
    names.append(f"{line['first name']}{line['last name']}")

# HTML Description of list
html_output+= f'<p>This is a list of {len(names)} names parsed from a CSV file. Woohoo!</p>'

# Open the list
html_output += '\n<ul>'

# HTML-formatted List of names
for name in names:
  html_output += f'\n\t<li>{name}</li>'

# Close the list
html_output += '\n</ul>'