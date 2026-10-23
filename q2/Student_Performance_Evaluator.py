#defining the calculation for th average
def calculate_average(s1, s2, s3):
  return (s1 + s2 + s3)/3

#defining the category of performance
def get_performance(average):
  if 85 <= average <= 100:
    return "Mastery"
  elif 70 <= average < 85:
    return "Developing"
  else:
    return "Needs reviewing"

#defining eligibility based on the aquired average and input of completed tasks
def is_eligible(average, completed_tasks):
  return average >= 85 and completed_tasks >= 3

#giving value to variables
s1 = float(input("Enter Score 1: "))
s2 = float(input("Enter Score 2: "))
s3 = float(input("Enter Score 3: "))
completed_tasks = int(input("Completed Tasks: "))

#calling the functions
average = calculate_average(s1, s2, s3)
performance = get_performance(average)
eligible = is_eligible(average, completed_tasks)

#Displaying results
print (f"Average: {average:.2f}")
print (f"Performance: {performance}")
print (f"Eligible for Challenge: {eligible}")

#Documentation Questions

# 1. Which function returns a number, which returns a string, and which returns a Boolean?
#-The function calculate_average() returns a number, the function get_performance returns a string, and the function is_eligible returns a Boolean.

# 2. Explain how the average moves from calculate_average() into get_performance()
#-The average moves from calculate_average() into get_performance by using variables (calculate_average gets the average of the 3 scores, which is stored in the variable "average") and function arguments (the value of average is passed to get_performance as an input argument)

# 3. What happens when a student has a high average but has completed fewer than three tasks?
#-The student will have the performance category of mastery. However, they will be labeled "false" in the eligible for challenge section.

# 4. Why is return more appropriate than simply printing the result inside each function?
#-Using return is more appropriate because it allows functions to pass inputted information back to the main program for various uses, while using print simply dispkays text on screen and discards values



