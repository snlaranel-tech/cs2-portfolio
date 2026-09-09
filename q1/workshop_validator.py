# f-string lets the user substitute different variables and expressions directly into the string
# defining a print error message to display for all invalid inputs
# global is_valid searches for the variable is_valid outside of the code block

is_valid = True  # Tracks if all inputs are valid and is a global variable

def print_error(message):
  global is_valid
  is_valid = False
  print ("\n----------------------------")
  print ("REGISTRATION NOT ACCEPTED")
  print (f"{message}")
  print ("------------------------------")
  return

# Name validation
name = (input("Enter student name: ").strip())
if not name:
  print_error ("Student name is required.")

# Age validation
age_input = input("Enter student age: ").strip()

try:
  age = int(age_input)
  if not (11 <= age <= 18):
    print_error("Age must be from 11 to 18")

except ValueError:
  print_error("Age must be a valid number.")
# Grade level (gl) validation
try:
  grade_level = int(input("Enter student grade level: ").strip())
  if not grade_level >= 7 and grade_level <= 12:
    print_error ("Invalid Grade Level")
except ValueError:
  print_error("Grade level must be a valid number.")

# Email validation
email = input("Enter student email: ")
if "@" in email and "." in email:
    pass
else:
  print_error ("Invalid email")

# Registration code validation
# len(regis_code) counts how many characters are entered in regis_code
# != means "not equal to" and detects if the input is not equal to 6 characters
regis_code = input("Enter workshop registration code: ").strip()
if len(regis_code) != 6:
  print_error ("The registration code must contain exactly 6 characters.")

if is_valid:
  print ("\n------------------------------")
  print ("REGISTRATION ACCEPTED!!")
  print ("------------------------------")
  print (f"Student: {name}")
  print (f"Age: {age}")
  print (f"Grade Level: {grade_level}")
  print (f"Email: {email}")
  print (f"Registration Code: {regis_code}")
