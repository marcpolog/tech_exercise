import os.path
from os import path

names = []
errors = []

def main(file_test):
  # Check file extension
  extension = os.path.splitext(file_test)[1]

  # Check if file exists and extension is "TXT"
  if (path.exists(file_test) and extension.upper() == '.TXT'):
    # save filename to check later if already exists for Deadlock
    names.append(file_test)
    tot = 0
    file = open(file_test, "r").read().split('\n')
    # Loop all lines in file
    for line in file:
      try:
        # Check line content is an integer number
        # NOTE: can be float if is required (exercise does not mention it)
        num = int(line)
      except:
        # Check Deadlock (Stack Overflow error)
        if line not in names:
          # Recursive call
          num = main(line)
        # Shows error and Exit loop
        else:
          errors.append(True)
          print("ERROR: The sum of", line, "cannot be calculated becase the filename", file_test, "cannot be a child element (Stack Overflow)")
          break
      # try auto-increment total
      try:
        tot += num
      except:
        errors.append(True)
    
    # Only shows total sum if no errors
    if not len(errors):
      print("The sum of", os.path.abspath(file_test), "is", tot)

    return tot

  # Print error if file does not exists
  else:
    error = True
    print("ERROR: File", os.path.abspath(file_test), "does not exist or is not a TXT file") 

# User input filename
file_test = input("Enter a full path filename: ")

# Execute main function
main(file_test)