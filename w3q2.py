def mersenne_prime(n):
    # Check if n + 1 is a power of 2 
    if (n + 1) & n == 0:
        for i in range(2, int(n/2) + 1):
            if n % i == 0:
                return False
        return True
    return False
a=int(input("Enter a number to check whether it's mersenne prime or not: "))
if(mersenne_prime(a)):
    print(f"{a} is mersenne prime!")
else:
    print(f"{a} is not mersenne prime")