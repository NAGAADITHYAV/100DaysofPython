import random

NUMBER = random.randint(1, 100)

def play_game():
    difficulty = input('How do you wanna play easy/hard: ').lower()
    attempts = 10 if difficulty == 'easy' else 5
    while(attempts>0):
        guessNum = int(input('Guess the number: '))
        if guessNum == NUMBER:
            print('You have guessed the number correclty.')
            break
        elif guessNum < NUMBER:
            print('Your guess is lower than the correct one.')
        elif guessNum > NUMBER:
            print('Your guess is higher than the correct one.')
        attempts -= 1
    if attempts == 0:
        print(f"Correct Guess is {NUMBER}")
    print()



play_game()
while(input('Do you wanna play again(y/n): ').lower() != 'n'):
  play_game()