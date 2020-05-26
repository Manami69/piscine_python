import random

print("This is an interactive guessing game!\
\nYou have to enter a number between 1 and 99 to find out the secret number.\
\nType 'exit' to end the game.\
\nGood luck!\n")


def print_finish(number, attempts):
    if attempts == 1 and number == 42:
        print("The answer to the ultimate question of life,\
the universe and everything is 42.")
    if attempts == 1:
        print("Congratulations! You got it on your first try!")
    else:
        print("Congratulations ! you've got it!\nYou won in \
{} attemps !".format(attempts))


number = random.randint(1, 99)
attempt = 1
while True:
    guess = input("What's your guess between 1 and 99?\n>> ")
    if guess.isdigit() is False:
        if guess == 'exit':
            print("Goodbye !")
            break
        else:
            print("That's not a number.")
    else:
        if int(guess) > number:
            print("Too high!")
        elif int(guess) < number:
            print("Too low!")
        elif int(guess) == number:
            print_finish(number, attempt)
            break
    attempt += 1
