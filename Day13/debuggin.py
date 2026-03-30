def prompt_positive_integer(message):
    try:
      while True:
        age = int(input(message))
        if age >= 0:
          return age
        print('Enter an Interger grater than 0')
    except ValueError:
      print('Value Error: Enter proper Integer')

age = prompt_positive_integer('How old are you? ')

print(f"Your age is {age}")