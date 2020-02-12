"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to
print out a calendar for April in 2015, but if you omit either the year or both values,
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime


args = sys.argv
print(args)


# if no args are supplied we
# print a text calendar for current month and year
if(len(args) == 1):
    month = datetime.today().month
    year = datetime.today().year
    calendar.prmonth(year, month)

    # if 1 arg is supplied ..
    # Check if it's an int 1-12 print out calendar for that month , current year
elif(len(args) == 2):
    month = int(args[1])
    year.datetime.today().year
    calendar.prmonth(year, month)
    # if 2 args are supplied..
    # Check if 1 is int 1-12, check if 2 is an int
    # Print out calendar for that month and year
elif(len(args) == 3):
    month = int(args[1])
    year = int(args[2])
    calendar.prmonth(year, month)
    # Otherwise, print an error with usage hint
else:
    print("error: coomand must be in the form year, month")
    exit()


calendar.prmonth(year, month)

# if (len(sys.argv) == 3):
#     month = sys.argv[1]
#     year = sys.argv[2]
# elif (len(sys.argv) == 2):
#     month = sys.argv[1]
#     year = datetime.now().year
# else:
#     year = datetime.now().year
#     month = datetime.now().month

# print(calendar.month(int(year), int(month)))
