import random
from art import LOGO
from data import DATA

def get_random_movie(exclude_set):
    """Returns a movie index not present in the exclude_set."""
    while True:
        index = random.randint(0, len(DATA) - 1)
        if index not in exclude_set:
            return index

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
    idx_a = get_random_movie(set())
    idx_b = get_random_movie({idx_a})
    used_indices = {idx_a, idx_b}

    while game_should_continue:
        movie_a = DATA[idx_a]
        movie_b = DATA[idx_b]

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
            
            # Move B to A and get a new B
            idx_a = idx_b
            idx_b = get_random_movie(used_indices)
            used_indices.add(idx_b)
            
            # Optional: Reset used_indices if you run out of movies
            #here we are also not re using shows already used
            if len(used_indices) == len(DATA):
                used_indices = {idx_a, idx_b}
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

if __name__ == "__main__":
    play_game()