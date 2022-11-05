# You are given a date. Your task is to find what the day is on that date.

import calendar

# print(calendar.TextCalendar(firstweekday=6).formatyear(2022))

day_in_week = ['MONDAY', 'TUESDAY', 'WEDNESDAY', "THURSDAY", "FRIDAY", 'SATURDAY', 'SUNDAY']
date = list(map(int,input().split()))
day = calendar.weekday(date[2], date[0], date[1])
print(day_in_week[day])