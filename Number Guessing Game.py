import random
num = random.randint(1, 100)
print("Welcome to NumberGuessing game")
print("Guess the number")
def is_valid(guess):
    if 1 <= guess <= 100:
        return True
    else:
        return False


n = 1
while n <= 7:
    guess = int(input())
    if is_valid(guess):
        if guess < num:
            print("Your numbers is lower, try again. You have {} attempts left!".format(7 - n))
        elif guess > num:
            print("Your number is higher, try again. You have {} attempts left!".format(7 - n))
        elif guess == num:
            print("Correct, Yipeeeee!!!!")
            break
    else:
        print("Try number from 1 to 100")
    n += 1
else:
    print("You're out of attempts((( Try again")