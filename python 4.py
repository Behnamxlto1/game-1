import random

pc_number = random.randint(1,20)
n = 0

while True:
    user_number = int(input("Guess a number between 1 and 20 chances:"))
    
    n += 1

    if pc_number == user_number:
        print("Well done, you guessed right. The number of your guesses :", n)
        break

    if user_number < pc_number :
        print ("The desired number is higher")
    else:
        print ("The desired number is less")
