def check_even_odd(number):
    if number % 2 == 0:
        print(number, "is even.")
    else:
        print(number, "is odd.")

def main():
    try:
        number = int(input("Enter a number: "))
        check_even_odd(number)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
