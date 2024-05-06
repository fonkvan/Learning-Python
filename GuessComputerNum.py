import random

def guess(x):
    random_number = random.randint(1, x)
    player_guess = 0
    while player_guess != random_number:
        player_guess = int(input(f"Guess the computer number between 1 and {x}: "))
        if(player_guess < random_number):
            print("Too low!")
        elif(player_guess > random_number):
            print("Too high!")
    print("You win!")

if __name__ == "__main__":
    guess(100)