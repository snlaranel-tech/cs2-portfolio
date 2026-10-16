# Calculates the total purchase cost
def calculate_total(price, quantity):
  return price * quantity

# Calculates the total change or shortage in payment
def calculate_change(payment, total): 
  return payment - total

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
# -
# 3. Where is the returned total stored, and how is it reused?
# -
# 4. Why is it useful to separate total calculation from change calculation?
# -


