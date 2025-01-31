a=int(input("enter your number: "))
sum=0
for i in range(1,a):
    if(a % i == 0):
        sum = sum + i
if(sum==a):
    print(a,"is perfect number")
else:
    print(a,"is not a perfect number")
