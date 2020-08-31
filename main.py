import calendar
import datetime
import time

print(calendar.weekheader(4))

print()

print(calendar.firstweekday())

print()

print(calendar.month(2020,4,w=4,l=2))

print()

print(calendar.monthcalendar(2020,8))

print()

print(calendar.calendar(2020,w=4,l=2))

day_of_the_month = calendar.weekday(2021,4,17)

print(day_of_the_month)

is_this_a_leap_year = calendar.isleap(2020)

print(is_this_a_leap_year)


print()

how_many_leap_days = calendar.leapdays(2000,2020)

print( how_many_leap_days)


