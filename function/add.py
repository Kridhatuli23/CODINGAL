def add(p,q):
    return p+q
def subtract(p,q):
    return p-q
def multiply(p,q):
    return p*q
def divide(p,q):
    return p/q
print("a. addition")
print("b. subtraction")
print("c. multiplication")
print("d. division")
fun=input("Please select an option out of the following (a/b/c/d):")
num1=int(input("Kindly enter the first number:"))
num2=int(input("Kindly enter the second number:"))
if fun=="a":
    print(num1,"+",num2,"=",add(num1,num2))
elif fun=="b":
    print(num1,"-",num2,"=",subtract(num1,num2))
elif fun=="c":
    print(num1,"*",num2,"=",multiply(num1,num2))
elif fun=="d":
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("This is an invalid input")
    