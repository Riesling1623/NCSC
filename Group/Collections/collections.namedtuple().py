# Basically, namedtuples are easy to create, lightweight object types.
# They turn tuples into convenient containers for simple tasks.
# With namedtuples, you don’t have to use integer indices for accessing members of a tuple.

from collections import namedtuple

# Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks, names and classes.

# Your task is to help Dr. Wesley calculate the average marks of the students.

# n = the total number of students
n = int(input())
spreadsheet = namedtuple('spreadsheet', input().split())
sum_marks = 0

for _ in range(n):
    student = spreadsheet(*input().split()) #*input to input more values
    sum_marks += int(student.MARKS)
print('%.2f'%(sum_marks / n))
