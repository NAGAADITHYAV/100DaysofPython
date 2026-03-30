import random
from art import LOGO
from data import DATA

def get_random_movie():
    """Returns a movie index not present in the exclude_set."""
    return random.choice(DATA)

def format_movie_data(movie):
    """Returns a readable string for the movie display."""
    return f"{movie['name']} ({movie['year']}), {movie['genre']}"

def get_user_choice():
    """Handles input and ensures the user enters 'a' or 'b'."""
    choice = input("Which show has a higher rating? (A/B): ").lower()
    while choice not in ['a', 'b']:
        choice = input("Invalid input. Please enter 'A' or 'B': ").lower()
    return choice

def play_game():
    print(LOGO)
    score = 0
    game_should_continue = True
    
    # Initial setup
    movie_b = get_random_movie()

    while game_should_continue:
        movie_a = movie_b
        movie_b = get_random_movie()
        while movie_a == movie_b:
          movie_b = get_random_movie()

        print(f"Compare A: {format_movie_data(movie_a)}")
        print("vs")
        print(f"Against B: {format_movie_data(movie_b)}")

        choice = get_user_choice()
        
        # Determine the correct answer
        a_rating = movie_a['rating']
        b_rating = movie_b['rating']
        is_correct = (choice == 'a' and a_rating >= b_rating) or (choice == 'b' and b_rating >= a_rating)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.\n")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

if __name__ == "__main__":
    play_game()