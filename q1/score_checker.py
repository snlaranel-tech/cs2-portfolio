# Ask the user to input their numerical grade as an integer
score = int(input("Enter your score: "))

#Validate if the entered score is within the allowed range
# Ask for a new number if the entered value is outside the allowed range
while score < 0 or score > 100:
    print("Invalid score")
    score = int(input("Please enter a valid number: ")) 

#Determine the values aappropriate performance classification
if 90 <= score <= 100:
  print("Outstanding")
elif 80 <= score < 90:
  print("Very Satisfactory")
elif 75 <= score < 80:
  print("Satisfactory")
elif 0 <= score < 75:
  print("Needs Improvement")
