import random

top_range = input("type a number: ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print('please type a number larger than 0 next time ')
        quit()
else:
    print('please type a number next time ')
    quit()

random_number = random.randint(0, top_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('please type a number next time ')
        continue

    if user_guess == random_number:
        print("you got it!")
        break
    elif user_guess > random_number:
        print("your guess was above the number!")
    else:
        print("your guess was below the number!")

print("you got it in", guesses, "guesses")
