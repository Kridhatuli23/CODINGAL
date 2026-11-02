items=["pencil","eraser","sharpener,""glue"]
counts=[12,5,4,9,7]
inventory={item:count for item, count in zip(items,counts)}
print("Full invetory:",inventory)
in_stock_items=[item for item in items if inventory[item]>0]
print("Items in stock:",in_stock_items)
chosen_item=input("Which item would you want to buy?")
if chosen_item not in inventory or inventory[chosen]==0:
    print(chosen_item,"is out of stock! Stopping the checker.")
    exit()
prices=[10,5,80,76,45]
markup=int(input("Please enter the markup amount to add to every product."))
marked_up_prices=list(map(lambda p:p+markup,prices))
print("The marked up prices are:",marked_up_prices)
item_index=items.index(chosen_item)
chosen_price=marked_up_prices[item_index]
print(item_index)
print("Price of",chosen_item,"after markup:",chosen_price)
inventory[chosen_item]=inventory[chosen_item]-1
print(chosen_item, "purchased!Remaining stock:",inventroy[chosen_item])