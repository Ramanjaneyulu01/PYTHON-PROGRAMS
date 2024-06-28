def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)

    armstrong_sum = 0

    for digit in num_str:
        armstrong_sum += int(digit) ** num_digits

    if armstrong_sum == number:
        return True
    else:
        return False

number = int(input("Enter a number: "))
if is_armstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
