
print("Welcome to the Tip Calculator.")
total_bill = float(input("What was the total bill? "))
tip_percentage = int(input("How much tip would you like to give? 10, 12 or 15? "))
# tip_amount = total_bill * (tip_percentage / 100)
# total_amount = total_bill + tip_amount
total_amount = total_bill * (1 + (tip_percentage / 100))
people = int(input("How many people to split the bill? "))
print("Each person should pay: ", round(total_amount / people, 2))

