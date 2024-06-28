def calculate_bill(units_consumed):

    if units_consumed <= 100:
        rate_per_unit = 1.50
    elif units_consumed <= 200:
        rate_per_unit = 2.50
    elif units_consumed <= 300:
        rate_per_unit = 3.50
    else:
        rate_per_unit = 4.50

    # Calculate total bill amount
    total_bill = units_consumed * rate_per_unit
    return total_bill

# Input units consumed from the user
units = float(input("Enter the units consumed: "))

# Calculate the electricity bill
bill_amount = calculate_bill(units)

# Print the bill amount
print("Electricity Bill Amount: $", bill_amount)
