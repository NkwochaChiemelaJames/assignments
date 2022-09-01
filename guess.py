import random
number = random.randint(1, 100)
guess = int(input("Enter a number from 1 to 99:\n "))
while number != "guess":
    if guess < number:
        print ("guess is low")
        guess = int(input("Enter a number from 1 to 99:\n "))
    elif guess > number:
        print ("guess is high")
        guess = int(input("Enter a number from 1 to 99:\n "))
    else:
        print ("you guessed it!")
        break
    