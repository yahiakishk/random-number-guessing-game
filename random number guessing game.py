import random

lowest = 1
highest = 10

while True:
    guesses = 0
    answer = random.randint(lowest, highest)

    guess = input(f"Guess a number ({lowest}-{highest}): ").strip()

    if guess.isdigit():
        guess = int(guess)
        if guess == answer:
            print(
                f"Congrats you picked the right number with {guesses} wrong attempts")
            restart = input("Do you want to restart (y/n): ").lower()
            if restart != ("y"):
                print("Goodbye!")
                break
        elif guess < lowest or guess > highest:
            print("Number is is out of range, please try again")
        elif guess < answer:
            print("Your guess was lower than the number. Try again: ")
            guesses += 1
        else:
            print("Your guess was higher than the number. Try again: ")
            guesses += 1

    else:
        print("Input invalid, please only eneter whole positive integers")
