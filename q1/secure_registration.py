is_valid = True 

def print_error(message):
  global is_valid
  is_valid = False
  print ("\n----------------------------")
  print ("REJECTED")
  print (f"{message}")
  print ("------------------------------")
  return

# Name Validation
name = str(input("Enter student name: ").strip())
if not name:
  print_error("Error: Student name is required.")

# Section Validation
section = str(input("Enter class section: ").strip())
# List of valid section inputs
valid_sec = ["Dahlia", "Sampaguita", "Rosal", "Ilang-ilang"]
if section not in valid_sec:
  print_error("Error: Please enter a valid section.")

# Club Choice Validation
club = str(input("Enter chosen club: ").strip())
# List of valid club choices
valid_club = ["Robotics", "Science", "Mathematics", "Programming"]
if club not in valid_club:
  print_error(" Error: Please choose a valid club.")

# Email validation
email = input("Enter student email: ")
if "@" in email and "." in email:
    pass
else:
  print_error ("Error: Please enter a valid email")

# Attendance status
attendance = str(input("Enter student attendance status: ").strip())
# List of different attendance statuses
valid_att = ["Present", "Late", "Absent"]
if attendance not in valid_att:
  print_error("Error: Please enter  attendance status.")

if is_valid:
  print ("\n------------------------------")
  print ("REGISTRATION ACCEPTED!!")
  print ("------------------------------")
  print (f"Student: {name}")
  print (f"Section: {section}")
  print (f"Club: {club}")
  print (f"Email: {email}")
  print (f"Attendance: {attendance}")
