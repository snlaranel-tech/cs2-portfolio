# Calculate_total() function multiplies the item's price by its quantity to get the total cost.
def calculate_total(price, quantity):
  return price * quantity

# Calculate_change calculates the difference between the payment amount and the total cost. A positive result means the person buyer gets change, zero means exact payment, and a negative result means a shortage in the payment.
def calculate_change(payment, total): 
  return payment - total

# assigning variables
price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
payment = float(input("Enter amount paid: "))

total = calculate_total(price, quantity)
change = calculate_change(payment, total)

print ("Total Cost: PHP", total)
# Determines if the amount paid is sufficient, and if not, asks for an additional payment.
if change >= 0:
  print ("Change: PHP", change)
else:
  shortage = (change)
  print ("Insufficient payment!! Additional amount needed: PHP", change)

# DOCUMENTATION QUESTIONS
# 1. What does each function do?
# -calculate_total() multiplies the item price by its quantity to compute the purchase's total cost. calculate_change() subtracts the payment by the total cost from the previous function.
# 2. What is the difference between the parameters price and quantity and the actual arguments passed to the function?
# -The parameters price and quantity are variables presented in the function that receives values. Actual arguments are the values assigned to the function when it is called.
# 3. Where is the returned total stored, and how is it reused?
# -The returned total is stored in the variable "total". It is reused in calculate_change() to determine the change or shortage in payment and in the print() code to display the total cost of the item/s bought.
# 4. Why is it useful to separate total calculation from change calculation?
# -It is useful to separate the calculations because it makes the code more organized, easier to understand, and easier to control if anything goes wrong. It also allows each function to perform a specific task independently without interferance.


