import random

number = random.randint(1,10)

for i in range(3):
    user = int(input("guess the number (1-10):"))

    if user == number:
        print(f"hurray! you guessed the number right,it's {number}.")
        break
    else:
        print("wrong guess.try again!")

if user !=number:
    print(f"sorry,you've used all attempts. the number was {number}.")
