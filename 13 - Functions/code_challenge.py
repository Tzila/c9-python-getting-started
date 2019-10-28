# Create a calculator function
# The function should accept three parameters:
# first_number: a numeric value for the math operation
# second_number: a numeric value for the math operation
# operation: the word 'add' or 'subtract'
# the function should return the result of the two numbers added or subtracted
# based on the value passed in for the operator
# Test your function with the values 6,4, add
# Should return 10
# Test your function with the values 6,4, subtract
# Should return 2
# BONUS: Test your function with the values 6, 4 and divide
# Have your function return an error message when invalid values are received


def calc_add(first_number, second_number):
    total = (int(first_number) + int(second_number))
    return total


def calc_sub(first_number, second_number):
    total = (int(first_number) - int(second_number))
    return total


first_number = input('Enter a first number to add or subtract: ')
second_number = input('Enter a second number to add or subtract: ')
addOrSubtract = input('Do you want to Add or Subtract? ')

if addOrSubtract.lower() == 'add':
    print(calc_add(first_number, second_number))

elif addOrSubtract.lower() == 'subtract':
    print(calc_sub(first_number, second_number))

else:
    print('ERROR')
