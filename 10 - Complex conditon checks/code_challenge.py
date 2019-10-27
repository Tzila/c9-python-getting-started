# When you join a hockey team you get your name on the back of the jersey
# but the jersey may not be big enough to hold all the letters
# Ask the user for their first name
userFirstName = input('What is your first name? ')
# Ask the user for their last name
userLastName = input('What is your last name? ')
# if first name is < 10 characters and last name is < 10 characters
# print first and last name on the jersey
if len(userFirstName) < 10 and len(userLastName) < 10:
    print(userFirstName.capitalize() + ' ' + userLastName.capitalize())
# if first name >= 10 characters long and last name is < 10 characters
#       print first initial of first name and the entire last name
elif len(userFirstName) >= 10 and len(userLastName) < 10:
    print((userFirstName[0].capitalize()) + ' ' + userLastName.capitalize())
# if first name < 10 characters long and last name is >= 10 characters
#       print entire first name and first initial of last name
elif len(userFirstName) < 10 and len(userLastName) >= 10:
    print(userFirstName.capitalize() + ' ' + userLastName[0].capitalize())
# if first name >= 10 characters long and last name is >= 10 characters
#       print last name only
elif len(userFirstName) >= 10 and len(userLastName) >= 10:
    print(userLastName.capitalize())
# Test with the following values
# first name: Susan  last name: Ibach
# output: Susan Ibach
# first name: Susan  last name: ReallyLongLastName
# output: Susan R.
# first name: ReallyLongFirstName  last name: Ibach
# output: R. Ibach
# first name: ReallyLongFirstName  last name: ReallyLongLastName
# output: ReallyLongLastName
