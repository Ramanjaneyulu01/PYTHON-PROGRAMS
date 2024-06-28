def fibonacci(n):
    fib_sequence = [0, 1]  # Initialize the sequence with the first two terms
    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]  # Calculate the next term
        fib_sequence.append(next_term)  # Add the next term to the sequence
    return fib_sequence

def main():
    try:
        num_terms = int(input("Enter the number of terms for Fibonacci sequence: "))
        if num_terms <= 0:
            print("Please enter a positive integer.")
        else:
            sequence = fibonacci(num_terms)
            print("Fibonacci sequence with", num_terms, "terms:", sequence)
    except ValueError:
        print("Please enter a valid integer for the number of terms.")

if __name__ == "__main__":
    main()
