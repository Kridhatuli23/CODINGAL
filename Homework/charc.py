ch = input("Enter a character: ")

if len(ch) == 1 and (('A' <= ch <= 'Z') or ('a' <= ch <= 'z')):
    print("It is an alphabet.")
else:
    print("It is not an alphabet.")