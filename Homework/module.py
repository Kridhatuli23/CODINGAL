import random
print("I will tell you your luck number today!")
num=random.randint(1,100)
print("Your lucky number is",num)

funchoices="Play a card came","Watch a newly released hollywood movie","read a fun comic book","play an outdoor game with friends","Spend some time with your family","Learn a new skill like cooking, playing an instrument","Listen to your favourite songs","Do your homework"
activity=random.choice(funchoices)
print("The random activity you need to perform is",activity)



print("I will think of a random number between 1 and 20, and you need to guess it in three tries.")
num1=random.randint(0,20)

try:
    num2=int(input("Please enter your guess 1:"))
    if num2==num1:
        print("Your guess is right")
    else:
        print("Your guess is incorrect")
    guess2=int(input("Please enter your guess 2:"))
    if guess2==num1:
        print("Your guess is right")
    else:
        print("Your guess is incorrect")
    guess3=int(input("Please enter your guess 3:"))
    if guess2==num1:
        print("Your guess is right")
    else:
        print("The numebr I was thinking about was",num1)
except ValueError:
    print("Invalid number. Please enter a number between 0 and 20")

import math
num=float(input("Enter a decimal number to check where it round off: "))
round=math.ceil(num)
print("Your number rounded off to",round)
num2=float(input("Add a decimal number to check the number it is rounded down to: "))
down=math.floor(num2)
print("Your number rounded off to",down)
num3=int(input("Enter a negative number to get its absolute value:"))
abso=math.fabs(num3)
print("The absolute value of the number you entered is",abso)
print("Now, we will find out HCF or two numbers")
num4=int(input("Enter 1st number: "))
num5=int(input("Enter 2st number: "))
common=math.gcd(num4,num5)
print("The highest common factor of the numbers you entered is",common)


