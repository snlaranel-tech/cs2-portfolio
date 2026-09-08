#Student Name Validation
name = input("Enter student name: ")
if not name:
  print("\n------------------------------")
  print("REGISTRATION IS NOT ACCEPTED")
  print("Reason: Student name is required.")
  print("------------------------------")

#Age Validation
ageinput = input("Enter age: ")
age = int(ageinput)
print("\n------------------------------")
print("REGISTRATION IS NOT ACCEPTED")
if age < 11 or age > 18:
  print("Reason: Age must be an integer from 11 to 18.")
  print("------------------------------")

#Grade Level Validation
gradeinput = input("Enter grade level: ")
validgrades = ["7", "8", "9", "10", "11", "12"]
if gradeinput not in validgrades:
  print("\n------------------------------")
  print("REGISTRATION IS NOT ACCEPTED")
  print("Reason: Invalid grade level.")
  print("------------------------------")

#Email Validation
email = input("Enter email address: ").strip()
if "@" not in email or "." not in email:
  print("\n------------------------------")
  print("REGISTRATION IS NOT ACCEPTED")
  print("Reason: Invalid email format. Email must contain '@' and '.'")
  print("------------------------------")

#Registration Code Validation
regiscode = input("Enter registration code: ").strip()
if len(regiscode) != 6:
  print("\n------------------------------")
  print("REGISTRATION NOT ACCEPTED")
  print("Reason: The registration code must contain exactly 6 characters.")
  print("------------------------------")
 
#Final Success Output
  print("\n------------------------------")
  print("REGISTRATION ACCEPTED")
  print("------------------------------")
  print(f"Student: {name}")
  print(f"Age: {age}")
  print(f"Grade Level: {gradeinput}")
  print(f"Email: {email}")
  print(f"Registration Code: {regiscode}")
  print("------------------------------")

if __name__ == "__main__":
  main()
  
