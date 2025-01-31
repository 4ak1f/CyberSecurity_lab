def is_narcissistic(num):
    digits = [int(digit) for digit in str(num)]  #digits of the number
    num_digits = len(digits)
    return num == sum(digit ** num_digits for digit in digits)

def display_narcissistic_numbers(n):
    print(f"Narcissistic numbers up to {n}:")
    for num in range(1, n + 1):
        if is_narcissistic(num):
            print(num)

n = int(input("Enter a number n: "))

display_narcissistic_numbers(n)
