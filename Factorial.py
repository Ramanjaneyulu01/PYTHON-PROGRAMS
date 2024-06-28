def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def main():
    try:
        num = int(input("Enter a number to calculate its factorial: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print("Factorial of", num, "is", factorial(num))
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
