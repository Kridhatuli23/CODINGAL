import random
playing=True
number= str(random.randint(0,9))
print("I will generate a number from 0 to 9, and you will have to take chnaces to guess that number.")
print("The game ends after you get 1 hero!")
while playing:
    guess=input("Give me your best guess!")
    if number==guess:
        print("You win the game")
        print("The number is",number)
        break
    else:
        print("Your guess was incorrect, try again")