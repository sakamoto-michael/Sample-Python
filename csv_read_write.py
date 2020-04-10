# Working with CSV files - reading, modifying, creating
import csv

# Read the CSV file
with open('new\\names.csv', 'r') as csv_file:
  # Open a reader to read the CSV file
  csv_reader = csv.reader(csv_file)

  # Skips the first row (header values)
  # next(csv_reader)

  # Copying the file with a new '-' delimeter
  with open('new_names.csv', 'w') as new_file:
    csv_writer = csv.writer(new_file, delimiter='\t') # \t Represents a tab

    # For each row in the original, write the same line to the new file.
    for line in csv_reader:
      csv_writer.writerow(line)

# Using dictionary reader and writer, this time removing the email column
with open('new\\names.csv', 'r') as csv_file:
  csv_reader = csv.DictReader(csv_file)

  with open('new_names.csv', 'w') as new_file:
    fieldnames = ['first name', 'last name']

    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

    csv_writer.writeheader()

    for line in csv_reader:
      del line['email']
      csv_writer.writerow(line)
