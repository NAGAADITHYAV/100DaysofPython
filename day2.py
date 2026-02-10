print(type(123))
print(type(123.45))
print(type("Hello"))
print(type(True))

#BMI claculator
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
bmi = weight / (height * height)
print("Your BMI is: ", bmi)

print("Welcome to the Tip Calculator.")
total_bill = float(input("What was the total bill? "))
tip_percentage = int(input("How much tip would you like to give? 10, 12 or 15? "))
# tip_amount = total_bill * (tip_percentage / 100)
# total_amount = total_bill + tip_amount
total_amount = total_bill * (1 + (tip_percentage / 100))
people = int(input("How many people to split the bill? "))
print("Each person should pay: ", total_amount / people)

