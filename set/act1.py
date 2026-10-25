bas1={"apple","banana","strawberry","grapes","blueberry","mango"}
bas2={"pear","guava","pineapple","pear","grapes"}
print("basket 1:",bas1)
print("basket 2:",bas2)
bas1.add("orange")
print("Basket 1 after adding oranges",bas1)
fruits=bas1.intersection(bas2)
print("The common fruit in both baskets is",fruits)

import array as ar
fruitcount=ar.array('i',[1,2,2,3,44,5,5])
fruitcount[3]=98
print("Fruit counts array:",fruitcount)

fruitcount.insert(2,88)
fruitcount.append(90)
print("Fruit counts after adding items",fruitcount)

countof4=fruitcount.count(2)
print("Number of times 2 appears:",countof4)
fruitcount.reverse()
print("Reversed fruit counts array:",fruitcount)
