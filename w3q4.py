def order_of_r(r, n):
    if r % n == 0:
        return -1
    for i in range(1, n):
        if pow(r, i, n) == 1:
            return i
    return -1

r = int(input("Enter the value of r: "))
n = int(input("Enter the value of n: "))
print("Order of", r, "under modulo", n, "is:", order_of_r(r, n))
