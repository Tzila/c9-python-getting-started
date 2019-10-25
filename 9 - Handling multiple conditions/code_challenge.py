# Ask a user their name
userFirstName = input('What is your first name? ')
# If their first name starts with A or B
userFirstName = userFirstName.lower()

if userFirstName.startswith('a') or userFirstName.startswith('b'):
    print('Go to room AB')
# tell them they go to room AB
# IF their first name starts with C
elif userFirstName.startswith('c'):
    print('Go to room CD')
# tell them to go to room CD
else:
    userLastName = input('What is your last name? ')
    userLastName = userLastName.lower()
    if userLastName.startswith('z'):
        print('Go to room Z')
    else:
        print('Go to room OTHER')
# If their first name starts with another letter, ask for their last name
# IF their last name starts with Z, tell them to go to room Z
# if their last name starts with any other letter tell them to go to room OTHER
# When you are done
# Anna should be in room AB
# Bob should be in room AB
# Charlie should be in room C
# Khalid Haque should be in room OTHER
# Xin Zhao should be in room Z
