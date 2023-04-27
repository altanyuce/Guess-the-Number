import random
from art import logo

number = int(random.randint(1,100))
print(number)

def game():
    print(logo)
    print("Welcome to the Guess The Number!\nI'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'Easy' or 'Hard': ")

    if difficulty == "easy":
        easy()
    elif difficulty == "hard":
        hard()

def easy():
    i = 10
    while i > 0:
        if i < 10:
            print("Guess again.")
        print(f"You have {i} attempts remaining to guess the number.")
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
    i = 5
    while i > 0:
        if i < 10:
            print("Guess again.")
        print(f"You have {i} attempts remaining to guess the number.")
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

game()


