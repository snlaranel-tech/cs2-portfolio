#Exercise 1: Count Even Numbers
for num in range (2, 21, 2):    #For loop counting by 2 from 2 till 21, not including 21
  print (num)     #Prints the results vertically

#Exercise 2: The Countdown Timer
countdown_timer = 10     #countdown is set to start at 10
while countdown_timer > 0:     #checks to see if countdown_timer is more than 0 before continuing
  print (countdown_timer)     #displays the countdowm_timer
  countdown_timer -= 1     #subtracts the result inside the countdown_timer and loops until it is 0 and does not meet the given condition

print ("Time is up!")     #prints once the loop ends

#Exercise 3: Skip Multiples
for num in range(1, 16):     #sets the code to start at 1 and end at 16, not including 16
  if num % 3 == 0:     #the "%" returns the remainder after dividing numbers. Checks to see if a number divided by 3 has a remainder of 0, therefore being a multiple of 3
    continue     #checks the truth value of the if statement, if it is, it skips the rest of the code in the loop
  print (num)     #displays the results vertically without the detected multiples of 3

#Exercise 4. Multiplication Table Generator
def show_table(number):     #the function show_table waits for the value of number to run the block of code
  for i in range(1, 11):     #for loop repeats the code beneath it. i is where the number is multiplied and starts from 1 to 11, not including 11.
    m = (number * i)     #m stands for multiplication as it multiplies the entered number by i
    print (f"{number} * {i} = {m}")     #f replaces the variables in the curly brackets with their value gained from the code, then displays it

number = int(input("Enter a number from 1-10: "))     #asks the user for an integer from 1-10
show_table(number)     #passes the entered value for number into the function above to kickstart the code


