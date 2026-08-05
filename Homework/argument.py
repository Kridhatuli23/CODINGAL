def final_bill(amount, tip):
    bill=amount+(tip/100)*amount
    bill=round(bill)
    print("The total amount to be paid is",bill,"rupees")
user=int(input("Please enter the total amount to be paid: "))
tip_give=int(input("Please enter the tip percentage you would like to offer: "))
final_bill(user,tip_give)