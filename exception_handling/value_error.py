try:
    char=float(input("Enter a decimal number:"))
    print("The decimal number entered is",char)
except ValueError as ex:
    print("Exception:",ex)
