try:
    num1, num2=eval(input("Enter two numbers and add a comma between them:"))
    result=num1/num2
    print("The result is",result)
except ZeroDivisionError as ex:
    print("error",ex)
except SyntaxError:
    print("Add a comma between the number. Like this: 1,2")
except:
    print("Wrong input")
else:
    print("No error in the input")
finally:
    print("This will execute no matter what")