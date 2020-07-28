# Guessing correct number game implementation using python
import random
print("welcome to the game of correct guess")
print("Rule:Guess the right number under 5 guess")
print("Hint:The number is between 0 to 20")

secret_num = random.randint(1, 21)

guess_count = 0
guess_limit = 5
while guess_count <= guess_limit:
    guess = int(input("guess a number:"))
    guess_count += 1
    if guess > secret_num:
        print("num is too large")
    elif guess < secret_num:
        print("num is too small")
    elif guess == secret_num:
        print("Great! you guessed correct number")
        break
else:
    print(" Sorry you failed!")

print("Thank you :)")
