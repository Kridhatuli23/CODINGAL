amount=int(input("Please enter total amount"))
money=int(input("Please enter money given by customer:"))
change_due=money-amount
if change_due == 0:
    pass
else:
    print(f"Here is your change: {change_due} units")



coin=int(input("Please enter no. of coins:"))
if coin != 1 and coin != 5 and coin != 10 and coin != 25:
    print("Invalid coin, try again!")
    pass