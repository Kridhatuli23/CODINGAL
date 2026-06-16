num=int(input("Enter the number whose sum you want to find: "))
sum=0
for i in range(1, num+1, 2):
    sum=sum+i
    print("Sum=",sum)
