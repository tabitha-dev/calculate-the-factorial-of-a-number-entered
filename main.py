import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

while True:
    print("\n=====================================")
    print("\033[1mWelcome to the Calculator App!\033[0m")
    print("=====================================")
    print("Options:")
    print("\033[33m1. Calculate Factorial\033[0m")
    print("\033[34m2. Calculate GCD\033[0m")
    print("\033[31m3. Quit\033[0m")

    choice = input("\033[32mEnter your choice (1/2/3): \033[0m")

    if choice == '1':
        num = int(input("\033[32mEnter a positive integer: \033[0m"))
        if num < 0:
            print("\033[31mPlease enter a positive integer.\033[0m")
        else:
            result = factorial(num)
            print(f"\033[36mThe factorial of {num} is {result}\033[0m")
    elif choice == '2':
        num1 = int(input("\033[32mEnter the first integer: \033[0m"))
        num2 = int(input("\033[32mEnter the second integer: \033[0m"))
        result = gcd(num1, num2)
        print(f"\033[36mThe GCD of {num1} and {num2} is {result}\033[0m")
    elif choice == '3':
        print("\033[35mGoodbye!\033[0m")
        break
    else:
        print("\033[31mInvalid choice. Please select 1, 2, or 3.\033[0m")
