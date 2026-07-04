secret=32
guess=int(input("Please enter the number you guessed between 1 and 50:"))
if guess==32:
    print("Correct guess")
else:
    print("Wrong guess")
    print("The number is greater than 15")

guess2=int(input("Please enter the second number you guessed between 1 and 50:"))
if guess2==32:
    print("Correct guess")
else:
    print("Wrong guess")
    print("The number is less than 45")
guess3=int(input("Please enter the third number you guessed between 1 and 50:"))
if guess3==32:
    print("Correct guess")
else:
    print("Wrong guess")
    print("The number is between 30 and 40")
guess4=int(input("Please enter the forth number you guessed between 1 and 50:"))
if guess4==32:
    print("Correct guess")
else:
    print("Wrong guess")
    if guess4 < 35:
        print("You are very close to guessing the fianl no.")
    guess5=int(input("Please enter the fifth number you guessed between 1 and 50:"))
if guess5==32:
    print("Correct guess")
else:
    print("Wrong guess")
Print("The secret number is 32")