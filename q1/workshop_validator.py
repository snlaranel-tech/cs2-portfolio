def print_error(message):
  print ("\n----------------------------")
  print (" REGISTRATION IS NOT ACCEPTED ")
  print (f" {message} ")
  print ("------------------------------")
  return

name = input("Enter student name: ").strip()
if not name:
  print_error ("Student name is required.")

age_input = input("Enter student age: ").strip()
age = int(age_input)
if not (11 < age < 18):
  print_error ("Age must be from 11 to 18")

grade_level = int(input("Enter student grade level: ").strip())
valid_gl = (7, 8, 9, 10, 11, 12)
if not grade_level <= 7 and grade_level >= 12:
  print_error ("Invalid Grade Level")

email = input("Enter student email: ")
if "@" in email and "." :
    pass
else:
    print_error ("Invalid email")
