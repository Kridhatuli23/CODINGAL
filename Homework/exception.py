valid=False
while not valid:
    try:
        amount=int(input("Please enter the total cost for the clothing you bought."))
        if amount<=0:
            raise ValueError
        if 0<amount<2000:
                bill=amount*10/100
                print("You will get 10 percent discount. The total amount you have to may is",bill)
        elif 0<amount<=5000:
                bill=amount*50/100
                print("you will get 50 percent discount.The total amount you have to may is",bill)
        elif amount>5000:
                bill=amount*60/100
                print("You will get 60 percent discount. The total amount you have to may is",bill)
    except ValueError:
        print("exception: Cost as 0 rupees is invalid")

