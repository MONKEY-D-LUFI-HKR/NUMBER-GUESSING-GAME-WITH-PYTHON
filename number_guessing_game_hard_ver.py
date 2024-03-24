import random

def get_top_range():
    while True:
        top_range = input("Type a positive number as the maximum range: ")
        if top_range.isdigit() and int(top_range) > 0:
            return int(top_range)
        print("Please type a positive number.")

def get_user_guess():
    while True:
        user_guess = input("Make a guess: ")
        if user_guess.isdigit():
            return int(user_guess)
        print("Please type a number.")

def play_game(top_range):
    random_number = random.randint(0, top_range)
    max_guesses = 5  # Maximum number of guesses allowed
    guesses = 0

    while guesses < max_guesses:
        guesses += 1
        user_guess = get_user_guess()

        if user_guess == random_number:
            print("You got it!")
            return True
        elif user_guess > random_number:
            print("Your guess was above the number!")
        else:
            print("Your guess was below the number!")

    print("You ran out of guesses. The number was:", random_number)
    return False

def main():
    top_range = get_top_range()
    print("You have 5 guesses to find the number.")
    if play_game(top_range):
        print("Congratulations!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
