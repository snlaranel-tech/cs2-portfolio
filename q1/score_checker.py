# Asks the user to input their numerical grade as an integer.
score = int(input("Enter your score: "))

#Validates if the entered numerical score is within the allowed range of 0 to 100.
#Asks for a new number if the entered value is outside the allowed range using a loop.
while score < 0 or score > 100:
    print("Invalid score")
    score = int(input("Please enter a valid score: ")) 

#Determines the values aappropriate performance classification to be printed.
if 90 <= score <= 100:
  print("Outstanding")
elif 80 <= score < 90:
  print("Very Satisfactory")
elif 75 <= score < 80:
  print("Satisfactory")
elif 0 <= score < 75:
  print("Needs Improvement")
