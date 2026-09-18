def print_error(message):
  global is_valid
  is_valid = False
  print ("\n----------------------------")
  print ("REJECTED")
  print (f"{message}")
  print ("------------------------------")
  return

#Name Validation
name = str(input("Enter student name: ").strip())
if not name:
  print_error ("Student name is required.")

#Section Validation
valid_sec = [""]
section = str(input("Enter class section: ").strip())

