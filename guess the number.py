import random
from art import logo

number = int(random.randint(1,100))
print(number)
def easy():
    i = 10
    while i > 0:
        print(f"Guess again.\nYou have {i} attempts remaining to guess the number.")
        player_guess = int(input("Make a guess: "))
        if player_guess == number:
            print(f"You got it! The answer was {number}")
            i = 0
        else:
            if number < player_guess:
                print("Too high.")
            elif number > player_guess:
                print("Too low.")
            i -= 1
        if i == 0:
            print("You've run out of guesse, you lose.")
def hard():
    ii = 5
    while ii > 0:
        print(f"Guess again.\nYou have {ii} attempts remaining to guess the number.")
        player_guess = int(input("Make a guess: "))
        if player_guess == number:
            print(f"You got it! The answer was {number}")
            ii = 0
        else:
            if number < player_guess:
                print("Too high.")
            elif number > player_guess:
                print("Too low.")
            ii -= 1
        if ii == 0:
            print("You've run out of guesse, you lose.")



print(logo)
print("Welcome to the Guess The Number!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'Easy' or 'Hard': ")

if difficulty == "easy":
    easy()
elif difficulty == "hard":
    hard()



