# print today's date
from datetime import datetime, timedelta

today = datetime.now()
minusDay = timedelta(days=1)
yesterday = today - minusDay
# print yesterday's date
print(str(yesterday))
# ask a user to enter a date
userDateInput = input('Enter a date mm/dd/yyyy: ')
userDate = datetime.strptime(userDateInput, '%m/%d/%Y')
# print the date one week from the date entered
addWeek = timedelta(days=7)
weekFromUserDate = userDate + addWeek
print(str(weekFromUserDate))
