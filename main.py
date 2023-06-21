"""
Random Number Generator Game (WIP)

Involve a starting balance for players. $500
Player enter an amount they would like to bet.

Player will enter the difficulty of how many tries they want.
    More tries = less payout
    Less tries = more payout
    Option to allow hinting(generous payout without)
The game will always be in a rage from 1-20
After each game, you will have the option to play again, cash out, or go to shop

Shop consist of:
WIP

Cash out:
When cashing out, players will be given the option if they would like to enter their paycheck into the IRS.
If not, a text about being careful

If they do, compliment their integrity
"""
import random
money = 500


def game():
    random_number = random.randint(1, 20)
    lives = int(input("Before we start, how many tries would you like? 5 or 10\n"))
    guess = 0

    print(random_number)

    while lives != 0:
        while guess != random_number:
            guess = int(input("Enter a number between 1 and 20: "))

            if lives == 0:
                break
            if guess > random_number:
                print("Too high!")
                lives -= 1
                break
            elif guess < random_number:
                print("Too low!")
                lives -= 1
                break
            elif guess == random_number:
                print("Correct!")
                menu()
                break
    print("Out of lives. Game over!")


def shop():
    print("Welcome to the shop!")


def menu():
    x = int(input("Main Menu. Please respond with the following number.\n1.Play\n2.Shop\n3.Quit\nInput: "))
    while True:
        if x == 1:
            game()
            break
        elif x == 2:
            shop()
            break
        elif x == 3:
            print("Goodbye")
            break


menu()











