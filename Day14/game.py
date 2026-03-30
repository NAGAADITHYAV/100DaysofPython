from art import LOGO
from data import DATA

import random

number_of_shows = len(DATA)

print(LOGO)

def print_movie(movie, C):
  print(f"{C} : {movie['name']}({movie['year']}),\n {movie['genre']}")

score = 0

a = random.randint(0, number_of_shows-1)
b = random.randint(0, number_of_shows-1)
while(a == b):
  b = random.randint(0, number_of_shows-1)

chosen = set([a,b])

while(True):
  print_movie(DATA[a], 'A')
  print_movie(DATA[b], 'B')
  correct_choice = 'a' if DATA[a]['rating'] >= DATA[b]['rating'] else 'b'
  choice = input('Which of the shows has Higher rating(A/B)? ').lower()
  while choice not in 'ab':
    choice = input('Enter a vaild Choice\nWhich of the choices has Higher rating? ')
  
  if choice == correct_choice:
    score  = score +1
    print('You are correct, Try next one, your current Score is ',score)
    c = random.randint(0, number_of_shows-1)
    while c in chosen:
      c = random.randint(0, number_of_shows-1)
    a, b = b, c
  else:
    break
    

print('Your total score is', score)