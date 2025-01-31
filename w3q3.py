import math

def euler_totient(n):
    count = 0
    for i in range(1, n + 1):
        if math.gcd(i, n) == 1:
            count += 1
    return count

n = int(input("Enter a number: "))
print(f"The Euler's Totient of {n} is: {euler_totient(n)}")
