amount=float(input("Please enter the actual cost:"))
sale_amount=float(input("Please enter the sale amount:"))
if sale_amount>amount:
    prof= sale_amount-amount
    print("Total profit=",prof,"rupees")
else:
    print("No profit!!")