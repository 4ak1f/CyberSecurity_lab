num_1=int(input("Enter first number: "))
num_2=int(input("Enter secoond number: "))

a, b= num_1, num_2
while b!=0:
    a, b =b, a % b
if a == 1:
    print(f"{num_1} and {num_2} are relatively prime")
else:
    print(f"{num_1} and {num_2} are not relatively prime")