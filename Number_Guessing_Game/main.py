import random 


def guess_the_number():
    seceret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the game !")
    print("I'm thinking the number is in between 1 to 100")


    while True:
        try:
            guess = int(input("Guess the number : ").strip())
            attempts += 1
            if guess < seceret_number:
                print("Too low! Try Again.")
            elif guess > seceret_number:
                print("Too Big! Try Again.")
            elif guess == seceret_number:
                print(f"Congratulation! you guessed the number in {attempts} attempts.")
            else:
                print("Invalid Number!")
        except ValueError:
            print("Please Enter a valid number !")


guess_the_number()