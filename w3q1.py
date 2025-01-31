def is_power_of_two(n):
    
    return n > 0 and (n & (n - 1)) == 0
a=int(input("Enter a number to check if it's in the form of 2^k or not : "))
if(is_power_of_two(a)):
    print(f"{a} is in the form of 2^k")
else:
    print(f"{a} is not in the form of 2^k")