import random

print("Number guessing game")

# randint function to generate the
# random number b/w 1 to 9
number = random.randint(1, 9)


chances = 0

print("Guess a number (between 1 and 9):")


while True:

    # Enter a number between 1 to 9
    guess = int(input())


    if guess == number:

       
        print(
            f'CONGRATULATIONS! YOU HAVE GUESSED THE \
            NUMBER {number} IN {chances} ATTEMPTS!')
        # Printing final statement using the f-strings method;
        break


    elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess)

    else:
        print("Your guess was too high: Guess a number lower than", guess)

    chances += 1
    
