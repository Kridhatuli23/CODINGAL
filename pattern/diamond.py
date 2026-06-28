row=int(input("Enter the number of rows:"))
if row%2==0:
    diam=int(row/2)
else:
    diam=int(row/2)+1
space=diam-1
for i in range(1,diam+1):
    for j in range(1,space+1):
        print(end=" ")
    space=space-1
    num=1
    for j in range(2*i-1):
        print(end=str(num))
        num=num+1
    print()

space=1
for i in range(1,diam):
    for j in range(1,space+1):
        print(end=" ")
    space=space+1
    num=1
    for j in range(1, 2*(diam-i)):
        print(end=str(num))
        num=num+1
    print()
