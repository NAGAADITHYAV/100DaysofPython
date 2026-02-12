from HANGMAN_ASCI_ART import HANGMANPICS, WORDS, CHAR_SET, GAMEOVER
import random

while True:
    stop = input("Press 'y' to play the game(any other to quit): ")
    if stop.lower() != 'y':
        print('Good Bye !!!!!')
        break

    word = random.choice(WORDS)
    hidden_word = ['_' for _ in word]
    lives_lost = 0
    guessed_set = set()

    while lives_lost< len(HANGMANPICS)-1:
        if '_' not in hidden_word:
            print(f"\n✨ Victory! The word was: {word}")
            break

        print(HANGMANPICS[lives_lost])
        print(f"Word: {' '.join(hidden_word)}")
        print(f"Guessed: {', '.join(sorted(guessed_set))}")

        guess = input("Guess a letter ").lower()

        if len(guess) != 1:
            print(">> Please enter exactly one letter.")
            continue
        if guess not in CHAR_SET:
            print(">> Invalid character. Please use the alphabet.")
            continue
        if guess in guessed_set:
            print(f">> You already guessed '{guess}'. Try again!")
            continue
        guessed_set.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for idx, letter in enumerate(word):
                if letter == guess:
                    hidden_word[idx] = guess
        else:
            print(f"Sorry, '{guess}' is not there.")
            lives_lost += 1
    else:
        print(HANGMANPICS[lives_lost])
        print(GAMEOVER)
        print(f"The word was: {word}")


