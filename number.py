import random
num=random.randint(1, 100)
print("Welcome to the random number game!")
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == num:
        print("Congratulations! You guessed the number!")
        break
    elif guess < num:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")