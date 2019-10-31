# Create a calculator function
# The function should accept three parameters:
# first_number: a numeric value for the math operation
# second_number: a numeric value for the math operation
# operation: the word 'add' or 'subtract'. The default operation is 'add'
# the function should return the result of the two numbers added or subtracted
# based on the value passed in for the operator
# Test your function using named notation passing in only the numbers 6 and 4
# Should return 10
# Test your function using named notation with the values 6,4, subtract
# Should return 2
# BONUS: Test your function with the values 6, 4 and divide
# Have your function return an error message when invalid values are received


def calculate(first_number, second_number, operation):
    if operation == 'subtract':
        return (int(first_number) - int(second_number))
    elif operation == 'add':
        return (int(first_number) + int(second_number))
    else:
        return "Error"


first_number = input('enter a first number to add or subtract: ')
second_number = input('enter a second number to add or subtract: ')
operation = input('Would you like to add or subtract?: ')
operation = operation.lower()

print(calculate(first_number, second_number, operation))
