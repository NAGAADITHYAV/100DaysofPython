# while True:
#     number = int(input("Enter a number: "))
#     if number % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

#Roller Coaster Ticket Price Calculator
# while True:
#     height = int(input("Enter your height in cm: "))
#     if height >= 120:
#         print("You can ride the roller coaster.")
#         age = int(input("Enter your age: "))
#         if age < 18:
#             print("You have to pay $5.")
#         elif age >= 18 and age < 45:
#             print("You have to pay $10.")
#         else:
#             print("You have to pay $15.")
        
#         photo = input("Do you want a photo? (yes/no): ")
#         if photo == "yes":
#             print("You have to pay $3.")
#         else:
#             print("You have to pay $0.")
#     else:
#         print("You cannot ride the roller coaster.")

# Treasure Island
while True:
    print("Welcome to the Treasure Island.")
    print("Your mission is to find the treasure.")
    
    direction = input("you are at a cross road. Where do you want to go? Type 'left' or 'right'")
    if not direction == "left":
        print("Game Over. You have Fall into a hole.")
    swin = input("You have come to a lake. Type 'wait' to wait for a boat. Type ' swim' to swim across.")
    if not swin == "wait":
        print("Game Over. You have been attacked by a trout.")
    door = input("You have come to a house after crossing the lake. There are three doors. One red, one yellow and one blue. Which door do you want to enter?") 
    if door == "red":
        print("Game Over. You have been burned by fire.")
    elif door == "blue":
        print("Game Over. You have been eaten by beasts.")
    else:
        print("You have found the treasure. You win!")